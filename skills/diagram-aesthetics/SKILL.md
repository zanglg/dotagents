---
name: diagram-aesthetics
description: "Apply or review a coherent visual style for technical diagrams, ER/UML diagrams, and scientific charts. Use for color, typography, line weight, geometry, spacing, and cross-figure consistency; not for modeling notation or tool-specific drawing instructions."
---

# Diagram Aesthetics

Make different figures recognizable as one family, not copies of one template.
The default identity is light, restrained, and precise: cool-neutral structure,
blue-centered accents, clear typography, clean lines, and deliberate white space.

This skill defines visual outcomes, not modeling rules or drawing techniques.
Domain-defined shapes, compartments, line patterns, and endpoint semantics take
precedence over styling. User requirements, publication rules, and accessibility
also override defaults; never distort meaning or hide data for appearance.

## Visual principles

- **Color:** organize colors by role, with coordinated visual weight and selective
  emphasis. Distinguish theme, category, quantity, and state rather than assigning
  colors arbitrarily. Color must not be the only information channel.
- **Typography:** give headings, prose, and technical identifiers stable roles.
  Establish hierarchy through relative size, weight, and space, not fixed fonts
  or pixel values. Choose families appropriate to the language and medium.
- **Lines and geometry:** let supporting structure recede and relationships remain
  clear. Prefer simple forms and restrained decoration where notation allows;
  emphasis must not imply a false meaning or weight.
- **Space:** express grouping through coherent spacing and comfortable white space.
  Keep comparable elements visually balanced without forcing equal dimensions.
  Do not shrink necessary labels or discard information to fit a composition.
- **Integrity:** keep each element visually continuous. Without semantic reason,
  avoid partial color changes, abrupt stroke-weight changes, unintended breaks,
  or occlusion. Meaningful segmentation and independent state cues are allowed.

Layout and density adapt to content. Shared style does not require identical
arrangements, a focal point among equal peers, or the same shapes across notations.

## Cross-figure continuity

Use the user's shared theme first, then compatible supplied companion figures,
then the [default theme](references/default-theme.md). Read that reference when
choosing or extending defaults, rather than inventing a new style for each figure.

Once selected, reuse font and palette roles, compatible stroke hierarchy, corner
treatment, and spacing rhythm. Keep recurring category and state mappings stable.
Aim for comparable apparent weight at final size, not identical source values.
Explain material departures; continuity relies on available references, not
assumed session memory. A brief reusable style summary may accompany the output;
create a separate persistent theme file only when requested.

## Application and checks

Choose or reuse a theme, apply it to the requested drawing or source, and inspect
the result at its intended size. For consultation, give guidance; for review,
identify concrete visual problems and alternatives. Preserve meaning first when
tools cannot express the preferred style.

- **Coherence:** check family resemblance and element integrity without treating
  layout differences or notation-required forms as defects.
- **Readability:** check labels, overlaps, and actual font fallback, including
  mixed-language glyphs, alignment, and wrapping. Use actual adjacent/composited
  colors: ordinary text needs 4.5:1 contrast; large text needs 3:1 (at least 18 pt
  or 14 pt bold at final size). Necessary graphics normally need 3:1; decorative
  surfaces do not all need that contrast.
- **Meaning:** retain accurate encodings and distinguishable combined states.
  Check non-color identification, grayscale, and color-vision behavior as relevant.
- **Evidence:** report checks actually performed, material tool limitations, and
  relevant untested rendering or print behavior. Style compliance is not evidence
  of rendering quality or formal accessibility conformance.
