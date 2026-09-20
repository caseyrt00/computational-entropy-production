# Referee C — claims, oracle propositions, open-problem prose, interpretation, citation discipline

Manuscript: `passes/pass16/ENTROPY_PRODUCTION.md` (line numbers below are of that file; "L" = line). Typeset copy consulted for nothing beyond page count.
Joint: Propositions 4–7 (§7); §7.5–7.6; §1 and §1.1; §6; §8.1, §8.3, §8.4, §8.5; Appendix tables and notes; Conventions; reference list.
Sources: `passes/pass16/sources/` (.txt files as held; `hn_eccc_tr21-161`, `hn_ccc2022_lipics234-25`, `hn_focs2021_ea`, `hmo_eccc_tr26-021`, `bendavid_simons_slides`, `landauer1961` re-extracted with pdftotext into scratch; line numbers for those five refer to the scratch extractions and are marked "(scr)"). Nothing else in the repository was read. No web.

---

## Verdict

**Major corrections** for this joint. Single most important finding: §1.1 (L58) and its plain reading (L60) claim the open problem is "immune to relativizing proof in both directions of the same-time sandwich, in the sense of Propositions 5 and 6", but Proposition 6 is an [Inference] about two natural test distributions and exhibits no oracle world in which BEM holds and NP ⊄ BPP; nothing in the paper shows the top arrow immune to relativizing proof. The abstract (L26) states the bottom arrow only, correctly; §1.1 contradicts it, and the plain reading drops every hedge ("only that one family of proof methods cannot settle either arrow").

