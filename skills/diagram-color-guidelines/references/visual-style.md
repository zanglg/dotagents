# Typography, Geometry, and Lines

Use with [Palette and color roles](palette.md). Keep the visual grammar stable;
let composition change. Values below are useful starting tokens, not mandatory
measurements or acceptance tolerances.

## Size and visual weight

Work at the intended display or publication size. CSS px are not physical device
pixels; SVG user units equal CSS px only with a corresponding display scale.
A 1400-unit-wide SVG shown at 700 px halves its apparent sizes. Coordinate text,
strokes, arrows, dash patterns, and spacing rather than fixing strokes alone.
For print, use the required publication dimensions and pt sizes.

| Role | Starting value |
| --- | --- |
| Container stroke | 1 px |
| Card stroke | 1.5 px |
| Core card stroke | 2 px |
| Connector stroke | 2 px |
| Emphasized path stroke | 3 px |
| Guide stroke | 1 px |
| Focus ring stroke | 2 px |
| Card radius | 8 px |
| Container radius | 12 px |
| Card padding | 16 px |
| Container padding | 24 px |
| Content gap | 8 px |
| Card gap without line labels | 32 px |
| Parallel lane spacing | 16 px |
| Connector clearance from unrelated content | 8 px |
| Visible focus-ring gap | 3 px |
| Filled triangular arrow | 8 x 8 px |

Preserve the hierarchy of light containers, clear connectors, and deliberate
emphasis when adapting values. Use consistent role-level styles within a figure
instead of arbitrary per-object differences. Related figures should have
comparable apparent weight, not necessarily identical source numbers.

Use modest rounding for ordinary cards and containers. Tables, memory cells,
matrices, and domain notation may be square. Avoid decorative shadows, glows,
and double borders. A focus ring represents a state, not generic emphasis.
Spacing may follow a 4 px grid but must accommodate labels and content. Stroke
width signals emphasis unless explicitly mapped to a quantitative scale.

SVG normally scales as a whole. Use `vector-effect="non-scaling-stroke"` only
when fixed screen-width strokes are needed; check marker and dash sizing too.

## Typography anchors

| Role | Default family stack | Starting size / weight |
| --- | --- | --- |
| Figure title | `Georgia, "Times New Roman", serif` | 28 px / 700 |
| Group title | `Georgia, "Times New Roman", serif` | 18 px / 600 |
| Group label / supplementary tag | `Arial, Helvetica, Inter, sans-serif` | 13 px / 600 |
| Card title | `Georgia, "Times New Roman", serif` | 18 px / 600 |
| Subtitle | `Arial, Helvetica, Inter, sans-serif` | 16 px / 400 |
| Body and relationship label | `Arial, Helvetica, Inter, sans-serif` | 16 px / 400 |
| Annotation and metadata | `Arial, Helvetica, Inter, sans-serif` | 14 px / 400 |
| Code, address, and index | `"Courier New", "SFMono-Regular", "SF Mono", "Roboto Mono", monospace` | 14 px / 400 |

Maintain the heading/prose/code role distinction across independently produced
figures. A compatible replacement stack is acceptable when required by the
platform, language, user, or publisher. Check glyph coverage, available weights,
and actual width; these stacks do not guarantee identical cross-platform or
multilingual rendering. Monospace is for real code and technical identifiers,
not an excuse to add irrelevant API details.

Use a group title when the heading is the main way to identify or navigate a
section. A small group label is suitable for a short supplementary tag whose
context is already clear. Position and surrounding space distinguish a group
title from card titles even when they share a size. Do not demote a necessary
heading to a small label merely to fit a crowded layout.

Body line height starts around 1.4, with an 8 px heading/body gap. Adapt both to
content and final scale. Headings use size and weight to establish hierarchy;
coordinate their colors with body text as described in the palette reference.

Alignment is a composition choice, not a style invariant. Short concept cards
can center the heading and description as one block; lists and long descriptions
usually read better left-aligned. Choose coherently for comparable content.
Check rendered bounds and padding, not just anchors or baselines. Do not require
identical card sizes, force uppercase prose, or shrink labels to fit a template.
SVG multiline text needs explicit line positions or supported text layout;
CSS `line-height` alone does not create wrapping in ordinary SVG text.

### Chinese and mixed-language typography

For Simplified Chinese or mixed Chinese/Latin text, extend the font roles with
explicit CJK families. These are optional family choices, not installation
requirements; select an available compatible family when the tool lacks font
fallback stacks.

| Role | Suggested family stack |
| --- | --- |
| Titles | `Georgia, "Noto Serif CJK SC", "Source Han Serif SC", "Songti SC", serif` |
| Prose, group labels, and annotations | `Arial, "Noto Sans CJK SC", "Source Han Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif` |

Use region-appropriate families for Traditional Chinese. Keep the code role for
technical identifiers; Chinese text inside code or aligned cells needs a
CJK-capable monospace fallback and a check of actual column alignment. Do not
assume Chinese and Latin characters have equal advances.

Check mixed-script baselines, apparent weight, punctuation, and line breaks at
the final display size. For multiline Chinese or bilingual labels, start with
line height around 1.5 and adapt to the chosen fonts. Use language-appropriate
wrapping, avoiding stranded opening or closing punctuation; keep identifiers
intact where practical. Measure rendered bounds instead of estimating width
from character count. Font substitution or export can change wrapping, so
recheck padding and line spacing in the delivered format.

## Composition and routing

Choose a single figure, multiple panels, or separate figures based on clarity.
Preserve important relationships and use an overview or cross-references when
splitting would otherwise lose context. Shared objects retain their meanings
and style roles, but layouts need not match.

