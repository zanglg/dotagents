# Default Theme

A starting visual identity and extension guide, not a mandatory template.
Use with the principles and checks in [SKILL.md](../SKILL.md).

## Color family

Build structure with white and cool-neutral surfaces, dark neutral text, and
quiet boundaries. Center accents on blue, extending toward cyan and blue-violet,
with cool green when useful. Use a subset, not every hue in every figure.

Coordinate peer colors' perceived lightness, chroma, and visual weight. Low
saturation alone is not refinement: thin lines and small marks need enough depth,
and pale fills are not reliable identifiers. Add restrained ochre/orange or other
contrasting hues when distinction or meaning requires them, not to fill the hue
wheel. A warm peer category should not accidentally look like a warning or focus.

OKLCH can help coordinate extensions, but equal coordinates do not guarantee
visual balance or distinguishability; check target gamut and actual output.

### Starting colors

These sRGB values anchor a light theme, not fixed component skins or a complete
category palette. They are neither acceptance tolerances nor limits on category
count or hue range. Extend by the family principles above and reuse the chosen
category mappings across the series.

| Role | Starting value |
| --- | --- |
| Background | `#FFFFFF` |
| Supporting surface | `#F3F5F6` |
| Primary text | `#2B3137` |
| Supporting text | `#626D76` |
| Soft decorative border | `#CBD2D8` |
| Essential lines and outlines | `#6D7881` |
| Theme accent | `#4F6F9F` |

Use the accent selectively, not automatically for text or large backgrounds.
Derive pale accent surfaces only as needed and recheck contrast. Soft borders
are insufficient for essential boundaries. A dark theme needs a separately
checked palette, not automatic inversion.

### Extend by meaning

- **Categories:** choose distinguishable hues without suggesting rank through
  shade alone. Pair color with labels or other appropriate cues. If nearby cool
  hues are too similar, widen the hue range rather than sacrificing readability.
- **Quantities:** use a lightness-ordered sequential scale for ordered values,
  or a diverging scale around a meaningful baseline with a neutral midpoint.
  Prefer validated quantitative palettes; the component theme is not a
  perceptually uniform data scale, and data needs can override its hue family.
- **States:** distinguish selection, warning, and error from category and theme
  through independent markers, labels, or outlines. Combined states must not
  overwrite one another; overlapping category/state hues need disambiguation.

## Typography and visual rhythm

A serif heading with sans-serif prose is one compatible direction, not a required
pairing. Monospace can help with code or aligned identifiers; a separate font for
every role is unnecessary. Favor readable, understated typography over ornamental
lettering, with annotations subordinate but still legible.

Use quiet structural outlines, clear relationship lines, and sparing emphasis.
Where shape is stylistic, modest rounding can soften containers without making
every object a card. Favor proportional padding and more space between groups
than within them when content permits. Extend this vocabulary for new content
without adding decorative effects or a new visual treatment for every object.