No BLOCKING error: every proposition in the joint that is labelled Proved or Proved-conditional is correct as a mathematical statement given its stated hypotheses (Propositions 4, 5, 7 verified line by line; Proposition 8's transcription of Kabanets–Kolokolova Theorem 3.4 verified; the authors' catch of a time-parameter gap in KK's proof of Theorem 3.4 is real and their fix is sound).

---

## Findings, ranked

### BLOCKING

None.

### MAJOR

**M1. §1.1, L58 and plain reading L60 — top-arrow immunity is asserted without a result.**
Quoted (L58): "The open problem of Section 7 is not shown to be hard, only immune to relativizing proof in both directions of the same-time sandwich, in the sense of Propositions 5 and 6 as stated: Proposition 5 for the bottom arrow, and Proposition 6, an inference from the natural test distributions with the general case left open, for the top." Plain reading (L60): "does not show its open problem is hard, only that one family of proof methods cannot settle either arrow."
Issue: immunity of "BEM ⇒ NP ⊆ BPP" to relativizing proof requires an oracle O with BEM^O true and NP^O ⊄ BPP^O. Proposition 6 (L647) says only that, relative to two errorless oracles, *specific* samplers have bounded moments; L647 itself: "This is a statement about those samplers, not about every sampler; the general case is the open question below." L657: "the general case, same-time BEM relative to the Hirahara–Nanashima 2021 oracle, is open." So the top arrow is not shown immune to anything. The abstract (L26) is right ("no relativizing argument reverses it" refers to the second arrow only). §1.1 is the section titled "What the results are not"; it must be exact.
Fix: L58 → "…only immune to relativizing proof for the bottom arrow, no io-OWF ⇒ BEM (Proposition 5, conditional as stated there). For the top arrow the relativization test has been run only on the natural test distributions of two errorless oracles (Proposition 6, [Inference]); whether same-time BEM holds relative to either oracle is open, so no barrier statement is made for that arrow." L60 → "…only that one family of proof methods cannot deliver the bottom arrow; for the top arrow nothing of the kind is shown."

**M2. Conventions (L10, L12) versus §1.1 (L58): statements resting on unread sources; a missing load-bearing citation; a physical condition used as a computational one.**
(a) L10: "no statement rests on a source that was not read." L58 rests on four sources tagged "cited via research note B30 §0, summary only; not opened": Gu et al. 2024 (the factual claim "pseudomagic for stabilizer entropy"), Gärttner et al. 2017, Mi et al. 2021, Google Quantum AI 2025 (the factual claims "more than a hundred trapped ions", "53 superconducting qubits", "65 qubits", and "none of these readings is a reading of complexity"). L12 defines "cited via X" as "taken from source X, which was read"; a search-result summary in an internal note is not a read source, so the tag is misused and the Conventions sentence is false as written.
(b) L58: "since a meter is by definition a distinguisher between pseudorandom and Haar-random states". This presupposes that pseudorandom quantum states exist under quantum-secure one-way functions. The manuscript contains no citation for that theorem (grep for "Ji", "JLS", "pseudorandom state", "Haar" returns only L58 and the title of Lee–Kwon–Cho in the reference list). The whole "complexity meter" sentence hangs on it.
(c) L18 (Conventions): "'efficiently samplable' is a condition on the running time of a sampler and is never presented as a physical condition." L58 uses "efficiently measurable observable" as a physical condition identified with an efficient quantum circuit, which is the same move for measurements, and it is made in the paper's own voice with no label. §6 (L486) says "if fast physical processes are quantum, the natural class is the BQP-samplable distributions, and nothing in this paper is stated for that class"; §1.1's quantum reading carries no such caveat.
Fix: (a) read Gu et al. and the three experimental papers, or delete the pseudomagic clause and the three experimental sizes; either way add a fourth read-status tag or stop using "cited via" for summaries, and amend L10 to what is true. (b) cite the pseudorandom-state existence theorem (a Read citation) or delete "by definition". (c) label the meter sentence [Inference], state the identification it uses ("an efficiently measurable observable is one implemented by a polynomial-size quantum circuit", i.e. the quantum extended Church–Turing thesis), and repeat the §6 caveat that Theorems 1–4 are stated for BPP samplers.

**M3. §7.1, L504–506 "What a proof would have to use. [Inference]" — a structural conclusion drawn from a construction the reader cannot see.**
Quoted: "Pass 16, research note 07, Proposition 6 exhibits, conditional on the existence of an injective one-way function that is exponentially secure, as stated there, a polynomial-time samplable pair distribution that violates BEM although its own function is not even weakly one-way … So a proof of the converse of Theorem 3 … must use the global hypothesis … it cannot proceed distribution by distribution."
Issue: the construction and its proof are not in the manuscript; the reference is to an internal note. The [Inference] label covers the reading, not the existence of the construction. A referee cannot check it, and the paragraph tells the reader what shape a proof must have.
Fix: inline the construction and its proof (if it is short) as a labelled Proposition-with-hypothesis, or cut the paragraph. Same standard for every "(Pass NN, research note …)" parenthetical in §7 (see m4).

**M4. Plain readings and one body sentence that turn an informal remark, an analogy, or an open question into a fact.**
(i) L717 (body): "Hirahara argues that a relativizing technique cannot improve the depth term in his own setting". Source, `hirahara_ccc2022_lipics234-26.txt:1322–1334`: "Below, we informally argue that a relativizing proof technique is unlikely to improve the error term cd^{t,p(t)}(y) … which contradicts the relativization barrier of [36]." "Informally … unlikely" is not "argues that … cannot".
(ii) L719 (plain reading): "Searching for the shortest program instead costs a time that is exponential in n over log n, and a black-box argument cannot do better than that. The paper works in black-box terms throughout, so this route to the converse is shut for it." The body (L717) says "by the analogy of the depth term and not by citation … ruled out on quantitative grounds [Inference]". The plain reading states "cannot" and "shut" with no hedge.
(iii) L46 (plain reading of the route): "the last arrow is standard (Section 2.3) and does not reverse"; L98 (§2.3 plain reading, outside the joint but the same defect): "The arrows do not reverse". P ≠ NP ⇒ OWF is open; it is not known to fail.
Fix: (i) "argues informally that a relativizing technique is unlikely to improve"; (ii) "…and Hirahara argues informally that a black-box argument is unlikely to do better. If that is right, this route is closed to the black-box methods this paper uses [Inference]"; (iii) "is not known to reverse".

### MINOR

**m1. Proposition 5, hypothesis (iii) (L615) and its use (L641): the stated justification misdescribes the proof it relies on; a shorter, fully black-box route exists.**
Quoted (L615): "the reason for the inference: Theorem 3's proof is the search-to-decision reduction of Ben-David, Chor, Goldreich and Luby, restated as HILNO's Theorem 34, with pairwise-independent hashing; the direction of Proposition 1 used here turns short preimage descriptions into an inverter".
Source: HILNO §5 (`hilno_eprint2023-424.txt:1880–1882`): "In Section 5.1, we show Item 1 ⇒ Item 4. In Section 5.2, we show Item 4 ⇒ Items 2, 3, and 5." Item 1 ⇒ Item 4 is Lemma 33 (BCGL Theorem 34 plus hashing, :1903–1960). Item 4 ⇒ Item 2 is Lemma 39, whose proof (:2333–2335) reads "By Conditional Extrapolation and Proposition 38, there is no infinitely-often one-way function. Thus, by Theorem 13 (Item 1 ⇒ Item 2) …" — i.e. Theorem 3 (1 ⇒ 2) passes through the no-OWF ⇒ conditional-coding direction of Theorem 13, whose proof uses the Impagliazzo–Luby estimator (Theorem 15, :987–1000) and the pK^t coding theorem. The paper's one-line reason omits that half.
The conclusion the paper needs, "no io-OWF^O", does not need Theorem 3 (1 ⇒ 2) at all: Lemma 33 (p. 37; DistNP ⊆ HeurBPP ⇒ Conditional Extrapolation, via Theorem 34) followed by Proposition 38 (p. 42, one paragraph: Conditional Extrapolation ⇒ no io-OWF, by running CondExt on y = f(x)) gives it; both steps are black-box in the oracle. HN 2022's own Fig. 1 (`hn_ccc2022 (scr):292–297`) marks "∃ OWF ⇒ DistNP ⊄ HeurP" as "trivial".
Fix: replace (iii) by "HILNO Lemma 33 and Proposition 38, taken to relativize [Inference]; the reason: Lemma 33 is BCGL's search-to-decision reduction with pairwise-independent hashing and Proposition 38 runs the extrapolator on f(x); both are black-box in the oracle", and drop Proposition 1 from (iii) and from L641.

**m2. Proposition 5(b) (L623): the sharper conclusion needs (i) and (ii) only — say so; and the abstract omits the (iii) dependence.**
"DistNP ⊆ HeurP ⇏_rel BEM" follows from the measure-1 set of Theorem 15 (ii) intersected with the measure-≥1/3 set of part (a) (i); hypothesis (iii) [Inference] is used only for "no io-OWF^O". Splitting the label upgrades the clause the §7.5 divide (L695) actually uses to Proved-conditional on Read facts alone. The abstract (L26) says the barrier result is "conditional on an oracle construction of Hirahara and Nanashima [2022, Read] as read"; for the "no io-OWF ⇒ BEM" half it is also conditional on (iii). Fix: state both dependences in the statement of (b) and in the abstract, or cite the (i)–(ii)-only clause there.

**m3. Proposition 6 (L647–655), its title, and the sentences that lean on it (L657, L693): the evidence is thinner than the words.**
In the 2021 world the paper's own text says the natural sampler cannot see the hidden symbol ("a sampler cannot see a hidden symbol except by guessing it … each of the four description lengths is within O(1) of the corresponding log-probability by printing"), so the check there is trivial; the parameter count is applied to "a direct-evaluation variant of that oracle … 'not Hirahara–Nanashima's oracle, not verified line by line'". In Impagliazzo's world the source was not opened (L647: "the original was not opened"), and the construction details the argument uses ("the reverse conditional is bounded through the helper's syntactic answers to range questions") go beyond what HN 2021 §2.2 (`hn_eccc_tr21-161 (scr):335–381`) describes (a random permutation, a restricted NP oracle A, restrictions assigning "at least N − √N entries"). The title says "passes"; L657 says the test "moved from not run to run … and passed"; L693 says "the natural distributions pass".
Fix: rename to "Remark (the natural test distributions in two errorless worlds) [Inference]"; state that the 2021 check is trivial and that the nontrivial count concerns a variant not in the literature; mark the Impagliazzo half as resting on a description cited via HN 2021; remove "passes/passed" from L58, L657, L693.

**m4. Other claims resting on internal research notes (not checkable from the manuscript); the Obstruction A/B clause.**
Direct answer to the question asked of this joint: the clause at L717 identifying Obstructions A and B ("identifies the two obstructions as one wall seen from the two ends of the block-size trade-off") *is* labelled [Inference]; the reasoning given in the text is one clause ("a logarithmic global saving cannot be localised to a block") plus a pointer to an internal file, and that is *not* sufficient for the label — an [Inference] must show the evidence it follows from, and here the evidence is off the page. The two obstructions themselves are described accurately against KK 2025 (Theorem 4.3's block partition with ℓ = n/(c log t), `kk_eccc_tr25-089.txt:1298–1320`; Appendix B's 2^{O(n/log n)} search, :2200–2217).
The other internal-note dependencies: L647/653 (research note 12); L717 Obstruction A ("[Inference, pass 20, research note B37, `passes/pass20/wallA_attempt.md`]"); L731 Prop 8's clause (research note B36 §6) — the gap is real and the fix is sound (see Verified list), so it can be stated in the text as the authors' own observation, no note needed; L757 (research note B31 §4) — inline the two-sentence reason (largeness only on average over (w, w′), where Definition 2.11 demands it for every conditioning string); L589, L659, L685 and the other "(Pass NN, …)" parentheticals.
Fix: inline the argument in each case or drop the claim; if any parenthetical remains, call it "unpublished note of the authors" so that its status is visible.

**m5. §1.1, L58: "the dissipation statement is strictly stronger than P ≠ NP and cannot be a restatement of it."**
"Strictly stronger" is not known: whether P ≠ NP implies io-OWF is open. What is true is what the sentence's first half says (they differ in Pessiland). Fix: "is not known to be equivalent to P ≠ NP: in Pessiland the two statements have different truth values, so the one is not a restatement of the other."

**m6. §8.5, L917: "Fox, Karamchedu and Mygdalas [2026, Read] give the first concrete instance of Aaronson's second criterion".**
Unlabelled novelty claim about others' work. Aaronson 2005 §10 itself gives instances of the criterion (`aaronson2005_quant-ph0502072.txt:883–890`: "the energy needed to accelerate to relativistic speed in one case, and the linearity of quantum mechanics in the other"). Fix: "a concrete instance".

**m7. Appendix A.2 row 10 (L974): Massey's result does not say what the cell says it says.**
Cell: "almost all permutations f have C(f⁻¹) ≤ 10·C(f) … 'every function is hard to invert' is false, and one-wayness is the rare case." Source (`birget2007_arxiv0704.1569.txt:128–131`): "for almost all permutations f of {0,1}^m, the circuit complexities C(f) and C(f⁻¹) are very similar: (1/10) C(f) ≤ C(f⁻¹) ≤ 10 C(f)", by Shannon–Lupanov counting, i.e. for permutations that are themselves of near-maximal circuit complexity. That is a statement about computational *asymmetry* being rare among all permutations; it says nothing about how rare one-wayness is among efficiently computable functions, which is the population the row's "law" concerns. Fix: "almost all permutations are as hard to compute as to invert [Massey]; computational asymmetry is the rare case among all permutations" and drop "one-wayness is the rare case", or label the inference.

**m8. §8.2, L875 (Liu–Pass paraphrase) — a quantifier is dropped.** [Unverifiable here: the source is not held.]
"so with no one-way function some fast algorithm computes K^t on all but a 1/p(n) fraction of the strings, for every polynomial p". The negation of "for some polynomial p every PPT fails on ≥ 1/p(n) of the strings for all large n" is "for every p some PPT succeeds on > 1 − 1/p(n) of the strings for infinitely many n" (or the i.o. variant of the theorem, if that is the one used). Add "for infinitely many n" or cite the i.o. form.

**m9. §8.4 table (L905), A.2 rows 9 and 13 (L973, L977), closing paragraph (L987): Ben-David–Halevi gloss.**
(a) "standard one-way functions survive" → "are not refuted by their Cor. 11". Cor. 11 (`ben-david_halevi_1992_ocr.txt:645`) kills their Def. 8 notion only; it says nothing positive about standard OWFs.
(b) Def. 8 (:626–641) is also *worst-case* ("we only demand that [the] algorithm will fail reversing f(z) on at least one input of every length") and *deterministic*; the gloss "one-way functions secure against super-polynomial adversaries" omits both. The consequence the paper draws still holds (an average-case OWF against super-polynomial deterministic adversaries is a Def.-8 OWF, so killing the latter kills the former), but the reader should be told which notion is being killed.
(c) "the strong form of the law" (L905, L909, L983, L987) is never defined. Define once: "one-way functions secure against super-polynomial adversaries".
(d) "forcing included" (L973, L987): BDH treat forcing in §1.1 (:55–60, "forcing cannot prove the independence (from set theory) of any [absolute] statement") and their Cor. 3 (:430–432) says "any of the approaches currently known"; the phrase is defensible but is the paper's gloss; point it at §1.1.

**m10. "the law" in the paper's own voice (L60, L905, L909, L921, L983, L987).** Elsewhere the same object is "the assumption" (L58), "the principle" (L58), "the dissipation statement" (L58). One term per object (the repository's own rule); if "law" is kept for the computing side, say once that it is borrowed from the physics column of §8.4.

