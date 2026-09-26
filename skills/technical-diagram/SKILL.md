---
name: technical-diagram
description: Create clean, restrained, publication-quality technical diagrams and portable SVGs for systems, architecture, data flow, memory layout, pointer graphs, algorithms, firmware, virtualization, and related engineering topics. Use when the user asks to draw, redesign, or standardize a technical diagram.
---

# Technical Diagram

Version: 0.1.0
Status: experimental

This skill defines visual grammar, not domain ontology.

Use it to produce technical diagrams that remain suitable for systems papers,
technical books, engineering documentation, white-background slides, web pages,
and PDF output. The same visual system should work across domains such as kernel
internals, firmware, virtualization, hardware architecture, memory systems,
storage, networking, and algorithms without adding domain-specific style tokens.

## Design priorities

Apply decisions in this order:

1. clarity
2. structure
3. hierarchy
4. alignment
5. spacing
6. typography
7. color
8. decoration

White space defines structure.
Neutral tones define hierarchy.
Muted tones distinguish local semantic groups.
Blue defines focus.
Lines define relationships.
Position defines architecture.

Color must not carry information that layout, labels, line style, or containment
can express more clearly.

## Overall visual character

The result should feel like:

- systems-paper figures
- kernel or firmware documentation
- technical textbook illustrations
- precise engineering documentation

It should not feel like:

- a marketing presentation
- an enterprise dashboard
- a colorful infographic
- a card-heavy product UI

Keep the canvas predominantly white. Use low-saturation color only where it
materially improves comprehension.

Do not use:

- gradients
- shadows
- glow
- 3D effects
- skeuomorphism
- decorative illustrations
- large rounded cards
- saturated categorical palettes
- large colored subsystem backgrounds
- ornamental icons unless the diagram specifically requires them

## Workflow

Before drawing, perform these steps in order.

### 1. Model the content

Identify:

- the primary entities
- containment or ownership boundaries
- relationships and flows
- transient versus long-lived objects when relevant
- execution contexts or actors when relevant
- current or active state when relevant
- annotations needed to explain non-obvious behavior

Do not assign colors yet.

### 2. Choose one primary reading direction

Prefer one of:

- left to right
- top to bottom

Do not create two competing primary axes.

### 3. Build the structural layout

Use:

- position
- containment
- whitespace
- alignment
- titles
- borders
- connectors

to express the architecture before introducing color.

### 4. Determine text sizing before box sizing

Always size in this order:

font
-> font size
-> line height
-> rendered text bounds
-> padding
-> box bounds
-> local layout
-> overall layout

Never choose a small fixed box first and then force text into it.

If the diagram does not fit, prefer a larger canvas before reducing text below
the recommended readable sizes.

### 5. Assign local semantic tones

Only after structure is clear, identify the minimum number of semantic groups
whose distinction would materially improve reading speed.

Assign those groups to the available muted tones.

Tone meaning is local to the current diagram. No tone has a permanent technical
meaning across diagrams.

### 6. Add relationship semantics

Choose solid, dashed, or dotted lines according to relationship meaning.
Use the focus blue only for current or active paths.

### 7. Validate

Run the QA checklist at the end of this document before finalizing.

## Color system

### Neutral foundation

| Role | Value |
| --- | --- |
| Canvas | #FFFFFF |
| Surface 1 | #F8FAFB |
| Surface 2 | #F2F5F7 |
| Surface 3 | #E9EEF2 |
| Normal border | #CBD2D8 |
| Strong border | #9AA6B2 |
| Primary text | #20262D |
| Secondary text | #5F6B76 |
| Muted text | #7D8892 |
| Normal connector | #66737F |

Never use pure black as the default text color.

Neutral depth should progress gradually:

#FFFFFF -> #F8FAFB -> #F2F5F7 -> #E9EEF2

Avoid abrupt jumps from white to medium or dark gray.

### Muted tone palette

