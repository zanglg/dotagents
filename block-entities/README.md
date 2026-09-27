# Block 层长期实体关系图

以用户指定的 `/Volumes/workspace/linux` 源码为准。
新版总图核对版本为 `v7.3-rc4-606-gfd179f8a05be`；原局部图基于
`v7.3-rc2-27-g893e11787f78`。对比两个版本，本图涉及的结构定义和初始化代码未变。

## 总图（默认入口）

[Block 层长期实体关系总图](00-overview.svg)

将原有五张图的实体与关系整合到一张 `1600 × 1408` CSS px 的 SVG 中，
以 `request_queue` 为中心，保留 13 条数量关系、共享模式及可选调度器语义。
所有实体连接都是单一直线段，无折线、曲线或交叉；同类型的 Driver / Scheduler
Tag 池仍分别画出，避免误认为同一实例。建议原尺寸或放大查看，不缩成小缩略图阅读。

## 原局部图（保留参考）

以下五张旧图未覆盖，仍可独立查看，原始尺寸均为 `1040 × 744` CSS px。

1. [设备、分区与请求队列](01-device-queue.svg)
2. [软件上下文与硬件上下文](02-cpu-hardware-contexts.svg)
3. [调度器：队列实例与注册类型](03-scheduler.svg)
4. [Driver Tag：集合共享与池共享](04-driver-tags.svg)
5. [Scheduler Tag：调度器自己的资源池](05-scheduler-tags.svg)

## 范围与读图规则

- 展示 blk-mq 的核心设备、队列、上下文、调度器及 tag 资源，
  不是所有 block 子系统结构的穷举，也不覆盖 bio-based 驱动路径。
- “长期”指在驱动、设备、分区或调度器的初始化/注册过程中建立，
  跨多次 I/O 复用；不是“仅开机时创建”或“生命周期内不可替换”。
  分区增删、CPU 拓扑改变、硬件队列数量调整和调度器切换可能重建相关对象。
- 数量关系描述已初始化、配置稳定的状态，不计拆卸或重配置的过渡对象。
- 箭头表示结构关联及数量关系的阅读方向，不表示 I/O 执行顺序，
  也不一概表示内存所有权或单向指针。字段标签说明实际关联依据。
- `1:N`、`N:1` 中的 `N` 是该条关系的局部数量，不同连线的 `N` 不必相等，
  且可为 1。允许 0 个对象的情况另作说明；`0..1` 表示可选单实例。
- `H` 是所属 `request_queue` 的 `nr_hw_queues`。
  `1:N / 1:1` 等并列标注表示两种配置模式，具体条件写在图下注释中。
- 实线表示明确建模的关系；虚线仅表示选择调度器后才存在的关联。
  实线卡片表示实体，蓝灰色强调当前局部主题，不表示选中状态。
- 多张图中的同名节点是重复展示同一类对象，不意味着额外创建一份。

不展示 `bio` 和单次 I/O 的 `request`。尤其注意：blk-mq 会预分配并复用
`request` 存储，所以“排除单次 I/O 对象”不等于断言其内存只在每次 I/O 时分配。
图中的 `blk_mq_tags` 则是管理这些资源的长期池对象。

为保持图形清晰，没有展开 `backing_dev_info`、`blkcg_gq`、`rq_qos`、
flush/zoned 资源、`kobject`、静态回调表及驱动/调度器私有结构。
`blk_mq_tag_set.map[]` 的映射含义在总图注释及图 02 中说明，未单独画出嵌入的
`blk_mq_queue_map`；`ops` 等回调表仅作为字段出现。

## 关键数量关系

| 起点 -> 终点 | 数量关系 | 限定条件 |
|---|---|---|
| `gendisk` -> `request_queue` | `1:1` | 已关联的 blk-mq 磁盘与队列 |
| `gendisk` -> `block_device` | `1:(1+P)` | 一个整盘 `part0`，加 `P` 个分区 |
| `blk_mq_tag_set` -> `request_queue` | `1:0..N` | 图中按已有挂接关系画 `1:N` |
| `request_queue` -> `blk_mq_ctx` | `1:N` | `N = num_possible_cpus()`，不只计算在线 CPU |
| `request_queue` -> `blk_mq_hw_ctx` | `1:H` | `H = q->nr_hw_queues` |
| `blk_mq_ctx` -> `blk_mq_hw_ctx` | 固定 type 为 `N:1` | 每个 ctx 的该类型槽位指向一个 hctx；跨类型可为 `M:N` |
| `request_queue` -> `elevator_queue` | `1:0..1` | `none` 时为 NULL |
| `elevator_queue` -> `elevator_type` | `N:1` | 每个实例一个类型；已注册类型可以没有实例 |
| `blk_mq_tag_set` -> Driver `blk_mq_tags` | 普通模式 `1:N`；HCTX_SHARED 模式 `1:1` | 普通模式独立池数不大于 `set->nr_hw_queues` |
| 已映射的 `blk_mq_hw_ctx` -> Driver `blk_mq_tags` | `N:1` | 可跨队列共享；无 CPU 映射的 hctx 的 `tags` 可为 NULL |
| `elevator_queue` -> `elevator_tags` | `1:1` | 已挂接的调度器实例 |
| `elevator_tags` -> Scheduler `blk_mq_tags` | 普通模式 `1:H`；HCTX_SHARED 模式 `1:1` | 此处 H 是分配时 `et->nr_hw_queues` |
| `blk_mq_hw_ctx` -> Scheduler `blk_mq_tags` | 普通模式 `1:1`；HCTX_SHARED 模式 `N:1` | 仅启用调度器时；否则 `sched_tags == NULL` |