**m11. A.2 row 12 (L976): "held by consensus, as the second law is"** contradicts L987: "The second law is a claim about the world and can only be earned by observation." Fix: "held by consensus; the second law is held by observation".

**m12. §7.6, L729: the last arrow's converse attribution, and a source-folder inconsistency.**
"the converse is the theorem of [Ilango, Ren and Santhanam 2021, cited via HILNO §2, not opened]". HILNO §2 (`hilno_eprint2023-424.txt:579–582`) states only the forward direction ("Under the assumption that there is no one-way function, it was shown in [IRS21] that … there exists an efficient average-case algorithm A that approximates … K(x)"). The converse is indeed IRS21's (`irs21_eccc_tr21-082.txt:15`: "We show that one-way functions exist if and only if there is some samplable distribution …"), and that file *is held* in `sources/` although the reference list (L1029) says "not opened". Fix: read it (it is on disk), upgrade the tag, and write the last arrow as ⇔; or keep "cited via HILNO" and drop the converse.

**m13. A.1 plain reading (L957): "Rows 4, 7, 8, 10 and 16 are theorems on both sides."**
Row 4's physics cell (L942) is "an assumption satisfied for Crooks's two classes of process on one side"; row 16's physics cell (L954) is "an arrow of time: some driven process has ⟨ω⟩ > 0", an observed fact, and row 13's note (L951) says so ("settled by observation, not by theorem"). Fix the plain reading to match the cells.

**m14. Proposition 4's title (L581): "the skewed top arrow does not reverse".**
Relative to HN 2021's oracle both DistNP ⊆ AvgBPP and BEM_skew hold, so the oracle refutes only the composite reversal "BEM_skew ⇒ NP ⊆ BPP" (the body says this correctly: "no argument that relativizes collapses the skewed sandwich to its top"). The reversal of Proposition 2(a)'s own arrow, "BEM_skew ⇒ DistNP ⊆ AvgBPP", is untouched by this oracle. Retitle: "no relativizing argument collapses the skewed sandwich to NP ⊆ BPP".

### NIT

**n1.** Prop 5 Step B (L631): the case list ("an F-query at a pair of P other than (z, w) … at (z, w, ℓ) … A-queries") omits F-queries at length n outside P (bits open but unmasked at level i(t)) and at other lengths; they are independent of the true pair, so no gap in truth. Add half a sentence.
**n2.** Prop 5 (L615): "the search-to-decision reduction of Ben-David, Chor, Goldreich and Luby" carries no inline read-status tag (the reference list has "cited via HILNO"). L12 says an untagged citation is an error.
**n3.** §8.3 step 2 (L887): "Reversible computation costs nothing in principle [Bennett 1973, abstract, Read]". Abstract (`bennett1973_logical_reversibility.txt:10–12`): "makes plausible the existence of thermodynamically reversible computers … dissipating considerably less than kT of energy per logical step". Write "arbitrarily little in the limit" or quote.
**n4.** §7.6 plain reading (L727) adds an aside not in the display ("here it needs no circuit-lower-bound assumption because pK^t is probabilistic"); move it to the body.
**n5.** §7.5, L709: "A 'no' would be an errorless world with hidden rows long relative to their rarity" — a description of a hypothetical oracle stated flatly; label [Inference].
**n6.** Conventions, L10: "[Unverified] … do[es] not occur in this paper" — the reference list carries "bibliographic details … are unverified" (L995) and "author initials not verified" (L1000, L1036). Reword to "no theorem, lemma, proposition or corollary carries these labels".
**n7.** L585 plain reading, "even one allowed almost exponential time" for BPTIME[2^{n/ω(log n)}]: HN's own word is "nearly"; either is acceptable, "sub-exponential" is exact.
**n8.** L905: "The assumption 'one-way functions exist' is an arithmetic sentence, expected to be a theorem, not a fact about the world." "Expected to be a theorem" is a belief, unlabelled; attribute ("the field expects") or label.
**n9.** L889: "In a physical realization of a one-way function, then, the step that throws away the trace is a dissipation step." L891: "in a physical realization the one-way property can appear only where the record of the action is thrown away." Both are physical claims in the paper's own voice inside a section that promises every such sentence is a named parallel; label [Inference] and point the "only where" at Bennett (reversal is free while the record is kept).
**n10.** Reference list: `sources/` holds files the paper does not cite (kashefi_kerenidis2007, geier2021, buxbaum_mahmoody2024, roldan_parrondo2012, bendavid_simons_slides) and one it cites as "not opened" (irs21, see m12). No action for the paper beyond m12; recorded for the audit.