These are visual resources only. They do not have permanent domain meanings.

| Tone | Fill | Border | Accent |
| --- | --- | --- | --- |
| Blue | #EAF0F5 | #B7C8D7 | #506E87 |
| Green | #EAF3EF | #B6CDBF | #557664 |
| Sand | #F4EEE7 | #D6C5B3 | #806A52 |
| Violet | #F1EDF3 | #CBBFD1 | #705F78 |
| Teal | #E8F2F1 | #AECBC8 | #4D7470 |
| Slate | #EDF0F4 | #BEC7D1 | #596A7B |
| Amber | #F5F1E5 | #D9CCA8 | #7B704C |

Do not assume, for example, that green always means queues or sand always means
drivers. The model must infer the local grouping from the current diagram.

### Semantic tone assignment policy

For each diagram:

1. Start neutral.
2. Identify the minimum useful number of semantic groups.
3. Assign muted tones only to groups that benefit from fast visual distinction.
4. Keep the same local group on the same tone.
5. Prefer layout and containment before adding another tone.
6. Do not create one color per object.
7. Nested objects do not automatically require a new color.
8. Use no more than 4 to 6 semantic tones in a figure unless there is a strong
   reason to exceed that range.

Typical usage:

- simple figure: 1 to 3 tones
- medium figure: 2 to 4 tones
- complex figure: 3 to 6 tones

The palette should usually occupy less area than the white and neutral surfaces.

### Recommended area balance

Approximate target:

- white and neutral surfaces: 65 to 75 percent
- muted semantic entity fills: 20 to 28 percent
- active focus accents: 3 to 5 percent
- error or warning color: below 2 percent

These are visual balance targets, not geometric requirements.

## State semantics

State semantics are global and may remain stable across domains.

### Active or current

Use for:

- selected object
- current iteration
- current pointer
- active execution path
- current memory range
- current data path
- immediate focus

| Property | Value |
| --- | --- |
| Fill when needed | #E8EEF4 |
| Border | #4F6F8F |
| Text | #39566F |
| Connector | #4F6F8F |

If an entity already has a local semantic fill, preserve that fill when possible
and indicate active state primarily with the blue border and blue connector.

This keeps two dimensions separate:

- fill answers: what group is this in?
- border and line answer: what is active now?

### Error or invalid

Use only when the diagram truly expresses failure, invalid state, stale
reference, or exceptional behavior.

| Property | Value |
| --- | --- |
| Fill | #F6ECEC |
| Border | #875C5C |
| Text | #875C5C |

Do not use red merely to increase visual variety.

## Typography

### Font families

For titles, section headings, labels, and annotations, prefer:

- IBM Plex Sans
- Inter
- Helvetica Neue
- Arial
- sans-serif fallback

For structures, fields, addresses, offsets, code-like names, and values, prefer:

- IBM Plex Mono
- JetBrains Mono
- SFMono-Regular
- Consolas
- Liberation Mono
- monospace fallback

Do not embed font files.
Do not convert text to paths.

### Recommended sizes

| Role | Size | Weight |
| --- | --- | --- |
| Figure title | 26 to 28 px | 600 |
| Section title | 19 to 21 px | 600 |
| Entity title | 16 to 17 px | 600 |
| Field or code | 14 to 15 px | 400 |
| Relationship label | 13 to 14 px | 400 or 500 |
| Annotation | 13 to 14 px | 400 |
| Weak metadata | 12 to 13 px | 400 |

Prefer no more than four visually dominant size levels in one figure.

### Text rules

One logical text region should be one SVG text object.

For multiline text, use one text element containing multiple tspan elements.

Do not simulate one logical text box with many unrelated text elements.
Do not merge multiple independent labels into one oversized text object.

## Box sizing and spacing

### Minimum padding