Use these composition checks as content-dependent guidance, not a fixed layout:

- **Reading order:** in an explanatory flow, make the entry point and main path
  easy to locate through placement and alignment, with restrained emphasis
  where useful. Comparison panels and peer categories may need equal weight
  instead of one dominant focal point. Do not invent a sequence or hierarchy.
- **Grouping:** keep related elements closer than unrelated groups where labels
  and routing permit. Use shared alignment and space before adding containers;
  retain any boundary needed to convey scope or another domain meaning.
- **White space:** reserve room around titles, between groups, and along labeled
  routes. Keep margins and comparable gaps coherent without forcing symmetry.
  Check for crowded corners and accidental empty regions; preserve space that
  helps explain separation or leaves a relationship traceable.
- **Visual weight:** let supporting containers recede so important content and
  connections remain prominent. Avoid emphasizing every box equally; preserve
  equal treatment when the content represents peers. Adjust placement, spacing,
  and grouping before increasing saturation or adding decoration.
- **Density:** keep essential text readable at the intended size. For crowded
  regions, reflow or expand the layout, move explanatory prose to a nearby
  caption, or split panels while keeping labels and cross-references clear.
  Do not remove needed information or add filler to equalize panel density.

Prefer the simplest readable route: a straight line when it works, a small
number of segments to avoid obstacles, organized orthogonal lanes where useful,
or curves for clear return paths, loops, and dense relationships. These are
options, not a mandatory sequence of experiments. Fixed ports, domain notation,
automatic-layout capabilities, and label space can justify a route directly.

Avoid crossings, excessive bends, and unrelated objects. Keep endpoints and
arrow directions obvious. A tidy appearance must not create a false connection
or hide a relationship. Orthogonal paths normally approach ports along the
boundary normal; other paths may use clear diagonal approaches.

For reciprocal relationships, prefer separate, traceable lanes when directions
have distinct labels or meanings. Parallel, balanced routes are useful defaults,
not a requirement to rearrange every diagram. Fixed ports and obstacles may
justify different paths. A single double-headed arrow is suitable for one
symmetric relationship whose directional behaviors need not be distinguished.
An undirected association uses no arrow. Do not imply timing or simultaneity
through arrow choice alone.

## Line and boundary semantics

Geometry answers how a line travels; its style answers what it means. Bending a
line does not make the relationship optional. Define only the styles needed.

| Style | Default relationship meaning | Default boundary meaning |
| --- | --- | --- |
| Solid | Explicit modeled relationship or path | Explicit modeled object or boundary |
| Dashed | Optional, conditional, or hypothetical relationship | Optional, conditional, hypothetical, or planned object/group |
| Dotted | Annotation or explanatory association | Explanatory logical grouping, not an independent execution boundary |

Label the relevant condition or grouping when it is not obvious. Domain
standards override these defaults with a clear legend or local explanation;
data-series dash styles identify series rather than optional relationships.
A security, process, deployment, or address boundary needs an accurate label,
not an inferred meaning from its appearance.

Do not use dashed lines merely for reverse direction, secondary importance,
asynchrony, distance, or decoration. Do not change an error relationship's line
style unless its underlying relationship meaning changes. A conditional parent
boundary does not automatically make every child dashed.

Starting SVG patterns:

- Solid: no `stroke-dasharray`.
- Dashed: `stroke-dasharray="6 4"`, `stroke-linecap="butt"`.
- Dotted: `stroke-dasharray="0 6"`, `stroke-linecap="round"`; use equally spaced
  circles if the renderer does not support zero-length round dots.
- Ordinary lines: `stroke-linecap="butt"`, `stroke-linejoin="round"`.

Keep dash rhythm recognizable at final size. A short line that cannot show a
recognizable pattern needs a clear label or another semantic cue, not forced
extra length solely to satisfy a token. Border widths follow their object roles,
not connector widths. Borderless grouping is acceptable with clear spacing and
titles, but not when an exact boundary is essential.

## Arrows, intersections, and labels

Default arrows are simple filled triangles sharing the line's color. Keep their
apparent size consistent for comparable relationships; a thicker emphasis line
need not automatically have a larger arrow. Domain notation may use other
markers with their established meanings.

For SVG, `markerUnits="userSpaceOnUse"` and `orient="auto-start-reverse"` help
control size and direction; align `refX` and `refY` to the tip. Account for the
whole figure's scale. Place the tip at the intended boundary or port, not inside
text. Keep a clear terminal direction and prevent arrow/label overlap.

A crossing is not a connection. Explicit junctions can use filled dots (starting
at 4 px diameter, adjusted for stroke weight). Distinguish them from repeated
dotted-line marks. Reduce ambiguous crossings through layout or routing; do not
add decorative bridge arcs without a reason.

Keep labels near their own lines, clear of arrows, bends, and adjacent lanes.
Parallel-line labels can sit outside the lanes or at separate readable segments.
Masking labels use the local background color with modest padding. Move content,
change routing, or expand the layout rather than making essential labels tiny.

## Applying the constraints

- A two-card request/response figure may use centered text and parallel arrows.
- A dense dependency graph may use left-aligned cards and orthogonal routes.
- A memory illustration may use square cells and an external current pointer.
- A data chart may use domain-standard axes, markers, and series dash patterns.

These figures can share typography roles, neutral surfaces, muted accents, and
line weight without sharing a template. Review them with the
[delivery checks](../SKILL.md#delivery-checks), not pixel-by-pixel equality.
