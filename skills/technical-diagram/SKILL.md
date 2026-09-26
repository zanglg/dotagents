---
name: technical-diagram
description: Create clean, restrained, publication-quality technical diagrams and portable SVGs for systems, architecture, data flow, memory layout, pointer graphs, algorithms, firmware, virtualization, and related engineering topics. Use when the user asks to draw, redesign, or standardize a technical diagram.
---

# Technical Diagram

Version: 0.1.1
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
A single muted accent family provides optional emphasis.
Border weight and line style define focus.
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

The visual target is academic rather than product-oriented: restrained,
rectilinear, information-dense without being crowded, and suitable for figures
in systems papers, research reports, and technical textbooks.

Hierarchy should come primarily from:

1. position and containment
2. whitespace and alignment
3. typography
4. border weight and line style
5. luminance
6. color

Color is a secondary hierarchy channel. The first impression should be the
structure of the figure; chromatic color should be noticed only afterward.

A single figure should normally use at most one chromatic hue family. Neutral
gray does not count as a hue family. Error or warning colors are exceptions and
must appear only when the content actually expresses an exceptional state.

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

### 5. Decide whether an accent family is needed

Only after structure is clear, decide whether chromatic color would materially
improve reading speed.

If color is useful, choose one low-saturation accent family for the entire
figure. Use neutral surfaces, tint strength, border weight, labels, and
containment to distinguish additional groups.

Accent-family choice is local to the current diagram. No family has a permanent
technical meaning across diagrams.

### 6. Add relationship semantics

Choose solid, dashed, or dotted lines according to relationship meaning.
Use the selected accent family only for current or active paths when chromatic
emphasis is needed.

### 7. Validate

Run the QA checklist at the end of this document before finalizing.

## Color system

### Neutral foundation

| Role | Value |
| --- | --- |
| Canvas | #FFFFFF |
| Surface 1 | #FAFAF9 |
| Surface 2 | #F3F4F4 |
| Surface 3 | #EAECED |
| Normal border | #C8CDD1 |
| Strong border | #9AA3A9 |
| Primary text | #252A2E |
| Secondary text | #626A70 |
| Muted text | #6D7882 |
| Normal connector | #68727A |

Never use pure black as the default text color.

Neutral depth should progress gradually:

#FFFFFF -> #FAFAF9 -> #F3F4F4 -> #EAECED

Avoid abrupt jumps from white to medium or dark gray.

### Selectable accent families

These are alternative visual families, not simultaneous semantic categories.
Choose at most one family for an ordinary figure.

| Family | Fill | Border | Accent |
| --- | --- | --- | --- |
| Blue-gray | #E7EDF0 | #B7C3C9 | #667F8D |
| Sage | #E9EEEA | #BBC6BE | #65786B |
| Slate | #E9ECEF | #BBC2C8 | #626F79 |
| Warm gray | #EEECE8 | #C8C1B7 | #766E63 |

Blue-gray is the default when no other family is justified.

Do not assign a different hue to every semantic category. If multiple local
groups need distinction, first use position, containment, neutral surface depth,
border treatment, labels, or different tint strengths within the selected
family.

### Chromatic restraint

For each diagram:

1. Start entirely neutral.
2. Determine whether color materially improves comprehension.
3. If color is useful, choose one accent family.
4. Use the palest fill for large areas and stronger accent values only on small
   borders, connectors, or focused details.
5. Keep unrelated entities neutral rather than inventing another hue.
6. Nested objects do not automatically require a new color.
7. Do not create one color per object or one hue per semantic category.
8. Preserve meaningful distinctions in grayscale.

As a visual target, large-area fills should have the lowest saturation. Small
focus accents may use moderately higher chroma, but should still remain muted.

### Recommended area balance

Approximate visual target:

- white and neutral surfaces: 75 to 85 percent
- subtle tinted surfaces from the selected accent family: 10 to 20 percent
- stronger chromatic accents: 3 to 8 percent
- error or warning color: below 2 percent

These are compositional heuristics, not geometric requirements. Do not optimize
the figure mechanically to match percentages.

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

