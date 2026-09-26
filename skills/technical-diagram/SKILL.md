---
name: technical-diagram
description: Create clean, restrained, publication-quality technical diagrams and portable SVGs for systems, architecture, data flow, memory layout, pointer graphs, algorithms, firmware, virtualization, and related engineering topics. Use when the user asks to draw, redesign, or standardize a technical diagram.
---

# Technical Diagram

Version: 0.1.2
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
Borders and connectors define focus.
Lines define relationships.
Position and visual balance define architecture.

Focus should be expressed primarily through position, border weight, and
connector emphasis. Do not rely on a blue fill alone.

Color must not carry information that layout, labels, line style, or containment
can express more clearly.

## Overall visual character

Default to an editorial technical figure rather than a UI-style engineering
dashboard. The default visual language should feel restrained, serious, and
publication-ready.

The result should feel like:

- systems-paper figures
- kernel or firmware documentation
- technical textbook illustrations
- editorial technical figures with a deliberate visual axis
- precise engineering documentation

Use the documentation / UI-neutral variant only when the user explicitly asks
for a slide-like, dashboard-like, or product-documentation presentation.

It should not feel like:

- a marketing presentation
- an enterprise dashboard
- a colorful infographic
- a card-heavy product UI

Keep the canvas predominantly white. Default to neutral surfaces plus at most
one muted accent family. Use additional semantic tones only when they encode a
real distinction that position, labels, containment, or line style cannot
express clearly.

Color should feel close to neutral. If a fill is noticeable before the structure
is noticeable, it is too strong.

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

When the subject supports it, establish a strong implicit visual axis or
compositional center. Mirrored peer groups may flank a focal center, but do not
force symmetry when the content does not support it.

Use equal dimensions for true peers when that improves scanning. Do not
normalize every box to the same size. Focal containers and central objects may
be larger when hierarchy or content justifies it.

Preserve balance even when the composition is intentionally asymmetric.
Auxiliary elements such as legends and notes must not accidentally read as an
additional peer component.

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

These are deliberately near-neutral visual resources. They do not have
permanent domain meanings.

| Tone | Fill | Border | Accent |
| --- | --- | --- | --- |
| Blue | #F1F5F8 | #C8D4DE | #607689 |
| Green | #F1F6F3 | #C9D7CF | #63796D |
| Sand | #F7F4EF | #D9D0C4 | #7A7063 |
| Violet | #F5F3F6 | #D5CFD8 | #766E7C |
| Teal | #F0F6F5 | #C7D7D5 | #607C79 |
| Slate | #F2F4F6 | #CBD2D9 | #63717E |
| Amber | #F7F5EF | #DCD5C4 | #7B7462 |

Do not assume, for example, that green always means queues or sand always means
drivers. The model must infer the local grouping from the current diagram.

### Semantic tone assignment policy

For each diagram:

1. Start neutral.
2. Use zero or one muted accent family by default.
3. Add a second semantic tone only when it materially reduces reading effort.
4. Add a third tone only when the diagram contains a real third taxonomy that
   cannot be expressed cleanly by position, containment, labels, or line style.
5. Keep the same local group on the same tone.
6. Do not create one color per object.
7. Nested objects do not automatically require a new color.
8. More diagram complexity is not a reason to add more colors.

Typical usage:

- simple figure: neutral only, or neutral plus 1 tone
- medium figure: neutral plus 1 tone
- complex figure: neutral plus 1 to 2 tones
- exceptional taxonomy-heavy figure: up to 3 tones

Treat more than 3 semantic tones as a design warning that requires a strong
reason.

The palette should occupy much less visual area than the white and neutral
surfaces.

### Visual area balance

Use these as visual heuristics rather than geometric targets:

- white and neutral surfaces should clearly dominate the figure
- muted semantic fills should occupy a minority of the canvas
- focus accents should be sparse and concentrated
- error or warning color should remain exceptional

Do not optimize a diagram to fixed color-area percentages. Judge balance at the
intended viewing size.

## State semantics

State semantics are global and may remain stable across domains.

### Active or current

Use focus color sparingly. In static architecture diagrams, do not introduce an
active/current treatment unless the figure actually depicts a current state,
selected object, or active path.

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

