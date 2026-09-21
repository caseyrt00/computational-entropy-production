# Referee E (blind) — ENTROPY_PRODUCTION.md, Revision 1

Paper: `problems/one-way-functions/passes/pass16/ENTROPY_PRODUCTION.md`, sha256 `bb12edc0…4c770d`, with its PDF (59 pp.) beside it. Date: 20 September 2026.

Protocol. Step 1 and step 2 verdicts were fixed before `B50_rules.md` was opened. One deviation: while sizing the file I listed its section headings once (a `grep` of `##` lines) before step 3; no rule text was read until step 3. HANDOFF.md, the B-tickets and the referee A–D reports were not opened. Line numbers below are those of the current paper unless marked "base" (B50's line numbers).

---

## Step 1 — fifteen minutes as an ECCC board member (pages 1–4 read, rest skimmed)

**Does this read like a complexity paper written by a human?** The core does: §§2–6, §8.2–8.4 and Appendix B are definitions, Kraft sums, HILNO citations, an oracle construction and a barrier filter, written the way the field writes them. Pages 1–4 do not. In order, a board member sees: a title that asserts an identity; an abstract followed by an italic "plain reading of the abstract"; a results box whose third column grades the paper's own theorems ("new / restated / assembled"); a bulleted §1 whose second bullet says its theorem "is a restatement, not a new theorem"; a five-row Crooks correspondence; a one-line route; a sentence saying §9 "adds nothing"; then §1.1, five hundred words of what the paper does not claim, ending in pseudorandom quantum states. That is the shape of an audited document with its audit trail left in, not the shape of a paper. The acknowledgements say why, and (g) below lists the tells.

**Would I accept it for posting?** Yes, after the "fix first" list at the end, and with two reservations I would voice. It is in scope (time-bounded Kolmogorov complexity, one-way functions, oracle separations), its objects are HILNO's, its unconditional content is small and says it is small (two Kraft sums and Jensen), and its open problem is well posed. Reservation one: 59 pages for that; §9 and Appendix A, about fourteen pages, are interpretation the paper itself says adds nothing. Reservation two: "as read", "not opened", "sources on disk" and "full-text search of the saved text" tell the board that some cited results were not checked at the source. ECCC does not police that; a board member notices it.

**The three sentences most likely to make a board member stop.**

1. Abstract, last sentence (line 9): *"Physics is the frame, not the subject."* After two hundred words of Crooks, entropy production and second laws, a disclaimer; disclaimers in abstracts stop readers.
2. §1 (line 53): *"…while the interpretation in Section 9 adds nothing beyond what [Aaronson 2005, §10], [Aaronson 2016a, footnote 20] and [Aaronson, Kardes and Hartle 2025, slide 27; unpublished] already say, and it says so."* A paper that tells the board a fifth of it adds nothing invites the question why it is there.
3. §1.1 (line 63), the sentence beginning *"Read as a principle, the assumption, in its quantum-secure form (one-way functions secure against quantum algorithms), predicts that no efficiently measurable observable is a complexity meter…"* and running 120 words through a parenthesis with four qualifications, the extended Church–Turing thesis and Ji–Liu–Song. It sits in a section titled "What the results are not", in a paper stated for BPP samplers.

Runners-up: §8.3, Proposition 11: *"the Impagliazzo half rests on Hirahara and Nanashima's description of that oracle, the original not having been opened"*; Acknowledgements: *"This paper was written with an AI system (Claude, Anthropic) as a research collaborator"*; §9.5, the semiclassical-gravity paragraph.

---

## Step 2 — the whole paper, by letter

Severity: **blocking** (false or unsupported as written), **minor** (wrong or inconsistent, one-sentence fix), **nit**.

### (a) The results box against §1's "what is new and what is restated"

**(a1) minor — the paragraph and the box do not list the same standings.** Line 53. The box grades four rows: new, restated, assembled, assembled. The paragraph names only Theorem 1 (new) and Theorem 2 (its reading new), says nothing of Theorems 3 and 4, and omits the three further novelty claims the body makes: Proposition 4(a) ("As far as we know, (a) is new", line 663), Proposition 6 ("the quantitative statement … is new", line 689) and Proposition 10's statement ("The statement is not in the literature; the oracle is", line 876).

BEFORE (line 53):
> What is new and what is restated, in one sentence: the time-bounded fluctuation inequality of Theorem 1 and the reading of HILNO as mean entropy production in Theorem 2 were found in no source, while the interpretation in Section 9 adds nothing beyond what [Aaronson 2005, §10], [Aaronson 2016a, footnote 20] and [Aaronson, Kardes and Hartle 2025, slide 27; unpublished] already say, and it says so.

AFTER:
> What is new and what is restated, in one sentence: the time-bounded fluctuation inequality of Theorem 1 was found in no source; Theorem 2 restates HILNO's Theorem 1, and its reading as mean entropy production was found in no source; Theorems 3 and 4 are assembled from named parts of HILNO and Lu–Oliveira–Zimand, as the results box says; Propositions 4(a), 6 and 10 are claimed as new where they are stated (§6, §8.3); and the interpretation in Section 9 adds nothing beyond what [Aaronson 2005, §10], [Aaronson 2016a, footnote 20] and [Aaronson, Kardes and Hartle 2025, slide 27; unpublished] already say, and it says so.

**(a2) minor — the Theorem 2 row says more than the theorem proves, by dropping the time quantifier.** Line 18. Theorem 2's "Equivalently" sentence (line 380) is: io-OWFs exist iff there is a D such that *for every polynomial p and every constant c, at t = p(n)*, the mean production exceeds c log n for infinitely many n. The row drops "for every polynomial p". Read at a single time bound, the row's ⇐ direction is not what the theorem proves: (1) ⇒ (2) bounds the mean only for t ≥ p(n) with p depending on D, so a process with large mean at one small polynomial t gives no one-way function. The §1 bullet (line 31), the route line (line 49) and the abstract (line 9) make the same omission; the row is where a reader takes the statement from.

BEFORE (line 18):
> One-way functions exist iff some polynomial-time samplable process has mean production above c log n for infinitely many n, for every constant c.

AFTER:
> One-way functions exist iff some polynomial-time samplable process has, at every polynomial time bound, mean production above c log n for infinitely many n, for every constant c.

**(a3) minor — the §1 Theorem 3 bullet says "both exponential moments", which is false for a single process.** Line 32. Theorem 3(a) proves E_D[2^{+σ_t}] ≥ n^a on D = (z, f(z)) and E_{D′}[2^{−σ_t}] ≥ n^a on the swap D′. On D itself the minus moment is *polynomially bounded*: 2^{−σ_t} = 2^{−σ^rev_D} · 2^{σ^fwd_D}, the forward side is at most n^{c_f} 2^d on every pair (proof of 3(a), line 503), and E_D[2^{−σ^rev_D}] ≤ (3/2)²(n + d)² by Theorem 1(a). So no process in the paper has both moments superpolynomial. The box row ("superpolynomial exponential moments", unlocalized) and the abstract are defensible; the bullet is not.

BEFORE (line 32):
> the existence of one-way functions forces both exponential moments to be superpolynomial infinitely often; whether the converse holds is the paper's open problem, Question 1.

AFTER:
> the existence of one-way functions forces, for the pair distribution of the function and for its swap, one exponential moment each to be superpolynomial infinitely often, so bounded exponential moments fail in both directions; whether the converse holds is the paper's open problem, Question 1.

**(a4) nit — Theorem 4 row, "inverts it".** Line 19. One inverts an output, not a pair; the theorem's word is "dominates the reverse conditional". AFTER: "σ is small on a pair iff the universal sampler, handed the output, produces the input with the right odds, up to a polynomial and outside a 1/n slice." The Theorem 1 row says only what Theorem 1 proves (it omits (c), which is allowed).

### (b) The figure in §8.1

Checked the tikz source (lines 738–748) against the rendered PDF page 28. Boxes: NP ⊆ BPP, BEM, no io-OWF. Solid arrow NP ⊆ BPP → BEM labelled "Thm 3(b)": matches 3(b). Solid arrow BEM → no io-OWF labelled "Thm 3(a)": see (b1). Dashed arrow no io-OWF → BEM labelled "Question 1": matches Question 1 exactly (line 729, "no io-OWF ⇒ BEM"). Note "no relativizing proof (Prop. 10, conditional)" under the BEM–no-io-OWF gap: matches Proposition 10(b) and §1.1's "(Proposition 10, conditional as stated there)"; it is placed under the dashed arrow, which is the arrow it is about. Caption: "The same-time sandwich, Theorem 3(c). Question 1 asks whether the second arrow reverses": matches. Plain reading: matches.

**(b1) minor — the second solid arrow is labelled with the wrong part.** Line 745. BEM ⇒ no io-OWF is the second arrow of Theorem 3(c); it is proved in (c) from (a) with the quantifier step t := max(p_D, t_D). Part (a) by itself is a statement about two named distributions, not the arrow. The caption already credits 3(c).

BEFORE (line 745):
> `\draw[-{Latex[length=2mm]}] ([yshift=5pt]b.east) -- node[lab, above] {Thm 3(a)} ([yshift=5pt]c.west);`

AFTER:
> `\draw[-{Latex[length=2mm]}] ([yshift=5pt]b.east) -- node[lab, above] {Thm 3(c), by (a)} ([yshift=5pt]c.west);`

### (c) Question 1

Citable as it stands: the hypothesis is Definition 3, the conclusion is Definition 7 with its quantifier order (one p_D and one C, then all t ≥ p_D(n) and all large n), the object is Definition 6, and the display "no io-OWF ⇒ BEM" is what a later paper would quote. The dependence on the universal machine and on the n-bit pairing convention is absorbed by Definition 7's polynomial slack, so the question does not change with U.

**(c1) nit — carry the three definition numbers in the sentence**, so it survives being quoted alone. Line 729.

BEFORE:
> Does the non-existence of infinitely-often one-way functions force bounded exponential moments of the same-time Zurek defect for every polynomial-time samplable pair distribution?

AFTER:
> Does the non-existence of infinitely-often one-way functions (Definition 3) force bounded exponential moments (Definition 7) of the same-time Zurek defect (Definition 6) for every polynomial-time samplable pair distribution?

**(c2) nit — the plain reading's "at one time budget".** Line 733. Definition 7 asks for every t ≥ p_D(n); "at one time budget" reads as "at some t". AFTER: "…stay under a polynomial for every fast process, once the time budget is a large enough polynomial, both orders of description sharing one clock?"

### (d) Every italic plain reading against its formula or paragraph

All 99 were read against what stands above them. Five do not match; the rest do.

**(d1) blocking — §9.4, "The axiom, in Kelvin's form": the paper claims to prove a three-way equivalence it does not prove, and the plain reading says "the paper proves these are one rule".** Lines 1070–1072. The paragraph: "The extra assumption of the computing column can be stated three ways that Theorems 2 and 4 make one statement: (i) infinitely-often one-way functions exist; (ii) some polynomial-time samplable process has mean computational entropy production above c log n for infinitely many n, for every constant c (Theorem 2); (iii) not every polynomial-time samplable process can be run backward by a polynomial-time sampler with the right odds within a polynomial, on all but a 1/n slice of its ends (Corollary 2 with Theorem 4)." What is proved: (i) ⇔ (ii) is Theorem 2; (ii) ⇒ (iii) is Corollary 2. What is not: (iii) ⇒ (i). Its contrapositive says that without one-way functions every process is dominated on *all the starts* of all but a 1/n slice of ends, and §6 "Average forms" (line 617) says in so many words: "That is a statement about pairs, not about ends: one start of small conditional mass can spoil an end, so nothing is claimed for all the starts of a typical end." So the three statements are not shown to be one, and the plain reading (line 1072) "the paper proves these are one rule" is a false proof claim. The paragraph's opening ("an inference from them and no new claim") does not cover a stated equivalence.

Fix A (minimal; keeps the ends form). BEFORE (line 1070):
> The extra assumption of the computing column can be stated three ways that Theorems 2 and 4 make one statement: (i) … (iii) not every polynomial-time samplable process can be run backward by a polynomial-time sampler with the right odds within a polynomial, on all but a 1/n slice of its ends (Corollary 2 with Theorem 4).

AFTER:
> The extra assumption of the computing column can be stated three ways, of which Theorems 2 and 4 make the first two one statement and derive the third from them: (i) … (iii) not every polynomial-time samplable process can be run backward by a polynomial-time sampler with the right odds within a polynomial, on all but a 1/n slice of its ends (Corollary 2 with Theorem 4; whether (iii) forces (i) back is not proved, §6, "Average forms").

BEFORE (line 1072, plain reading; the paper carries the three-sentence form, B50 rule 5.30 not having been applied):
> *Plain reading: the rule at the top of the page can be said as "locks exist", as "some fast process dissipates", or as "no fast machine reverses every fast process", and the paper proves these are one rule. Half the second law comes free here, without the rule. A smaller rule might sit underneath it, and whether it is really smaller is the open problem.*

AFTER:
> *Plain reading: the rule at the top of the page can be said as "locks exist" or as "some fast process dissipates", and the paper proves these are one rule; it also proves that they force "no fast machine reverses every fast process", but not the way back. Half the second law comes free here, without the rule. A smaller rule might sit underneath it, and whether it is really smaller is the open problem.*

Fix B (keeps the equivalence, changes (iii) to a pairs form the paper's tools do prove): "(iii) not every polynomial-time samplable process can be run backward by a polynomial-time sampler with the right odds within a polynomial on all but a 1/q fraction of its pairs, for every polynomial q". Then no io-OWF ⇒ (iii) fails is the "Average forms" paragraph (USamp dominates on all but 1/q + 1/n of pairs), and (iii) fails ⇒ no io-OWF is Theorem 4(⇐), whose proof is pointwise in the pair, giving σ ≤ c′ log n off a 1/n fraction of pairs at q = n, hence E[σ] ≤ (c′ + 1) log n and Theorem 2. That needs three sentences of proof in §6; Fix A needs none.

**(d2) minor — §1.2, the sandwich display's last line and its plain reading name Proposition 9 as a barrier on Question 1; it is not.** Line 93 and line 95. §8.2 (line 840): "Proposition 9 concerns the skewed top arrow only." §1.1 (line 63): for the top arrow "no barrier statement is made". Proposition 9 says no relativizing proof gives BEM_skew ⇒ NP ⊆ BPP; Question 1 is no io-OWF ⇒ BEM.

BEFORE (line 93):
> `    open: does no io-OWF force BEM?     barriers on record: Propositions 9 and 10`

AFTER:
> `    open: does no io-OWF force BEM?     barrier on record: Proposition 10 (conditional); Proposition 9 is the barrier for the top of the skewed sandwich`

BEFORE (line 95):
> *…the last line is the question the paper leaves open, with the two propositions that say which proof methods cannot answer it.*

AFTER:
> *…the last line is the question the paper leaves open, with the proposition that says which proof methods cannot answer it, and the one that says the same of the skewed sandwich's top.*

**(d3) minor — §1.1 plain reading counts two theorems where the paragraph names three.** Line 65. The paragraph opens "Theorems 1, 2 and 4 hold in every one of Impagliazzo's five worlds".

BEFORE: *the two main theorems are true no matter which of the five possible worlds we live in.*
AFTER: *Theorems 1, 2 and 4 are true no matter which of the five possible worlds we live in.*

**(d4) nit — §8.5, the characterization question's two plain readings.** Line 948: "never says it to a string with a short program given the helper" drops the 0.9 of hypothesis (i); AFTER: "and says "not random", with probability at least 0.9, to every string with a short program given the helper". Line 952: "the one attempt to do better found that a saving of a few bits spread over many pieces cannot be seen in any single piece" attributes to an unnamed attempt what the paragraph gives as the paper's own reasoning ("for a reason short enough to state … (an inference; the accounting is in an unpublished note …)"); AFTER: "and the reason, an inference of this paper, is that a saving of a few bits spread over many pieces cannot be seen in any single piece".

**(d5) nit — §8.5 divide, "provably not the moment bound by black-box means".** Line 930. The crossed arrow rests on Proposition 10's hypotheses (i) and (ii) "as read"; "provably" is stronger than the paper's own convention allows. AFTER: "…but, if the oracle is as read, not the moment bound by black-box means…".

Checked and true (a sample of the ones a referee would test): Theorem 1(a)–(c); Lemmas 2–8; Theorem 2(2) (true with Theorem 1(b) supplying the lower half); Lemma 10(iii) both lines; Theorem 3(a) ("neither exponential average", read as the two displayed averages, is right); Theorem 4(⇒) with its 1/n slice; Definition 9's Σ⁻(x, y) = Σ⁺(y, x); Proposition 10(a) ("about n more bits", n − o(n) in the proof); Appendix B.1's display (log |M_t| − log t); §9.5's Fox–Karamchedu–Mygdalas reading, both caveats present in the paragraph.

### (e) §1.3 Conventions: what the paper relies on and does not define

**(e1) minor — K^t, the deterministic time-bounded description length, is used and never defined.** Lines 127 (§2.1 convention (iii), "K^t(x | y, r) ≤ s"), 944 and 964 (Proposition 13's hypothesis (i), "natural property for conditional K^t", "K^t(x | y) ≤ |x| − O(log |x|)"), 956 and 962 (§8.6, symmetry of information for K^t), 976 and 990, and 1032 (§9.2, Liu–Pass, "K^t is mildly hard on average"). Only pK^t (Definition 1) and K (Theorem 0) are defined. Proposition 13's hypothesis is stated in terms of K^t, so a reader cannot check the hypothesis without a definition. Add after Definition 1's conditional sentence (line 125):

AFTER (insert):
> K^t(x) and K^t(x | y) are the deterministic time-bounded description lengths, Definition 1 with no random string and the program required to print x outright; they appear in cited hypotheses (§2.1(iii), §8.5, §8.6, §9.2) and in no proof of this paper.

**(e2) nit — "i.o." and "≥ ω(log n)".** Line 49, the route line, is the paper's only use of the abbreviation "i.o.", which the Conventions do not define, and "≥ ω(log n)" combines an inequality sign with little-omega. AFTER: "some polynomial-time samplable process has mean production above c log n for infinitely many n, for every c   ⇔   one-way functions exist   ⇒   P ≠ NP." (This also fixes the time-quantifier omission of (a2) if "at every polynomial time bound" is added.)

**(e3) nit — terms used once, in Appendix A.2 row 12, without definition:** "Wainer function", "SAT's approximation rate" (line 1137). Mark them as Ben-David and Halevi's terms: "(their terms)". "AvgSIZE" (line 848) and "DistPH" (line 832) appear only inside quoted oracle statements and can stay.

Everything else the Conventions promise holds: Proposition 11 is the only "(informal)"; every other statement has a proof or a pointer; every displayed formula has an italic reading; the numbering is as stated; no sentence runs from physics to complexity.

### (f) The reference list

Read status: all 65 entries end with a bracket. Two forms are irregular: Takesue 1987 "[via its abstract]" (line 1249) is neither "read: …" nor "via <read source>"; AFTER "[read: abstract]". Li–Vitányi carries no year and Zurek 1989 (line 1255) no title; Marletto–Vedral 2017 says "title not carried". Order: Aaronson–Wigderson (line 1199) is filed after Almheiri; Harlow–Hayden (line 1218) before Grünwald.

**(f1) minor — "Bogdanov and Trevisan 2006" is two entries and one citation does not say which.** Line 900: "[Feigenbaum and Fortnow 1993; Bogdanov and Trevisan 2006]", in the sentence on worst-case to average-case reductions collapsing PH. The context is the SIAM paper (entry 6.16), not the survey (entry 6.15); line 575 correctly says "survey".

BEFORE (line 900): `[Feigenbaum and Fortnow 1993; Bogdanov and Trevisan 2006]`
AFTER: `[Feigenbaum and Fortnow 1993; Bogdanov and Trevisan 2006, On worst-case to average-case reductions, §4 Thm 17 and §5 Thm 20]`
(or rename the entries 2006a and 2006b in the list and at lines 575 and 900).

**(f2) minor — "Aaronson [2016, fn. 20]" does not say 2016a or 2016b.** Line 1076. BEFORE: `Aaronson's footnote [2016, fn. 20]`. AFTER: `Aaronson's footnote [Aaronson 2016a, fn. 20]`.

**(f3) nit — "Aaronson's slide 2 [2025]".** §9.2, "Hidden splits further" paragraph (line 1030). The entry is Aaronson, Kardes and Hartle 2025. AFTER: `[Aaronson, Kardes and Hartle 2025, slide 2]`.

**(f4) minor — "the authors" in a single-author paper.** Lines 753 ("an unpublished construction of the authors"), 890, 932, 950 and 1180 ("an unpublished note of the authors"). The title page has one author and the acknowledgements say "the author's". AFTER, at each: "the author". (Line 1028, "the authors liken to counting in decimal", refers to Shiraishi and Takesue and is right.)

### (g) Sentences a human referee would call machine-written

Listed with location; each is a sentence a human would not write in a complexity paper, or a workflow artefact left in the text.

1. Line 9 and line 107: "Physics is the frame, not the subject." / "Physics is the frame of this paper, not its subject" — the same disclaimer, twice.
2. Line 28: "Four things come out."
3. Line 53: "…and it says so."
4. Line 326: "Nothing in Theorem 1 is deep; its point is that the two-line derivation survives the time bound with polynomial slack in place of equality."
5. Line 382: "its value is the sentence it licenses, *one-way functions exist if and only if some efficiently samplable process dissipates.*"
6. Line 531 and line 920: "This paragraph runs from computation to reading; nothing in Theorem 3 rests on it." / "The reading runs from computation to physics; nothing above rests on it."
7. Lines 663 and 689: "no statement of it was found in the sources on disk" / "it was not found in the sources on disk" — a search log, not a literature claim; a human writes "we did not find it in the literature".
8. Line 876: "The statement is not in the literature; the oracle is."
9. Line 880: "the original not having been opened".
10. Line 1024: "That is Theorem 4's sentence, … said of a quantum system, by other people, and before this paper … It is quoted as the parallel it is."
11. Line 1064, repeated at A.2's bold line and in the Score: "Same shape in every row but the last; in the last, opposite sign."
12. Line 1076: "[Suppes Lecture, 9 Oct 2025, slide 27; unpublished, slides only as of 2026-09-12]" — an ISO date inside prose.
13. Line 1084: "In one sentence: this paper adds theorems to that idea, not the idea."
14. Line 1116: "(full-text search of the saved text)".
15. The labels, by count: "(an inference …)" 13 times, "as read" 8, "not proved here" 6, "We expect, but do not prove" 4. A human referee reads a paper that hedges thirty times as a paper that has not decided what it claims; the results box and §1.1 already do the work these labels do.

---

## Step 3 — B50_rules.md

Opened after the above was written. The file has 39 item-1 rules over 35 statement sites (the header says both; the brief's "39" matches), 33 item-5 rewrites (32 applied; 5.30 not applied, see below) and 4 kept readings. Base-file line numbers 917 and 1045 are rules 5.23 and 5.31; in the current paper they are lines 952 and 1080.

### Item 1, the 39 "Proved." → "Proof." rules

For each: was a hypothesis weakened, a caveat dropped, or content from the "Proved." paragraph lost rather than moved?

| rule | site | change | weakened / dropped / lost |
|---|---|---|---|
| 1.1 | Lemma 1 | label | no / no / no |
| 1.2 | Theorem 1 | label paragraph → pointer sentence to §3.2–3.3 | no / no / no |
| 1.3–1.9 | Lemmas 2–8 | label | no / no / no |
| 1.10 | Theorem 0 | "Proved; known. [sources]" → "Proof. Known: [sources]." | no / no / no |
| 1.11 | Theorem 0 | adds ∎ | no / no / no |
| 1.12 | Proposition 1 | "Proved as an equivalence, by HILNO" → "Proof. This is [HILNO, Theorem 1, items 1 and 3], an equivalence. ∎"; "Whether either side holds is open" kept after ∎ | no / no / no (pointer made exact) |
| 1.13 | Theorem 2 | label paragraph → pointer sentence; "Not new:" paragraph kept verbatim | no / no / no |
| 1.14 | Lemma 9 | attribution "HILNO's Lemma 20 argument" → first sentence of proof | no / no / no |
| 1.15 | Lemma 10 | label | no / no / no |
| 1.16 | Lemma 11 | "Proved from [GKLO22, Lemma 21]" → "Proof. From [GKLO22, Lemma 21]" | no / no / no |
| 1.17 | Remark 3 | "Proved (an identity plus Lemma 11)" → "The following is an identity together with Lemma 11." | no / no / no |
| 1.18 | Theorem 3 | "from" → "use" | no / no / no |
| 1.19 | Remark 4 | "(the last sentence is Theorem 3(a) read contrapositively)" → ", which is Theorem 3(a) read contrapositively" | no / no / no |
| 1.20–1.21 | Proposition 2 | "Proved." paragraph (which lemma; why the general form is not used) becomes proof's first paragraph; the second paragraph's "Proof." label dropped | no / no / no (checked in the current paper, lines 547–549: one proof, ends ∎) |
| 1.22 | Corollary 1 | "Proved, the contrapositive" → "Proof. The contrapositive of Proposition 2. ∎" | no / no / no |
| 1.23 | Proposition 3 | label | no / no / no |
| 1.24 | Theorem 4 | "Proved." dropped before "Not new as parts", which stays verbatim; "Proof." paragraph follows | no / no / no |
| 1.25–1.29 | Cor. 2, Lemma 12, Props 4–6 | label | no / no / no |
| 1.30 | Remark 5 | "Proved." → "Proof." (the remark proves a display) | no / no / no |
| 1.31 | Remark 6 | "Proved; known in substance, being the content of LOZ's optimal coding theorem together with HILNO's Proposition 22" → "Proof. Known in substance: [LOZ 2022, Theorem 30; HILNO, Proposition 22]." | no / no / no (Theorem 30 is the coding theorem, per Lemma 5's proof) |
| 1.32–1.33 | Proposition 7 | source pointer moved from head to proof's first sentence; the clause "which states the special case without a conditioning string" not repeated | no / no / no: the clause is the proof's next sentence (line 786) |
| 1.34 | Proposition 8 | "Proved-conditional on [GKLO22, Lemma 26(1)] as read, specifically on …" → "Assume, as read, that the proof of [GKLO22, Lemma 26(1)] uses DistNP ⊆ AvgBPP only once … Then:" | no / no / no |
| 1.35–1.36 | Proposition 9 | "Proved-conditional on (i) …" → "Assume (i) …"; conclusion sentence added, "Then no relativizing argument proves BEM_skew ⇒ NP ⊆ BPP" | no / no / no: the added sentence equals the proof's last (line 838) |
| 1.37 | Proposition 10 | "(i)–(iii)" into the head as "Assume (i)–(iii), where hypothesis (iii) is itself inferred … not proved" | no / no / no; "Part (a) uses (i) only" kept |
| 1.38 | Proposition 12 | label | no / no / no |
| 1.39 | Proposition 13 | "Proved-conditional on [KK 2025, Theorem 3.4] as read, with one clause" → "Assume [KK 2025, Theorem 3.4, §3.3, p. 21] as read, with one clause" | no / no / no |

Verdict on item 1: no hypothesis weakened, no caveat dropped, nothing lost. The one clause that did not travel with its rule (1.32 → 1.33) is stated by the sentence that follows. The Conventions' promise (proof or exact pointer after every statement) holds after the change.

### Item 5, the plain-reading rewrites, for truth

Each AFTER is its BEFORE's sentences joined by connectives; no clause is dropped, with one exception (5.6: "It is Lemma 5 with one extra input" becomes "as in Lemma 5", a pointer kept). The caveats the rules say they keep are kept: 5.3 (arrows not known to reverse), 5.19 ("a guess, not a result"), 5.23 ("if that is right"), 5.28 ("not proved here"), 5.31 (both). 5.15 is an improvement: "a term that is zero when…" now attaches to H(Y | X, Z), where BEFORE's "that extra term" could be read as the log t.

Truth against the formula or paragraph above each (the brief's test):
- 31 of 33 are true of what stands above them, in both BEFORE and AFTER.
- 5.30 (base line 1037, now line 1072): BEFORE and AFTER both say "the paper proves these are one rule". False of the paragraph, for the reason in (d1). This rule was not applied: the paper still carries the three-sentence BEFORE at line 1072, and the (d1) fix is written against that text. The rewrite would have neither introduced nor fixed the error.
- 5.22 (base line 895, now line 930): BEFORE and AFTER both say "provably"; overstated for the reason in (d5). Same status.
- **Line 917** (5.23, now line 952): true of the paragraph in both versions; the caveat "if that is right" is kept; the two obstructions, the n/log n exponent and Hirahara's informal argument are all in the paragraph. One nit, (d4): "the one attempt to do better" names nothing in the paragraph. AFTER's "which Hirahara argues informally a black-box argument is unlikely to beat" is grammatical but strained.
- **Line 1045** (5.31, now line 1080): true of the paragraph in both versions; "the authors do not draw that line themselves" is the paragraph's "do not write the chain"; "assumes a noise-free machine" is the paragraph's "error-free only"; "their claim, not this paper's" is there twice.

The four kept readings (lines 11, 44, 1083, 1107 base) read a paragraph or a table, and the reasons given for keeping them hold.

---

## Verdict

fix first: (d1) §9.4 Kelvin paragraph and its plain reading, the unproved (iii) ⇔ (i); (a3) §1 Theorem 3 bullet "both exponential moments"; (a2) results-box Theorem 2 row, "at every polynomial time bound"; (d2) §1.2 last line and plain reading, Proposition 9 is not a barrier on Question 1; (d3) §1.1 plain reading "two" → "Theorems 1, 2 and 4"; (a1) the "what is new" sentence to match the box and the body; (e1) define K^t; (f1) and (f2) the two ambiguous short forms; (f4) "the authors" → "the author" at five lines; (b1) the figure's arrow label.