---

## Overclaim table

Sentences in the paper's own voice about the physical world, laws, P vs NP, or novelty, within the joint. Status: proved / measured / cited / [Inference] / UNLABELLED.

| L | sentence (quoted or closely paraphrased) | status | fix |
|---|---|---|---|
| 26 | "What is new is the time-bounded fluctuation inequality" | novelty, backed at L48 by "found in no source" | none; keep the "found in no source" wording |
| 26 | "no relativizing argument reverses it, a result conditional on an oracle construction of Hirahara and Nanashima [2022, Read] as read" | proved-conditional (i)–(iii); (iii) is [Inference] | add the (iii) dependence or cite the (i)–(ii)-only clause (m2) |
| 46 | "the last arrow is standard … and does not reverse" | UNLABELLED; not known | "is not known to reverse" (M4) |
| 58 | "the dissipation statement is strictly stronger than P ≠ NP" | UNLABELLED; not known | m5 |
| 58 | "immune to relativizing proof in both directions of the same-time sandwich" | UNLABELLED; false for the top arrow | M1 |
| 58 | "the assumption … predicts that no efficiently measurable observable is a complexity meter" | UNLABELLED physical prediction; identification of a physical with a computational condition; missing PRS citation | M2 |
| 58 | "the field has proved this one observable at a time" | cited: one Read-not-held, one not opened, one Read-not-held | M2(a); audit |
| 58 | "that absence is an experimental record … none of these readings is a reading of complexity" | UNLABELLED; rests on three unopened sources | M2(a) |
| 60 | "the law … predicts that no lab instrument can read how complex a state is" | UNLABELLED | M1, M2, m10 |
| 60 | "only that one family of proof methods cannot settle either arrow" | UNLABELLED; false for the top arrow | M1 |
| 486 | "nothing in this paper is stated for that class [BQP]" | honest scope statement | carry it into §1.1 (M2c) |
| 504–506 | "a proof of the converse … must use the global hypothesis … cannot proceed distribution by distribution" | [Inference], but the construction it rests on is not in the paper | M3 |
| 623 | "Hence no relativizing argument proves 'no io-OWF ⇒ BEM', and none proves the sharper 'DistNP ⊆ HeurP ⇒ BEM'" | proved-conditional; the sharper clause needs (i),(ii) only | m2 |
| 643 (4) | "The statement is not in the literature; the oracle is." | novelty; HN 2022 Theorem 4's list checked (scr:244–264) | none |
| 657 | "The relativization test for the same-time top arrow has therefore moved from not run to run … and passed" | [Inference] overstated | m3 |
| 693 | "Bounded exponential moments behave like an errorless condition, and one-wayness like an error-prone one." | [Inference] | none |
| 697 | "provably not the moment bound by black-box means" | proved-conditional on (i),(ii) once split | m2 |
| 717 | "Hirahara argues that a relativizing technique cannot improve the depth term" | cited; stronger than the source ("informally argue … unlikely") | M4(i) |
| 717 | "the natural-property route … is ruled out on quantitative grounds [Inference]" | [Inference] by analogy | keep label; fix plain reading (M4 ii) |
| 719 | "a black-box argument cannot do better than that … this route to the converse is shut for it" | UNLABELLED in the plain reading | M4(ii) |
| 723 | "The open problem is a form of a recognised one, not a new one. [Inference]" | [Inference], cited KK §1.3, §8 (verified) | none |
| 771 | "action contains the information" | interpretive slogan under the §8 disclaimer (L767) | none |
| 773 | "erase it and reversing costs work" | cited (Bennett p. 525, Landauer §4) | none |
| 793 | "if it holds, Lemma 9 and the proof of Theorem 2 … show that the process (p, q) ↦ pq dissipates" | proved-conditional, hypothesis named | none |
| 889 | "the step that throws away the trace is a dissipation step" | UNLABELLED physical claim ("describes the frame") | n9 |
| 891 | "Computation is a special case of physics, not the reverse, and … the one-way property can appear only where the record of the action is thrown away" | UNLABELLED | n9 |
| 893 | "nobody has proved that erasing the history makes the reverse expensive rather than merely not free" | negative claim, own voice; consistent with the open problem | none |
| 897 | five-slot claim "an observer with a limit sees an arrow that the laws do not contain…" | interpretive, §8 disclaimer | none |
| 905 | "it would nearly refute the strong form of the law" | cited (BDH Cor. 6–7, 11; verified) with an undefined term | m9(c) |
| 905 | "The assumption 'one-way functions exist' is an arithmetic sentence, expected to be a theorem, not a fact about the world." | UNLABELLED expectation | n8 |
| 907, 983 | "Same shape in every row but the last; in the last, opposite sign." / "Eleven match in shape" | the paper's own score of its own analogy; interpretive | m13 for rows 4, 16 |
| 917 | "give the first concrete instance of Aaronson's second criterion" | UNLABELLED novelty about others; contradicted by Aaronson §10 | m6 |
| 917 | "a robust null result … would say that gravity is classical, and with the semiclassical coupling that would put NP-complete problems in polynomial time" | inside a chain labelled [Inference] at the same line | soften "would say" to "would be evidence that" |
| 923 | "this paper adds theorems to that idea, not the idea." | novelty disclaimer | none |
| 951 | "ours is not such a world" (row 13) | observational, unlabelled | add "(observed)" |
| 955 | "The thermodynamic route to unbounded description length is closed by a theorem" (row 17) | cited K–W abstract, verified; "closed" is a gloss for "under both realizations they analyse" | none beyond keeping the qualifier already present |
| 974 | "one-wayness is the rare case" (row 10) | cited, misread | m7 |
| 976 | "held by consensus, as the second law is" | UNLABELLED; contradicts L987 | m11 |
| 987 | "No route to such a proof is known" | cited Aaronson 2003 (exact quote verified) | none |

---

## Citation table

File paths are relative to `passes/pass16/sources/` unless marked (scr) = scratch extraction with pdftotext of the held PDF. Match: exact / paraphrase / mismatch / not found.