Use the currently selected accent family. When no family has been selected, use
the default blue-gray values:

| Property | Value |
| --- | --- |
| Fill when needed | #E7EDF0 |
| Border | #667F8D |
| Text | #506976 |
| Connector | #667F8D |

If an entity already has a local tinted fill, preserve that fill when possible
and indicate active state primarily with border weight or the stronger accent
value.

This keeps two dimensions separate:

- fill answers: what structural region is this in?
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
| Figure title, when needed | 22 to 24 px | 600 |
| Section title | 17 to 19 px | 500 or 600 |
| Entity title | 14 to 16 px | 500 or 600 |
| Field or code | 13 to 14 px | 400 |
| Relationship label | 12 to 13 px | 400 or 500 |
| Annotation | 12 to 13 px | 400 |
| Weak metadata | 11.5 to 12.5 px | 400 |

Prefer no more than four visually dominant size levels in one figure.

When the figure will appear inside a paper or report with an external caption,
do not add a redundant figure title inside the SVG unless the title is
structurally necessary.

Use bold text sparingly. Hierarchy should remain visible without making every
entity label bold.

### Text density

Prefer concise labels and noun phrases.

For ordinary entities:

- use 1 to 3 lines of text
- prefer 2 to 5 words per line
- avoid explanatory sentences
- omit metadata that is not needed to understand the architecture

For containers:

- use one title line
- optionally use one short qualifier line

For connector labels:

- prefer 1 to 3 words
- use longer phrases only when the relationship cannot be named clearly

Move prose explanations to annotations, figure captions, or surrounding text.
A technical diagram should establish a mental model, not reproduce the body
text of a paper.

Avoid UI-style metadata such as STATUS, OWNER, MODE, TYPE, or READY unless those
values are themselves part of the technical argument.

### Text rules

One logical text region should be one SVG text object.

For multiline text, use one text element containing multiple tspan elements.

Do not simulate one logical text box with many unrelated text elements.
Do not merge multiple independent labels into one oversized text object.

## Box sizing and spacing

### Minimum padding

| Measurement | Recommended value |
| --- | --- |
| Entity horizontal padding | 12 to 16 px |
| Entity vertical padding | 10 to 14 px |
| Entity title to body gap | 8 to 10 px |
| Field line height | 18 to 21 px |
| Minimum safe inner clearance | 10 to 12 px |
| Section padding | 16 to 20 px |

Text must not touch or cross borders.

When exact rendered text measurements are available, use them to determine box
size. When they are not available, err on the side of larger boxes.

Do not box every concept. Draw a boundary only when it encodes a meaningful
entity, containment region, memory region, or structural unit. Simple labels,
relationship names, scalar states, and annotations may remain unboxed.

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

Aim for moderate academic information density: enough whitespace to separate
semantic groups, but avoid oversized presentation-style gaps or luxurious card
spacing.

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
| Active path | selected accent, default #667F8D | 1.9 px | solid |
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

This softens line geometry without making the figure decorative. If a stricter
paper-like appearance is desired, butt line caps and miter joins are also
acceptable for structural lines.

## Connector labels

Relationship labels should normally:

- use 13 to 14 px sans-serif text
- use #626A70
- sit approximately 4 to 8 px away from the connector
- avoid overlapping the line
- avoid colored pill backgrounds

If a dense connector field makes text hard to read, a small white or #F8FAFB
background behind the label is acceptable.

## Annotations

### Ordinary annotation

- text: #626A70
- fill: none or white
- border: none or #CBD2D8 at about 1 px

### Weak annotation

- text: #6D7882
- no border by default

### Focus annotation

When an annotation directly explains the active path, use the selected accent
family:

- fill: selected accent fill, default #E7EDF0
- border: selected accent, default #667F8D
- text: selected accent text, default #506976
- border width: about 1.3 px

Annotations should explain the diagram, not compete with its primary entities.

## Memory, array, and range diagrams

Recommended fills:

