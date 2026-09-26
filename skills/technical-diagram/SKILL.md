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
Neutral tones and luminance define hierarchy.
Typography and border weight define emphasis.
A single low-chroma accent family may establish focus or one local distinction.
Lines define relationships.
Position defines architecture.

Color must not carry information that layout, labels, line style, luminance, or
containment can express more clearly.

The figure should remain structurally understandable in grayscale.

## Overall visual character

The result should feel like:

- systems-paper figures
- kernel or firmware documentation
- technical textbook illustrations
- precise engineering documentation
- restrained research-report graphics

It should not feel like:

- a marketing presentation
- an enterprise dashboard
- a colorful infographic
- a card-heavy product UI
- a multi-hue architecture poster

Keep the canvas predominantly white or near-white. The first visual impression
should be structure, not color.

### Academic visual profile

Prefer a restrained, publication-oriented visual language.

Create hierarchy primarily through:

- whitespace
- alignment
- containment
- luminance
- typography
- border weight
- line style

Treat chromatic color as a secondary channel.

A single figure should normally use no more than one chromatic hue family.
Different lightness values within that family are allowed. Error or warning
color is the only routine exception, and only when the underlying content
actually contains an error, invalid state, or warning.

Use large tinted areas only at very low saturation. Slightly stronger chroma is
acceptable for small borders, arrows, or focal marks.

Do not use:

- gradients
- shadows
- glow
- 3D effects
- skeuomorphism
- glass effects
- decorative illustrations
- large rounded cards
- saturated categorical palettes
- multiple competing hue families
- large colored subsystem backgrounds
- ornamental icons unless the diagram specifically requires them

Do not add color merely to make the figure look richer. A neutral figure is a
valid and often preferable result.

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

### 5. Select a restrained accent family

Only after structure is clear, decide whether chromatic color materially
improves reading speed.

Start neutral.

If color is useful, choose one low-chroma accent family for the entire figure
and use lighter or darker variants of that same family.

Do not assign a separate hue to each semantic group.

Distinguish groups first through:

- position
- containment
- neutral surface depth
- border treatment
- line style
- labels

Tone meaning is local to the current diagram. No accent family has a permanent
technical meaning across diagrams.

### 6. Add relationship semantics

Choose solid, dashed, or dotted lines according to relationship meaning.

Use the selected figure accent only for current, active, or deliberately
emphasized paths. If no chromatic accent is needed, keep relationships neutral.

Do not introduce a second accent hue merely to distinguish another relationship
type.

### 7. Validate

Run the QA checklist at the end of this document before finalizing.

## Color system

### Neutral foundation

| Role | Value |
| --- | --- |
| Canvas | #FFFFFF |
| Surface 1 | #FAFBFB |
| Surface 2 | #F4F6F7 |
| Surface 3 | #ECEFF1 |
| Normal border | #C9CFD3 |
| Strong border | #98A2AA |
| Primary text | #23282D |
| Secondary text | #5F686F |
| Muted text | #6D7882 |
| Normal connector | #667078 |

Never use pure black as the default text color.

Neutral depth should progress gradually:

#FFFFFF -> #FAFBFB -> #F4F6F7 -> #ECEFF1

Avoid abrupt jumps from white to medium or dark gray.

Small informative text should remain clearly readable on its actual background.
Do not use very light gray merely to make metadata feel secondary.

### Accent family palette

These are alternative figure-level accent families. Choose at most one family
for an ordinary figure.

| Family | Fill | Border | Accent |
| --- | --- | --- | --- |
| Blue-gray | #E9EEF1 | #B7C2C9 | #607987 |
| Sage | #ECF0EC | #BCC6BE | #64766A |
| Sepia | #F1EEE9 | #CBC2B7 | #786D60 |
| Teal-gray | #E9F0EF | #B8C8C5 | #5D7773 |
| Violet-gray | #EFEDF0 | #C6C0C8 | #726A75 |

These colors are visual resources only. They do not have permanent domain
meanings.

Do not combine several families simply because the diagram contains several
semantic categories.

If the figure does not benefit from chromatic emphasis, use only the neutral
foundation.

### Accent assignment policy

For each diagram:

1. Start neutral.
2. Add chromatic color only when it materially improves scanning or focus.
3. If color is used, choose one accent family for the figure.
4. Distinguish semantic groups first with position, containment, luminance, and
   labels.
5. Reuse light, border, and accent variants from the selected family rather
   than adding new hues.
6. Do not create one color per object.
7. Nested objects do not automatically require color.
8. Complexity alone does not justify additional hue families.
9. Error or warning red is an exception only when semantically necessary.

Typical usage:

- simple figure: neutral only, or one accent family
- medium figure: neutral plus one accent family
- complex figure: still prefer neutral plus one accent family

### Recommended area balance

Approximate target:

- white and neutral surfaces: 80 to 90 percent
- lightly tinted accent surfaces: 8 to 18 percent
- stronger accent strokes or marks: 2 to 6 percent
- error or warning color: below 2 percent

These are visual balance targets, not geometric requirements.

Large areas should have the lowest chroma. Small focal marks may use somewhat
stronger chroma.

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

