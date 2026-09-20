# Referee report A — the unconditional core

**Manuscript.** `ENTROPY_PRODUCTION.md` (line numbers below refer to it; page numbers, marked "p.", to the typeset `ENTROPY_PRODUCTION.pdf`).
**Joint refereed.** Definitions 1–5; Lemmas 1–8; Theorem 1 (§3); Theorem 0 (§3.3); Proposition 9 and Corollary 1 (§8.2); Definition 10, Theorem 4 and Corollary 2 (§8.2, up to the paragraph "The arrow and its observer").
**Protocol.** Blind re-derivation first (from the Conventions block, Definitions 1–5 and the bare statements), written to a scratch file before any proof was opened; then the paper's proofs; then the sources. Disclosure for auditability: four proofs sit on the line directly after their statement and were seen during the statement pass — the one-line proof of Lemma 4, the three-line proof of Lemma 7, the "Proved / Not new as parts" paragraph of Theorem 4 (not its proof body), and the proof of Corollary 2. All other proofs (Lemmas 2, 3, 5, 6, 8; Theorem 1; Theorem 0; Proposition 9; Theorem 4 body) were read only after the re-derivations were written.

---

## Verdict

**Minor corrections** — every numbered statement in the joint is true and every proof correct in substance; the most important finding is that Proposition 9 is stated for "t ≥ t_D" (the polynomial §2.2 fixes from D's forward sampler alone) while its proof needs t ≥ p(T_R(n)) for the reverse sampler's own polynomial and says "enlarge t_D", so the statement as printed is stronger than what is proved (M1), and its hypothesis of an exact reverse sampler is, under Definition 2's strict time bound, an arithmetic condition met only on dyadic fibers (M5).

**Summary.** The blind re-derivations reproduce the paper's constants exactly (Theorem 4's b = 3a(1+d)/2 and exponent c+3; Theorem 1's (3/2)²(n+d)² and −2 log(3(n+d)/2)); Theorem 1(a)'s lower bound goes, as it must, through one all-zero-coins support pair and not through a conditional coding step; the one proof written in full, Lemma 6, matches Lu–Oliveira–Zimand's Lemma 31 and proof of Theorem 30 point for point, including the AC⁰ generator; Theorem 4's restatement of HILNO's Definition 21 and Proposition 22 is exact. Theorem 4(⇐), which does Proposition 9's job in the right generality, already states its time bound correctly as t ≥ max(t_D, p(t_S)); Proposition 9 and the sentences that lean on it should be routed through it. Nothing in the joint moves the paper's claims.

---

## Findings, ranked

### BLOCKING
None.

### MAJOR
None.

### MINOR

**M1. Proposition 9's time bound hides a dependence on R.** Location: Prop. 9, line 797 (p. 33), "Then for t ≥ t_D and every (x, y) ∈ supp D, σ^rev_D(x, y) ≤ O(log n)"; proof, line 807: "Lemma 6 applied to it gives pK^t(x | y) ≤ log 1/D(x | y) + O(log n) for t ≥ poly(T_R(n)) …; enlarge t_D to cover that polynomial."
Issue: §2.2, line 84 (p. 4), fixes t_D once per D ("For each samplable D fix a polynomial t_D = poly(T(n)) large enough that Lemma 5 below applies to D_1, D_2 and to the sampler"). R is a separate object; its running time T_R and the Lemma 6 polynomial p(T_R) can exceed any t_D fixed in advance. What the proof establishes is σ ≤ O(log n) for every t ≥ max(t_D, p(T_R(n))). "Enlarge t_D" is a redefinition of a symbol fixed elsewhere. The downstream cost is nil: Corollary 1 uses only that some polynomial works, because Theorem 2's dissipation quantifies over every polynomial p. But the Proposition as printed claims more than is proved.
Fix, in the paper's style: "Then there is a polynomial p_R, depending only on the code of R, such that for every t ≥ max(t_D, p_R(n)) and every (x, y) ∈ supp D, σ^rev_D(x, y) ≤ O(log n)"; in the proof replace "enlarge t_D to cover that polynomial" by "take p_R := p(T_R), the polynomial Lemma 6 assigns to R"; in Corollary 1's one-line proof add "at p = max(t_D, p_R)". This is exactly the form Theorem 4(⇐) already uses (line 843).

**M2. The Kraft constant (3/2)(n + d) is off by one length unless a convention on the empty program is stated.** Location: Lemma 2, line 162 (p. 7), "Σ_x 2^{−pK^t(x)} ≤ (3/2)(n + d)"; proof, line 166: "pick j ∈ {1, …, n + d} uniformly … By Definition 1 it outputs x with probability at least (1/(n + d)) · (2/3) · 2^{−pK^t(x)}"; Lemma 3, line 170, same constant.
Issue: the sampler covers strings with 1 ≤ pK^t(x) ≤ n + d. Definition 1 (line 70) and HILNO eq. (6) (source line 820: "min{k ∈ N …}") allow k = 0, the empty program, on the reading that their ℕ contains 0 [Inference: neither text says which convention it uses]; a string x with pK^t(x) = 0 is output by the sampler with probability 0, and the displayed lower bound on its output probability fails for it. My count (below) gives Σ_x 2^{−pK^t(x)} ≤ (3/2)(n + d + 1); or ≤ (3/2)(n + d) + 1, since at most one string of each length can have pK^t = 0 (two distinct strings cannot both be printed by the single empty program on two-thirds of the r's). LOZ's Lemma 36 (source lines 1420–1431, "j ∈ [n + d]") has the same gap; the paper inherits it. The constant is stated as exact and propagates: log(3(n + d)/2) in Lemma 7 (line 204) and Lemma 8 (line 215); (3/2)²(n + d)² in Theorem 1(a) (line 229); −2 log(3(n + d)/2) in Theorem 1(b),(c) (lines 237, 243); the set G in Theorem 4 (line 855); b = 3a(1 + d)/2 (line 839).
Fix (either): (i) add after Definition 1 the convention "U(ε, r) prints no string of length ≥ 1, so pK^t(x) ≥ 1 for every x of length n ≥ 1" — then every constant stands as printed; or (ii) draw j ∈ {0, …, n + d} and replace (n + d) by (n + d + 1) in Lemmas 2, 3, 7, 8, Theorem 1, Theorem 4's G, and set b := 3a(2 + d)/2. Also: Lemma 2 says "For every t and n", but pK^t(x) ≤ n + d is asserted (line 76) only for t ≥ |x|; write "for every t ≥ n and every n".

**M3. The Markov-chain sentence after Corollary 1 over-claims unless the state space is polynomially small.** Location: §8.2, line 817 (p. 34): "Every finite-state Markov chain with polynomial-time computable transition probabilities has a reverse chain with polynomial-time computable transition probabilities, ratios of forward probabilities and of marginals obtained by matrix powers, hence a polynomial-time reverse sampler from the endpoint, so that … every model system of stochastic thermodynamics of that kind has O(log n) computational production".
Issue, two parts. (i) Computable reverse transition probabilities yield a reverse *sampler* only when the states can be enumerated. Counterexample on n-bit states: the deterministic chain x ↦ f(x) with f a one-way permutation, uniform start. Its transition probabilities are 0/1 and polynomial-time computable; all marginals are uniform; the reverse transition probability P(x′ | x) = [f(x′) = x] is polynomial-time computable — and sampling one reverse step is inverting f. Matrix powers on 2^n states are not polynomial-time either. The sentence is correct only when "finite-state" means a state space of size polynomial in n (the usual model systems), which is presumably what is meant [Inference], but the paper's D lives on {0,1}^n × {0,1}^n and the reader will apply the sentence there. (ii) Even for a two-state chain the sentence cannot go through Proposition 9, because Proposition 9 asks for an *exact* reverse sampler. A sampler in the sense of Definition 2 (line 80: "running in time T(n)") and of HILNO's footnote 2 (source lines 784–786) reads at most T(n) fair coins, so every forward probability, and every marginal, is a multiple of 2^{−T(n)}; the reverse transition probabilities are ratios of such numbers (for instance (3/4)(1/2)/(5/8) = 3/5) and are in general not dyadic, so no strictly time-bounded R samples them exactly. What is true, and what the paper's own Theorem 4(⇐) delivers, is a *dominating* reverse sampler: compute each reverse conditional to T(n) + 2 + log L bits (L the trajectory length), sample the truncation step by step; since every support conditional is at least 2^{−T(n)}, the truncation dominates within a constant factor, and Theorem 4(⇐) with Y = supp D_2 gives σ ≤ c′ log n on every support pair.
Fix: "Every Markov chain on a state space of size polynomial in n with polynomial-time computable transition probabilities has a polynomial-time reverse sampler from the endpoint that dominates the reverse conditional within a constant factor (truncate the backward transition probabilities, obtained from matrix powers, to T(n) + O(log n) bits), so by Theorem 4(⇐) …", with x the trajectory and y the endpoint, both padded to n bits as Definition 2 requires.

**M4. Lemma 6's plain reading says more than the formula.** Location: line 197 (p. 8): "It is Lemma 5 with one extra input, and the same constant."
Issue: the formula's constant (the O(log t) term) depends on the code of S; Lemma 5's c_D depends on the code of D's forward sampler. They are constants of the same kind, fixed by the program's code, not the same constant. "About k bits" also hides the O(log t) that the displayed inequality carries.
Fix: "It is Lemma 5 with one extra input, with a constant that, as there, depends only on the code of the program: about k bits plus a few log t."

**M5. Proposition 9's hypothesis is an arithmetic condition, and Corollary 1's closing sentence over-reads it.** Location: Prop. 9, line 797 (p. 33): "suppose there is a polynomial-time randomized algorithm R such that R(y) samples D(· | y) for every y ∈ supp D_2"; Cor. 1, line 811 (p. 34): "then D(· | y) is not samplable in polynomial time given y … Dissipation in this paper's sense lives only where the reverse process is computationally hard."
Issue: under Definition 2 (line 80, "running in time T(n)"; HILNO footnote 2, source lines 784–786, is the same strict convention) a sampler reads at most T(n) fair coins, so D(x, y) and D_2(y) are multiples of 2^{−T(n)} while D(x | y) = D(x, y)/D_2(y) generally is not: a fiber of three equally likely starts has conditional 1/3. A strictly time-bounded R has dyadic output probabilities and cannot produce 1/3, so Proposition 9's hypothesis holds only when every fiber conditional is dyadic — an arithmetic accident, not a statement about hardness [Inference that R is meant strictly time-bounded, as every other algorithm in the paper is; the paper nowhere allows expected time]. Concretely, D = (x, f(x)) with x uniform and f merging the last two bits {00, 01, 10} ↦ 00 is trivially reversible up to a factor 4/3 yet has no exact reverse sampler, so Proposition 9 does not apply to it and Corollary 1's hypothesis is met by it for arithmetic reasons. Corollary 1 as a mathematical statement stays true; the gloss "lives only where the reverse process is computationally hard" is earned by Corollary 2 and Theorem 4(⇐) (domination within a polynomial), not by Corollary 1. The paper's own "Proved" paragraph of Theorem 4 (line 853) already records Proposition 9 as "its case S = R exact, Y = supp D_2, c = 0".
Fix: either state Proposition 9 with domination within a constant (Theorem 4(⇐) at Y = supp D_2, c any positive constant), which is the natural "efficiently reversible" hypothesis and covers the dyadic obstruction; or keep it as is, add the sentence "exact sampling is a strong hypothesis: a strictly time-bounded R has dyadic output probabilities, so Proposition 9 covers only processes whose fibers are dyadic; the general case is Theorem 4(⇐)", and move the closing sentence of Corollary 1 to Corollary 2.

### NIT

**N1.** Theorem 1, line 225 (p. 9), "Then for every n": the lower-bound program (line 253) "has length c_0 log n", which is 0 at n = 1. Write "for every n ≥ 2", or "length c_0 log n + c_0" and n^{−2c_0} 2^{−2c_0}.

**N2.** §2.2, line 84: "t_D … large enough that Lemma 5 below applies to D_1, D_2 and to the sampler." Theorem 1(a)'s lower bound (line 253: "it runs within t_D ≤ t steps") needs t_D to cover U's simulation of one run of the sampler. LOZ's coding-theorem polynomial does cover that (their decoder runs the sampler on H_w(v), source lines 1296–1313), so if t_D is taken to be that polynomial the requirement is met [Inference: the paper does not say that this is how t_D is chosen], but the sentence does not say it. Add: "and so that U simulates one run of the sampler within t_D(n) steps".

**N3.** Lemma 7, line 202: "every y" — D(· | y) is undefined off supp D_2. Write "every y ∈ supp D_2" (the source, HILNO Lemma 9 item 2, line 866, says exactly that).

**N4.** Theorem 1, line 236: "The upper bound holds for every distribution on pairs, samplable or not." So do (b) and (c), which use only the upper bound; say so, since Theorem 4(⇒) leans on Lemma 7 for arbitrary D.

**N5.** Definition 10, line 827 (p. 34): USamp_t runs U "with oracle access to the bits of y and r for t steps", whereas Definition 1 (line 76) gives y on a tape and r on a tape, and Proposition 22 uses the same t on both sides. HILNO Definition 21 (source lines 1261–1270) has the same mismatch. The overhead is a fixed polynomial and nothing in Theorem 4 changes, but fix the access model once (or define USamp_t to run for the steps needed to simulate t tape-steps) so that USamp_t and pK^t carry the same t honestly.

**N6.** Theorem 0, line 269 (p. 10): "with K the unbounded prefix complexity … [Zvonkin and Levin 1970, cited via HILNO p. 3 …] … [Li and Vitányi, Theorem 3.9.1 for the prefix version with O(1) …]". Both pointers check out (HILNO line 113 on p. 3: "[ZL70] credits Levin and Kolmogorov independently"; Grünwald–Vitányi lines 1106–1117). Two nuances: HILNO's K on p. 3 is plain complexity, and GV line 1115 says the Kolmogorov–Levin theorem is "for the plain (non-prefix) version … up to an additive logarithmic term"; the O(1) prefix form, GV eq. (3.9), conditions on y* (y together with a shortest program for it), not on y. The displayed statement — prefix K, plain conditional K(x | y), ± O(log n) — is true, since prefix and plain differ by O(log n) for strings of length n. Add: "(the original is for plain complexity; the prefix form with O(1) error conditions on y* rather than on y)".

**N7.** Corollary 2 proof, line 871: "at every t ≥ p′(n) := max(t_D, p(t_S(n)))" — the maximum of two polynomials is not literally a polynomial, and Theorem 2's condition asks for one. Use t_D + p(t_S); Lemma 4 makes the bounds monotone in t. Same in Theorem 4(⇐), line 843.

**N8.** Theorem 4(⇒) plain reading, line 837: "on a pair that the process reverses without computational cost" — the hypothesis is σ ≤ c log n, a small cost, not zero. "with at most c log n bits of computational cost".

**N9.** "Average forms", line 867: "Proposition 1(ii) with Lemma 5 puts σ^rev_D within O(log n) of zero on all but a 1/q fraction" — those two give the upper side only; the lower side is Theorem 1(c) (Lemma 7), as line 875 correctly says ("Proposition 1(ii) together with Lemmas 5 and 7"). Add "and Theorem 1(c)".

**N10.** Corollary 2 plain reading, line 873, drops "for infinitely many n". End it "…on all but a 1/n slice of ends, for infinitely many lengths".

**N11.** Lemma 6 statement, line 192: "not on x, y, n or t" — p is applied to t, so the phrase is confusing. "a polynomial p and a constant, both fixed once the code of S is fixed".

**N12.** Definition 4, line 106 (p. 5), calls m_R and m_F "universal fast semimeasures". A semimeasure sums to at most 1; Theorem 1(a)'s own upper bound is Σ_{x,y} m_R ≤ (3/2)²(n + d)², and the Kraft count in Lemma 2 allows each program length to contribute up to 3/2, so the sum can exceed 1 by a polynomial factor. "Semimeasure up to a polynomial factor", or drop the word; this is also the honest name for why the integral fluctuation "identity" of Theorem 1(a) has polynomial slack where Crooks's eq. (4) has equality.

---

## Blind re-derivations (written before the proofs were read)

Notation: K := (3/2)(n + d), the paper's Kraft constant; K′ := (3/2)(n + d + 1), my count.

**Lemma 2.** For fixed r and k let A_r(k) := {x ∈ {0,1}^n : ∃p ∈ {0,1}^k, U(p, r) = x within t steps}; |A_r(k)| ≤ 2^k, one output per program. Let N_k := #{x : pK^t(x) = k}. Each such x has Pr_r[x ∈ A_r(k)] ≥ 2/3, so (2/3) N_k ≤ E_r|A_r(k)| ≤ 2^k, i.e. N_k ≤ (3/2) 2^k. Then Σ_x 2^{−pK^t(x)} = Σ_k 2^{−k} N_k ≤ (3/2) · #{admissible k}; k ranges over 0, …, n + d, so the bound is K′ = (3/2)(n + d + 1); it is K iff k = 0 never occurs. (Had HILNO's eq. (6) used programs of length at most k, the bound would double to 3(n + d + 1); I checked eq. (6), source line 820: it uses p ∈ {0,1}^k, exactly k, as the paper's Definition 1 says. A prefix-free U would give 3/2 with no factor n; the factor (n + d) is the mark of a plain machine.)

**Lemma 3.** Identical with y on the tape.

**Lemma 7.** Z(x) := 2^{−pK^t(x|y)} / D(x | y) on x ∈ supp D(· | y). E_{x ~ D(·|y)} Z = Σ_{x ∈ supp} 2^{−pK^t(x|y)} ≤ K by Lemma 3. Markov: Pr[Z ≥ 2^α K] ≤ 2^{−α}, and Z ≥ 2^α K ⟺ pK^t(x | y) ≤ log 1/D(x | y) − α − log K. So Pr[pK^t(x | y) ≤ log 1/D(x | y) − α − log K] ≤ 2^{−α}; the paper's strict "<" is the weaker statement. Second form from Lemma 2, same steps. No samplability used.

**Theorem 1.** (a) upper: E_D[2^{−σ}] = Σ_{supp D} m_R = Σ_{supp} 2^{−pK^t(y)} 2^{−pK^t(x|y)} ≤ Σ_y 2^{−pK^t(y)} Σ_x 2^{−pK^t(x|y)} ≤ K², any D, any t.
(a) lower: Lemma 5 cannot give it in general. 2^{−pK^t(y)} ≥ D_2(y) n^{−c_D} is fine, but the conditional term has no coding theorem when one-way functions exist (that is the paper's hinge), and pairing Lemma 5 for D_1 with Lemma 5 for D_2 gives Σ_{supp D} D_1(x) D_2(y), which is 2^{−n} for a permutation graph. Jensen from an upper bound on E[σ] gives only 2^{−n−O(1)}. The working route is one simple support pair: run the sampler on 1^n with all-zero coins; the output (x_0, y_0) is in supp D_n. The program "run the sampler on 1^n with zero coins, print the second component" has length ≤ c_1 log n (code plus a self-delimiting n) and runs in poly(T(n)) steps, so pK^t(y_0) ≤ c_1 log n; "…print the first component" gives pK^t(x_0 | y_0) ≤ c_2 (n = |y_0| can be read off the tape), hence E_D[2^{−σ}] ≥ m_R(x_0, y_0) ≥ n^{−2c_0} with c_0 depending on the sampler's code and U, and t need only cover one simulated run of the sampler. Prediction recorded before reading: if the paper's proof applies a conditional coding bound to every pair, that step is false.
(b) 2^{−u} is convex, so 2^{−E σ} ≤ E 2^{−σ} ≤ K²; E σ ≥ −2 log K. Any D.
(c) Markov on 2^{−σ}: Pr[2^{−σ} ≥ 2^α K²] ≤ 2^{−α}, and that event is σ ≤ −α − 2 log K.

**Proposition 22 fact (Definition 10).** Pr[USamp_t(y) = x] ≥ Pr[length drawn = k_0] · E_r[#{d ∈ {0,1}^{k_0} : U(d, r; y) = x}] / 2^{k_0} ≥ (1/(a′n)) (2/3) 2^{−k_0} for k_0 = pK^t(x | y), where a′n is the size of the length range, which must contain 0..n + d. So a = (3/2) a′. For real k ≥ pK^t(x | y): pK ≤ ⌊k⌋ and 2^{⌊k⌋} ≤ 2^k, so the bound 1/(a n 2^k) holds for real k with no ceiling loss.

**Theorem 4 (⇒).** G := {y ∈ supp D_2 : pK^t(y) ≥ log 1/D_2(y) − log n − log K}; Lemma 7 second form at α = log n gives D_2(G) ≥ 1 − 1/n. For y ∈ G and σ(x, y) ≤ c log n: pK^t(x | y) = σ + log 1/D(x, y) − pK^t(y) ≤ c log n + log 1/D(x, y) − log 1/D_2(y) + log n + log K = log 1/D(x | y) + (c + 1) log n + log K =: k. Then USamp_t(x | y) ≥ 1/(a n 2^k) = D(x | y) / (a K n^{c+2}) = D(x | y) / ((3a/2)(n + d) n^{c+2}) ≥ D(x | y) / ((3a/2)(1 + d) n^{c+3}), using n + d ≤ (1 + d) n. So b = 3a(1 + d)/2 and the exponent is c + 3: (c+1) from the σ-bound, +1 from the n in Proposition 22, +1 from n + d ≤ (1 + d) n. t ≥ t_D is not needed for this direction.

**Theorem 4 (⇐).** y ∈ Y and (x, y) ∈ supp D give S(x | y) ≥ D(x | y)/n^c > 0, so x ∈ supp S(· | y). Lemma 6: pK^{p(t_S)}(x | y) ≤ log 1/S(x | y) + C_S log t_S(n) ≤ log 1/D(x | y) + (c + C_S · deg t_S) log n + O(1). Lemma 4 lifts this to every t ≥ p(t_S); Lemma 5 gives the y-bracket ≤ c_D log n for t ≥ t_D. So σ ≤ c′ log n for t ≥ max(t_D, p(t_S)), c′ = c + c_D + C_S deg t_S + o(1), depending on the code of S (which fixes t_S), c and c_D.

**Theorem 4 (universal witness).** With the same k := log 1/D(x | y) + (c + C_S deg t_S) log n + O(1), Proposition 22 at time p(t_S) gives USamp_{p(t_S)}(x | y) ≥ D(x | y) / (a 2^{O(1)} n^{1 + c + C_S deg t_S}) =: D(x | y)/n^{c″}. Holds on exactly Y, no exceptional set, no t_D.

**Proposition 9.** y-bracket ≤ c_D log n for t ≥ t_D (Lemma 5 on D_2). x-bracket: Lemma 6 with S = R gives pK^{p(T_R)}(x | y) ≤ log 1/D(x | y) + O(log T_R) = log 1/D(x | y) + O(log n) on every x ∈ supp D(· | y). Needs t ≥ p(T_R(n)), which the §2.2 t_D does not cover. Moments follow from the pointwise bound.

**Corollary 2.** Contrapositive. If for all large n some S dominates within n^c on Y_n with D_2(Y_n) ≥ 1 − 1/n: on Y_n-pairs σ ≤ c′ log n at t = t_D + p(t_S); off Y_n (mass ≤ 1/n) σ ≤ pK^t(x | y) + pK^t(y) + log D(x, y) ≤ 2(n + d). So E σ ≤ c′ log n + 2(n + d)/n ≤ (c′ + 1) log n once log n ≥ 2 + 2d, contradicting Theorem 2's dissipation at p = t_D + p(t_S), C = c′ + 1.

### Comparison table

| quantity | mine | paper's | who is right |
|---|---|---|---|
| Kraft sum bound, Lemmas 2 and 3 | (3/2)(n+d+1); equals (3/2)(n+d) iff pK^t ≥ 1 | (3/2)(n+d) | mine as printed; the paper's under the convention of M2(i) |
| Lemma 7 slack | log K | log(3(n+d)/2) | same, modulo M2 |
| Lemma 7 event | "≤" | "<" | both true; paper's is the weaker form |
| Lemma 7 quantifier on y | y ∈ supp D_2 | "every y" | mine (N3), cosmetic |
| Theorem 1(a) upper bound | K², any D, any t | (3/2)²(n+d)², "every distribution" | same |
| Theorem 1(a) lower bound, route | one all-zero-coins support pair; Lemma 5 not usable | one all-zero-coins pair (line 253); Lemma 5 not used | same route; both agree the lower bound does not use Lemma 5 |
| Theorem 1(a) lower bound, time | t ≥ one simulated sampler run | t ≥ t_D ("runs within t_D ≤ t steps") | same, provided §2.2 is read to cover it (N2) |
| Theorem 1(a) lower bound, value | n^{−2c_0}, c_0 from sampler code and U | n^{−2c_0}, same dependence | same |
| Theorem 1(b) | E σ ≥ −2 log K | −2 log(3(n+d)/2) | same |
| Theorem 1(c) | Pr[σ ≤ −α − 2 log K] ≤ 2^{−α} | with "<" | same |
| Proposition 22 constant a | (3/2) × (length-range size / n), U only | "a, depending only on the universal machine" | same |
| Theorem 4(⇒), set G | Lemma 7 second form, α = log n, D_2(G) ≥ 1 − 1/n | same (line 855) | same |
| Theorem 4(⇒), bound | D(x\|y)/((3a/2)(1+d) n^{c+3}) | b = 3a(1+d)/2, exponent c+3 | identical |
| Theorem 4(⇒), time | any t | "t ≥ t_D a polynomial" | both true; t_D is not used in this direction |
| Theorem 4(⇐) | c′ = c + c_D + C_S deg t_S + o(1); t ≥ max(t_D, p(t_S)) | c′ = c + c_D + O(1); same t | same |
| Universal witness | c″ = 1 + c + C_S deg t_S + O(1); on exactly Y; time p(t_S) | same (line 863) | same |
| Proposition 9, time | t ≥ max(t_D, p(T_R)) | t ≥ t_D | mine (M1) |
| Corollary 2 | p = t_D + p(t_S), C = c′ + 1 | p′ = max(t_D, p(t_S)), C = c′ + 1 | same (N7 cosmetic) |

---

## Lemma 6 against its source (plan item 2)

(a) **Statement of Lemma 31 as quoted.** LOZ, source lines 1255–1268: "For any T ∈ N and δ ∈ [0, 1], there exists a family of functions H = {H_w : {0,1}^ℓ → {0,1}^T}_{w ∈ {0,1}^k} where k = poly(T) and ℓ = log(1/δ) + O(1) such that the following holds. Let M : {0,1}^T → {0,1}^* be a function computable in time T and let x ∈ Range(M) be such that Pr_{z}[M(z) = x] ≥ δ. It holds that Pr_{w ∼ {0,1}^k}[∃v ∈ {0,1}^ℓ such that M(H_w(v)) = x] ≥ 2/3. Moreover, given w and v, H_w(v) can be computed in time poly(T)." The paper (line 199) quotes: family "with k = poly(T) and ℓ = log 1/δ + O(1), quantified before the function M and so independent of it, such that for every M computable in time T and every x with Pr_z[M(z) = x] ≥ δ, for at least 2/3 of the seeds w there is a v … and H_w(v) is computable from w and v in time poly(T)". Quantifier order (H before M), seed length, ℓ and the 2/3 all match. Correct.

(b) **Advice independent of y.** In the pK^t definition (Definition 1; HILNO eq. (6), source line 820) the existential over the program sits inside Pr_r, so the program may depend on r; LOZ's own decoder (source lines 1304–1308) uses this: "some good v (which could depend on w)". The paper's advice α = (T, code of S, code of the generator, v): v depends on x, y and w, which is permitted since pK^t(x | y) is computed for fixed x, y; what matters is |α| = ℓ + O(log T), and y enters only through the tape. The family H is the output of a fixed AC⁰ generator with parameters N = 2^ℓ T and s = 2^{poly(T)} (source lines 1282–1291), which depend on T and δ only; the y-dependent AC⁰ check (y hardwired) has the same size, so the same generator fools it [Inference: this step is my reconstruction and the paper's (line 199); LOZ state Lemma 31 for an M with no auxiliary input and do not write this sentence]. Correct; the paper's sentence "α does not carry y, which is why the constant survives" (line 201) is the right reason.

(c) **p(T) and the constant depend only on S's code.** LOZ Theorem 30 (source lines 1246–1252): "the constant behind the O(·) depends on |A| and is independent of the remaining parameters"; t(n) = poly(T(n)). The paper's transfer to S is faithful. One remark: the polynomial p depends on U's simulation overhead and on the generator's per-bit time, not on S's code except through T; the paper's "depending on the code of S only" is harmless (N11).

(d) **"Pseudorandom generator for AC⁰".** LOZ, source lines 1282–1285: "Now we will try to generate a good H using a pseudorandom generator for AC⁰ circuits. It is known that there is a pseudorandom generator G : {0,1}^r → {0,1}^N that (1/10)-fools AC⁰ circuits on N bits of size at most s, where the seed length r is at most polylog(Ns) … (see e.g., [Nis91, TX13, Tal17, ST19])." The paper's description matches. The NP-to-AC⁰ step is LOZ's too (source lines 1276–1281, citing [RST15]).

One internal wobble in the source, not in the paper: LOZ's Lemma 31 has ℓ = log(1/δ) + O(1) while their proof of Theorem 30 (line 1299) writes ℓ = log(1/δ) + O(log T). The paper uses the Lemma's O(1) for ℓ and puts the O(log T) in the advice, which is the consistent reading.

Also verified: the paper's page citations "Lemma 31, §5.1, p. 25" and "proof of Theorem 30, §5.1, p. 26" agree with the page markers in the source text (line 1293 marks p. 25; the Theorem 30 proof follows it).

---

## Theorem 4 against HILNO (plan item 3)

HILNO Definition 21 (source lines 1261–1270): USamp(1^n, 1^t, y): "1. Pick a uniformly random k ∼ [O(n)], 2. … r ∼ {0,1}^t, 3. … d ∼ {0,1}^k, 4. Outputs x which is the output of a universal oracle Turing machine … U, on input d with an oracle to the bits of y and r (i.e. U^{y,r}(d)), running for t steps." Proposition 22 (lines 1276–1278): "if pK^t(x | y) ≤ k, then USamp(1^n, 1^t, y) outputs x with probability Ω(1/(n · 2^k))". The paper's restatement (line 827–831) is exact: k uniform from [O(n)], oracle access to y and r, 1/(a n 2^k) with a a U-only constant. (HILNO's statement quantifies an unused "ℓ ∈ N"; a typo in the source, irrelevant.) The oracle-versus-tape mismatch is N5, inherited from HILNO. The constant b = 3a(1 + d)/2 and exponent c + 3 recompute exactly as above; the paper's line 859 does the arithmetic with k := pK^t(x | y) an integer, which avoids even the ceiling question.

---

## Verified correct

- Definition 1 = HILNO eq. (6): programs of length exactly k, Pr over r ∼ {0,1}^{t(|x|)}, threshold 2/3 (source line 820). Conditional form "y on a separate input tape" = HILNO line 829, which is on p. 17 (page marker at line 842). Correct.
- Definition 3's io-OWF convention = HILNO lines 793–794 (p. 16) and Theorem 1 item 1 (line 220); "≤ n^{−c}" versus "< 1/q(n)" are the same quantifier up to reparametrization; the negation stated at line 100 is right.
- Definition 5's two lines agree: D(x, y) = D(x | y) D_2(y).
- Lemma 1: tautology from Definition 5; Crooks eq. (7) (source line 178, p. 3) → eq. (2) (line 56) is the parallel claimed.
- Lemma 2's sampler = LOZ Lemma 36 (source lines 1415–1431), with the M2 caveat shared with the source.
- Lemma 3's sampler = HILNO Definition 21; Kraft from Proposition 22 gives the same constant.
- Lemma 4's proof: the time-t event depends only on the first t bits of r′, which are uniform. Correct.
- Lemma 5 = LOZ Theorem 5 (source lines 329–334, with T(n) ≥ n) = Theorem 30 (line 1246); constant depends on |A|; t = poly(T). Applied to the marginal projections of the sampler. Correct.
- Lemma 6: see the section above. Correct, and the proof is a faithful relativization.
- Lemma 7 = HILNO Lemma 9 item 2 (source lines 860–870) with Lemma 3 for Kraft. Correct.
- Lemma 8: first line Lemma 5 for D_2, second Lemma 7 second form. Correct.
- Theorem 1(a) upper, (b), (c): Kraft × Kraft, Jensen, Markov. Correct for every distribution on pairs.
- Theorem 1(a) lower: the all-zero-coins pair (line 253). Correct; c_0 from the sampler's code and U, as stated; Lemma 5 is not used and is not needed (my blind route is the same).
- Remark 2's "The proof of (c) is [HILNO, Lemma 9]": HILNO Lemma 9 is Markov on the Kraft sum (source lines 860–880). Correct.
- Theorem 0: statement true for prefix K with ± O(log n); attributions verified at HILNO line 113 (p. 3) and GV lines 1106–1117 (N6 nuance).
- Proposition 9's "Proved" paragraph: "the general conditional form … is equivalent to NP ⊆ BPP [HILNO, Theorem 4, item 2]" = HILNO lines 398–409 (Worst-Case Conditional Coding ⇔ NP ⊆ BPP). Correct.
- Proposition 9's proof: Lemma 5 + Lemma 6 with S = R; moments from the pointwise bound. Correct apart from M1; the reach of its hypothesis is M5.
- Corollary 1 = contrapositive of Proposition 9 (with M1's polynomial). Correct as a statement; its closing gloss is M5.
- Definition 10's Levin-domination usage is the standard one (Bogdanov–Trevisan pointer not re-checked; not in my joint's mathematics).
- Theorem 4 (⇒), (⇐), universal witness: all three match my derivations, constants included. Theorem 4's "Proved / Not new as parts" attributions: HILNO §1.3 "Part 1" exists (source line 434) and lines 500–512 show the same mechanism (a short conditional description yields a sampler with matching odds). Correct.
- "Average forms" paragraph (line 867): the 1/q + 1/n union bound is right (N9 for the lower side).
- Corollary 2: proof correct (N7 cosmetic); the negation of "dissipates" is handled correctly.
- Plain readings of Definitions 1, 4, 5, Lemmas 1, 2, 3, 5, 7, 8, Theorem 1(a)(b)(c), Theorem 1's proof line, Theorem 0 (both), Proposition 9 (both), Corollary 1, Definition 10 (both), Theorem 4(⇐), universal witness, Theorem 4's proof line: each says what its formula says. Exceptions are M4, N8, N10.

---

## Sources read

- `ENTROPY_PRODUCTION.md`: lines 8–23 (Conventions), 64–126 (§2), 127–284 (§2.5 end through §3.3), 783–882 (§8.2 through "The arrow and its observer"). Nothing else in the manuscript, nothing else in the repository.
- `sources/hilno_eprint2023-424.txt`: 104–122 (p. 3, symmetry of information and [ZL70]); 185–210 (informal pK^t, p. 4); 212–250 (Theorem 1, pp. 4–5); 398–425 (Theorem 4 and §1.3 head); 434 (Part 1); 770–835 (pp. 16–17: OWF definition, K^t, rK^t, eq. (6), conditional pK^t); 856–880 (Lemma 9, pp. 17–18); 1255–1300 (Definition 21, Proposition 22, p. 25).
- `sources/lu_oliveira_zimand_2022_arxiv2204.08312.txt`: 325–350 (Theorem 5, p. 7); 1244–1320 (§5.1: Theorem 30, Lemma 31 with proof, proof of Theorem 30, pp. 25–26); 1410–1445 (Lemmas 36–37).
- `sources/grunwald_vitanyi2004_arxiv0410002.txt`: 1100–1118.
- `sources/crooks1999_arxiv9901352.txt`: equation and page markers only (lines 56, 83, 178; page markers 69, 131, 205).
- `ENTROPY_PRODUCTION.pdf`: converted with pdftotext for page numbers only.

---

## Audit items

- Li and Vitányi, Theorem 3.9.1 (2nd ed.): not on disk; checked only through Grünwald–Vitányi's citation of it. [Unverifiable here]
- Zvonkin and Levin 1970: not on disk; checked only through HILNO p. 3. [Unverifiable here]
- The PH-oracle-to-AC⁰ step ([RST15]) and the AC⁰ generator parameters ([Nis91, TX13, Tal17, ST19]) inside LOZ's Lemma 31: taken from LOZ as read; the originals are not on disk. [Unverifiable here]
- HILNO's Proposition 22 states Ω(1/(n · 2^k)) with no explicit constant; the paper's a is a definition of that constant, not a quotation. Fine as used.
- Bogdanov–Trevisan §1.1.2 footnote 3 for the word "dominates": not re-read; not load-bearing for any inequality in the joint.
- The claim (line 817) that "every model system of stochastic thermodynamics of that kind" is a poly-size-state Markov chain is a modelling assertion, not checked here; see M3.

---

## In plain words

Everything in this part of the paper that is claimed as a theorem is true, and the proofs work. I re-derived the main inequalities on my own before looking at the authors' arguments, and I got the same numbers they did, down to the exact constants; the one longer proof they wrote out, the coding theorem with an extra input, matches its source paragraph by paragraph. What needs fixing is bookkeeping. The most important item is that one proposition promises its bound at a time budget fixed earlier in the paper, while its proof needs a possibly larger budget that depends on the reverse program being discussed; the fix is to state the larger budget, which the paper already does correctly in the theorem next to it. That same proposition also asks for a reverse program that reproduces the process's backward odds exactly, and a program that runs in a fixed number of steps can only produce odds that are fractions with a power-of-two denominator, so "exactly" quietly rules out most processes, including trivially reversible ones; the paper's Theorem 4 already has the right hypothesis, "approximately, within a polynomial factor", and the proposition and the sentence that draws the moral from it should lean on that theorem instead. A second item is a counting constant that is off by one unless the paper states a convention about the empty program; a one-sentence convention makes every printed constant right. A third is a sentence about Markov chains that is true for small state spaces, once routed through the approximate-reversal theorem, but false for large ones as written; it needs one qualifying clause and a different pointer. The rest are word-level: a plain reading that says "the same constant" when it should say "the same kind of constant", a citation that should name which version of an old theorem it means, and a few quantifiers. All of it is an afternoon's work and none of it changes any result.
