# Palette and Color Roles

Use with [Typography, geometry, and lines](visual-style.md). These concrete
sRGB defaults define a restrained light-background identity, not immutable brand
colors. Choose a subset; do not use every swatch in every figure.

## Color identity

- White and near-neutral surfaces establish structure. Muted blue is the default
  theme accent, not an automatic indicator of selection.
- Use pale fills for regions, deeper colors for text and meaningful graphics.
  A core object may have a more distinct fill than an ordinary category card.
- Favor one accent or related hues when sufficient. Add distinguishable hues for
  unordered categories rather than implying an order through lightness alone.
- Give peer categories comparable visual weight unless an intentional emphasis
  is justified. Category mappings are contextual, not permanent object types.
- Avoid decorative gradients, neon effects, arbitrary per-object colors, and
  large vivid subsystem backgrounds. Validated quantitative color maps and
  domain conventions may differ.
- Do not impose a saturation percentage without a color space. For extensions,
  OKLCH can help coordinate lightness and chroma; check the target output gamut
  and actual contrast.

## Neutral foundation

| Role | Default |
| --- | --- |
| Canvas | `#FFFFFF` |
| Surface 1 | `#F8FAFB` |
| Surface 2 | `#F3F5F6` |
| Surface 3 | `#ECEFF1` |
| Soft gray fill | `#F1F3F5` |
| Ordinary border | `#CBD2D8` |
| Strong border | `#A9B2BA` |
| Essential boundary | `#7C8791` |
| Primary text | `#2B3137` |
| Softer primary text | `#3F474E` |
| Secondary text | `#626D76` |
| Supporting text | `#606D76` |
| Disabled control text | `#9AA2A9` |
| Ordinary line | `#6D7881` |
| Weak line | `#8B949C` |

Surface levels are optional nesting aids, not distinguishable data categories.
Soft borders do not guarantee the contrast needed for essential boundaries.
Use the essential-boundary color or a deeper alternative where the outline is
necessary to understand an object, and verify against adjacent colors.

Disabled text is only for genuinely disabled controls. Indices, annotations,
history, and consumed data remain readable information. Weaken emphasis through
placement and decoration, not whole-object opacity or illegible text.

## Cards and hierarchy

| Card | Fill | Border | Primary text | Secondary text |
| --- | --- | --- | --- | --- |
| Ordinary | `#FFFFFF` | `#CBD2D8` | `#2B3137` | `#626D76` |
| Secondary | `#F8FAFB` | `#CBD2D8` | `#2B3137` | `#626D76` |
| De-emphasized | `#F3F5F6` | `#D1D7DC` | `#3F474E` | `#606D76` |

Default blue core card:

| Role | Default |
| --- | --- |
| Fill | `#DFE9F2` |
| Border | `#587795` |
| Heading and body | `#465E73` |
| Supporting text | `#50677B` |

The core text/fill contrasts are approximately 5.49:1 and 4.79:1; the border/fill
contrast is approximately 3.80:1. Neutral secondary text `#626D76` gives only
about 4.30:1 on this fill, so do not reuse it for ordinary small text here.

Evaluate emphasis against the actual parent container. Category blue `#F1F4F6`
on surface `#F8FAFB` gives only about 1.06:1 between backgrounds: it is not enough
by itself to emphasize a core card. Use a distinct fill, outline, or narrow
structural accent. Backgrounds do not all need 3:1 contrast with each other;
visual hierarchy depends on boundaries, hue, area, and non-color cues too.

## Seven candidate color families

| Family | Pale fill | Soft border | Graphic accent | Colored text |
| --- | --- | --- | --- | --- |
| Blue | `#F1F4F6` | `#C4CED6` | `#627789` | `#50677B` |
| Green | `#F1F5F3` | `#C5D0CA` | `#687C71` | `#52685B` |
| Sand | `#F6F3EF` | `#D4CCC3` | `#7B7064` | `#6B6054` |
| Purple | `#F4F2F5` | `#CEC8D1` | `#756C79` | `#655A6C` |
| Teal | `#F0F5F4` | `#C1CFCD` | `#647A77` | `#506965` |
| Slate | `#F1F3F5` | `#C7CDD3` | `#667481` | `#566573` |
| Amber | `#F7F5EF` | `#D5D0C1` | `#7D7561` | `#6D644F` |

Pale fills are deliberately close. Blue/slate, green/teal, and sand/amber may
serve as alternatives; if used together as categories, add labels, position,
shapes, or meaningful outlines. Do not rely on their small fill differences.
There is no required hue combination or minimum category count.