Use the selected figure accent family. If the figure has no established accent
family, Blue-gray is the default restrained focus family.

Default Blue-gray focus values:

| Property | Value |
| --- | --- |
| Fill when needed | #E9EEF1 |
| Border | #607987 |
| Text | #4C626D |
| Connector | #607987 |

If an entity already has a lightly tinted accent fill, preserve that fill when
possible and indicate active state primarily with the stronger border and
connector.

This keeps two visual dimensions separate:

- fill answers: what local region or grouping does this belong to?
- border and line answer: what is active or emphasized now?

Do not introduce blue into a figure that already uses another accent family.
Use that figure's selected accent instead.

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
| Figure title | 24 to 26 px | 600 |
| Section title | 18 to 20 px | 600 |
| Entity title | 15 to 16 px | 500 |
| Field or code | 14 to 15 px | 400 |
| Relationship label | 13 to 14 px | 400 or 500 |
| Annotation | 13 to 14 px | 400 |
| Weak metadata | 12 to 13 px | 400 |

Prefer no more than four visually dominant size levels in one figure.

Use bold text sparingly. Hierarchy should be visible without making most entity
labels bold.

### Text density

Prefer concise noun phrases over prose.

For ordinary entities:

- use 1 to 3 lines of text
- prefer roughly 2 to 5 words per line
- keep the entity name visually dominant
- omit descriptive sentences unless they are essential to understanding
- move longer explanation to an annotation, caption, or surrounding document

For containers:

- prefer a one-line title
- allow at most one short qualifier when necessary

For connector labels:

- prefer 1 to 3 words
- avoid sentence-like labels

Weak metadata, badges, status chips, owner labels, and UI-like field stacks
should be omitted by default. Include them only when they encode information
that the figure itself must communicate.

A diagram should help establish a mental model, not reproduce the surrounding
prose.

### Text rules

One logical text region should be one SVG text object.

For multiline text, use one text element containing multiple tspan elements.

Do not simulate one logical text box with many unrelated text elements.
Do not merge multiple independent labels into one oversized text object.

## Box sizing and spacing

### Minimum padding

| Measurement | Recommended value |
| --- | --- |
| Entity horizontal padding | 12 to 14 px |
| Entity vertical padding | 10 to 12 px |
| Entity title to body gap | 8 to 10 px |
| Field line height | 18 to 20 px |
| Minimum safe inner clearance | 10 px |
| Section padding | 18 to 22 px |

Text must not touch or cross borders.

When exact rendered text measurements are available, use them to determine box
size. When they are not available, err on the side of slightly larger boxes.

Avoid presentation-style oversized padding. The figure should feel compact and
publication-oriented while remaining readable.

### Spacing scale

Use an 8 px base rhythm.

Prefer:

- 8 px
- 16 px
- 24 px
- 32 px
- 48 px

Keep distances within a group smaller than distances between subsystems.

Do not try to fill the whole canvas. Empty white regions are part of the visual
structure, but whitespace should clarify grouping rather than create a luxury
presentation aesthetic.

## Borders

### Widths

| Border role | Width |
| --- | --- |
| Very light separator | 0.75 to 0.8 px |
| Normal entity | 1.0 to 1.1 px |
| Structural container | 1.2 px |
| Active entity | 1.4 to 1.5 px |
| Error entity | 1.4 px |

### Corner radius

| Object | Radius |
| --- | --- |
| Normal entity | 2 to 3 px |
| Large container | 2 to 4 px |
| Array or memory cell | 0 to 2 px |
| Annotation box | 2 to 3 px |

Square corners are acceptable.

Keep technical diagrams close to rectilinear geometry.
Avoid pill shapes, soft cards, and large UI-like radii.

### Boundary discipline

Do not draw a box around every concept.

Use a visible boundary only when it encodes at least one of:

- entity identity
- containment
- a meaningful structural unit
- a range, memory region, or addressable object
- a deliberately emphasized state

Plain labels, actors, intermediate concepts, and relationship names may remain
unboxed.

Avoid repeated card framing where whitespace and alignment already communicate
the grouping.

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
| Normal | #667078 | 1.3 px | solid |
| Weak or optional | #6D7882 | 1.15 px | dashed |
| Contextual or logical | #6D7882 | 1.15 px | dotted |
| Active path | selected accent, default #607987 | 1.5 px | solid |
| Error path | #875C5C | 1.4 px | solid or dashed as appropriate |
| Guide line | #6D7882 | 1.0 px | solid or dotted |

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

Use the selected accent only when the relationship itself is active or
deliberately emphasized.

Do not introduce a different hue for data, control, async, ownership, or other
relationship categories when line style and labels can express the distinction.

Do not color a connector merely because the connected entity has an accent
fill.

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
- use #5F686F
- sit approximately 4 to 8 px away from the connector
- avoid overlapping the line
- avoid colored pill backgrounds

If a dense connector field makes text hard to read, a small white or #F8FAFB
background behind the label is acceptable.

## Annotations

### Ordinary annotation

- text: #5F686F
- fill: none or white
- border: none or #C9CFD3 at about 0.9 px

### Weak annotation