| Measurement | Recommended value |
| --- | --- |
| Entity horizontal padding | 16 px |
| Entity vertical padding | 14 to 16 px |
| Entity title to body gap | 10 to 12 px |
| Field line height | 20 to 22 px |
| Minimum safe inner clearance | 12 px |
| Section padding | 20 to 24 px |

Text must not touch or cross borders.

When exact rendered text measurements are available, use them to determine box
size. When they are not available, err on the side of larger boxes.

### Spacing scale

Use an 8 px base rhythm.

Prefer:

- 8 px
- 16 px
- 24 px
- 32 px
- 48 px
- 64 px

Keep distances within a group smaller than distances between subsystems.

Do not try to fill the whole canvas. Empty white regions are part of the visual
structure.

## Borders

### Widths

| Border role | Width |
| --- | --- |
| Very light separator | 0.8 px |
| Normal entity | 1.2 px |
| Structural container | 1.35 px |
| Active entity | 1.7 px |
| Error entity | 1.5 px |

### Corner radius

| Object | Radius |
| --- | --- |
| Normal entity | 4 px |
| Large container | 5 px |
| Array or memory cell | 2 to 4 px |
| Annotation box | 4 px |

Keep technical diagrams close to rectilinear geometry.
Avoid pill shapes and large card-like radii.

## Containers

Large subsystem or section containers should visually recede.

Preferred:

- fill #FFFFFF, or
- fill #F8FAFB when a light surface is needed
- border #CBD2D8
- structural width about 1.35 px

Do not fill an entire large subsystem with a semantic tone merely because its
contained entities share a group.

Put most semantic color on the entities themselves.

For neutral nesting, prefer:

#FFFFFF
-> #F8FAFB
-> #F2F5F7
-> #E9EEF2

Use color only when neutral hierarchy is insufficient.

## Connectors

### Base styles

| Relationship | Color | Width | Style |
| --- | --- | --- | --- |
| Normal | #66737F | 1.6 px | solid |
| Weak or optional | #7D8892 | 1.4 px | dashed |
| Contextual or logical | #7D8892 | 1.4 px | dotted |
| Active path | #4F6F8F | 1.9 px | solid |
| Error path | #875C5C | 1.7 px | solid or dashed as appropriate |
| Guide line | #7D8892 | 1.2 to 1.3 px | solid or dotted |

### Dash patterns

Weak or optional:

stroke-dasharray: 6 5

Contextual or logical:

stroke-dasharray: 2 4

Do not use color alone to distinguish relationship types.

### Relationship semantics

Use solid lines for:

- direct references
- ownership
- ordinary pointers
- normal data or control flow
- direct structural relationships

Use dashed lines for:

- optional relationships
- policy-dependent relationships
- weak references
- deferred or indirect relationships

Use dotted lines for:

- contextual relationships
- operates-on relationships
- explanatory logical mappings
- non-owning conceptual relations

Use blue solid lines only when the relationship itself is active or currently
being emphasized.

Do not color a connector merely because the connected entity has a semantic
tone.

## Routing geometry

Prefer routing in this order:

1. horizontal straight line
2. vertical straight line
3. orthogonal polyline with 90-degree turns
4. curve only when necessary

Use curves sparingly for:

- avoiding crowded regions
- long cross-layer references
- a small number of back edges
- pointer graphs where orthogonal routing would create more crossings

Do not use decorative curves on normal architecture relationships.

Reduce long diagonal lines. Prefer orthogonal routes for long connections.

### Connection points

Attach connectors preferentially at the center of:

- left edge
- right edge
- top edge
- bottom edge

Avoid random corner attachment.
Never route connectors through text.

For left-to-right diagrams, prefer right-edge output and left-edge input.
For top-to-bottom diagrams, prefer bottom-edge output and top-edge input.

If too many connectors accumulate on one side of a box, restructure the layout
or introduce a clear hub instead of stacking unreadable lines.

## Arrowheads

Use small, simple filled triangular arrowheads.