Choose one primary text profile per figure and use it consistently.

Editorial / academic profile — default:

- Source Serif 4
- Charter
- Georgia
- Times New Roman
- serif fallback

Use this profile by default for architecture, systems, kernel, firmware, memory,
and data-structure figures intended to look like a paper or textbook figure.

Documentation / UI-neutral profile — opt in when appropriate:

- IBM Plex Sans
- Inter
- Helvetica Neue
- Arial
- sans-serif fallback

Use the documentation profile when the user explicitly asks for a slide-like,
dashboard-like, web-product, or UI-neutral engineering-documentation style.

Do not mix serif and sans-serif merely to add visual variety.

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

### Box proportions

Use repeated dimensions to reinforce peer relationships, not as a blanket grid
rule.

Allow focal or central components to be larger than surrounding peers when
doing so strengthens hierarchy. Avoid making every object the same width and
height when that produces a dashboard-like or spreadsheet-like rhythm.

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

Wide layer containers may span most of the canvas when they express a real
architectural layer. Keep their fill nearly white, keep their border quiet, and
anchor the section title consistently so whitespace remains the dominant
separator.

Inside a focal container, do not box every subordinate concept by default.
Prefer typography, spacing, or a light divider when another nested rectangle
would make the figure feel like a card UI.

Put most semantic color on a small number of focal entities. Supporting entities
should usually remain white or neutral rather than each receiving their own
tone.

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

The default connector is a straight line. Routing should look engineered rather
than decorative.

Prefer routing in this order:

1. straight line when source and target can be connected cleanly
2. one-bend orthogonal polyline when a straight line would cross content or
   create an awkward attachment point
3. a simple two-segment orthogonal route when one bend is insufficient
4. a single shallow curve only when it expresses one smooth directional change
   more clearly than an elbow

Prefer the primary reading direction for long relationships. Short local
vertical lines are normal when they directly connect stacked entities, but avoid
using long bare vertical connectors as the default way to cross multiple
regions.

A permitted curve should resemble one restrained arc or one smooth bend. It may
be useful for:

- a centered fan-out or fan-in
- connecting a central object to a laterally offset lower or upper object
- avoiding one crowded region without introducing several orthogonal elbows
- a small number of long cross-layer references where a shallow arc improves
  separation

Do not use:

- S-shaped connectors
- serpentine or multi-inflection curves
- curves with several bends
- decorative waves
- a curved route when a single clean straight or elbow route is equally clear

When a bend is needed and a curve offers no clear readability advantage, prefer
the orthogonal polyline because it feels more precise and serious.

Short, symmetric diagonal straight connectors are acceptable when they make a
centered fan-out or fan-in clearer. Reduce long diagonal lines and use them only
when they improve the composition.

### Connection points

Prefer connector paths with zero or one directional change. Two changes are
acceptable when required by obstacle avoidance; more than two should trigger a
layout reconsideration.

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

- use 13 to 14 px text from the figure's primary text profile, or monospace for
  literal function / field / API names
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

## Legends and auxiliary elements

Prefer direct labels when a separate legend is unnecessary.

When a legend is needed:

- make it visually smaller and lighter than primary entities
- place it outside subsystem interiors when practical, or reserve a dedicated
  margin for it
- align it to the outer layout grid
- avoid a corner placement that makes an otherwise balanced composition feel
  bottom-heavy or side-heavy
- do not style it so similarly to entities that it reads as another component

The same rules apply to scale keys, notation keys, and other auxiliary panels.

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

Version 0.1.2 is portable SVG first.

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

For version 0.1.2, prefer literal CSS values in the SVG style element rather than
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
2. choose the composition strategy and primary visual axis
3. start from neutral surfaces and decide whether one accent tone is actually
   needed
4. establish typography and text bounds
5. size boxes around text and hierarchy
6. establish subsystem layout and overall balance
7. reserve space for legends and auxiliary annotations when needed
8. route connectors with straight lines first, then minimal-bend polylines, and
   only rarely a single shallow curve
9. add active or error state only if semantically justified
10. enlarge the canvas when needed rather than squeezing content
11. produce editable vector SVG when SVG is requested
12. validate the result against the QA checklist