| citation in the paper | file:lines | match |
|---|---|---|
| Aaronson 2005 §1 "might eventually attain the same status as (say) the Second Law of Thermodynamics" (L915) | aaronson2005_quant-ph0502072.txt:50–51 (§1 begins :19) | exact |
| Aaronson 2005 §10 "has the same character" (L915) | :958–959 (§10 begins :863) | exact |
| Aaronson 2005 §10 "could be falsified by a purely mathematical discovery such as P = NP" (L915) | :962–963 | exact |
| Aaronson 2005 §10 "whether accepting it places interesting constraints on new physical theories" (L917) | :882–883 | exact |
| Aaronson 2005 §5 "the noise-tolerant version is undemonstrated" (L917) | :396–399 ("But what if we allow error … I am not convinced that Abrams and Lloyd have demonstrated this") | paraphrase, faithful |
| Aaronson 2016 fn 20, physicists would have declared P ≠ NP a law (L915) | aaronson2016_pnp_survey.txt:1214–1217 | paraphrase, faithful |
| Aaronson 2003 "utterly new techniques would be required to show that" (L987) | aaronson2003_pnp_independent.txt:732 | exact |
| Aaronson–Kardes–Hartle slide 2 bullets "limited information", "computational intractability", chaos, "irrationality / biases" (L795) | aaronson_kardes_hartle2025_suppes_slides.txt:10–13 | exact |
| AKH slide 27 "the appearance of the Second Law can be protected only by computational complexity" (L915) | :171–173 | exact |
| Bennett 1973 abstract "considerably less than kT of energy per logical step" (L773) | bennett1973_logical_reversibility.txt:11–12 | exact |
| Bennett 1973 abstract, "erasure" (L482, L773) | :13 | exact |
| Bennett 1973 p. 525 "must be allowed to save its input – otherwise it could not be reversible and still carry out computations in which the input was not uniquely determined by the output" (L789) | :33–36 | exact (OCR spacing) |
| Landauer 1961 §1 "independent of the rate of the process" (L482, L893) | landauer1961_irreversibility.txt:45–46 (§1 begins :26) | exact |
| Landauer 1961 §4 "0.6931 kT per restored bit" (L482, L773) | :297, right column; §4 header at :298 in the left column; by two-column reading order the sentence sits in §4 | exact |
| Landauer "restore to one" (L482, L773) | landauer_layout.txt (scr):64, 75, 232, 241 ("r e s t o r e t o o n e", letter-spaced in the original typesetting) | exact |
| Crooks 1999 eq. (2) P_F(+ω)/P_R(−ω) = e^{+ω} (L143, A.1 row 6) | crooks1999_arxiv9901352.txt:56 | exact |
| Crooks eq. (4) ⟨e^{−ω}⟩ = 1 (L143, L263) | :83 | exact |
| Crooks eq. (5) microscopic reversibility, ratio = exp(−βQ) (L303, row 5) | :83–87 | exact |
| Crooks eq. (7) path-level identity (L139) | :178–179 | exact |
| Crooks boundary condition ρ_F(x_{+τ}) = ρ_R(x_{+τ}) (L221, row 4) | :165–167 | exact |
| Crooks §IV "Jensen on the integral identity" (L265) | :320–323 ("From the relation ⟨exp(−ω)⟩ = 1, Eq. (4) … on average the entropy production is positive") | paraphrase; the word Jensen does not appear, the inequality used is Jensen's |
| Jarzynski 2006, exponential averages dominated by rare realizations that look like typical reverse realizations run backward (L687, row 9) | jarzynski2006_arxiv0603185.txt:14–16, 45–46, 74–77, 166 | paraphrase, faithful |
| Ebtekar–Hutter Lemma 5 / Theorem 7 / eq. (44) (L50) | ebtekar_hutter2024_arxiv2308.06927.txt:1913 (Lemma 5, App. B), 641–643 and 993–994 (Theorem 7), 997 (eq. 44), 521 (Kraft, eq. 13) | exact locations |
| Shiraishi–Takesue 2025 §8, orbit "the authors liken to counting in decimal" (L793) | shiraishi_takesue_2025_arxiv2408.06691.txt:3821 (§8 Open problems), 3848–3852 | paraphrase, faithful |
| Kolchinsky–Wolpert abstract "the thermodynamic complexity of any desired output is bounded by a constant (unlike the conventional Kolmogorov complexity)" (row 17) | kolchinsky_wolpert2020_arxiv1912.04685.txt:22–23 | exact |
| K–W §II.B "if the physical Church-Turing thesis is true, then no real-world physical system can take any desired string x as input and produce the value of K_U(x) as output" (row 17) | :350–352, under "II. BACKGROUND … B. Algorithmic Information Theory" (:220, :332) | exact |
| K–W "contains no time bound and does not treat logical depth" (row 17) | grep "logical depth", "time bound", "time-bound": no hits | confirmed |
| Goldreich 2019 §1.1 "is not easier than proving that P ≠ NP" (row 12) | goldreich2019_foundations_of_cryptography.txt:162 (§1.1 begins :90) | exact |
| Birget 2007 §1.2, Massey: almost all permutations have C(f⁻¹) ≤ 10·C(f) (row 10) | birget2007_arxiv0704.1569.txt:128–131 | exact for the inequality; the reading drawn from it is m7 |
| Bogdanov–Trevisan survey §1.1.2, "dominates" (Definition 10, L825) | bogdanov_trevisan2006_arxiv0606037.txt:222, 260 | exact (footnote number not verifiable in the txt) |
| Bennett–Gács–Li–Vitányi–Zurek §VIII, Zurek's antisymmetric cost = erased bits minus provided bits (L470, row 12, L482) | bennett_gacs_li_vitanyi_zurek1998_information_distance.txt:788, 852–870 | paraphrase, faithful (formulae stripped in the txt) |
| Grünwald–Vitányi, Li–Vitányi Theorem 3.9.1 (L281) | grunwald_vitanyi2004_arxiv0410002.txt:1116 | exact |
| LOZ Theorem 5 = Theorem 30; Lemma 31; Lemma 36 (L168, L190, L198) | lu_oliveira_zimand_2022_arxiv2204.08312.txt:329, 1246; 1255; 1415 | exact |
| HILNO eq. (6) pK^t, conditional form (L70, L76) | hilno_eprint2023-424.txt:822–829 | exact |
| HILNO Theorem 1 items 1, 3 (Prop 1; L289) | :217–243 | exact |
| HILNO Theorem 3 items 1–2 (L615, L641, row 15) | :368–388 | exact |
| HILNO Theorem 4 (L452, row 14) | :398–412 | exact |
| HILNO Theorem 34 = BCGL92 search-to-decision (L615) | :1916–1920 | exact; but see m1 for the route |
| HILNO §5 route 1 ⇒ 4 ⇒ 2, Lemma 39 via Prop 38 and Theorem 13 (m1) | :1880–1882, :2333–2335 | exact |
| HILNO Lemma 9 (L210) | :860–875 | exact |
| HILNO Lemma 20 argument (paper's Lemma 9, L329) | :1256–1320 | exact |
| HILNO Definition 21, Proposition 22 (L825–831) | :1261–1279 | exact |
| HILNO HeurBPP pp. 17–18 (L595) | :836–844 | exact |
| HILNO io-OWF convention (Definition 3) | :793–794 | exact |
| HILNO p. 3 Zvonkin–Levin credit (L281) | :113 | exact |
| HILNO §2 p. 12, IRS21 forward direction (L729) | :579–582 | exact for the forward direction; converse not stated there (m12) |
| HILNO Lemma 41 = Imp95 Prop 3 (L595 convention) | :2447–2450 | exact |
| HN 2021 Theorem 3, DistPH^O ⊆ AvgP^O and UP^O ∩ coUP^O ⊄ BPTIME^O[2^{n/ω(log n)}] (Prop 4, L581–583) | hn_eccc_tr21-161 (scr):134–136 | exact |
| HN 2021 §6.1 construction: V(x, y) = 1 iff y = f(x); alphabet size ℓ(n) = t(n)²; p(n) = t(n)^{−ε(n)^{1/2}} (Prop 6, L653) | (scr):1212–1260 | exact; the paper's "2n/(ε(n) log n) bits" = log ℓ(n) ✓ |
| HN 2021 §2.2, Impagliazzo's oracle: random permutation plus restricted NP oracle; "assign at least N − √N entries" (Prop 6, L647) | (scr):335–347, 380–381 | exact |
| HN 2021 §6.3 Corollary 3, DistPH ⊆ AvgP with probability 1 | (scr):1421–1422 | exact |
| HN 2022 Theorem 4 (L597–603, L643) | hn_ccc2022_lipics234-25 (scr):244–264 | exact, including the primitives list HSG/AIOWF/AIPRG/AIPRF |
| HN 2022 §3.1 errorless / error-prone heuristic schemes (L595) | (scr):644–663 | exact |
| HN 2022 p-random restriction (assigned values uniform) — Fact M | (scr):611–618 | exact |
| HN 2022 §4 Construction: p(n) = t(n)^{−6} = 2^{−6an/log n}, i_max = (1/c) log log t(n) = (1/7a) log(an/log n), c = 7a, masks S_{n,i} of size p·|S_{n,i−1}|, A's rule (L605) | (scr):811–852 | exact |
| HN 2022 Proposition 14 (L605) | (scr):853–870 | exact |
| HN 2022 Theorem 15 and its proof's use of Imp95 Prop 3 (L603, L595) | (scr):877, 974–988 | exact |
| HN 2022 §1.2 five worlds; refs [22], [24], [25] (L58, L595, reference list) | (scr):273–283; 1341, 1346, 1348 | exact |
| HN 2022 Fig. 1 "∃ OWF ⇒ DistNP ⊄ HeurP, trivial" (for m1) | (scr):292–297 | exact |
| GKLO22 §1.2 relativization remark (L595, L761) | gklo_ccc2022.txt:395–397 | exact |
| GKLO22 remark after Definition 17 "all the results also hold with any oracle" (Prop 4 (ii), L587) | :1078–1091; Lemma 26 is in §3.4 (:1326), inside the section the remark covers | exact |
| GKLO22 Lemma 26(1), special case without conditioning (H1, L539) | :1334–1355 | exact (source has ">" where the paper writes "≥") |
| GKLO22 L and D in the proof of Lemma 26(1) (Definition 9, L563–565) | :1357–1366 | exact |
| GKLO22 "Using the assumption that DistNP ⊆ AvgBPP, it follows that (L, D) ∈ AvgBPP" (L579) | :1368–1369 | exact |
| GKLO22 Lemma 6, Lemma 21 (L563, L394) | :717–722; :1145–1148 | exact |
| KK 2025 Definition 2.11 (L711, L731) | kk_eccc_tr25-089.txt:686–691 | exact |
| KK 2025 Theorem 3.4 statement (L743–745) | :1124–1131 | exact |
| KK 2025 proof of Theorem 3.4 calls A(−, 1^{2t}) on a conditioning string containing r ∈ {0,1}^{2t} (Prop 8 clause, L731) | :1147–1160 | exact; the gap is real |
| KK 2025 Theorem 4.3, ℓ = n/(c log t), brute force per block (L717) | :1298–1320 | exact |
| KK 2025 footnote 2, two-string chain rule not known to give multi-string (L717) | :168 | paraphrase, faithful |
| KK 2025 §8 concluding remarks: characterize worst-case SoI; derive a poly-time natural property from SoI; 2^{O(n/log n)} from App. B (L717, L723) | :1893–1898 | exact |
| KK 2025 Appendix B, Lemma B.1, Theorem B.2, time 2^{O(n/log n)} (L717) | :2200–2217 | exact |
| KK 2025 §1.3 "sandwiched between two average-case assumptions", "exact complexity-theoretic characterization … is missing" (L723) | :457–463 | exact |
| KK 2025 Theorem 1.2 (L723) | :209–211 | exact |
| Hirahara 2022 Remark 6.4 (L717) | hirahara_ccc2022_lipics234-26.txt:1319–1334 | paraphrase with strength mismatch (M4 i) |
| Hirahara 2022 Theorem 1.2, Theorem 1.3, instance checker, [38] (L723, L729) | :133, :148–169 | exact |
| HMO 2026 §1.2, unconditional failure of SoI for rKt and pKt (L729) | hmo_eccc_tr26-021 (scr):147–235 | exact |
| Ben-David–Halevi abstract, DTIME(n^{log*(n)}) on infinitely many huge intervals (L905, L973, L987) | `ben-david_halevi_1992_pages/p19.png` (abstract, read from the page image; the OCR at ocr.txt:23 is garbled) | exact |
| BDH Cor. 2 (L987) | ben-david_halevi_1992_ocr.txt:391 | exact |
| BDH Cor. 3 and the sentence before it (L973, L987) | :420–432 | exact |
| BDH §1.3 fn 2 (Gödel-style self-reference) | :192–195 | exact |
| BDH Theorem 4 (row 12) | :507–508 | exact |
| BDH Cor. 6, Cor. 7 (interval form) | :534–536, :558–561 | exact |
| BDH Def. 8, "the usual", "the common" (L905) | :626–641 | exact; the gloss omits worst-case/deterministic (m9 b) |
| BDH Cor. 11 | :645 | exact |
| Fredkin–Toffoli abstract "the functional behavior of a general-purpose digital computer can be reproduced by a perfect gas placed in a suitably shaped container and given appropriate initial conditions" (L885) | fredkin_toffoli1982_conservative_logic.txt:23–25 | exact |
| F–T §7 "by our losing knowledge (and thus control) of a mechanical mode's current state … through such a complex relationship that we may not be willing or able to unravel it" (L891) | :706–708 (§7 begins :697) | exact |
| F–T §8 "there is no necessary connection between the energy involved in a computation and its length or complexity" (L482, L893) | :931–933 (§8 begins :917) | exact |
| F–T §4, §6 (computation universality; billiard-ball model) (L885) | :392, :550 | exact section headers |
| Takesue 1989 held and titled as cited | takesue1989_ergodic_I.txt:6–13 | exact |
| Body ↔ reference list | script over the manuscript: 60 entries; every body citation has an entry; every entry is cited in the body (Poincaré is cited at L974 without its year; Li–Vitányi carries no year in either place) | no orphans either way |

---

## Verified correct

- Proposition 4: with HN 2021 Theorem 3 as read, DistNP^O ⊆ AvgBPP^O, Prop 2(a) relativized gives BEM_skew^O, UP ∩ coUP ⊆ NP and BPP ⊆ BPTIME[2^{n/ω(log n)}] give NP^O ⊄ BPP^O; GKLO22's Lemma 26 sits in §3.4, inside the scope of the "any oracle" remark after Definition 17. Correct.
- Proposition 5, construction transcription: p(n) = 2^{−6an/log n}, i_max(n) = (1/7a) log(an/log n), c = 7a, A's rule and Proposition 14 match `hn_ccc2022 (scr):811–870`; Fact M follows from the p-random restriction assigning uniform values (:611–618) and from Proposition 14.
- Proposition 5, i(t) ≤ (1/c) log log t and i(t) < i_max(n) for polynomial t and large n; log(1/μ) = 6an·i(t)/log n ≤ (6/7) n (log log m + log k)/log n = o(n). Correct.
- Proposition 5, Step A: fewer than 2^{n−5} programs of length ≤ n − 6; Σ_P Pr_r[touch] ≤ t; E[ν_{(z,w)}(R_z(w)0^n)] ≤ 2^{−n}; E[#bad] ≤ (3/2)·2^{n−5}·(t + |M_t|) ≤ (3/32)N using t ≤ |M_t|. Correct.
- Proposition 5, Step B: exchangeability of untouched masked pairs given the transcript makes each query hit the true pair with probability ≤ 1/(N − t); Pr[Q(y) = (z,w)] ≤ (t+1)/(N−t) ≤ 2(t+1)/N; fewer than N/(32t) programs; E[#bad] ≤ (3/2)(N/(32t))·2(t+1) ≤ (6/32)N. Correct.
- Proposition 5, assembly: E|P∖G| ≤ N/2 ⇒ Pr[|G| ≥ N/4] ≥ 1/3 by Markov; on G, σ_t ≥ log|M_t| − log t − O(1); D_m(G) ≥ μ/4; E[2^{σ_t}] ≥ μ²2^n/(2^{O(1)}t) = 2^{n−o(n)}; conditioning on an arbitrary visible restriction gives the unconditional bound. Correct.
- Proposition 5(b): reverse Fatou for indicators, Pr[limsup_n E_n(t)] ≥ limsup_n Pr[E_n(t)] ≥ 1/3; second application along t_k = m^k; for O in the limsup set and any p_D ≤ m^j, some k ≥ max(j, k_0) has O ∈ A_{t_k}, so Definition 7 fails at every (p_D, C). Correct as probability.
- §7.3 "skewed object in the error-prone world" [Inference] paragraph: Σ⁺_{s,P} is pointwise non-increasing in P (Lemma 4), so the events at the common threshold 2^{n/2} are nested in j and the intersection of the decreasing sets, each of measure ≥ 1/3, has measure ≥ 1/3. Correct.
- Proposition 7 and the quantifier remark after it: G depends on q and p, not t; the Kraft bound Σ_G m_R ≤ (3/2)²(n+d)²; the converse sentence via Theorem 3(a). Correct.
- §7.5 displayed chain (L695): each arrow is justified (Prop 2(a), Prop 2(c), HILNO Theorem 3 with Prop 1 — or, better, Lemma 33 + Prop 38 — and Prop 5(b)).
- §7.6 placement chain (L725): arrows justified in order by Prop 3(c), Prop 3(b), Prop 2(c), HILNO Theorem 1 items 1–2 (:217–232), HILNO §2 (:579–582). The last arrow is in fact ⇔ (m12).
- Proposition 8: transcription of KK Theorem 3.4 exact; the Definition 2.11 / proof-of-Theorem-3.4 time-parameter gap is real (Def. 2.11 needs t ≥ p(n + m); the proof calls A at time 2t with |r| = 2t inside the conditioning string, so m ≥ 2t); the proposed fix (call the property at p(n + m) ≥ 2t) keeps the yes-side (K^{p(n+m)} ≤ K^{2t}), largeness and polynomial time. Correct.
- §7.7 barrier filter: no circuit lower bound is argued; Theorem 3(a) is conditional on an OWF; Proposition 5 is an oracle construction, which is a legitimate relativization statement; nothing algebrizes or yields a natural property. No argument in the joint contradicts relativization, natural proofs or algebrization.
- Definition 9 (H_pK): L and D match GKLO22's proof of Lemma 26(1) (:1357–1366); the single use of the hypothesis is the quoted sentence (:1368–1369).
- Conventions' read-status tags are present on every inline citation in the joint except the BCGL mention at L615 (n2).
- Plain readings in the joint, every one checked against the formula or claim above it (step 6 of the plan). These say neither more nor less than their text: L585 (HN 2021 oracle), L601 (HN 2022 Theorem 4), L611 (log 1/μ), L621 (Prop 5(a)), L637 (assembly bound), L651 (Prop 6 display), L661 (skewed object in the error-prone world), L677 and L683 (Prop 7), L697 (divide chain; "provably" acceptable once m2 is applied), L707 (sharpened question), L715 (characterization question), L737, L741, L747, L755 (Prop 8 and the two-tops display), L779 (§8.1 display), L909 (§8.4 caption), L919 (§8.5 Fox et al.), L981 (A.2 table), L985 (Score), L989 (closing paragraph). The ones that say more than their text are L46 (M4 iii), L60 (M1, M2), L719 (M4 ii), L727 (n4), L957 (m13).
- Reference list versus body: no orphans (script).
- Physics and mathematics quotations in the joint (Aaronson 2005 ×4, Aaronson 2003, Aaronson 2016 fn 20, AKH slides 2 and 27, Bennett ×3, Landauer ×3 including "restore to one", Crooks eqs. (2), (4), (5), (7), Fredkin–Toffoli ×3, Kolchinsky–Wolpert ×2, Goldreich, Birget/Massey inequality, BDH abstract/Cor. 2, 3, 6, 7, 11/Def. 8/Thm 4, KK Def. 2.11/Thm 3.4/Thm 4.3/§8/App. B, GKLO22 remarks and Lemma 26, HN 2021 Theorem 3, HN 2022 Theorem 4/15/§4) are exact or faithful paraphrase at the cited places.

---

## Sources read (with line ranges)

- ENTROPY_PRODUCTION.md: 1–1058 (whole file).
- hn_ccc2022_lipics234-25 (scr): 100–135, 236–300, 605–700, 760–880, 974–1000, 1114–1125, 1338–1362.
- hn_eccc_tr21-161 (scr): 118–166, 331–420, 1203–1320, 1404–1430.
- hn_focs2021_ea (scr): extracted, not needed (the paper cites the ECCC version).
- hmo_eccc_tr26-021 (scr): 50–108, 147–235.
- gklo_ccc2022.txt: 80–100 (headers), 390–410, 715–735, 1075–1095, 1145–1175, 1326–1400.
- hilno_eprint2023-424.txt: 110–116, 217–262, 368–420, 575–585, 785–800, 838–875, 960–1012, 1256–1330, 1844–1990, 2270–2340, 2440–2462.
- kk_eccc_tr25-089.txt: 168, 209–222, 445–470, 686–695, 1124–1200, 1298–1345, 1880–1898, 2200–2245.
- hirahara_ccc2022_lipics234-26.txt: 133, 148–169, 361–384, 1319–1342.
- ben-david_halevi_1992_ocr.txt: 18–32, 55–60, 161–200, 385–440, 505–575, 620–665; page image p19.png (abstract).
- aaronson2005_quant-ph0502072.txt: 45–55, 320–475 (grep), 795–810, 878–890, 955–965; aaronson2016_pnp_survey.txt: 1214–1217; aaronson2003_pnp_independent.txt: 727–733; aaronson_kardes_hartle2025_suppes_slides.txt: 7–13, 171–173.
- bennett1973_logical_reversibility.txt: 9–14, 33–37; landauer1961_irreversibility.txt: 26–46, 288–300 and landauer_layout.txt (scr) grep; fredkin_toffoli1982_conservative_logic.txt: 23–27, 392, 550, 697–708, 917–933.
- crooks1999_arxiv9901352.txt: 35–200, 309–334 (grep-guided); jarzynski2006_arxiv0603185.txt: 3–16, 45–46, 74–77, 99–166 (grep-guided); ebtekar_hutter2024_arxiv2308.06927.txt: 521, 641–652, 993–1000, 1910–1913 (grep-guided).
- shiraishi_takesue_2025_arxiv2408.06691.txt: 3821, 3848–3852; kolchinsky_wolpert2020_arxiv1912.04685.txt: 17–22, 220, 332–356 (grep-guided); goldreich2019_foundations_of_cryptography.txt: 90, 162; birget2007_arxiv0704.1569.txt: 112–140; bogdanov_trevisan2006_arxiv0606037.txt: 222–266; bennett_gacs_li_vitanyi_zurek1998_information_distance.txt: 788–905; grunwald_vitanyi2004_arxiv0410002.txt: 1116; lu_oliveira_zimand_2022_arxiv2204.08312.txt: 329, 1246–1298, 1415; takesue1989_ergodic_I.txt: 1–30; irs21_eccc_tr21-082.txt: 15, 65, 140 (grep only, for m12).

---

## Audit items — [Unverifiable here]

Sources tagged "Read" in the reference list but not held in `sources/`; the claims resting on them could not be checked from disk:
- Aaronson, Bouland, Fefferman, Ghosh, Vazirani, Zhang, Zhou 2024, Corollary 1.0.1 (pseudoentanglement) — L58.
- Lee, Kwon, Cho 2025, Theorem 1 "unconditional" — L58.
- Liu–Pass 2020, Theorem 1.1 and the definition of mild average-case hardness — L875 (see m8 for the quantifier).
- Fox, Karamchedu, Mygdalas 2026 (abstract, §I, §II, §V) — L917.
- Marletto, Deutsch, Vedral 2026 §2.3 — L917.
- Wolfram 2023 — L915.
- Takesue 1990 — L143 (outside the joint; listed for completeness).
Sources cited "via research note B30 §0 (search-result summary); not opened": Gu et al. 2024; Gärttner et al. 2017; Mi et al. 2021; Google Quantum AI 2025 — L58 (M2a).
Sources "cited from memory": Aaronson–Wigderson 2008; Baker–Gill–Solovay 1975; Bogdanov–Trevisan 2006 (SIAM); Feigenbaum–Fortnow 1993; Loschmidt 1876; Poincaré 1890; Razborov–Rudich 1994; Zermelo 1896 — none used in a proof (checked: §7.4 obstacle prose, §7.7, §8.2, §8.4 and A.2 cells only).
Sources "cited via" a read source whose original was not opened, used in the joint: Impagliazzo 1995 (via HN 2022 §1.2 and proof of Theorem 15 — the cited places verified); Impagliazzo 2011 (via HN 2021 §1.1, §2.2 — verified); Hirahara–Santhanam 2022 (via HN 2022 [22] and Hirahara 2022 [38] — verified); Longpré–Mocas 1993, Longpré–Watanabe 1995, Goldberg–Kabanets 2022 (via KK 2025 §1.3 — verified); Zurek 1989 (via BGLVZ §VIII — verified); Massey 1996 (via Birget §1.2 — verified); Zvonkin–Levin 1970 (via HILNO p. 3 — verified); Li–Vitányi Theorem 3.9.1 (via Grünwald–Vitányi — verified); BCGL92 (via HILNO Theorem 34 — verified); IRS21 (via HILNO §2 — held on disk, see m12); Marletto–Vedral 2017 (via Fox et al. — not checkable, Fox et al. not held).
Page numbers quoted from PDFs (HILNO "p. 5, 8, 9, 17–18, 37"; K–W "p. 6"; GKLO22 "16:18, 16:22–16:24"; Hirahara "26:22"; KK "p. 12, 21–22, 24") were checked only where the text extraction carries page headers (Hirahara: the "26:23" header is printed at :1335, so Remark 6.4 at :1319–1334 is on 26:22; GKLO22: a "16:23" header appears within the printed range :1330–1400 just after the definition of L, consistent with "16:22–16:24"; KK: page numbers "21" and "24" appear within the printed ranges :1124–1200 and :1298–1345); the rest are consistent with the order of the text but not verified as numbers.

---

## For the owner, in plain words

The mathematics in this part of the paper holds up. The two oracle results that matter (Propositions 4 and 5) were checked against the two Hirahara–Nanashima papers line by line: the parameters of the random oracle are copied correctly, the counting steps and the probability steps are right, and the conclusion — that no black-box argument can get from "nothing is one-way" to the paper's moment bound — follows. Proposition 7 is right, and the paper's catch of a small gap in a recent Kabanets–Kolokolova proof is real and their patch works. The reference list is clean: everything cited is listed and everything listed is cited, and the forty-odd quotations I checked against the source files are accurate, including the one from the 1992 Ben-David–Halevi report that had to be read off a page image.

What is wrong is in the words around the mathematics. The introduction's "what the results are not" paragraph says the open problem is protected from black-box proof in both directions; the paper proves that for one direction only, and its own text admits the other direction is open. The same paragraph makes a claim about laboratory instruments that rests on papers the authors say they never opened, which breaks the paper's own stated rule, and it leans on a known theorem about pseudorandom quantum states that is never cited. Several sentences in §7 point to internal notes instead of giving the argument, so a reader cannot check them; one of them tells the reader what shape any future proof must have. A few plain-language readings say "cannot" or "does not reverse" where the text says "unlikely" or "not known". The rest is wording: an undefined phrase ("the strong form of the law"), a misread of a counting result about random permutations, a "first" that is not first, and a source sitting in the folder that the list says was never opened.

How much work: the fixes are edits, not new mathematics. The two big ones (the introduction paragraph and the "read" rule) are an afternoon: rewrite one paragraph, either read four short papers or delete four clauses, and add one citation. Inlining or cutting the internal-note claims is another afternoon. The plain-reading and wording fixes are an hour. Nothing found here requires a theorem to be withdrawn.