Recommended nominal size:

- length: 7 px
- width: 6 px

Arrowheads use the same color as their connector.

Do not use:

- oversized arrowheads
- ornamental arrow shapes
- heavy block arrows
- decorative double arrows

Use bidirectional arrows only when the relationship is truly bidirectional.

Some contextual guide lines and containment guides may omit arrowheads.

## Line cap and join

Prefer:

- stroke-linecap: round
- stroke-linejoin: round

This softens line geometry without making the figure decorative.

## Connector labels

Relationship labels should normally:

- use 13 to 14 px sans-serif text
- use #5F6B76
- sit approximately 4 to 8 px away from the connector
- avoid overlapping the line
- avoid colored pill backgrounds

If a dense connector field makes text hard to read, a small white or #F8FAFB
background behind the label is acceptable.

## Annotations

### Ordinary annotation

- text: #5F6B76
- fill: none or white
- border: none or #CBD2D8 at about 1 px

### Weak annotation

- text: #7D8892
- no border by default

### Focus annotation

When an annotation directly explains the active path:

- fill: #E8EEF4
- border: #4F6F8F
- text: #39566F
- border width: about 1.3 px

Annotations should explain the diagram, not compete with its primary entities.

## Memory, array, and range diagrams

Recommended fills:

| State | Fill |
| --- | --- |
| Empty | #FFFFFF |
| Ordinary allocated | #F2F5F7 |
| Semantic memory region | choose a local muted tone, often Teal when appropriate |
| Current range | #E8EEF4 |
| Consumed | #F2F5F7 plus hatch |
| Invalid | #F6ECEC |

Ordinary boundary:

#CBD2D8

Current boundary:

#4F6F8F

Addresses, offsets, indexes, and raw values should normally use monospace text
in #5F6B76. Current addresses or indexes may use #39566F.

Prefer a neutral hatch for consumed ranges instead of inventing another color.

## Pointer and object graphs

Keep objects neutral or locally tone-grouped.
Do not assign one unique color to each node.

Pointer semantics:

| Pointer | Appearance |
| --- | --- |
| Normal | solid #66737F |
| Current | solid #4F6F8F |
| Weak | dashed #7D8892 |
| Invalid | #875C5C, dashed or solid according to meaning |

Pointer color describes relationship state, not target category.

## Portable SVG profile

Version 0.1.0 is portable SVG first.

Do not add editor-specific namespaces or metadata.

Do not rely on:

- Inkscape attributes
- Sodipodi attributes
- editor-specific path effects
- editor-specific flowed text
- proprietary connector metadata

### Preferred standard SVG elements

Use the smallest sufficient subset of standard SVG:

- svg
- g
- rect
- circle
- ellipse
- line
- polyline
- polygon
- path
- text
- tspan
- defs
- style
- marker
- pattern
- title
- desc

Use clipPath, symbol, or use only when they materially simplify the diagram and
do not reduce editability.

Avoid by default:

- filter
- mask
- foreignObject
- embedded raster images
- JavaScript
- animation
- complex clipping
- textPath

### SVG grouping

Organize the file using standard g elements and stable ids.

A useful high-level order is:

1. background
2. header
3. containers
4. entities
5. connectors
6. labels
7. annotations
8. details

Individual logical modules may use their own nested g groups.

Use id for object identity within the current diagram.

Do not use CSS class names as a domain ontology.

Good visual classes include concepts such as:

- entity
- container
- tone-blue
- tone-green
- tone-sand
- tone-violet
- tone-teal
- tone-slate
- tone-amber
- state-active
- state-error
- connector-normal
- connector-weak
- connector-context
- connector-active
- text-title
- text-section
- text-entity
- text-field
- text-label
- text-annotation

Avoid global style classes such as:

- driver
- queue
- firmware
- hypervisor
- database
- CPU

Those belong to diagram content, not the visual style system.

### SVG styles