When the user supplies their own explicit visual constraints, follow them unless
they conflict with the requested output format or make the diagram unreadable.

## QA checklist

Before finalizing, verify all of the following.

### Structure

- Is there one clear primary reading direction?
- Is there a clear visual axis or compositional center where appropriate?
- Are related entities grouped spatially?
- Are different subsystems separated by meaningful whitespace?
- Are true peers visually consistent without forcing every box to be identical?
- Is deliberate asymmetry still compositionally balanced?
- Are legends and auxiliary elements visually subordinate?
- Is containment understandable without color?
- Would the main architecture remain understandable in grayscale?

### Text

- Does every text block fit fully inside its border?
- Is there at least about 12 px of safe inner clearance where practical?
- Are field lists using readable line height?
- Are logical multiline labels represented as single text objects?
- Is one primary typography profile used consistently?
- If a serif profile is used, is it still readable at normal viewing scale?
- Is the text still readable at normal viewing scale?

### Color

- Is the canvas predominantly white?
- Are large containers neutral?
- Would neutral-only rendering still preserve the primary structure?
- Is there a clear reason for every semantic tone that is present?
- Is the figure using neutral plus no more than 1 to 2 tones in ordinary cases?
- Are supporting entities left neutral rather than colored individually?
- Is the number of tones minimal?
- Does every local tone mapping remain consistent?
- Is blue focus used only for active or current state?
- Is error color used only for real error or invalid state?

### Borders and geometry

- Are normal entity borders about 1.2 px?
- Are structural container borders about 1.35 px?
- Are active borders about 1.7 px?
- Are corner radii small?
- Are box proportions driven by hierarchy and peer relationships rather than a
  uniform grid?
- Are subordinate concepts left unboxed when another rectangle would add no
  useful structure?
- Does the figure avoid UI-card styling?

### Connectors

- Are normal relationships solid?
- Are optional or weak relationships dashed?
- Are contextual relationships dotted?
- Is the active path the only ordinary use of blue connectors?
- Are arrowheads small and consistent?
- Do connectors avoid passing through text?
- Are crossings minimized?
- Could each connector be a straight line?
- If not, could it use a single orthogonal bend?
- Are routes with more than two directional changes eliminated?
- Are long bare vertical connectors avoided when they merely bridge distant
  regions?
- If a curve is used, is it a single shallow arc with one directional change?
- Are S-curves, serpentine routes, and decorative waves absent?

### SVG portability

- Is the output true vector SVG?
- Is there no embedded raster version of the whole diagram?
- Is text still text?
- Are there no editor-specific namespaces or attributes?
- Are visual classes domain-neutral?
- Does the SVG use standard elements and standard styling?
- Is the file understandable and editable without a specific editor?

## Version 0.1.2 notes

This patch makes the default visual language more specific and reproducible.
It refines visual composition rather than domain semantics.

Changes from 0.1.1:

- make the editorial / academic technical profile the default for systems,
  architecture, kernel, firmware, memory, and data-structure figures
- make the sans-serif documentation / UI-neutral profile an explicit opt-in
  variant when that presentation is requested
- move to a neutral-first palette with materially lower-saturation semantic
  tones
- reduce ordinary color usage to neutral plus 0 to 2 semantic tones; more than
  3 tones now requires an exceptional justification
- make straight connectors the default
- prefer a one-bend orthogonal polyline when a straight connector is blocked
- allow only a restrained single shallow curve when one smooth directional
  change is clearer than an elbow
- explicitly reject S-curves, serpentine routes, and multi-inflection connector
  shapes
- discourage long bare vertical connectors that cross multiple visual regions
- strengthen connector QA around bend count and curve shape
- keep supporting entities neutral so hierarchy comes primarily from layout,
  whitespace, typography, borders, and connector geometry

During trial use, continue observing:

- which constraints are repeatedly violated by generated diagrams
- whether the palette needs adjustment
- whether text sizing rules need stronger measurement requirements
- whether routing rules need additional patterns
- whether SVG portability requirements are too strict or too loose
- whether recurring use cases justify supporting reference files or validators

Do not expand the style vocabulary merely because a new technical domain is
introduced. Add a new global rule only when it represents a reusable visual
concept across domains.
