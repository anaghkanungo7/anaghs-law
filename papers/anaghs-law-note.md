# Anagh's Law

## A Named Heuristic for Monotonic Feasibility Under Geometric Containment

Anagh Kanungo | 10 October 2026 | Version 1.0.0

*Clear the maximum, clear the rest.*

## Abstract

This note documents Anagh's Law, a name for an elementary geometric clearance heuristic: a placement that clears a containing spatial envelope also clears every envelope contained within it, when that placement is admissible for both. The argument follows directly from preservation and transitivity of set inclusion. A bus-and-tunnel example motivates the formulation. The note distinguishes containment from lower volume or mass, extends the statement to a common admissible motion, and explains the limits of conservative bounds. The contribution is a memorable name, a documented formulation, and a proposed experiment in communication and attribution. No new mathematical theorem or empirical evidence of adoption is claimed.

## 1. Motivation and definition

Clearance checks recur in packaging, fixtures, and collision geometry. When many variants share one containing envelope, certifying that envelope can replace repeated geometric checks, provided containment is easier to establish and the same placement is allowed. On 10 October 2026, the author coined “Anagh's Law,” inspired by the observation that a vehicle contained within a bus's clearance envelope can inherit the bus's clearance through a tunnel [1].

**Definition.** If one object’s spatial envelope contains another’s, any placement that clears the containing envelope also clears the contained envelope, provided that placement is admissible for both.

Here, an envelope is the occupied region or a conservative enclosing region. “Maximum” means a common containing envelope for the family under consideration. It does not mean greatest volume, heaviest object, or greatest value of one dimension. A suitable common envelope may be synthetic rather than an actual member of the family.

## 2. Formal model and proof

Let A and B be subsets of Euclidean space, expressed in a common coordinate system after any permitted alignment, with B contained in A. Let S be the available region. Let T be a common placement, typically a rigid transformation, admissible for both objects. Define geometric feasibility at that placement by T(A) being contained in S. Direct images under the same map preserve inclusion, so:

> B ⊆ A and T(A) ⊆ S imply T(B) ⊆ T(A) ⊆ S.

**Proof.** Every point of B belongs to A. Its image under T therefore belongs to T(A), which lies in S. Thus every point of T(B) lies in S. No special geometric theorem is required.

If placement is a choice, a feasible placement for A is a witness for B only when that same placement is admissible for B. With a shared set of allowed placements, existential geometric feasibility is downward closed under inclusion. Different supports, alignment rules, or orientation restrictions can invalidate the transfer.

<!-- pagebreak -->

## 3. Motion and the bus–tunnel corollary

For a continuous motion T_t over 0 ≤ t ≤ 1, require T_t(A) to lie in the available space at every time. Applying the same argument pointwise gives T_t(B) contained in T_t(A) and therefore in the available space, for every t. The entire motion must be admissible for both objects. Checking only the entrance or a few sampled positions is not a proof of continuous passage.

**Bus–tunnel corollary.** If a bus can clear a tunnel, any vehicle geometrically contained within the bus's relevant clearance envelope can also clear it under the same admissible conditions.

In the canonical page's simplified illustration, a rectangular opening is 3.2 m wide and 3.8 m high. A bus envelope is 2.5 m wide and 3.2 m high; a van is 2.1 m by 2.5 m and a car is 1.8 m by 1.5 m. At the same centered, ground-aligned orientation, the van and car cross-sections are contained within the bus envelope. All three clear the opening. These are illustrative dimensions, not measurements of specific vehicles. The calculation uses zero additional safety margin and says nothing about route bends, vehicle length, or dynamics [1].

## 4. Counterexamples and limits

**Lower volume is insufficient.** A box of dimensions 1 × 1 × 4 has less volume than a 2 × 2 × 2 box but exceeds its height. Against a 3-unit-high opening in a fixed upright orientation, the latter clears and the former does not. Lower mass likewise supplies no geometric containment guarantee.

**There may be no largest member.** A tall, narrow envelope and a short, wide envelope can be incomparable under inclusion. A common conservative bound can certify both if it clears; otherwise separate checks may succeed. Set inclusion is a partial order, not an ordering by a single scalar measure.

**The inference is one-way.** If a containing envelope fails, a contained envelope might still clear. For example, a 2.5 m-wide bus fails a 2.0 m-wide opening while a 1.8 m-wide car may clear. Likewise, failure of an enclosing bounding box does not establish failure of the enclosed geometry.

**A path is not a placement.** Entrance clearance does not establish clearance around a bend. Turning radius, steering constraints, wheel contact, suspension, articulation, and support conditions can make a transferred path inadmissible even when its occupied sets would avoid obstacles.

**Additional constraints require additional models.** Geometric containment does not certify load capacity, strength, friction, deformation, or manufacturing tolerances. For a fixed geometric safety margin, first define a reduced available region or inflated envelopes consistently, then apply containment to those regions. Different margin requirements cannot be transferred without checking them.

## 5. Practical uses and existing context

Examples include a product-family envelope checked against a compartment, a gauge enclosing a family of parts, and a conservative collision envelope in a virtual scene. In each case the useful work is establishing a valid envelope, alignment, and admissible placement or motion; the inclusion argument itself is immediate.

Geometric modeling, transformations, configuration spaces, and motion planning under differential constraints are established subjects. LaValle's *Planning Algorithms* provides background in Chapters 3, 4, and 13 [2]. This note does not introduce a replacement planning method or claim a measured speedup.

<!-- pagebreak -->

## 6. Naming and communication experiment

The proposed experiment is to publish a precise canonical explanation, record a versioned public formulation, and observe whether other people use the name accurately. A memorable phrase may help communicate a familiar idea; whether this particular phrase does so is an empirical question. No result is claimed in this version.

Useful milestones are: indexing of the canonical page; discoverability for the exact phrase; accurate independent citations; correct search-assisted explanations with public sources; and unprompted use by people outside the author's own publications. The distinction between publication and adoption is essential: multiple uploads by the same author do not constitute independent recognition.

A transparent observation log should record the date, exact query or prompt, service and mode, URLs returned, and any intervention that preceded a mention. Search rankings depend on location and context, and AI answers vary across retrieval and non-retrieval modes. A generated answer alone does not show that a phrase entered training data. Solicited mentions should be labeled separately from unprompted uses.

## 7. Provenance and citation

The naming and formulation recorded here are attributed to Anagh Kanungo, dated 10 October 2026. The canonical public page is [1]. The repository's v1.0.0 release records the original formulation [3]; actual commit and release timestamps are supplied by GitHub. These records document publication and do not prove absence of prior similar terminology or confer ownership of the underlying mathematics.

This is an author-prepared explanatory note and a personal communication experiment. It has not been peer reviewed. No affiliation, endorsement, independent adoption, or DOI is claimed.

Suggested citation: Kanungo, Anagh. (2026). *Anagh's Law: A Named Heuristic for Monotonic Feasibility Under Geometric Containment*. Version 1.0.0. Author-prepared note accompanying the Original Formulation release [3].

## References

[1] Kanungo, Anagh. (2026, October 10). *Anagh's Law: Clear the maximum, clear the rest*. Original formulation, version 1.0. https://www.anaghkanungo.com/anaghs-law

[2] LaValle, Steven M. (2006). *Planning Algorithms*. Cambridge University Press. Chapters 3, 4, and 13. Author's online edition: https://lavalle.pl/planning/

[3] Kanungo, Anagh. (2026). *Anagh's Law: Original Formulation*. Version 1.0.0. GitHub release. https://github.com/anaghkanungo7/anaghs-law/releases/tag/v1.0.0