Coordinate text across each card: either neutral heading and body text, or a
deep, near-neutral family color for both. Establish heading hierarchy primarily
through size and weight, not a colored heading over accidentally near-black
body text. One primary and one supporting color normally suffice. Independently
meaningful state labels may differ. Recheck all text after changing a fill.

## Lines and labels

| Role | Default |
| --- | --- |
| Ordinary relationship | `#6D7881` |
| Weak or optional relationship | `#8B949C` |
| Context relationship | `#858F97` |
| Guide | `#929AA1` |
| Current or active path | `#64798C` |
| Failed or invalid relationship | `#8A6666` |
| Line label | `#626D76` |

Ordinary connectors remain neutral unless color encodes a data series or
relationship category. Arrows share their line's color. Weak and guide colors
may not meet essential-graphic contrast on every surface: deepen them when the
information is necessary. Secondary importance alone does not mean optional.

A label masking a line uses the actual local background, not an arbitrary white
rectangle. See the geometry reference for line-style semantics.

## States and composition

| State | Optional fill | Border or ring | Text | Line or accent |
| --- | --- | --- | --- | --- |
| Current / selected / focused | `#F0F3F6` | `#64798C` | `#4D6273` | `#64798C` |
| Error / invalid | `#F6F0F0` | `#8A6666` | `#805F5F` | `#8A6666` |
| Warning | `#F7F4EC` | `#CFC5AA` | `#766D56` | `#8A816B` |

Theme blue and state blue are deliberately similar. Add an explicit current
pointer, selection ring, focus marker, or label. Distinguish current position,
selected object, and keyboard focus when relevant; a static figure need not
invent states it does not use. Preserve category fills where useful.

Use independent channels for combinations: theme/category via fill or a local
accent, error/warning via label or icon and state border, selection/focus via an
outer ring or separate marker. An invalid selected node keeps its error marker
and adds a selection cue; do not overwrite one state with the other. Leave a
visible gap between ring and border, or use a separate pointer if unsupported.

Error red is for real failure, invalidity, or explicitly destructive outcomes,
not decoration. Stale but usable information may be a warning rather than an
error. Sand/amber categories and warnings need explicit labels or icons when
coexisting. The warning's soft border may need the deeper accent color.
Established red categories are permissible with unambiguous independent error
markers; do not falsely label the category as an error.

Annotations use readable neutral text on white or the actual underlying surface.
Memory and array cells may use white for empty, neutral fill for ordinary or
consumed data, family fills for categories, and state accents for current or
invalid cells. Shared fills require labels or conventional marks to distinguish
states. Keep indices and addresses readable and essential cell boundaries clear.

## Data charts

Component colors are not automatically suitable for thin data lines.

- One series can use one accent; multiple series need sufficiently deep colors
  plus markers, line styles, or direct labels.
- Ordered values use a lightness-ordered sequential scale. Unordered categories
  must not acquire an unintended ranking through shade alone.
- Deviations around a baseline use a diverging palette with a neutral midpoint.
- Continuous quantitative maps may use validated perceptual gradients. Do not
  invent perceptual uniformity claims for this component palette.

Optional discrete blue sequence; select only the levels the data needs:

| Level | Data fill | Internal text |
| --- | --- | --- |
| 1 | `#EDF2F7` | `#2B3137` |
| 2 | `#D9E3EE` | `#2B3137` |
| 3 | `#BACCDD` | `#2B3137` |
| 4 | `#8BA7C1` | `#2B3137` |
| 5 | `#557797` | `#FFFFFF` |
| 6 | `#365775` | `#FFFFFF` |

This scale is ordered, not guaranteed perceptually equidistant. Pale data shapes
may need outlines on white. Deep data colors need not become container fills.
Do not impose color-area quotas on data or failure-analysis figures.

## Readability requirements

Use actual adjacent colors and composited backgrounds, including transparency:

- Ordinary text: at least 4.5:1 contrast.
- Large text: at least 3:1; the WCAG size threshold is 18 pt, or 14 pt bold,
  measured at the final size, not relative to other text in the figure.
- Necessary non-text graphics: normally at least 3:1 against relevant adjacent
  colors. Decorative surfaces and redundant soft outlines are not essential
  boundaries merely because they exist.

Pure black may replace softer text for high-contrast, print, or publication
needs. Dark fills may use white text after contrast verification. Inspect
non-color identification, grayscale, and common color-vision conditions where
relevant. Report which checks were actually performed. Use the
[delivery checks](../SKILL.md#delivery-checks) for the final assessment.
