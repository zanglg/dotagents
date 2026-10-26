# Diagram Aesthetics

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Give technical diagrams and scientific charts a coherent visual identity through
color, typography, line weight, geometry and spacing. This is visual guidance, not
modeling-notation instruction or a drawing-tool tutorial.

## Examples

- "Use diagram-aesthetics to make these diagrams look like one visual family."
- "Review this ER diagram's visual hierarchy and readability without changing meaning."
- "Apply our supplied publication theme to this chart and report rendering limits."

## Inputs and outputs

Provide the figure or editable source, intended display/print size and any theme,
companion figures, notation or accessibility requirements. Output can be styling
guidance, visual review findings or authorized drawing/source changes. A reusable
style summary is optional; no persistent theme file is created by default.

## Installation and collaboration

Copy this whole folder to your host's skill directory, such as `.agents/skills/`,
including supporting files. No other Skill is required. Use with the drawing tools
your host provides; it does not supply a renderer. User/publication requirements
and modeling semantics take precedence over visual defaults.

## Validation and references

See the [default theme](references/default-theme.md). Check final-size readability,
contrast, font fallback, cross-figure consistency and preservation of meaning.
Report actual rendering checks separately from style advice; neither proves formal
accessibility conformance. In this repository, [validation guidance](../../docs/validation.md)
covers packaging checks, not visual quality or this Skill's behavior.
