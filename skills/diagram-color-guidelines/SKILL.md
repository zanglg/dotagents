---
name: diagram-color-guidelines
description: "Create, restyle, or review technical diagrams with a recognizable shared aesthetic across independently produced figures. Use for architecture, flow, relationship, memory and array diagrams, academic illustrations, and statistical charts when choosing fonts, colors, lines, arrows, or geometry. Keep visual identity stable while adapting layout and detail to the content; do not require identical results."
---

# Technical Diagram Aesthetic Constraints

## Intent

Make figures produced at different times look like members of the same visual
family, not copies of the same template. This skill defines visual language,
not a diagram generator or a mandatory layout algorithm. The existing
`diagram-color-guidelines` name is retained for discovery compatibility.

The default identity is light, restrained, and precise: neutral structural
surfaces, muted blue emphasis, coordinated text colors, role-based typography,
clean lines, and modest rounding. Dark themes need a separately validated
palette, not an automatic inversion.

## Three layers of constraints

1. **Style anchors:** keep font roles, palette character, text tone, relative
   stroke weights, arrow shapes, and corner treatment recognizable across
   figures. Reference values are defaults, not exact output requirements.
2. **Content adaptations:** choose canvas size, layout, card dimensions,
   alignment, routing, category count, and level of detail for the information.
   Different figures may use different solutions within the same style.
3. **Quality requirements:** preserve semantic accuracy, readable text,
   distinguishable states, clear directions, and freedom from misleading
   overlaps. Never sacrifice these to match the aesthetic.

User instructions, established notation, publication rules, and accessibility
needs override stylistic defaults. Explain material departures; do not override
information accuracy or hide necessary data.

## Workflow

1. Identify the diagram type, content, intended display size, background, output
   tool, and any supplied companion figures. Reuse their compatible style
   anchors; otherwise use the defaults without repeatedly asking about minor
   aesthetic choices. Do not invent access to previous figures or sessions.
2. Read [Palette and color roles](references/palette.md) before choosing colors.
   Read [Typography, geometry, and lines](references/visual-style.md) before
   creating or changing those elements. Read both for a complete drawing.
3. Select a small set of role-level styles. Map canvas, containers, cards, text,
   connectors, and any necessary states. Prefer component styles or tokens over
   per-object improvisation. Keep the mapping stable within the figure.
4. Adapt the composition to the content. Establish the reading order, grouping,
   and balance of visual weight and white space. Use the simplest clear layout
   and routing available, but do not require trial of every routing family.
   Split or combine figures when it improves comprehension; do not force one
   canvas or a dominant focal point for content that needs equal treatment.
5. Apply the style to the actual drawing or source, not just a written proposal.
   For consultation, provide the requested style guidance; for review, identify
   concrete objects, problematic combinations, and suitable alternatives.
6. Inspect the result at its intended size. Separate aesthetic coherence from
   readability and semantic correctness. Report checks actually performed and
   material limitations, without treating specification compliance as rendering
   evidence.

## Tool limitations and continuity

When a tool cannot control fonts, ports, markers, or spacing precisely, choose
its closest supported styles. Prioritize meaning and readability, then preserve
as many anchors as possible. State consequential deviations; do not mark
unsupported or untested properties as verified. Change tools only when required
by the task or necessary to preserve essential information.

For a related series, reuse available shared styles. A compact style summary
(font roles, palette roles, stroke hierarchy, arrow and corner treatment) may
accompany the requested output when useful. Do not create separate persistent
style files or scratch artifacts unless requested. Continuity must come from
available references or the documented defaults, not assumed session memory.

## Delivery checks

Check applicable items; identify unverified items rather than claiming success.

- **Family resemblance:** typography, color character, stroke hierarchy, arrows,
  and corner treatment are coherent with the chosen visual language. Layout
  differences alone are not defects; exact pixel matching is not required.
- **Content fit:** reading order, grouping, white space, visual weight, routing,
  and density serve this figure. No key relationship or data is removed merely
  to simplify the look.
- **Readability:** text and necessary graphical elements have sufficient contrast
  against their actual backgrounds; labels, arrows, and content do not collide
  at the intended display size. Group titles remain easy to find; font fallback
  and mixed-language text preserve legible glyphs, spacing, and line breaks.
- **Meaning:** categories, directions, line styles, and boundaries are accurate;
  theme emphasis is not confused with selection or error. Combined states remain
  visible, and color is not the only information channel.
- **Evidence:** disclose relevant tool constraints, deviations, and unperformed
  rendering, contrast, grayscale, color-vision, or print checks. Do not infer
  formal accessibility conformance from this checklist alone.
