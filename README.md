# Anagh's Law: Monotonicity of Geometric Clearance

A short mathematical note by **Anagh Kanungo**, revised **11 October 2026**, version **1.1.0**.

**Canonical page:** https://www.anaghkanungo.com/anaghs-law

The note defines compact envelopes in Euclidean three-space, rigid placements, strict clearance, and shared admissibility. Its clearance theorem follows immediately from monotonicity of direct images under set inclusion. It also records corollaries for a shared continuous motion and a common safety margin, and a proposition showing that containment is a partial order rather than a total order.

The mathematics is elementary and is not new. The references place the geometric model alongside configuration-space geometry, AABB hierarchies, and convex-set distance computation. They do not establish a new theorem or collision-detection algorithm.

## Mathematical note

- [LaTeX source](papers/anaghs-law-mathematical-note.tex)
- [Typeset PDF](output/pdf/anaghs-law-mathematical-note.pdf)

The PDF uses numbered theorem environments and cross-references. The canonical page renders its mathematics from TeX on the server while retaining the site's plain HTML presentation.

## Citation

> Kanungo, Anagh. (2026, October 11). Anagh's Law: Monotonicity of Geometric Clearance (Version 1.1.0). https://www.anaghkanungo.com/anaghs-law

Machine-readable citation: [CITATION.cff](CITATION.cff). This revision is author prepared and has not been peer reviewed. It has not been deposited as a new Zenodo version.

## Build the mathematical note

A TeX installation with `pdflatex`, Latin Modern, AMS packages, `microtype`, and `hyperref` is required:

```sh
sh scripts/build_mathematical_note.sh
```

The script compiles twice to resolve cross-references, disables shell escape, and writes the PDF to `output/pdf/`. Compilation intermediates stay in ignored `tmp/`.

## Earlier edition and provenance

The original formulation was published on 10 October 2026. These artifacts preserve that edition:

- [Original v1.0.0 GitHub release](https://github.com/anaghkanungo7/anaghs-law/releases/tag/v1.0.0)
- [Original Markdown source](papers/anaghs-law-note.md)
- [Original PDF](output/pdf/anaghs-law-note.pdf)
- [Original Zenodo archive and DOI](https://doi.org/10.5281/zenodo.23285520)
- [Deposit details](docs/zenodo-deposit.md)

The DOI identifies the original **v1.0.0** explanatory note, archived under CC BY 4.0. It does not identify the revised mathematical note above. The original tag, release assets, source, and PDF are preserved. To rebuild the original PDF, install `requirements.txt` and run `python3 scripts/build_pdf.py`.

The origin and naming experiment are now described in a [separate blog post](https://www.anaghkanungo.com/blog/naming-anaghs-law). The [experiment log](docs/experiment-log.md) remains a separate record of observations and uncertainty.
