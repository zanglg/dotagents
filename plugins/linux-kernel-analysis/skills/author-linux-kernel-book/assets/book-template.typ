// Reusable Typst helpers for source-grounded Linux kernel books.
// Copy this file into the generated book project and adapt project metadata in
// typst/book.typ rather than editing the skill asset in place.

#let kernel-book(
  body,
  title: none,
  subtitle: none,
  author: none,
  source-baseline: none,
  body-font: none,
  mono-font: none,
) = {
  set page(
    paper: "a4",
    margin: (top: 22mm, bottom: 22mm, left: 24mm, right: 24mm),
    numbering: "1",
  )
  set text(size: 10.5pt, lang: "zh")
  if body-font != none {
    set text(font: body-font)
  }
  set par(justify: true, leading: 0.72em)
  set heading(numbering: "1.1")
  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    set text(size: 22pt, weight: "bold")
    block(above: 8mm, below: 7mm)[#it]
  }
  show raw: it => {
    set text(size: 8.5pt)
    if mono-font != none {
      set text(font: mono-font)
    }
    block(
      width: 100%,
      inset: 7pt,
      radius: 3pt,
      fill: rgb("f5f6f7"),
      stroke: rgb("d8dde3"),
      breakable: true,
      it,
    )
  }

  align(center + horizon)[
    #text(size: 30pt, weight: "bold")[#title]
    #if subtitle != none { v(8mm); text(size: 15pt)[#subtitle] }
    #if author != none { v(20mm); text(size: 11pt)[#author] }
    #if source-baseline != none {
      v(7mm)
      text(size: 9pt, fill: rgb("4f5965"))[#source-baseline]
    }
  ]
  pagebreak()
  outline(title: [Contents], depth: 2)
  pagebreak()
  body
}

#let evidence(kind, body) = {
  let color = if kind == "source" {
    rgb("e8f4ff")
  } else if kind == "derivation" {
    rgb("fff3d6")
  } else {
    rgb("f3eef8")
  }
  block(
    width: 100%,
    inset: 8pt,
    radius: 4pt,
    fill: color,
    breakable: true,
  )[
    #strong(upper(kind)) #h(5pt) #body
  ]
}

#let volume-page(title, question: none) = {
  pagebreak(weak: true)
  place(center + horizon)[
    #text(size: 26pt, weight: "bold")[#title]
    #if question != none {
      v(8mm)
      text(size: 12pt, fill: rgb("4f5965"))[#question]
    }
  ]
  pagebreak()
}
