# Thread B31: is there an instance checker, or an errorless heuristic, for pK^t-compressibility?

Date: 2026-09-15. Literature audit for the converse `BEM_skew ⇒ H_pK` of the paper's open problem
(§7.5–7.6 of `pass16/ENTROPY_PRODUCTION.md`), placed in `pass20/characterization_attempt.md` as an
instance of the errorless-versus-error-prone gap for computing time-bounded Kolmogorov complexity.

**One-line outcome.** No instance checker for any K^t/pK^t/MINKT-type problem exists in the
literature. For one specific object — **sublinear-time-bounded conditional gap K^t**, the one the
recent NP-hardness line actually reaches — building a checker is *equivalent* to building one for SAT,
the Blum–Kannan open problem of 1995 (Beigel's theorem plus randomized NP-hardness). That equivalence
does **not** extend to GapMINKT proper, which no relativizing reduction can make NP-hard (Ko's oracle),
so for the field's own characterization object the honest status is still plain "open, nobody has built
one". The one route that is not barred is the natural-property route; on it, `H_pK` **implies** a
natural property for conditional K^t (proved below), the converse implication has two identified gaps,
and the derivation of the property from SoI is stuck at 2^{O(n/log n)} behind a relativization barrier
that is tight at that exponent. No oracle in hand separates `BEM_skew` from `H_pK`.

---

## 0. Reading status of every source

Rule: **Read** = the cited text was opened and the named section read this session. **Read (local)** =
same, from the copy on disk in `pass16/sources/`. **Abstract-only** = only the abstract/announcement
was read. **cited via X** = taken from X, which was read. Nothing below is cited from memory; the
three items that would have been are marked and are the only candidates for the audit list.

| source | what was read | status |
|---|---|---|
| Hirahara, *Symmetry of Information from Meta-Complexity*, CCC 2022 | §1 (Thms 1.2, 1.3), §6.2 + Remark 6.4, §7 (Defs 7.2/7.4, Lemma 7.5), §8 (Def 8.1, Thm 8.2 + fn 19, Lemma 8.3, proof of Thm 8.2), relativization passage pp. 26:6 | **Read (local)** `hirahara_ccc2022_lipics234-26.txt` |
| Hirahara & Santhanam, *Errorless Versus Error-Prone Average-Case Complexity*, ITCS 2022, LIPIcs 215:84 | Abstract, §1–1.1, Defs 2/3/4/7/9/11/18, Props 5/6/15/19, Thms 8/13/14/17/20/21/22/25/28, proofs of Thm 8 and Thm 20 | **Read** (downloaded full PDF) |
| Hirahara & Nanashima, *Finding Errorless Pessiland in Error-Prone Heuristica*, CCC 2022 | Abstract, §1 (Questions 1 and 2, Thm 4 list), §1.2 related-work passage on HS22 | **Read (local)** `hn_ccc2022_lipics234-25.pdf`, text extracted |
| Hirahara & Nanashima, *On Worst-Case Learning in Relativized Heuristica*, FOCS 2021 / ECCC TR21-161 | Abstract of both versions (the 2^{n/ω(log n)} oracle and its near-optimality) | **Read (abstract + intro only)** |
| Kabanets & Kolokolova, *Chain Rules for Time-Bounded Kolmogorov Complexity*, ECCC TR25-089 | §1 intro, §2.3 (Defs 2.7/2.10/2.11, Thm 2.8, Cor 2.9), §2.4 (Lemmas 2.15/2.16, Cors 2.17/2.19), §8 Concluding Remarks, **Appendix B in full** (Lemma B.1, Thm B.2 and its proof) | **Read (local)** `kk_eccc_tr25-089.txt` |
| GKLO22, *Probabilistic Kolmogorov Complexity with Applications to Average-Case Complexity*, CCC 2022 | Defs of AvgBPP (p. 16:8), Lemma 6, Lemma 26 (carried from `characterization_attempt.md`, which read the proof line by line this week) | **Read (local)**, Lemma 26 proof **cited via** `characterization_attempt.md` |
| HILNO, *A Duality between One-Way Functions and Average-Case Symmetry of Information*, eprint 2023/424 | Thms 1 and 3, §2 passage on [IRS21], §3.1 heuristic-scheme definitions | **Read (local)** |
| Mahmoody & Xiao, *On the Power of Randomized Reductions and the Checkability of SAT*, CCC 2010 | Abstract, §1.1–1.2.2 (Beigel's Thm 1.3, Cor 1.4, the checkability/testability discussion, Blum–Kannan characterization of checkable languages) | **Read** (downloaded full PDF, first 4 pp.) |
| Hirahara, *Capturing One-Way Functions via NP-Hardness of Meta-Complexity*, STOC 2023 / ECCC TR23-037 | Abstract, §1 (the three questions), §2.1–2.1.3 including **footnote 7** and Theorem 10.3 | **Read** (downloaded full PDF, §1–2) |
| Hirahara, Kabanets, Lu & Oliveira, *Exact Search-To-Decision Reductions for Time-Bounded Kolmogorov Complexity*, CCC 2024 | Abstract, §1.4 Concluding Remarks + Table 1 | **Read** (downloaded full PDF, abstract + §1.4) |
| Mazor & Pass, *Search-To-Decision Reductions for Kolmogorov Complexity*, CCC 2024 | Abstract, §1 opening | **Read** (downloaded full PDF, abstract + §1 opening) |
| Ren & Santhanam, *A Relativization Perspective on Meta-Complexity*, STACS 2022 | §2 in full (Thms 13–18 and the surrounding discussion, incl. the "instance checkers for EXP-complete problems are non-relativizing" remark) | **Read** (downloaded full PDF, §2) |
| Goldberg & Kabanets, *Consequences of Randomized Reductions from SAT to Time-Bounded Kolmogorov Complexity*, RANDOM 2024 | Abstract (items 1–4) | **Abstract-only** |
| Bogdanov & Trevisan, *Average-Case Complexity* (survey), 2006 | §1 passages on non-adaptive worst-to-average reductions; Defs 6/9 of errorless heuristics | **Read (local)**, partial |
| Nanashima, *Open Questions in Relativized Heuristica*, Simons Meta-Complexity open-problems list, Spring 2023 | Problems 11 and 12 verbatim | **Read** (downloaded full PDF) |
| Liu, Mazor & Pass, *Cryptographic Implications of Worst-Case Hardness of Time-Bounded Kolmogorov Complexity*, ECCC TR26-051 (Apr 2026) | Abstract | **Abstract-only** |
| Liu & Pass, TCC 2024, *On One-Way Functions, the Worst-Case Hardness of Time-Bounded Kolmogorov Complexity, and Computational Depth* | Publisher abstract/summary only | **Abstract-only** |
| Lu & Santhanam, ICALP 2024, *Impagliazzo's Worlds Through the Lens of Conditional Kolmogorov Complexity* | Publisher abstract/summary only | **Abstract-only** |
| Blum & Kannan, *Designing Programs That Check Their Work*, JACM 42(1), 1995 | **Not opened.** Every statement attributed to it here is taken from Mahmoody–Xiao §1.2 or Hirahara–Santhanam §1.1, both Read. | **cited via MX10 / HS22 — for the audit list** |
| Beigel's theorem on checkability under mutual randomized reductions | **Not opened** (Beigel's original is unpublished; it is cited in Blum–Kannan). Statement taken verbatim from Mahmoody–Xiao Theorem 1.3. | **cited via MX10 — for the audit list** |
| Impagliazzo–Levin domination / Ilango MCSP self-reducibility | Only search-result summaries; no primary text opened. The two claims made below from them are labelled **[Unverified]** and go on the audit list. | **[Unverified]** |
| Li, Pyne & Tell, *Distinguishing, Predicting, and Certifying*, ECCC TR24-139 | Search-result summary only; judged off-target (ROBP derandomization of Yao's predictor, not certification of incompressibility) | **Abstract-only, not used** |
| Monroe, *Hardness as an Information Constraint*, arXiv 2606.04257; *Witness Complexity of Short Descriptions*, arXiv 2606.31370 | Abstracts only; both judged off-target | **Abstract-only, not used** |

---

## 1. Definitions and the theorem (Question 1)

### 1.1 Blum–Kannan instance checker, stated from a read source

The definition below is Mahmoody–Xiao's statement of Blum and Kannan's notion, **Read** in MX10 §1.2
(the original JACM paper was not opened):

> "C is a program checker for a problem Π if, when C is given an instance x and a program P, if P
> decides Π correctly (for all inputs, not just x), then C(P, x) outputs the correct answer for x with
> high probability, while if P decides x incorrectly then with high probability C(P, x) either outputs
> 'error' or finds the correct answer despite the incorrectness of P(x). Most checkers C require only
> oracle access to P and not the code of P."

*Plain reading: a checker is a fast referee. Hand it an input and a black box that claims to solve the
problem. If the box is honest, the referee reports the right answer. If the box lies on this input, the
referee either catches the lie and says "error", or gets the right answer anyway. Crucially the referee
must be sound against **every** box, honest or not — it can never be talked into a wrong answer.*

MX10 §1.2, Read, also records Blum and Kannan's characterization:

> "L is checkable (with C using only oracle access to P) if and only if L and L̄ have interactive proofs
> where the prover answers only queries of the form 'x ∈ L?' and soundness is only required to hold
> against non-adaptively cheating provers."

*Plain reading: a language has a checker exactly when both it and its complement can be proved by an
interactive proof whose only prover is a membership oracle for the language itself. So a checker for L
is an interactive proof of **non**-membership whose prover is no more powerful than L.*

The precise average-case version we actually need is **Hirahara–Santhanam Definition 7** (Read):

> For a class C of oracle algorithms, a randomized oracle algorithm C ∈ C is an **AvgC-instance
> checker** for a distributional problem (L, D) if for every (n, δ⁻¹) ∈ ℕ²:
> 1. Pr_{x∼D_n, C}[ C^L(x; n, δ) ≠ L(x) ] ≤ δ  (completeness against the honest oracle);
> 2. Pr_C[ C^A(x; n, δ) ∉ {L(x), ⊥} ] ≤ δ for **every** x ∈ supp(D_n) and **every** oracle A
>    (soundness, worst-case in x and in the oracle);
> 3. C^A halts in time poly(n/δ) on every oracle and every x ∈ supp(D_n).
>
> If item 2 is weakened to hold only on average over x ∼ D_n, C is a **HeurC-instance checker**.

*Plain reading: the checker may be wrong only on a δ fraction when the box is honest; but against a
lying box it must never produce a wrong answer on **any** input — only the right answer or "I don't
know". The whole difficulty is that item 2 is a worst-case condition.*

Note the asymmetry that decides everything below: item 1 is average-case, item 2 is worst-case.

### 1.2 The Hirahara–Santhanam theorem, stated from the paper

Two theorems, not one. HS22's headline is an **equivalence for NP**, and a separate **generic
transfer** that applies to any problem.

**HS22 Theorem 8 (generic; Read).** Let (C, D) ∈ {(BPP, PSamp), (BPP/poly, PSamp/poly)}. If there is
a *nonadaptive* AvgC-instance checker for (L, D), then there is a distribution D′ ∈ D and an
*errorless-to-error-prone nonadaptive C-reduction* from (L, D) to (L, D′).

**HS22 Proposition 6 (Read)** says what that reduction buys, and this is the operative statement for us:

    an errorless-to-error-prone BPP-reduction from (L, D) to (L′, D′)   ⟺   for every oracle R,
    (L′, D′) ∈ HeurBPP^R  implies  (L, D) ∈ AvgBPP^R.

*Plain reading: the checker converts "there is a fast algorithm that is right on most inputs and may
lie" into "there is a fast algorithm that is right on most inputs and never lies" — for the same
problem, at a different input distribution, and in every oracle world.*

**HS22 Theorem 20 (Read, with proof).** Let L and H be languages. If there is a *checker for L by H*
(HS22 Prop. 19: a pair of PCP systems, one for L and one for L̄, whose honest oracles are H), then
`{H} × PSamp^H ⊆ HeurBPP` implies `{L} × PSamp^H ⊆ AvgBPP`.

*Plain reading: if you can prove both "x is in L" and "x is not in L" to a fast verifier, using a
helper that answers questions about H, then an error-prone average-case algorithm for H upgrades to an
errorless average-case algorithm for L.*

**HS22 Theorem 14 (Read).** For every NP-complete L, the following are equivalent: (1) for every
D ∈ PSamp/poly there is a nonadaptive AvgBPP/poly-instance checker for (L, D); (2) for every
D ∈ PSamp/poly there is an errorless-to-error-prone nonadaptive BPP/poly-reduction from (L, D) to
some (L′, D′) with L′ ∈ NP, D′ ∈ PSamp/poly.

Three corrections to how this theorem is usually paraphrased, all from the text:

- The equivalence is for **NP-complete** L only, and needs **non-uniformity** (BPP/poly, PSamp/poly).
  HS22 says why: the direction (2) ⇒ (1) uses Mahmoody–Xiao's non-uniform tester, whose advice is the
  probability that a yes-instance is sampled.
- The average-case notion is **AvgBPP / HeurBPP** — randomized errorless and randomized error-prone
  heuristic schemes. That is exactly the notion `H_pK` is stated in (GKLO22 Def. 4 / Lemma 6), so the
  notions line up with no translation.
- The theorem is about **decision problems and their distributions**, not promise/gap problems. HS22
  never states it for a promise problem. **[Inference]** for GapMINKT one would first have to fix a
  decision version; nothing in HS22 forbids that, but it is not covered by the statement as written.

**What HS22 prove unconditionally, without any checker (Read):** Theorem 22, DistP ⊄ AvgNC¹ ⇒
DistP ⊄ HeurNC¹; Theorem 25, Dist(UP ∩ coUP) ⊄ AvgP ⇒ Dist(UP ∩ coUP) ⊄ HeurP. These are the only
unconditional errorless/error-prone equivalences in the literature we found.

### 1.3 What is known to have instance checkers

From HS22 §1.1 (Read) and MX10 §1.2 (Read):

- **P^{#P}-, PSPACE-, EXP-complete languages have instance checkers**, via the interactive-proof line
  (LFKN, Shamir, BFL). [*cited via HS22 §1.1 and MX10; the IP papers were not opened.*]
- **TFNP relations are trivially checkable** (MX10 §1.2.1, Read): given a claimed solution, verify the
  relation; totality means the oracle can never truthfully say "no solution exists". *This is the one
  structural feature that makes checking easy, and it is exactly the feature compressibility lacks.*
- **NP: open since 1995.** MX10 §1.2, Read: "Whether or not SAT is checkable has been an open problem
  since checkability was defined [6]." HS22 §1.1, Read, sharpens the upper bound:

  > "Using the connection between interactive proof systems and instance checkers, this question is
  > essentially equivalent to whether coNP can be proved by multi-prover interactive systems with
  > honest provers being NP. The best upper bound is P^{#P}, which follows from [LFKN]. Improving this
  > upper bound is a well-known open question."

  *Plain reading: to check SAT you must be able to prove **unsatisfiability** to a fast verifier using
  a helper that only answers satisfiability questions. Today the weakest helper anyone knows how to use
  is a counting oracle, which is much stronger than NP. Closing that distance is the open problem.*

- **What is NOT a barrier.** The commonly-recalled "checkable ⇒ NEXP ∩ coNEXP" is real but vacuous
  here: NP ⊆ EXP ⊆ NEXP ∩ coNEXP, so it rules nothing out for SAT or MINKT. Anyone quoting it as an
  obstruction is quoting the wrong fact. **[Inference]** from the containment; the NEXP ∩ coNEXP claim
  itself is **[Unverified — search summary only]**.
- HS22 Theorem 17 (Read): every NP-complete problem *does* admit a nonadaptive **HeurBPP/poly**-instance
  checker — the error-prone weakening of Definition 7, where soundness only holds on average. So the
  entire difficulty of checking NP is concentrated in strengthening item 2 from average-case to
  worst-case soundness.

### 1.4 What an instance checker for MINKT/GapMINKT would imply structurally

This is the sharpest thing in the note, and it is a theorem rather than a guess.

**Beigel's theorem, verbatim from MX10 Theorem 1.3 (Read; original unpublished, cited via Blum–Kannan):**

> "Suppose Π is decidable by a randomized reduction A with oracle access to Π′, and conversely Π′ is
> decidable by a randomized reduction A′ with oracle access to Π. Then Π is checkable if and only if
> Π′ is checkable."

*Plain reading: checkability travels in both directions along mutual randomized reductions. Two
problems that can each solve the other are checkable together or not at all.*

Now apply it. One direction is free: MINKT ∈ NP, so MINKT reduces to SAT. The other direction is the
recent NP-hardness line. **Hirahara CCC 2022 §6.2 (Read):** "Gap_τ MINcKT is NP-hard under randomized
reductions if τ(|x|, |y|, t) is sublinear in the length of y"; in fact it is NP-hard to approximate
K^t(x | y) within a factor |x|^{1/(log log |x|)^{O(1)}}. [Allender–Cheraghchi–Myrisiotis–Tirumala–Volkovich
and Liu–Pass proved NP-hardness of sublinear-time-bounded conditional K^t; *cited via Hirahara CCC 2022
§1.2, Read*. Huang–Ilango–Ren STOC 2023 proved NP-hardness of approximating meta-complexity by a
cryptographic route; *Abstract-only*.]

**[Inference] B31.1 (scope-limited).** Write `Π_sub` for `Gap_τ MINcKT` with τ sublinear in the length
of the conditioning string — **exactly** the object Hirahara CCC 2022 §6.2 proves NP-hard under
randomized reductions. `Π_sub ∈ NP` reduces to SAT; SAT randomized-reduces to `Π_sub` by that
NP-hardness. So by Beigel's theorem, **a Blum–Kannan instance checker for `Π_sub` exists if and only if
SAT is checkable.** The inference is labelled because Beigel's statement is for "randomized reduction
with oracle access" and the NP-hardness reductions of this line are randomized many-one/Turing
reductions whose exact form was not matched to Beigel's hypothesis line by line.

**What B31.1 does NOT cover, and this matters.** Beigel's theorem needs the *same* problem on both
sides, and meta-complexity problems are not interchangeable:

- **GapMINKT proper — the object of Hirahara's Theorem 1.3 and of the field's SoI characterization —
  is not reached.** Ko constructed an oracle under which NP ≠ P but GapMINKT is easy, so no relativizing
  reduction makes GapMINKT NP-hard [Hirahara CCC 2022 p. 26:6, Read]. B31.1 therefore says nothing
  about a checker for GapMINKT; for that object the status remains the plain "open, nobody has built
  one", with no equivalence to SAT-checkability in hand.
- **Our own `L` is not obviously covered either.** Its time bound is `|w|`, linear in the length of the
  conditioning pair (w, w′), not sublinear, so it is not an instance of `Π_sub` as stated.
- **The brittleness is a documented phenomenon, not a technicality.** Ren–Santhanam Theorem 13 (Read)
  gives relativized worlds where MCSP[2^{n/2}] ∈ P while MCSP[2^{n/4}] is very hard: "a slight change
  in the definition of a meta-complexity problem could result in a completely different problem."

Independent confirmation that the field reads it this way: HS22's own second motivation (§1.1, Read)
is "the only obstacle to basing the existence of one-way functions on the worst-case hardness of MINKT
is the gap between errorless and error-prone average-case complexity", and Hirahara–Nanashima CCC 2022
§1 (Read) states flatly that HS22 "identified a deep connection between the question of errorless
versus error-prone average-case complexities and the question of constructing an instance checker for
NP, which is another long-standing and important open question raised in the seminal work of Blum and
Kannan."

**Consequence for us.** The object `characterization_attempt.md` §4 item 3 proposed to build ("build the
instance checker for pK^t in moment form") is not merely open. For the one variant the NP-hardness line
reaches it is **[Inference]** equivalent to a named 30-year-old open problem with a known and apparently
unmovable upper bound (P^{#P} honest provers); for the variants nearer our `L` and nearer GapMINKT it is
open with no equivalence established in either direction. Either way a session-sized attempt was already
called not credible there, and B31 does not change that; what B31 adds is that the *first* variant is
provably as hard as SAT-checkability rather than merely unstudied.

---

## 2. Partial and related results (Question 2)

Searched: instance checker MCSP/MINKT; self-correction for Kolmogorov complexity; worst-case to
average-case MINKT errorless; Hirahara errorless/error-prone; Ilango MCSP self-reducibility; Hirahara
STOC 2023; Liu–Pass leakage-resilient MK^tP; Ren–Santhanam; Mazor–Pass 2024; probabilistic Kolmogorov
instance checker 2024–2026. Result by result, with the question "does this give a checker?":

| result | does it give a checker? |
|---|---|
| **Hirahara CCC 2022 §7, Def. 7.2 + Lemma 7.5 (Read)** — a "checker" C in a *strong universal heuristic scheme* (S, C): C(x, 1^t, 1^k) = 1 whenever cd^{t,p^{(3)}(t)}(x) ≤ k, and C(x,1^t,1^k)=1 implies the solver is right on x. Built from the algorithm of Fact 3.4 by estimating **computational depth**, i.e. K̃(x,1^t) − K̃(x,1^{p^{(2)}(t)}) ≤ k + log p^{(3)}(t). | **No — and this is the grep-trap.** It is a *one-sided depth certifier*, not a Blum–Kannan instance checker: it certifies "the solver's answer on this input is trustworthy", it is not sound against an adversarial oracle, and Lemma 7.5 assumes **GapMINKT ∈ P** — it consumes exactly the worst-case algorithm we would want as a conclusion. Circular for our purpose. |
| **Longpré–Watanabe, via Hirahara CCC 2022 Lemma 8.3 (Read, with proof)** — SoI ⇒ a poly-time M that on (x, 1^t, 1^{2^k}) with cd^{t,q(t)}(x) ≤ k outputs the lexicographically first minimum-length t-time program for x. | **No.** It is a *search* algorithm, and Hirahara's own comment (Read) is that it "does not satisfy the definition of a weak universal heuristic scheme in that the parameter t cannot be chosen independently of the instance". Its cost is 2^k where k is the computational depth — the same 2^{O(n/log n)} wall as everywhere else. |
| **Hirahara–Santhanam ITCS 2022 Theorem 17 (Read)** — every NP-complete problem admits a nonadaptive **HeurBPP/poly**-instance checker. | **Partial, on the wrong side.** It is the error-prone weakening of Definition 7 (soundness only on average). It is exactly the object one gets for free from Mahmoody–Xiao's tester; upgrading average-case soundness to worst-case soundness is the whole problem. |
| **Hirahara–Santhanam ITCS 2022 Theorems 22, 25 (Read)** — unconditional errorless-from-error-prone for DistP against NC¹ and for Dist(UP ∩ coUP) against P. | **No checker, but a genuine unconditional closure** — for classes with unique witnesses on both sides (UP ∩ coUP) or with a weak adversary class. The "unique witnesses on both sides" structure is exactly the "yes and no both certified" structure compressibility lacks. |
| **Mahmoody–Xiao CCC 2010 §1.2.2 (Read) + Nanashima ITCS 2021 + Hirahara STOC 2023 footnote 7 (Read)** — "an auxiliary-input one-way function is instance-checkable": given an inversion oracle I and a query q, sample y, check f_q(I(q, f_q(y))) = y; if it fails, output ⊥. | **Yes — a real instance checker, but for the inversion oracle, not for a meta-complexity problem.** This is the best existing positive result of the whole search, and it is the mechanism by which Hirahara STOC 2023 Theorem 10.3 (Read) *conditionally closes the errorless/error-prone gap*: NP ≤^{BPP}_{tt} {I : I inverts f}/poly ⇒ DistNP ≤^{AvgBPP}_{tt} {I : I inverts g}/poly. The reason it works is that **inversion is a yes-side-only object: a claimed preimage verifies itself.** |
| **Hirahara STOC 2023 (Read, §1–2)** — OWF exists ⟺ approximating *distributional* Kolmogorov complexity is NP-hard under randomized reductions **and** NP is worst-case hard. Gap closed "by combining Nanashima's proof techniques of showing 'limits' of black-box reductions (ITCS'21) with non-black-box worst-case-to-average-case reductions of Hirahara (FOCS'18)". | **No checker for K^t.** It routes *around* the missing checker by putting the checkable object (the inverter) in the middle. This is the single most important structural lesson in the note; §3.3 below applies it to `H_pK`. |
| **Hirahara–Kabanets–Lu–Oliveira CCC 2024 (Read: abstract + §1.4 + Table 1)** — exact average-case search-to-decision for K^t in **both** errorless and error-prone settings under E ⊄ i.o.SIZE[2^{o(n)}]; unconditional errorless search-to-decision for rK^t over every samplable distribution; and a worst-case search algorithm from errorless average-case decision running in **2^{O(n/log n)}**, succeeding only at some explicitly computed t ≤ 2^{n^ε} depending on x. | **No checker.** Search-to-decision *within* each setting; it never crosses from error-prone to errorless. Their own open problem 4 (Read) is that their reductions are **non-black-box** — "Is it possible to obtain black-box search-to-decision reductions?" — which is the same wall from another side. Their item 3 reproduces the KK25 Appendix B parameters exactly: 2^{O(n/log n)} and a superpolynomial t. |
| **Mazor–Pass CCC 2024 (Read: abstract + §1 opening)** — first non-trivial search-to-decision for GapMINKT, running in 2^{εn} for any ε > 0, querying the oracle only on thresholds s + O(log |x|); plus a direct, length-preserving average-case search-to-decision for K^t. Central component: Kolmogorov–Levin SoI. | **No checker.** 2^{εn} is far above polynomial, and the reduction is search-to-decision, not errorless-from-error-prone. |
| **Ren–Santhanam STACS 2022 §2 (Read)** — Thm 13: relativized worlds where MCSP ∈ P but search-MCSP is very hard, and where MCSP[2^{n/4}] admits a poly-time errorless heuristic but MCSP[2^{n/2}] does not. Thm 14/15: a relativized world where a 2-approximation to Levin's Kt is in P, coexisting with EXP = ZPP. Thms 17/18: relativized worlds where GapMCSP (resp. GapMINKT) is hard on average under *some* samplable distribution and no auxiliary-input OWF exists. | **A reason none exists by relativizing means, for a related object.** RS22 note explicitly that the EXP-complete instance-checker results of Allender et al. are **non-relativizing** ("these results use the non-relativizing 'instance checkers' for EXP-complete problems"), and that they could not extend their oracle to an algebrizing one. Note also their own caveat on Thm 18: the hard distribution is *not* uniform, precisely because Liu–Pass's equivalence pins the uniform case to OWF. |
| **Ren–Santhanam via HS22 §1.1 and MX10 (Read)** — no result anywhere constructs an instance checker for any gap/approximate version of MCSP or MINKT. | **Nothing.** The literature contains zero checkers, full or gap, for meta-complexity problems. |
| **Goldberg–Kabanets RANDOM 2024 (Abstract-only)** — randomized NP-hardness of exact K (time-unbounded) under a many-one reduction with failure ≤ 1/t_R^{16} ⇒ coNP ⊆ NISZK, hence **NP ⊆ coAM**; and for K^t within n^δ additive error under honest non-adaptive randomized reductions, NP = coNP. | **A reason the conclusion is suspicious, not a checker.** These are the collapse consequences of the randomized reductions that Beigel's theorem would be applied to; they do not directly bar the checker. Flagged for the audit list as abstract-only. |
| **Liu–Mazor–Pass ECCC TR26-051, Apr 2026 (Abstract-only)** — the most recent work on the same wall; their own framing: "The notion of errorless average-case hardness, however, is seemingly insufficient for cryptographic applications where one needs to consider average-case hardness against attacks that simply may err with some probability." | **No checker as far as the abstract says.** Confirms the gap is still open as of April 2026. |
| **Ilango MCSP self-reducibility; Hirahara–Santhanam pseudorandom self-reductions for MCSP** | **[Unverified]** — no primary text opened. Search summaries say MCSP has a *pseudorandom* self-reduction under cryptographic assumptions (a relaxation of random self-reduction) and that a relativization barrier applies to deterministic search-to-decision and self-reduction for MCSP. Goes on the audit list; not used in any claim below. |
| **Nanashima, Simons open problems Spring 2023, Problem 12 (Read verbatim)** — "Does DistPH ⊆ HeurP imply DistNP ⊆ AvgP? Or can we show a relativization barrier?" … "The problem above is open even for a weaker consequence that DistNP ⊆ AvgSIZE[2^{O(n/log n)}]." | **Confirms there is no known barrier for the PH version**, while HN22 supplies one for the NP version. The 2^{O(n/log n)} appears again. |

---

## 3. Other routes across the errorless/error-prone gap (Question 3)

### 3.1 The routes, and whether pK^t has them

| route | what it needs | does pK^t / the GKLO22 language have it? |
|---|---|---|
| **Random self-reducibility** | decide x by querying the oracle at uniformly random points | **No, and not known for any meta-complexity problem.** Feigenbaum–Fortnow-style results say NP-complete problems are not non-adaptively RSR unless PH collapses; for MCSP only a *pseudorandom* self-reduction is claimed, under cryptographic assumptions [**[Unverified]**]. Note the direction: RSR ⇒ self-correction (Blum–Luby–Rubinfeld) [**[Unverified]**], and self-correction is precisely error-prone-to-errorless for the *worst case*. This is the classical route and it is closed. |
| **Downward self-reducibility** | decide length-n instances from shorter ones | Not known for MINKT; HKLO CCC 2024 open problem 1 (Read) states the *worst-case* search-to-decision question is open, and Ren–Santhanam Thm 13 (Read) gives a relativized world where MCSP ∈ P but search-MCSP is hard, so even search-to-decision needs non-relativizing tools. |
| **Search-to-decision plus verification** | find a witness, then verify it | **Partially yes, and this is the live one.** See §3.3. |
| **Bogdanov–Trevisan style** | rules out non-adaptive worst-to-average reductions for NP unless NP/poly = coNP/poly | Applies to the *top* arrow of our sandwich, not this one. HS22 §1.1 (Read) states flatly: "the implication of this result to errorless-to-error-prone reductions is left unexplored." So BT is neither a route nor a barrier here. |
| **Impagliazzo–Levin domination** | reduce samplable distributions to the uniform one | Already used implicitly: Hirahara CCC 2022 footnote 4 (Read) records that restricting D to {uniform, tally} loses nothing, "a consequence of the theorems of Impagliazzo and Levin, Buhrman et al." So `H_pK` being stated on uniform inputs costs nothing in generality. It does **not** cross the errorless/error-prone divide. **[Unverified]** as to the exact form of IL's theorem; not opened. |
| **Instance checker** | §1 | Equivalent to SAT checkability, **[Inference] B31.1**. |
| **The testable-object detour (Nanashima/Hirahara STOC 2023)** | put a *self-verifying* object in the middle of the reduction | **This is the only route that has actually worked.** §3.3. |

### 3.2 Certifying incompressibility: the sharpest statement

The brief asks for the sharpest statement about certifying `K(x) > c`. Three levels, kept separate:

1. **Unbounded, proof-theoretic.** Chaitin's incompleteness: a sound theory proves only finitely many
   statements of the form K(x) > c, for c above a constant depending on the theory. **[Unverified —
   search summaries only; no primary source opened.]** This is the *right shape* but the wrong object:
   it is about a fixed theory, not about a polynomial-time algorithm, and it is about unbounded K.
2. **Time-bounded, algorithmic — the correct version.** For K^t and pK^t the corresponding statement
   is *not* an impossibility; it is a **natural property**. KK25 Definition 2.11 (Read): a natural
   property for conditional K^t with usefulness s(n,t) is a predicate P with (a) P(x,y,1^t) = 1
   whenever K^t(x|y) ≤ s(n,t), for **all** x, y; and (b) for every y, Pr_{x uniform}[P(x,y,1^t) = 0]
   ≥ 1/2. The rejecting side of such a P is a poly-time-recognized set containing **no** string of
   complexity ≤ s. *Plain reading: a natural property is a fast test that never says "hard" about an
   easy string, and says "hard" about at least half of random strings. Its "hard" verdicts are exactly
   certificates of incompressibility — not for one named string, but for a whole recognizable set.*
   So the honest statement is: **certifying incompressibility for K^t in polynomial time is possible
   in principle, and is the same object as a natural property; no unconditional obstruction applies.**
3. **The reason no checker follows from this.** A natural property's "hard" verdicts are sound for all
   inputs (that is item (a), a worst-case condition), but a natural property is *not* an interactive
   proof of incompressibility — it gives the verifier no way to be convinced by an adversarial helper.
   That is why §1's checker question stays open even though §2's certification question does not.

### 3.3 The asymmetry, stated exactly

The GKLO22 language of `H_pK` is
`L = {(u, v, w, w′, 1^s) : ∃ M of length s, M(w, w′) prints uv in |w| steps, s = |u|+|v|−10}`,
with D uniform on (u, v, w, w′).

- **The yes-side is *soundness*-free, but not *answer*-free — distinguish these.** A yes-instance has a
  poly-time-verifiable witness: the program M itself (run it for |w| steps and compare the output). So
  an errorless algorithm that answers "yes" can never be wrong — it only answers yes when it holds a
  witness. This is *exactly* the structure that makes an auxiliary-input one-way function
  instance-checkable (Hirahara STOC 2023 fn. 7, Read: "we can approximately check whether the oracle
  inverts f on q … if this does not hold … output ⊥"). **[Inference]** therefore any error-prone
  *search* heuristic that finds short programs on the compressible slice upgrades for free to errorless
  yes-answers, by verifying the witness. **But verification is not finding.** Yes-instances are a
  *constant* fraction of the uniform inputs — up to 2^{−10} — not a negligible one, so an AvgBPP scheme
  with failure δ ≪ 2^{−10} must actually *answer* "yes" on most of them, and that needs an average-case
  **search** algorithm for short programs on the compressible slice. Nothing certifies the yes-side into
  existence; it has to be computed.
- **The no-side is the other half of the problem.** "No program of length |uv|−10 prints uv from
  (w, w′) in |w| steps" has no witness. Certifying it is certifying incompressibility, which by §3.2
  means exhibiting a natural property, which by §4 is one of the two things the converse needs.

*Plain reading: half of the errorless algorithm is sound for free and the other half is the open
problem — but even the free half still has to produce answers. Saying "this string is compressible" is
easy to **prove** once you have found the short program; finding it is a separate job. Saying "this
string is not compressible" has nothing to show at all.*

---

## 4. Our specific problem: is `H_pK` the same thing as a natural property? (Question 4)

### 4.1 The equivalence, worked out

**[Inference] B31.2 (H_pK ⇒ a natural property).** Let A be a randomized errorless heuristic scheme
for (L, D) with failure parameter δ, as in `H_pK`. Define
`P(u,v,w,w′) := 1` iff A does **not** output "no" (i.e. A outputs "yes" or ⊥). Then:

1. **Usefulness, worst-case.** If K^{|w|}(uv | w,w′) ≤ |uv| − 10 then (u,v,w,w′) ∈ L, and A is
   errorless, so A never outputs "no" on it; hence P = 1 on *every* compressible input.
2. **Largeness.** At most 2^{|uv|−10} programs exist, so for each (w,w′) at most a 2^{−10} fraction of
   (u,v) is a yes-instance. A is correct on ≥ 1 − δ of inputs, so it outputs "no" on at least
   1 − δ − 2^{−10} of all inputs; that is, Pr[P = 0] ≥ 1 − δ − 2^{−10}.

Note the measure: `L` quantifies over **deterministic** programs M, so B31.2 produces a natural property
for conditional **K^t**, not for pK^t. That is the right typing — conditional K^t is exactly what KK25
Definition 2.11 and Lemma 2.16 take as input. (A pK^t property would be the *stronger* object, since
pK^t ≤ K^t + O(1); we do not have it.)

Item 1 is exactly KK25 Definition 2.11(1) with usefulness `n − 10`; item 2 is Definition 2.11(2) with
largeness `1 − δ − 2^{−10}`, far stronger than the required 1/2, except that KK25 demand largeness
**for every** conditioning string y while `H_pK` gives it only on average over (w,w′).

*Plain reading: an errorless algorithm for the compressibility problem **is** a natural property. Its
"no" answers are the property's rejections: they are sound on every input because the algorithm never
lies, and they cover almost every random input because the algorithm almost always answers.*

**B31.3 (the converse direction is NOT established; two separate gaps).** A BPP-computable natural
property P for conditional K^t with usefulness `n − 10` yields the algorithm "output no if P = 0,
output ⊥ if P = 1". Two things stop that from being an errorless heuristic scheme for (L, D):

- **Gap 1, largeness.** The algorithm fails on a `1 − (largeness)` fraction. With KK25's largeness 1/2
  that is a `1/2`-errorless heuristic, **not** an AvgBPP scheme, which requires failure ≤ δ for every
  δ = 1/poly. **Whether largeness for conditional K^t amplifies from 1/2 to 1 − 1/poly is not answered
  by anything we read, and is flagged open.** (The natural candidate — re-randomising the helper string
  (w, w′) and taking an OR of rejections — changes the usefulness parameter, and was not checked.)
- **Gap 2, the missing yes-answers (§3.3).** The property never outputs "yes". Yes-instances carry up to
  a constant `2^{−10}` of the mass, so a scheme with failure δ ≪ 2^{−10} must answer "yes" on most of
  them; the property supplies no such answers. Closing this needs an average-case *search* algorithm for
  short programs on the compressible slice, which is a second, independent requirement.

**Verdict on Question 4 as posed: one direction only.** `H_pK ⇒` a BPP-computable natural property for
conditional K^t, useful against small programs, is **[Inference] B31.2** and is solid. The converse is
*not* established: a natural property is the no-side of `H_pK`, and `H_pK` needs both sides. So
`BEM_skew ⇒ H_pK` is **at least as strong as** `SoI-moment-bound ⇒ natural property`, which KK25 §8
(Read) names as their technical challenge; the two are the same statement only if both gaps close:

> "One specific technical challenge is to try to derive a polynomial-time computable natural property,
> say for K^t, from the assumed SoI for K^t. It is possible to get a 2^{O(n/log n)} computable natural
> property from SoI for K^t (see Appendix B), but it is not clear how to get time, say 2^{O(√n)}."

### 4.2 How much the converse would prove (this is bigger than it looks)

KK25 Lemma 2.15 and Lemma 2.16 (both Read, with proofs) run the loop in both directions:

- **Lemma 2.15:** `Gap_{τ,δ}McK^tP ∈ promise-P` ⇒ a P-computable natural property for conditional K^t
  with usefulness `n − δ(n,t) − 2`.
- **Lemma 2.16:** a P-computable natural property with usefulness `n − δ(n,t)` ⇒ (under E ⊄
  io-SIZE[2^{o(n)}]) `Gap_{τ,δ′}McK^tP ∈ promise-P` with `δ′(n,t) = δ(2n,2t) + O(log(nt))`, by feeding
  the direct-product generator DP_x^k into the property and using it as a distinguisher.
- **Corollary 2.19 (Read):** the same equivalence for **pK^t** and BPP, and — this matters for us —
  **without** the E ⊄ io-SIZE assumption, because pK^t is probabilistic.

*Plain reading: a fast test that recognises most random strings as hard is the same thing as a fast
worst-case algorithm that approximates description length. Kabanets and Kolokolova prove this both ways,
and in the probabilistic version they need no extra assumption.*

**[Inference] B31.4, with one gap named.** Chaining B31.2 into Lemma 2.16 at `δ = 10` would give:
`H_pK` implies `Gap_{τ, O(log nt)} McK^tP ∈ promise-P` (or its BPP/pK^t form via Cor 2.19) — a
**worst-case**, logarithmic-gap algorithm for conditional K^t. **The chain is not clean as it stands.**
Lemma 2.16's proof applies the assumed property at the conditioning string `z ∘ y` for an *adversarial*
y, so it consumes KK25's **per-y** largeness; B31.2 delivers largeness only on average over (w, w′).
Closing that mismatch is part of Gap 1 and is not done here.

If the chain is repaired, then with `H_pK ⇒ BEM_skew` (Prop. B21.1(b) of
`characterization_attempt.md`) the converse `BEM_skew ⇒ H_pK` would give

    BEM_skew  ⟺  H_pK  ⟺  Gap_{τ,O(log)} McK^tP worst-case easy  ⟺  natural property for conditional K^t

*Plain reading: if those conditions really are the same thing, then proving our converse would not just
settle our open problem. It would exactly characterize an exponential-moment symmetry of information by
the worst-case complexity of approximating description length — the characterization Hirahara says needs
an instance checker, and the one Kabanets and Kolokolova say is missing.* **[Inference]** subject to the
two gaps: our converse is at least as strong as, and plausibly the same as, (a moment-form instance of)
the field's problem.

**The hub that might make Gap 1 unnecessary, and the reason it is the cheap next check.** The worst-case
problem may be the right centre rather than the property. The candidate chain is: natural property
(largeness 1/2 suffices) ⇒ [KK25 Cor 2.19] worst-case `Gap McK^tP` easy ⇒ [Hirahara Theorem 8.2, item
1 ⇒ 2, whose proof is "Theorems 4.1 and 8.6"] an errorless scheme computing the **value** of
`K^t(−)` on every samplable D — which decides `L` at any threshold, and so supplies *both* the yes-side
and the no-side at once. If that holds in the conditional pK^t setting, largeness amplification is never
needed. Two things must be read to know: **Hirahara Theorem 8.6** (on disk, line 2053 of the local text;
only the proof *pointer* was read this session, not the theorem's proof), and whether GKLO22 contains the
conditional pK^t analogue (their Theorem 1, "Probabilistic Worst-Case to Average-Case Reductions", is the
place to look; also on disk). Both are an hour's reading, and neither was done here.

### 4.3 KK25 Appendix B: exactly what they get, and exactly why it stops

**Read in full.** Theorem B.2: assuming the chain rule for K^t with error δ(n,t) ≤ O(n^{1/2}/log n),
and for any sufficiently large polynomial t, there is a **2^{O(n/log n)}-time computable natural property
for K^t on n-bit inputs with usefulness s(n) = n − 2.**

The proof, in five steps as read:

1. Let `y_τ` be the lexicographically first K^τ(x)-witness — the shortest τ-time program for x.
2. SoI applied to the pair (x, y_τ) gives, for any large τ,
   `K^{p(τ)}(y_τ | x) ≤ K^τ(x) − K^{p(τ)}(x) + O(log τ) + O(n/log n)`.
   *Plain reading: given x, the shortest program for x costs at most the **computational depth** of x,
   plus lower-order terms. SoI turns "the pair is not cheaper than its parts" into "the witness is
   nearly free once you have x".*
3. **Lemma B.1 (Computational Depth Upper Bound, from Hirahara STOC 2021):** for every ε > 0 and
   polynomials q_dpt, p_dpt and large x, there **exists** a time bound t* with
   `q_dpt(n) ≤ t* ≤ 2^{n^ε}` and `K^{t*}(x) − K^{p_dpt(t*)}(x) ≤ O(n/log n)`.
4. At τ = t*: `K^{p(t*)}(y_{t*} | x) ≤ O(n/log n)`. Exhaustive search over all `w ∈ {0,1}^{O(n/log n)}`,
   running U(w) for 2^{n^ε} steps each, finds the witness; take the shortest output y that prints x.
5. Accept iff |y| ≤ n − 2. Soundness: (31) `|y| ≤ K^{t*}(x) ≤ K^t(x)` gives usefulness; (32)
   `K(x) ≤ |y|` with the counting bound `K(x) > n − c` for all but 2^{−c+1} of x gives largeness 1/2.

**Why it stops at 2^{O(n/log n)}, two independent defects, both read off the proof:**

- **(i) The depth term is O(n/log n), not O(log n).** Step 4's brute force is over `2^{O(n/log n)}`
  candidate conditional descriptions. To get polynomial time, Lemma B.1 would have to deliver a depth
  bound of `O(log n)`. Nothing in the literature gives that.
- **(ii) The time bound t* is superpolynomial and instance-dependent.** Lemma B.1 only promises *some*
  `t* ≤ 2^{n^ε}` depending on x, and each candidate is run for `2^{n^ε}` steps. A polynomial-time
  natural property must work at a fixed polynomial t. The same defect is visible in HKLO CCC 2024
  item 3 (Read): their worst-case search algorithm "only succeeds on some explicitly computed
  sub-exponential time bound t ≤ 2^{n^ε} that depends on x".

KK25's own gloss (§8, Read) confirms both: "it is not clear how to get time, say 2^{O(√n)}" — they do
not even claim the intermediate exponent, let alone polynomial.

---

## 5. Barriers (Question 5)

### 5.1 Razborov–Rudich is not a barrier here. Say so plainly.

The brief's phrasing invites the conclusion that a poly-time natural property for pK^t would violate
the natural-proofs barrier. It would not, and the argument is the same for K^t (the measure B31.2
actually delivers) and for pK^t. A BPP-computable natural property with usefulness n − O(1)
is a distinguisher, hence implies no one-way functions (KK25 §1 sketch, Read: "it breaks [the
generator] … allows one to distinguish between pairs"). But our sandwich **already** has `H_pK ⇒
BEM_skew ⇒ no io-OWF` (Prop. 2(c)). So the natural property's crypto-breaking consequence is
*implied by the hypothesis we are starting from*, not contradicted by it. Razborov–Rudich says
"natural properties and one-way functions cannot coexist"; we are working inside the branch where
one-way functions do not exist. **No contradiction, no barrier.** [Inference] from Cor 2.9 and §1 of
KK25 as read, plus Prop 2(c) of the paper.

Ren–Santhanam Theorem 16 (Read) is the relevant genuine caution in this neighbourhood, and it points
the other way: there is a relativized world where **neither** P/poly-natural properties useful against
SIZE[2^{δn}] **nor** auxiliary-input one-way functions exist. So "no OWF ⇒ natural property" is false
relative to an oracle. *That is a barrier against the bottom arrow of our sandwich reversing
(`no io-OWF ⇒ BEM`), which §7.3 already knows; it is not a barrier against `BEM_skew ⇒ H_pK`, whose
hypothesis is strictly stronger than "no OWF".*

### 5.2 The instance-checker route is barred in the only sense that matters

**[Inference] B31.1** (§1.4): an instance checker for **sublinear-time-bounded conditional gap K^t**
exists iff SAT is checkable. So for *that* object the route is not "barred" by a theorem saying it is
impossible; it is barred by being *equivalent to an open problem of 1995 whose best known upper bound
(P^{#P} honest provers, HS22 §1.1, Read) has not moved*. For research-planning purposes that is a
stronger deterrent than a barrier theorem, because a barrier at least tells you which technique to
abandon.

**The scope limit is load-bearing and must not be dropped.** For **GapMINKT** — the object of
Hirahara's Theorem 1.3, and the one whose checker would deliver the field's characterization — B31.1
gives nothing, because Ko's oracle (NP ≠ P with GapMINKT easy; Hirahara p. 26:6, Read) blocks any
relativizing NP-hardness reduction and so blocks the Beigel hypothesis. There, and for our own `L`
(whose time bound is linear, not sublinear, in the conditioning string), the status is the weaker and
honest one: open, unstudied, no equivalence proved in either direction.

Secondary, from Ren–Santhanam §2 (Read): the instance-checker technology that *does* exist (for
EXP-complete problems) is explicitly non-relativizing, and RS22 could not even extend their oracle to
an algebrizing one — so the tool that works for EXP leaves no relativizing trace to imitate.

### 5.3 The natural-property route is not barred, but it is quantitatively pinned

This is the sharpest obstruction we found, and it is a *quantitative* one.

- **Upper bound side.** Hirahara STOC 2021: `DistPH ⊆ AvgP ⇒ PH ⊆ DTIME(2^{O(n/log n)})`, and this
  holds **in every relativized world** [*cited via HN 2021 abstract, Read: "The lower bound on the time
  complexity is nearly optimal because Hirahara (STOC 2021) showed that DistPH ⊆ AvgP implies that PH
  can be solved in time 2^{O(n/log n)} under any relativized world."*]
- **Lower bound side.** Hirahara–Nanashima FOCS 2021 (Read, abstract): an oracle with `DistPH^O ⊆
  AvgP^O` while UP^O ∩ coUP^O and PAC learning are hard even for `2^{n/ω(log n)}`-time algorithms.
  Hirahara CCC 2022 p. 26:6 (Read) states the consequence: "a relativizing proof technique is incapable
  of improving the time complexity 2^{O(n/log n)} achieved in [Hir21] to 2^{o(n/log n)}."
- **The same exponent in the error-prone world.** HN22 (Read): `GapMINKT^O ∉ pr-SIZE^O[2^{o(n/log n)}]`.
- **Hirahara says the depth term itself is relativization-pinned.** Remark 6.4 (Read, verbatim in
  substance): if K^{t,SAT}(x|y) could be approximated with additive error `o(cd^{t,p(t)}(y))` under
  DistΣ₂^p ⊆ AvgP, "we would obtain an improved algorithm that solves every language L ∈ NP in time
  2^{o(n/log n)}, which contradicts the relativization barrier of [HN21]."

**[Inference] B31.5.** The step our converse needs — replacing the computational-depth error term
`O(n/log n)` of KK25 Appendix B by `O(log n)` — is the same step Hirahara's Remark 6.4 argues a
relativizing technique cannot take. §7.7 of the paper records that *every object in our paper
relativizes*. **So a proof of `BEM_skew ⇒ H_pK` through the natural-property route, using only the
paper's existing relativizing machinery, is ruled out on quantitative grounds.** The inference is
labelled because Remark 6.4's hypothesis is `DistΣ₂^p ⊆ AvgP` and its object is `GapMINcKT^NP`, not
`BEM_skew` and conditional pK^t; the transfer is by analogy of the depth term, not by citation.

### 5.4 No oracle in hand separates `BEM_skew` from `H_pK`

`characterization_attempt.md` §3 left this at "[not verified]" for the error-prone world. B31 closes it.

**[Inference] B31.6.** Relative to the Hirahara–Nanashima 2022 oracle O (error-prone Heuristica),
`BEM_skew^O` **fails**. Reason: the paper's Proposition 5 proof fixes an arbitrary polynomial time
bound t and lower-bounds `pK^t(y)` and `pK^t(x|y)` on the masked slice M_t, against a forward bracket
of `2n + O(1)`. For the skewed object `Σ⁺_{s,P}` the two lower-bounded terms are taken at the larger
time P(s); but P is a polynomial, so `i(P(s)) ≤ (1/c) log log P(s) = O(log log n)` is still a mask
level and `log(1/μ) = o(n)` still holds with `M_{P(s)}` in place of `M_s`, while the forward bracket at
time s is unchanged. So `E_D[2^{Σ⁺_{s,P}}] ≥ 2^{n − o(n)}` by the same two Markov steps.

**Corollary.** Relative to that same O, `H_pK^O` also fails, by the contrapositive of Proposition
B21.1(b) — which relativizes, since GKLO22 state that every result of their §3 holds with any oracle
(Read). So the error-prone world has **both** sides false, and the two errorless worlds (HN 2021,
Impagliazzo 2011, via Prop. 6) have both sides true. **Every oracle world on record is consistent with
the equivalence.** The obstruction is B31.5's quantitative one, not a separating oracle.

---

## 6. Summary table

| route | what it would give us | status | sharpest source |
|---|---|---|---|
| **Blum–Kannan instance checker for *sublinear-time-bounded conditional gap* K^t** | Would close the errorless/error-prone gap for that object | **Barred in effect** — [Inference] B31.1: equivalent to "is SAT checkable?", open since 1995, best honest-prover upper bound still P^{#P} | HS22 §1.1 (Read); MX10 Thm 1.3 + §1.2 (Read); Hirahara CCC 2022 §6.2 (Read) |
| **Blum–Kannan instance checker for GapMINKT itself, or for our `L`** | Closes `BEM_skew ⇒ H_pK`; closes the field's SoI characterization (Hirahara Thm 1.3 becomes an equivalence); same-time question untouched | **Open, and B31.1 does not reach it** — Ko's oracle blocks relativizing NP-hardness of GapMINKT, so Beigel's hypothesis is unavailable; `L`'s time bound is linear, not sublinear, in the conditioning string | Hirahara CCC 2022 p. 26:6 (Read); RS22 Thm 13 (Read) on variant-brittleness |
| **Depth certifier (Hirahara CCC 2022 §7, Lemma 7.5)** | Nothing new: assumes GapMINKT ∈ P | **Circular** — consumes the conclusion; also not sound against adversarial oracles, so not a checker at all | Hirahara CCC 2022 Def 7.2, Lemma 7.5 (Read) |
| **HeurBPP/poly-instance checker for NP (HS22 Thm 17)** | Nothing: soundness only on average | **Known, wrong side of the divide** | HS22 Thm 17 (Read) |
| **BPP-computable natural property for conditional K^t, usefulness n − O(log n)** | The **no-side** of `H_pK`, not all of it. Closes `BEM_skew ⇒ H_pK` only with Gap 1 (largeness 1/2 → 1−1/poly, and average-over-y → per-y) and Gap 2 (average-case search for the yes-side) both closed. By KK25 Cor 2.19 it also gives the worst-case log-gap `McK^tP`, i.e. the field's SoI characterization. Same-time question untouched | **Open, and pinned** — KK25 App B gets 2^{O(n/log n)} only, at a superpolynomial instance-dependent t*; [Inference] B31.5 says the missing step is relativization-barred | KK25 §8 + App B Lemma B.1/Thm B.2, Lemmas 2.15/2.16, Cor 2.19 (Read); Hirahara CCC 2022 Remark 6.4 (Read) |
| **`H_pK` ⇒ natural property (our direction)** | Shows the two are not unrelated: `BEM_skew ⇒ H_pK` is *at least as strong as* KK25's stated challenge | **[Inference] B31.2, solid** — the "no" answers of an errorless scheme are the property's rejections | B31 §4.1; KK25 Def 2.11 (Read) |
| **Search-to-decision + witness verification (yes-side)** | Soundness of the yes-side for free — but **not the answers**: yes-instances are a constant ~2^{−10} fraction, so they must be *found*, not merely verified | **Known, and smaller than it looks** — B31 §3.3 | Hirahara STOC 2023 §2.1.3 fn. 7 + Thm 10.3 (Read); MP24, HKLO24 (Read, abstracts + §1.4) |
| **Testable-object detour (Nanashima ITCS'21 / Hirahara STOC'23)** | Closes the errorless/error-prone gap *conditionally*, by routing through an inversion oracle that is self-checking | **Known, partial, and the best working template** — it never builds a checker for K^t | Hirahara STOC 2023 Thm 10.3, §2.1.3 (Read); MX10 §1.2.2 (Read) |
| **Worst-case `Gap McK^tP` / `McpK^tP` as the hub** | Would give **both** sides of `H_pK` at once and make largeness amplification unnecessary: property ⇒ [Cor 2.19] worst-case easy ⇒ [Hirahara Thm 8.2, 1⇒2, via Thm 8.6] errorless scheme computing the *value* of K^t on samplable D, which decides `L` at any threshold | **Unchecked — the cheapest open item.** Needs Hirahara Thm 8.6 read (on disk, not opened) and the GKLO22 conditional pK^t analogue located (their Thm 1) | Hirahara CCC 2022 Thm 8.2 + Thm 8.6 (proof pointer Read, theorem not); GKLO22 Thm 1 (Read, abstract level) |
| **Random / downward self-reducibility of K^t / pK^t** | Would give self-correction, i.e. errorless-from-error-prone directly | **Not available** — no meta-complexity problem is known to be RSR; MCSP only pseudorandomly self-reducible under crypto assumptions [**[Unverified]**]; relativized world where MCSP ∈ P but search-MCSP is hard | RS22 Thm 13 (Read); Ilango / HS pseudorandom self-reductions **[Unverified]** |
| **Bogdanov–Trevisan collapse** | Nothing for this arrow | **Not applicable** — HS22 says the implication of BT to errorless-to-error-prone reductions "is left unexplored" | HS22 §1.1 (Read); BT06 (Read, partial) |
| **Impagliazzo–Levin domination** | Confirms uniform-input `H_pK` loses no generality | **Known, already used, does not cross the divide** | Hirahara CCC 2022 fn. 4 (Read); IL original **[Unverified]** |
| **Relativizing oracle separating `BEM_skew` from `H_pK`** | Would kill the converse outright | **Does not exist in the literature, and [Inference] B31.6 says the obvious candidate fails**: in HN22's error-prone world both `BEM_skew` and `H_pK` are false | HN22 Thm 4 (Read); the paper's Prop. 5; GKLO22 §3 relativization remark (Read) |
| **Razborov–Rudich natural-proofs barrier** | — | **Not triggered.** A K^t (or pK^t) natural property implies no OWF, which the hypothesis already implies. Not a contradiction | KK25 Cor 2.9 + §1 (Read); paper Prop. 2(c) |

---

## 7. Verdict

There is exactly one route to `BEM_skew ⇒ H_pK` that is not known to be barred, and it is the
natural-property route, not the instance-checker route. The instance-checker route should be struck from
the thread list, for two different reasons depending on the object: for sublinear-time-bounded
conditional gap K^t, Beigel's theorem plus that problem's randomized NP-hardness makes a checker
*equivalent* to a checker for SAT — open since 1995, honest-prover bound still stuck at P^{#P} — while
for GapMINKT itself and for our own language `L` the equivalence is unavailable (Ko's oracle blocks
relativizing NP-hardness of GapMINKT, and `L`'s time bound is linear rather than sublinear in the
conditioning string), leaving them simply open and unstudied; either way there is no session-sized or
pass-sized attack. The natural-property route is different in kind, but weaker than it first looked:
§4 proves only **one** direction, that `H_pK` on uniform inputs *implies* a BPP-computable natural
property for conditional **K^t** (not pK^t — `L` quantifies over deterministic programs) with usefulness
`n − 10`; the converse needs two things a property does not supply, largeness amplified from 1/2 to
1 − 1/poly and from average-over-conditioning to per-conditioning, and an average-case *search*
algorithm for the yes-side, which carries a constant `2^{−10}` of the mass and must be answered, not
merely verified. So the accurate statement is that `BEM_skew ⇒ H_pK` is **at least as strong as**
Kabanets–Kolokolova's stated technical challenge, and is the same statement only if both gaps close.
Nothing *forbids* it: Razborov–Rudich is not triggered (a K^t natural property implies no one-way
functions, which our hypothesis already implies), and no oracle separates the two sides — B31.6 shows
that in Hirahara–Nanashima's error-prone world both `BEM_skew` and `H_pK` are false, so every oracle
world on record is consistent with the equivalence. What does stand in the way is quantitative and, as
far as we can tell, relativization-hard: KK25's Appendix B derives the natural property from SoI only at
2^{O(n/log n)} time and only at some superpolynomial instance-dependent time bound `t* ≤ 2^{n^ε}`,
because Hirahara's computational-depth lemma caps the depth at `O(n/log n)`, and Hirahara's own Remark
6.4 argues that improving that depth term by relativizing means would yield 2^{o(n/log n)} algorithms
for NP and contradict Hirahara–Nanashima's oracle; since §7.7 of our paper records that every object in
it relativizes, the paper's existing machinery cannot take that step. **The best next attempt is an
hour of reading, not a proof: check whether the worst-case problem is the hub.** If the chain "natural
property (largeness 1/2 is enough) ⇒ [KK25 Cor 2.19] worst-case `Gap McK^tP` easy ⇒ [Hirahara Theorem
8.2 item 1 ⇒ 2, via **Theorem 8.6**] an errorless scheme computing the *value* of K^t on every samplable
D" goes through in the conditional pK^t setting, then it decides `L` at any threshold and delivers both
sides of `H_pK` at once — Gap 1 and Gap 2 both evaporate and no largeness amplification is ever needed.
Two documents settle it and both are already on disk: Hirahara Theorem 8.6, of which only the proof
*pointer* was read this session, and GKLO22's Theorem 1 track for the conditional pK^t analogue. Do that
before attempting anything. The second-cheapest item is to write B31.6 into §7.3 of the paper, since it
upgrades `characterization_attempt.md` §3's "[not verified]" to a checked statement and removes the last
suspicion that an oracle separates the two sides.

**Correction, 15 Sep 2026 (thread B36, written into the paper at E68).** The linear-gap reading of §4.2 applies to Kabanets–Kolokolova 2025 Theorem 6.3 and Corollary 2.19 only. Their Lemma 2.16 and Theorem 3.4 are parametric in δ and give a logarithmic gap at logarithmic usefulness (`b36_worst_case_hub.md` §10); Theorem 3.4 at ℓ = 2, y = ε, δ = O(log n) gives (H1) of the paper's Proposition 2(a) directly, now the paper's Proposition 8. B31.6 is in the paper's §7.3 as of E68.