### 不要混淆两种共享

- `BLK_MQ_F_TAG_QUEUE_SHARED`：多个 `request_queue` 使用同一个 tag set，
  对应硬件队列索引的 driver tag 池可以共享；hctx 对象仍各属于自己的 queue。
- `BLK_MQ_F_TAG_HCTX_SHARED`：不同硬件队列索引也共用一个 driver tag 池。
  此标志还让**同一个 request_queue 内**的多个 hctx 共用一个 scheduler tag 池。
- Scheduler tag 池不会因为多个 queue 共用一个 tag set 而自动跨 queue 合并。
- `hctx->tags` 与 `hctx->sched_tags` 虽同为 `struct blk_mq_tags *`，
  但引用的是不同角色、不同实例的资源池。

## 本地源码依据

以下位置均相对于 `/Volumes/workspace/linux`，本次已核对相关文件在上述两个版本间无差异，行号保持不变。

| 关系/行为 | 定义与初始化依据 |
|---|---|
| 磁盘、整盘对象、队列双向关联 | `include/linux/blkdev.h:144`；`block/genhd.c:1454` 的 `__alloc_disk_node()` |
| blk-mq 磁盘和队列的分配 | `block/blk-mq.c:4460` 的 `__blk_mq_alloc_disk()` |
| bdev 共享磁盘及其队列 | `include/linux/blk_types.h:41`；`block/bdev.c:501` 的 `bdev_alloc()` |
| 分区对象创建/注册 | `block/partitions/core.c:328`、`:390` 的 `bdev_alloc()`、`bdev_add()` 调用 |
| 队列关键成员 | `include/linux/blkdev.h:488` 的 `struct request_queue` |
| tag set、映射类型、hctx 定义 | `include/linux/blk-mq.h:322`、`:488`、`:534` |
| ctx 定义及类型映射 | `block/blk-mq.h:19`；`block/blk-mq.c:4162` 的 `blk_mq_map_swqueue()` |
| possible CPU 上下文分配/初始化 | `block/blk-mq.c:4351`、`:4078` |
| hctx 数量及数组 | `block/blk-mq.c:4539` 的 `__blk_mq_realloc_hw_ctxs()` |
| queue 挂接到 tag set | `block/blk-mq.c:4329`、`:4621` |
| tag set 与池的分配 | `block/blk-mq.c:4834`、`:4683`、`:4128` |
| driver tags 共享及无映射例外 | `block/blk-mq.c:4131`、`:4231`；`include/linux/blk-mq.h:690` 起的 flags |
| tag 池结构 | `include/linux/blk-mq.h:774` 的 `struct blk_mq_tags` |
| 调度器类型及实例定义 | `block/elevator.h` 的 `elevator_type`、`elevator_queue` |
| 类型注册、实例分配和默认调度器 | `block/elevator.c:498`、`:123`、`:729` |
| scheduler tag 容器、池与 hctx 关联 | `block/elevator.h:26`；`block/blk-mq-sched.c:504`、`:614` |
| 调度器移除时清理 sched_tags | `block/blk-mq-sched.c:384` |

## 验证

- SVG XML 解析、相对文件链接检查。
- WebKit 按各图原尺寸渲染：总图 `1600 × 1408`，原局部图 `1040 × 744` CSS px。
- 总图检查文字边界、卡片内文字、文字间重叠、连线与文字净距、无关节点碰撞、端点及连线交叉。
- 文字对比度至少 4.5:1；必要边界与关系线至少 3:1。
- 总图已渲染灰度预览；实体名称、数量、共享模式及可选关系不依赖色相辨识。
- 未做打印或色觉缺陷模拟；不同系统的字体回退仍可能改变文字宽度。
