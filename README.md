# Anagh's Law

**Clear the maximum, clear the rest.**

A named geometric clearance heuristic, coined by **Anagh Kanungo on 10 October 2026**, inspired by a bus-and-tunnel observation.

**Canonical page:** https://www.anaghkanungo.com/anaghs-law

## Definition

> If one object’s spatial envelope contains another’s, any placement that clears the containing envelope also clears the contained envelope, provided that placement is admissible for both.

Let **B ⊆ A** be envelopes aligned in a common coordinate system, **S** the available space, and **T** a placement allowed for both objects. If **T(A) ⊆ S**, then **T(B) ⊆ T(A) ⊆ S**.

The underlying mathematics is elementary and is not new. This project documents the name, formulation, and a communication experiment. It does not claim a new theorem, peer review, institutional endorsement, or ownership of geometric containment.

## The bus–tunnel corollary

If a bus can clear a tunnel, any vehicle geometrically contained within the bus's relevant clearance envelope can also clear it under the same admissible conditions.

The same argument holds along an entire motion only when containment holds at every point and that motion is admissible for both vehicles.

## What “maximum” means

A containing envelope for the family being checked. It need not be a member of that family. Neither volume nor mass defines this order. A tall, narrow object and a short, wide object can be incomparable; use a common bound or separate checks.

## Limitations

- Less volume, mass, width, or height alone does not establish containment.
- Fitting at an entrance does not establish clearance along the whole path.
- Steering, turning radius, suspension, support, and other constraints may prevent the same motion.
- Load capacity, deformation, tolerances, and required safety margins need separate treatment.
- If a conservative enclosing box clears, the object clears. If the box fails, the object might still fit.
- The implication only transfers success to contained envelopes. A bus failing does not imply that a car fails.

## Note and stable version

- [Three-page note: editable Markdown](papers/anaghs-law-note.md)
- [Three-page note: PDF](output/pdf/anaghs-law-note.pdf)
- [v1.0.0 — Original Formulation](https://github.com/anaghkanungo7/anaghs-law/releases/tag/v1.0.0)
- [Introduction drafts](docs/introduction.md)
- [Experiment log](docs/experiment-log.md)
- [Zenodo deposit preparation](docs/zenodo-deposit.md)

The note is an author-prepared explanatory draft, not a peer-reviewed paper. No DOI has been issued for it.

## Citation

Canonical webpage:

> Kanungo, Anagh. (2026, October 10). Anagh’s Law: Clear the maximum, clear the rest. Original formulation, version 1.0. https://www.anaghkanungo.com/anaghs-law

Versioned repository:

> Kanungo, Anagh. (2026). Anagh's Law: Original Formulation (v1.0.0). GitHub. https://github.com/anaghkanungo7/anaghs-law/releases/tag/v1.0.0

Machine-readable repository citation: [CITATION.cff](CITATION.cff). The page remains the canonical explanation; the release records this repository version. A public timestamp records publication, not priority over all possible earlier uses.

## Rebuild the PDF

Python 3 and ReportLab are required:

```sh
python3 -m pip install -r requirements.txt
python3 scripts/build_pdf.py
```

The script reads the Markdown source, including its three explicit page divisions, and uses ReportLab's standard serif fonts. It needs no network access or private credentials. The included PDF is the release artifact.

## What counts as adoption

Author-owned pages and uploads establish a record. Independent citation, accurate explanation, and unprompted use are separate outcomes. Record evidence and uncertainty in the experiment log; do not infer adoption from the number of pages published by the author.