For version 0.1.0, prefer literal CSS values in the SVG style element rather than
requiring CSS custom properties.

For example, a tone class should resolve directly to its fill and stroke values.

This maximizes compatibility with SVG renderers and conversion tools.

### Text editability

Keep all text as text.

Do not:

- rasterize text
- convert text to paths
- embed the entire diagram as an image

A logical multiline label should remain one text object with tspan children.

## Canvas sizing

Do not force a diagram into an arbitrary fixed size if doing so causes:

- unreadably small text
- insufficient padding
- cramped connectors
- excessive crossings
- clipped labels

Preferred response to insufficient space:

1. increase canvas size
2. improve grouping
3. restructure routing
4. reduce unnecessary annotation
5. only then consider modest text reduction

Readable text and correct box sizing take priority over a predetermined image
dimension.

## Local semantic mapping example

The style system does not know what technical entities mean.

A diagram may locally decide:

- Group A -> Blue
- Group B -> Green
- Group C -> Sand
- Group D -> Violet

A different diagram may reuse those tones for entirely different semantic
groups.

The only requirement is internal consistency within the current figure.

The model should be able to use this skill for unrelated technical subjects
without extending the global palette vocabulary.

## Output behavior

When asked to create a technical diagram:

1. infer the local semantic groups from the user's content
2. choose the minimum useful tone mapping
3. establish typography and text bounds
4. size boxes around text
5. establish subsystem layout
6. route connectors
7. add active or error state only if semantically justified
8. enlarge the canvas when needed rather than squeezing content
9. produce editable vector SVG when SVG is requested
10. validate the result against the QA checklist

When the user supplies their own explicit visual constraints, follow them unless
they conflict with the requested output format or make the diagram unreadable.

## QA checklist

Before finalizing, verify all of the following.

### Structure

- Is there one clear primary reading direction?
- Are related entities grouped spatially?
- Are different subsystems separated by meaningful whitespace?
- Is containment understandable without color?
- Would the main architecture remain understandable in grayscale?

### Text

- Does every text block fit fully inside its border?
- Is there at least about 12 px of safe inner clearance where practical?
- Are field lists using readable line height?
- Are logical multiline labels represented as single text objects?
- Is the text still readable at normal viewing scale?

### Color

- Is the canvas predominantly white?
- Are large containers neutral?
- Is semantic color concentrated on entities rather than giant background areas?
- Is the number of tones minimal?
- Does every local tone mapping remain consistent?
- Is blue focus used only for active or current state?
- Is error color used only for real error or invalid state?

### Borders and geometry

- Are normal entity borders about 1.2 px?
- Are structural container borders about 1.35 px?
- Are active borders about 1.7 px?
- Are corner radii small?
- Does the figure avoid UI-card styling?

### Connectors

- Are normal relationships solid?
- Are optional or weak relationships dashed?
- Are contextual relationships dotted?
- Is the active path the only ordinary use of blue connectors?
- Are arrowheads small and consistent?
- Do connectors avoid passing through text?
- Are crossings minimized?
- Are curves used only when they improve clarity?

### SVG portability

- Is the output true vector SVG?
- Is there no embedded raster version of the whole diagram?
- Is text still text?
- Are there no editor-specific namespaces or attributes?
- Are visual classes domain-neutral?
- Does the SVG use standard elements and standard styling?
- Is the file understandable and editable without a specific editor?

## Version 0.1.0 notes

This is intentionally an experimental first version.

During trial use, prioritize observing:

- which constraints are repeatedly violated by generated diagrams
- whether the palette needs adjustment
- whether text sizing rules need stronger measurement requirements
- whether routing rules need additional patterns
- whether SVG portability requirements are too strict or too loose
- whether recurring use cases justify supporting reference files or validators

Do not expand the style vocabulary merely because a new technical domain is
introduced. Add a new global rule only when it represents a reusable visual
concept across domains.