| State | Fill |
| --- | --- |
| Empty | #FFFFFF |
| Ordinary allocated | #F2F5F7 |
| Semantic memory region | choose a local muted tone, often Teal when appropriate |
| Current range | selected accent fill, default #E7EDF0 |
| Consumed | #F2F5F7 plus hatch |
| Invalid | #F6ECEC |

Ordinary boundary:

#CBD2D8

Current boundary:

selected accent, default #667F8D

Addresses, offsets, indexes, and raw values should normally use monospace text
in #626A70. Current addresses or indexes may use the selected accent text,
default #506976.

Prefer a neutral hatch for consumed ranges instead of inventing another color.

## Pointer and object graphs

Keep objects neutral or locally tone-grouped.
Do not assign one unique color to each node.

Pointer semantics:

| Pointer | Appearance |
| --- | --- |
| Normal | solid #66737F |
| Current | solid selected accent, default #667F8D |
| Weak | dashed #7D8892 |
| Invalid | #875C5C, dashed or solid according to meaning |

Pointer color describes relationship state, not target category.

## Portable SVG profile

Version 0.1.1 is portable SVG first.

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
- tone-accent
- tone-accent-soft
- tone-neutral
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

For version 0.1.1, prefer literal CSS values in the SVG style element rather than
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

## Local accent mapping example

The style system does not know what technical entities mean.

A diagram may locally choose Blue-gray as its single accent family and use:

- neutral white for ordinary entities
- Surface 2 for secondary structural regions
- Blue-gray fill for one emphasized semantic group
- Blue-gray accent stroke for the current or active path

A different diagram may choose Sage or Warm gray instead.

Do not combine Blue-gray, Sage, Slate, and Warm gray merely because the diagram
contains four semantic groups. Those families are alternatives for the overall
figure, not a categorical palette.

The model should be able to use this skill for unrelated technical subjects
without extending the global palette vocabulary.

## Output behavior

When asked to create a technical diagram:

1. infer the structural and semantic groups from the user's content
2. establish a neutral grayscale hierarchy first
3. decide whether one low-saturation accent family improves comprehension
4. establish typography and text bounds
5. remove nonessential prose and metadata from entities
6. size boxes around text only where boxes carry structural meaning
7. establish subsystem layout
8. route connectors
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

- Is the canvas predominantly white or neutral?
- Are large containers neutral?
- Does the figure use no more than one ordinary chromatic hue family?
- Could the architecture still be understood in grayscale?
- Are large filled areas more desaturated than small accents?
- Is chromatic color concentrated on a small number of meaningful details?
- Is error color used only for real error or invalid state?
- Does the figure avoid categorical rainbow coloring?

### Borders and geometry

- Are normal entity borders about 1.2 px?
- Are structural container borders about 1.35 px?
- Are active borders about 1.7 px?
- Are corner radii small?
- Does the figure avoid UI-card styling?
- Are unneeded boxes removed rather than turning every concept into a card?
- Are shadows, gradients, glow, and decorative depth absent?

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

## Version 0.1.1 notes

Version 0.1.1 is an aesthetic refinement of the experimental 0.1 visual system.
It does not change the skill's domain scope.

The main changes are:

- stronger academic and publication-oriented visual direction
- neutral-first composition with at most one ordinary chromatic hue family
- lower-saturation accent families used as alternatives, not categorical colors
- hierarchy driven primarily by structure, luminance, typography, and line weight
- reduced text density and stronger preference for short noun-phrase labels
- explicit avoidance of unnecessary UI-card boxes and metadata
- slightly tighter spacing and typography for moderate academic information density
- improved muted-text contrast on white backgrounds

During trial use, prioritize observing:

- whether figures remain understandable in grayscale
- whether one-hue restraint is sufficient for complex diagrams
- whether text-density limits remove useful technical detail
- whether neutral hierarchy remains clear in nested architectures
- whether routing rules need additional patterns
- whether SVG portability requirements are too strict or too loose

Do not expand the style vocabulary merely because a new technical domain is
introduced. Add a new global rule only when it represents a reusable visual
concept across domains.