- text: #6D7882
- no border by default

### Focus annotation

When an annotation directly explains the active path:

- fill: selected accent fill, default #E9EEF1
- border: selected accent, default #607987
- text: selected accent text, default #4C626D
- border width: about 1.1 px

Annotations should explain the diagram, not compete with its primary entities.

Keep annotations concise. Prefer a short phrase or one compact sentence. Longer
explanation belongs in the figure caption or surrounding document.

## Memory, array, and range diagrams

Recommended fills:

| State | Fill |
| --- | --- |
| Empty | #FFFFFF |
| Ordinary allocated | #F4F6F7 |
| Semantic memory region | selected accent fill when color is needed |
| Current range | selected accent fill, default #E9EEF1 |
| Consumed | #F4F6F7 plus hatch |
| Invalid | #F6ECEC |

Ordinary boundary:

#C9CFD3

Current boundary:

selected accent, default #607987

Addresses, offsets, indexes, and raw values should normally use monospace text
in #5F686F. Current addresses or indexes may use the selected accent text.

Prefer a neutral hatch for consumed ranges instead of inventing another color.

Do not use different hues for adjacent memory regions unless the user explicitly
requires a categorical color encoding.

## Pointer and object graphs

Keep objects neutral or use the single selected accent family sparingly.

Do not assign one unique color to each node.

Pointer semantics:

| Pointer | Appearance |
| --- | --- |
| Normal | solid #667078 |
| Current | solid selected accent, default #607987 |
| Weak | dashed #6D7882 |
| Invalid | #875C5C, dashed or solid according to meaning |

Pointer color describes relationship state, not target category.

Prefer spatial grouping, labels, and line style over additional node colors.

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
- surface-neutral-1
- surface-neutral-2
- accent-fill
- accent-border
- accent-text
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

The style system does not assign technical meaning to colors.

A figure may locally choose Blue-gray as its accent family and use:

- neutral surfaces for ordinary structure
- Blue-gray fill for one emphasized region
- Blue-gray accent stroke for the current object or active path
- error red only for a real invalid or failure state

Another figure may choose Sage instead.

Do not use Blue-gray, Sage, Sepia, Teal-gray, and Violet-gray simultaneously to
represent unrelated categories in one ordinary figure.

The model should be able to use this skill for unrelated technical subjects
without extending the global palette vocabulary.

## Output behavior

When asked to create a technical diagram:

1. infer the entities, relationships, and containment from the user's content
2. establish typography and concise labels
3. size boxes around text
4. establish subsystem layout using neutral structure first
5. decide whether chromatic color is necessary
6. if needed, select one low-chroma accent family for the figure
7. route connectors with line style carrying relationship semantics
8. add active or error state only if semantically justified
9. enlarge the canvas when needed rather than squeezing content
10. produce editable vector SVG when SVG is requested
11. validate the result against the QA checklist

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
- Are boundaries used only where they encode real structure?

### Text

- Does every text block fit fully inside its border?
- Is there at least about 10 px of safe inner clearance where practical?
- Do ordinary entities usually contain no more than 1 to 3 lines?
- Are labels mostly short noun phrases rather than explanatory prose?
- Have unnecessary metadata, badges, and UI-like field stacks been removed?
- Are logical multiline labels represented as single text objects?
- Is the text still readable at normal viewing scale?

### Color

- Is the canvas predominantly white or neutral?
- Are large containers neutral?
- Does the figure use at most one chromatic accent family, apart from a
  semantically necessary warning or error?
- Are large tinted surfaces very low saturation?
- Is hierarchy carried primarily by structure and luminance rather than hue?
- Is stronger chroma concentrated in small focal marks?
- Is error color used only for real error or invalid state?
- Does the figure avoid looking multicolored at first glance?

### Borders and geometry

- Are normal entity borders visually light?
- Are structural borders only slightly stronger?
- Are active borders emphasized without becoming heavy?
- Are corner radii small or square?
- Does the figure avoid UI-card styling?
- Could any boxed concept be clearer as plain text plus alignment?

### Connectors

- Are normal relationships solid?
- Are optional or weak relationships dashed?
- Are contextual relationships dotted?
- Is the selected accent reserved for genuinely active or emphasized paths?
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

Version 0.1.1 is an aesthetic refinement of the experimental visual system.

The primary changes are:

- a more academic and publication-oriented visual profile
- neutral-first composition with at most one chromatic accent family per figure
- lower-saturation large-area fills
- stronger reliance on luminance, spacing, typography, and border weight
- reduced node text density and less explanatory prose inside boxes
- less UI-card framing and smaller corner radii
- lighter borders and connectors
- improved muted-text readability
- accent-aware active-state styling that does not introduce a second hue family

Continue to prioritize observing:

- whether diagrams remain readable when mostly neutral
- whether text-density limits remove useful information or improve scanability
- whether the single-accent rule needs narrowly defined exceptions
- whether routing and containment remain clear without categorical colors
- whether SVG portability requirements are too strict or too loose

Do not expand the style vocabulary merely because a new technical domain is
introduced. Add a new global rule only when it represents a reusable visual
concept across domains.
