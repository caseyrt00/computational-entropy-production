# Referee report D — the additions to §8.2 (Proposition 10 through Remark 6)

Manuscript refereed: `problems/one-way-functions/passes/pass16/ENTROPY_PRODUCTION.md` (1196 lines). Joint: lines 859–1006 (Proposition 10 up to the line before "**The arrow and its observer.**" at 1007), the Impagliazzo–Luby clause at line 917, and the parenthesis "(Proposition 12 below makes this exact)" at line 837. Blind referee: only the manuscript and `passes/pass16/sources/*.txt` were read; nothing else in the repository was opened. Date: 2026-09-19.

Notation used below: ℓ := log(3(n + d)/2), the constant of Lemmas 2, 3 and 7; d the literal-print constant after Definition 1.

---

## Verdict

**Minor corrections.** No statement in the joint is false and no proof needs reworking: every proof matches an independent re-derivation in mechanism and in constants, except that MINOR-4 and MINOR-6 note two slacks the paper states more tightly than its proofs give (O(log n) where O(log t) is proved; additive t where the paper's own convention gives c·t). The single most important finding: two displayed conclusions, Proposition 10's "σ^rev_D(x, y) ≤ O(log n)" (line 861) and Proposition 11(b)'s "σ^rev_{D_{G∘F}} ≤ O(log n)" (line 945), are stated without the time at which the cited results (Proposition 9, Theorem 4(⇐)) prove them, and Proposition 11's preamble time does not cover (b).

---

## Findings, ranked

### BLOCKING — none.

### MAJOR — none.

### MINOR

**MINOR-1. Time missing from two conclusions.**
(a) Proposition 10, line 861: "σ^rev_D(x, y) ≤ O(log n) for every (x, y) ∈ supp D". Proposition 9 (line 839) proves this for every t ≥ t_D + p_R(n), p_R the polynomial Lemma 6 assigns to R. The blanket convention of §2.2 (t ≥ t_D) is weaker. Fix: "for every t ≥ t_D + p_R(n), p_R the polynomial of Proposition 9 for this R,".
(b) Proposition 11(b), line 945: "by Theorem 4(⇐) σ^rev_{D_{G∘F}} ≤ O(log n) on every support pair". Theorem 4(⇐) (line 893) gives this for t ≥ t_D + p(t_S) with S = S_F∘S_G, t_S = t_{S_F} + t_{S_G}. The preamble (line 935) has t ≥ max(t_{D_F}, t_{D_G}, n), with no p(t_S) term. The marginal half is covered: the second marginal of D_{G∘F} is the law of Z, which is also D_G's second marginal, so Lemma 5 at t ≥ t_{D_G} serves; the Lemma 6 time for the composite is the gap. Fix: "≤ O(log n) on every support pair, at every t ≥ t_{D_G} + p(t_{S_F} + t_{S_G}), p the polynomial of Lemma 6 for the composite."

**MINOR-2. Proposition 10, line 865, misdirected pointer.** "the deterministic chain x ↦ f(x) with f a one-way permutation has polynomial-time computable transition probabilities and, by Corollary 1, no polynomial-time reverse sampler." Corollary 1 (line 853) requires "D dissipates in the sense of Theorem 2". Theorem 2 (lines 349–359) supplies only that *some* samplable D dissipates when io-OWFs exist, not that this D_f = (x, f(x)) does; at line 865 nothing has established that (Proposition 13, which would, comes later). The claim itself is true in one line. Fix: "and no polynomial-time R dominates D_f(· | y) within a constant K on every y, since such an R outputs f^{−1}(y) with probability at least 1/K, an inverter (or: Proposition 13 below)."

**MINOR-3. The Impagliazzo–Luby clause, line 917, overstates.** "Together with Lemma 6 and Theorem 2 this is Impagliazzo and Luby's characterization, that one-way functions exist exactly when some efficiently computable function is distributionally one-way, read per process and with the universal sampler as the witness." Kashefi–Kerenidis Definition 2(ii) (source lines 157–165) defines distributional one-wayness by total-variation distance at least 1/p(n) between (x, f(x)) and (S(f(x)), f(x)). The paper's object is domination within n^c on all but a 1/q + 1/n fraction of pairs. Total-variation closeness within 1/p implies domination within 2 on all but a constant multiple of 1/p of the D-mass of pairs (a pair with S < D/2 has D − S > D/2, so those pairs carry D-mass at most a constant times 1/p; the constant is 2 or 4 according as total variation is the half-sum or the full sum, which KK07 does not fix); domination within n^c implies nothing about total variation. The two notions differ, in opposite directions, in both halves of the equivalence, so "this is" is not right. Fix: "this is a polynomial-domination form of Impagliazzo and Luby's characterization …: their inverter must reproduce the conditional within 1/p in total variation [Kashefi and Kerenidis 2007, Definition 2(ii)]; ours need only dominate it within a polynomial factor on most pairs, a weaker demand that closeness implies (within 2, on all but an O(1/p) mass) and does not follow from."

**MINOR-4. Proposition 11(a), line 939: "+ O(log n)".** The proof's slack (line 961) is ℓ + 2 + O(log t), the O(log t) being Lemma 12's; that is O(log n) only for t polynomial in n, and the statement quantifies over every t ≥ max(t_{D_F}, t_{D_G}, n). Part (c) (line 951) writes O(log t) correctly. Fix: "+ O(log t)" in (a), or add "t polynomial" to the preamble.

**MINOR-5. Two plain readings misstate their formulas.**
(a) Proposition 12, line 971: "the mean excess of the bounded observer's description of the start, given the end, over what the start still leaves undetermined in Shannon's sense". H(X | Y) is what the *end* leaves undetermined about the *start*. The reading also drops the ± O(log n). Fix: "over what the end still leaves undetermined about the start in Shannon's sense, within about log n bits".
(b) Proposition 11(a), line 941: "plus the information the middle state carries that neither end determines". H(Y | X, Z) is what the two ends *together* do not determine; "neither end" reads as either end alone (H(Y | X) or H(Y | Z)). The reading's next sentence, "whenever the two ends fix the middle", has it right. Fix: "that the two ends together do not determine".

**MINOR-6. Remark 5, line 993: "at time t + 2T(n) + O(n)".** The conditional program receives ψ(y) on the conditional tape, computes y onto a work tape, and then runs the program for x given y, which expects y on the conditional tape; that run is a simulation with per-step overhead, which the paper elsewhere charges as a constant factor (Lemma 11: "the time is O(t) + O(n)", stated as ct; Lemma 12 the same). Additive t is not justified under the paper's own convention. Fix: "at time c t + 2T(n) + O(n), c the constant of Lemma 11" (or "O(t + T(n))"). Also, the O(1) is independent of n only if φ, ψ and their inverses are computed by fixed algorithms; add "by fixed algorithms" to the hypothesis.

**MINOR-7. Proposition 13, converse sentence (line 985) and its proof (line 987).** "E_D[σ^rev_D at time p(T)] ≤ E_x[log 1/Pr[A(f(x)) = x]] + O(log n), with p the polynomial of Lemma 6" / "Lemma 5 bounds the marginal term". (i) Lemma 5 needs t ≥ t_D, and p(T) ≥ t_D is not guaranteed; but Lemma 5 is not needed: for this D, log 1/D(x, f(x)) = n exactly, so σ(x, f(x)) = pK^t(x | f(x)) + pK^t(f(x)) − n ≤ pK^t(x | f(x)) + d by the literal-print bound after Definition 1, at every t ≥ n. The time p(T) stands as written and the proof should use the trivial bound; the additive term is then O(log T) + d, see (ii). (ii) Lemma 6 gives O(log T), which is O(log n) only for polynomial T, and Lemma 6 is stated for polynomial-time S while the hypothesis says only "A running in time T". Fix: "+ O(log T)" or "T polynomial". Optional sharpening: with Lemma 5 at t ≥ max(t_D, p(T)) one keeps −log |f^{−1}(f(x))| from log 1/D(x | f(x)), whose mean is H(X | f(X)), giving E[σ] ≤ E_x[log 1/Pr[A(f(x)) = x]] − H(X | f(X)) + O(log T) + c_D log n, the exact mirror of the lower bound.

**MINOR-8. Proposition 13, line 979: hypothesis "for every t ≥ t_D with c_U (t + n) ≤ T(n)".** The lower bound uses Definition 10's bound and the lower side of Proposition 12 (Lemmas 2 and 7), none of which needs t ≥ t_D; Lemma 5 is not used. As stated the proposition is empty whenever T(n) < c_U(t_D + n) (security against n^2-time inverters with a large t_D, say). Fix: "for every t ≥ n with c_U (t + n) ≤ T(n)".

### NIT

**NIT-1. Proposition 10 proof, line 867: "at least 2^{−B} for a polynomial B".** Correct, B being a polynomial bound on the bit-length of the numerator π_i(s) P(s′ | s); but the statement (line 859) has just said "every entry a dyadic rational with at most n^{O(1)} bits", and a reader who takes B for the entry bit-length gets a false lemma. With entry bit-length B_0 the backward factor can be as small as 2^{−B_0 m}, m up to |S|: chain on states 0, …, m with P(i → i+1) = 2^{−B_0}, P(i → 0) = 1 − 2^{−B_0} for i < m, P(m → 0) = 1, π_0 = δ_0; then Q(m | 0) = π_{k−1}(m)·1/π_k(0) ≈ 2^{−B_0 m}; numerically 2^{−18.0} at B_0 = 3, m = 6, k = 20, against 2^{−B_0} = 2^{−3}. Fix: "for B := (L + 2) B_0, B_0 the bit-length of the entries". Also b := B + log L + 2 should read B + ⌈log L⌉ + 2 (b is a number of coins).

**NIT-2. Proposition 11(a) and (c), lines 939 and 951: "at time ct + O(n)".** The proofs give the bounds at ct (Lemma 12 and Lemma 11 are stated at ct, which for t ≥ n already absorbs the O(n)). Consistent through Lemma 4, but state one time or invoke Lemma 4 for the move.

**NIT-3. Constants in Proposition 12, line 973 (and the same step in 11(a), 13).** Jensen on log with Lemmas 2 and 3 gives both brackets ≥ −ℓ with no additive 2; the paper's −ℓ − 2 (tail integration, 1/ln 2 rounded to 2) is correct and looser.

**NIT-4. Remark 6 plain reading, line 1003: "This is Levin's universality".** No citation, no dagger. The reference list's Zvonkin–Levin 1970 entry (line 1194) is "cited via HILNO p. 3" for symmetry of information, not for universality of the universal semimeasure. Fix: cite it for this use too (cited via, or dagger), or write "the time-bounded analogue of the universality of the universal semimeasure".

**NIT-5. Line 965, lead-in "Two more consequences of Lemmas 5 and 7 and of Definition 10".** Proposition 13's converse also uses Lemma 6.

**NIT-6. Line 963, "the two directions of slack are the two kinds of randomness a step can carry".** Interpretive, unlabelled, and the referent of "two directions" is unclear ((a)'s H(Y | X, Z) versus its O(log n)? (a) versus (b)?). Label [Inference] or delete.

**NIT-7. Line 865, "the theorem form of the 'different object' of Appendix row 17".** Row 17 (line 1087) is Landauer heat versus Zurek's description-length cost; the link to a Markov chain is the phrase "different object" alone. Acceptable as a pointer; "cf." rather than "theorem form of".

**NIT-8. Remark 5.** D^{φ,ψ} is polynomial-time samplable only for polynomial T, and Definition 5 defines σ for samplable D. Say "T polynomial", or that Definition 5's formula is taken as the definition.

**NIT-9. Proposition 13 plain reading, line 983.** "a function that no fast algorithm inverts … dissipates at least s bits per use" omits that the dissipation is measured at clocks t with c_U(t + n) ≤ T(n) and holds up to O(log n); "s bits of security are s bits of dissipation" should carry "at any clock below the security time, within about log n bits".

**NIT-10. Proposition 11 preamble.** t ≥ t_{D_F}, t_{D_G} is not used in (a) (Lemma 5 does not enter); harmless.

---

## Blind re-derivations

Written before the paper's proofs were read; the comparison table follows.

**A. Lemma 7's tail integrated into a mean bound on pK^t(y).** Two routes. (A1) Jensen with Lemma 2, no tail needed: E_y[log 1/D_2(y) − pK^t(y)] = E_y[log(2^{−pK^t(y)}/D_2(y))] ≤ log E_y[2^{−pK^t(y)}/D_2(y)] = log Σ_{y ∈ supp D_2} 2^{−pK^t(y)} ≤ ℓ; so E[pK^t(y)] ≥ H(Y) − ℓ, for every t ≥ n. Per y with Lemma 3: E_{x ~ D(·|y)}[pK^t(x | y)] ≥ H(X | Y = y) − ℓ; averaged, E[pK^t(x | y)] ≥ H(X | Y) − ℓ. (A2) Tail integration: W := log 1/D_2(y) − ℓ − pK^t(y) has Pr[W > α] ≤ 2^{−α} for α ≥ 0 (Lemma 7, marginal form), so E[W] ≤ E[W_+] = ∫_0^∞ Pr[W > α] dα ≤ 1/ln 2 ≈ 1.443; the discrete sum Σ_{k ≥ 0} Pr[W_+ > k] gives 2. Hence E[pK^t(y)] ≥ H(Y) − ℓ − 1/ln 2 (or − 2). Upper side: Lemma 5, E[pK^t(y)] − H(Y) ≤ c_D log n for t ≥ t_D.

**B. Proposition 12.** Exact identity for every t: E_D[σ] = (E[pK^t(x | y)] − H(X | Y)) + (E[pK^t(y)] − H(Y)). Second bracket ∈ [−ℓ, c_D log n] (A1 and Lemma 5; t ≥ t_D for the upper side). First bracket ≥ −ℓ (A1 per y). So E_D[σ] − (E[pK^t(x | y)] − H(X | Y)) ∈ [−ℓ, c_D log n].

**C. Proposition 11(a).** With x ~ X, y = F(x), z = G(y) and independent coins, given Y the variable Z depends only on G's coins, independent of X and of F's coins, so (X, Y, Z) is Markov and I(X; Z | Y) = 0. E[log D_{G∘F}(x, z) − log D_F(x, y) − log D_G(y, z)] = −H(X, Z) + H(X, Y) + H(Y, Z). General identity: H(X, Y) + H(Y, Z) − H(X, Z) = H(Y) + H(Y | X, Z) + I(X; Z | Y) (check: H(X,Y) + H(Y,Z) − H(Y) − H(X,Y,Z) = I(X;Z|Y) and H(X,Y,Z) − H(X,Z) = H(Y|X,Z)); under Markov it is H(Y) + H(Y | X, Z). Numerically confirmed on random chains (identity exact to 10^{−15}; a random non-Markov joint shows the extra I(X;Z|Y) = 0.1906 exactly). Then σ_F@t + σ_G@t − σ_{G∘F}@t′ = [pK^t(x|y) + pK^t(y|z) − pK^{t′}(x|z)] + pK^t(y) + [pK^t(z) − pK^{t′}(z)] + [log D_F + log D_G − log D_{G∘F}]; first bracket ≥ −O(log t) by Lemma 12 for t′ ≥ ct (Lemma 4 above ct), third ≥ 0 by Lemma 4 for t′ ≥ t, E of the fourth = −H(Y) − H(Y|X,Z), and E[pK^t(y)] ≥ H(Y) − ℓ. Result: E[σ_{G∘F}@ct] ≤ E[σ_F@t] + E[σ_G@t] + H(Y | X, Z) + ℓ + O(log t). H(Y | X, Z) = 0 when F is deterministic (H(Y | X) = 0). Only t ≥ n is used.

**D. Proposition 13.** E[σ@t] ≥ E[pK^t(x | f(x))] − H(X | f(X)) − ℓ (B, lower side, t ≥ n). USamp_t(y) draws k ∈ [O(n)], a program of at most O(n) bits, a tape of t bits, and simulates U for t steps: time O(t + n) in any model that simulates the fixed machine U with constant overhead per step (multi-tape TM, RAM), hence c_U(t + n) ≤ T(n) is the right form of the condition. Then ε ≥ Pr_x[USamp_t(f(x)) ∈ f^{−1}(f(x))] ≥ Pr_x[USamp_t(f(x)) = x] = E_x[USamp_t(x | f(x))] ≥ E_x[1/(a n 2^{K(x)})] ≥ 2^{−E[K]}/(a n), K(x) := pK^t(x | f(x)), the last step Jensen for the convex u ↦ 2^{−u} (E[2^{−K}] ≥ 2^{−E K}, the direction that turns an upper bound on E[2^{−K}] into a lower bound on E[K]; numerically confirmed). So E[K] ≥ log 1/ε − log(a n), and E[σ@t] ≥ log 1/ε − H(X | f(X)) − log(a n) − ℓ. The event inclusion {USamp = x} ⊆ {USamp ∈ f^{−1}(f(x))} is in the right direction. Converse: Lemma 6 for A gives pK^{p(T)}(x | f(x)) ≤ log 1/A(x | f(x)) + O(log T) whenever A(x | f(x)) > 0; with the trivial marginal bound pK^t(y) ≤ n + d, σ ≤ log 1/A(x | f(x)) + O(log T) + d at time p(T) ≥ n; with Lemma 5 instead (t ≥ max(t_D, p(T))) one keeps −log |f^{−1}(f(x))| whose mean is H(X | f(X)).

**E. Proposition 10.** Forward: dyadic entries with at most B_0 bits are sampled exactly with B_0 fair coins per step; Definition 2 asks for an exact sample, and a non-dyadic probability such as 1/3 cannot be produced exactly in bounded time, so the dyadic hypothesis is needed as Definition 2 stands (or D must be redefined as the sampler's own law). Reverse: by the Markov property the backward process is a time-inhomogeneous chain with Q_k(a | b) := Pr[s_{k−1} = a | s_k = b] = π_{k−1}(a) P(a → b)/π_k(b), π_k = π_0 P^k, dyadic with at most (k + 1)B_0 bits and computable exactly in polynomial time; the telescoping product Π_{i<L} Q_{i+1}(s_i | s_{i+1}) = π_0(s_0) Π P(s_i → s_{i+1})/π_L(s_L) = D(x | y). Q is a ratio of dyadics, in general not dyadic, so R must round. Lower bound on a factor on its support: Q_k(a | b) ≥ π_{k−1}(a) P(a → b) ≥ 2^{−B_0 k} · 2^{−B_0} = 2^{−B_0(k+1)} (a path of positive probability of length k − 1 reaches a); the bound 2^{−B_0} on Q itself is false (NIT-1 example). Rounding down to multiples of 2^{−b}, leftover mass to ⊥: q̃(a) ≥ q(a) − 2^{−b} ≥ (1 − 1/(4L)) q(a) iff 2^{−b} ≤ q(a)/(4L); with q(a) ≥ 2^{−B}, B := B_0(L + 1) or B_0(L + 2), b ≥ B + log(4L) = B + log L + 2 suffices, polynomial. Over L steps (1 − 1/(4L))^L ≥ 1 − L/(4L) = 3/4 (Bernoulli; numerically 0.750 at L = 1 rising to 0.779 at L = 1000), so R(x | y) ≥ (3/4) D(x | y): domination within 4/3 ≤ 2. Proposition 9 with K = 2 then gives σ ≤ log 2 + O(log n) for every t ≥ t_D + p_R(n).

**F. Remark 5.** D^{φ,ψ}(φ(x), ψ(y)) = D(x, y) and D^{φ,ψ}_2(ψ(y)) = D_2(y) since φ, ψ are bijections, so both probability terms are unchanged. Marginal: run the program for y, apply ψ: pK^{t+T+O(n)}(ψ(y)) ≤ pK^t(y) + O(1), one application of T. Conditional: apply ψ^{−1} to the tape contents (T), run the program for x given y on the recovered y (t, plus per-step simulation overhead since the recovered y sits on a work tape, not the conditional tape), apply φ (T): two applications of T, so pK^{ct+2T+O(n)}(φ(x) | ψ(y)) ≤ pK^t(x | y) + O(1). The O(1) is the code of φ, ψ, ψ^{−1}: independent of n only if these are fixed algorithms. The other direction uses φ^{−1}, ψ^{−1}.

**G. Remark 6.** Lemma 6: pK^{p(t_S)}(x | y) ≤ log 1/S(x | y) + O(log t_S) =: k when S(x | y) > 0. Definition 10 at the same time p(t_S): USamp_{p(t_S)}(x | y) ≥ 1/(a n 2^k) ≥ S(x | y)/(a n t_S^{O(1)}) = S(x | y)/n^e for polynomial t_S; e depends on the code of S through the O(log t_S) constant and the degree of t_S. The drawn length must reach k ≤ n + d, which [O(n)] does.

### Comparison table

| quantity | mine | paper's | who is right |
|---|---|---|---|
| 11(a) entropy term E[log D_{G∘F} − log D_F − log D_G] | H(Y) + H(Y\|X,Z), plus I(X;Z\|Y) without Markov | H(Y) + H(Y\|X,Z) | both, identical |
| 11(a) additive slack | ℓ + O(log t) | ℓ + 2 + O(log t), written O(log n) | both for polynomial t; O(log n) unproved for superpolynomial t (MINOR-4) |
| 11(a) time of σ_{G∘F} | ct | ct + O(n) in statement, ct in proof | both; NIT-2 |
| Lemma 7 tail → mean of pK^t(y) | ≥ H(Y) − ℓ (Jensen); − ℓ − 1/ln 2 (integral); − ℓ − 2 (sum) | ∫ ≤ ℓ + 1/ln 2, then − ℓ − 2 | both; paper's is the looser correct constant |
| 12: E[σ] − (E pK(x\|y) − H(X\|Y)) | [−ℓ, c_D log n] | [−ℓ − 2, c_D log n] | both (NIT-3) |
| 12: lower bound on the bracket | ≥ −ℓ | ≥ −ℓ − 2 | both |
| 13: Jensen step | E 2^{−K} ≥ 2^{−E K}, so E K ≥ log 1/ε − log(a n) | same | both |
| 13: final constant | log 1/ε − H(X\|f(X)) − log(a n) − ℓ | … − log(a n) − ℓ − 2 | both |
| 13: time hypothesis | t ≥ n suffices | t ≥ t_D | paper's is unnecessary (MINOR-8) |
| 13: sampler time condition | O(t + n), constant overhead: c_U(t + n) ≤ T | same | both |
| 13: converse | E σ@p(T) ≤ E log 1/A + O(log T) + d (trivial marginal bound); or − H(X\|f(X)) + O(log T) + c_D log n at t ≥ max(t_D, p(T)) | E σ@p(T) ≤ E log 1/A + O(log n), proof by Lemma 5 | statement right for polynomial T; proof's Lemma 5 needs t ≥ t_D and is not needed (MINOR-7) |
| 10: per-factor lower bound | Q ≥ 2^{−B_0(k+1)}; not ≥ 2^{−B_0} | ≥ 2^{−B}, B a polynomial (bits of the numerator product) | both, same content; NIT-1 naming |
| 10: coins per step | b ≥ B + log L + 2 | b := B + log L + 2 | both |
| 10: per-step loss, product | 1 − 1/(4L); (1 − 1/(4L))^L ≥ 3/4 | same | both |
| 10: constant | 4/3 ≤ 2 | 4/3 ≤ 2 | both |
| 10: time of conclusion | t ≥ t_D + p_R(n) | unstated | MINOR-1 |
| Remark 5: time | c t + 2T + O(n) | t + 2T + O(n) | mine, under the paper's Lemma 11 convention (MINOR-6); the O(1)-bit content is unaffected |
| Remark 5: applications of T | 2 (conditional), 1 (marginal) | 2 | both |
| Remark 6 | Lemma 6 + Definition 10 at the same time p(t_S) | same | both |

---

## Verified correct

- Proposition 10, forward exactness: dyadic entries with B_0 bits sampled exactly by B_0 coins via the cumulative table; against Definition 2 (line 114).
- Proposition 10, factorization D(x | y) = Π P̃_i(s_i | s_{i+1}): telescoping checked by hand.
- Proposition 10, per-factor bound 2^{−B} with B the polynomial bit-length of π_i(s)P(s′ | s): π_i(s) > 0 and P > 0 on supp D, numerator a positive dyadic with poly many bits, denominator ≤ 1.
- Proposition 10, rounding: (1 − 2^{−b+B}) = 1 − 1/(4L) at b = B + log L + 2; (1 − 1/(4L))^L ≥ 3/4 by Bernoulli; both numerically confirmed (L = 1, 2, 3, 7, 10, 100, 1000).
- Proposition 10, "detailed balance was not used": true; the proof uses only the Markov property.
- Lemma 12: same construction as Lemma 11 (line 434); 0.9 · 0.9 = 0.81 ≥ 2/3; time O(t) + O(n) ≤ ct for t ≥ n.
- Proposition 11 preamble: (X, Y, Z) is Markov as defined (independent coins).
- Proposition 11(a): the Δ decomposition; the entropy identity under Markov (numerically checked); Lemma 12 pointwise; Lemma 4 invoked for pK(z) moving from t to ct; Lemma 7 second form integrated with D_2 = law of Y; H(Y | X, Z) = 0 for deterministic F.
- Proposition 11(b): D_{G∘F}(x | z) = Σ_y D_G(y | z) D_F(x | y) by X ⊥ Z | Y; D_G(y | z) is the reverse conditional of D_G; domination within n^{a+b} on every z ∈ supp Z; Theorem 4(⇐) with Y = supp Z; ⊥ outputs harmless.
- Proposition 11(c): pointwise, for t ≥ n, n-bit x, x′: exact product of probabilities; Lemma 11 (hypothesis t ≥ n, n-bit strings) applied twice, once with pK^t(y′ | y) ≤ pK^t(y′) + O(1); the conditioning string of length 2n enters only through the construction, and no Kraft constant at length 2n enters a pointwise bound.
- Closing remark, line 963: the appended-random-bits example is loose by |r|, as stated (checked: σ_F, σ_G, σ_{G∘F} all O(log n) in mean while H(Y | X, Z) = |r|); the marginal direct-sum claim in the mean holds by Lemma 7 integrated at length 2n and Lemma 5 for D_2, D′_2 at t ≥ max(t_D, t_{D′}); the [Inference] label is present. The sentence "a direct-sum statement for conditional pK^t that is a form of symmetry of information" is not an overclaim: the mean direct-sum lower bound needs the hard direction of the conditional chain rule, which is what Section 7 (lines 442, 611) calls symmetry of information, and "a form of" is the right hedge.
- Plain readings of Proposition 10, Lemma 12, Proposition 11(b), Proposition 11(c), Remark 5, and the Δ display in 11(a)'s proof: each matches its display; only the four flagged in MINOR-5, NIT-4 and NIT-9 say more or less than their formulas.
- Proposition 12: the identity; upper side c_D log n (Lemma 5, t ≥ t_D); lower side −ℓ − 2 on both brackets (Lemma 7 first form per y then averaged, second form for the marginal).
- Line 837, "(Proposition 12 below makes this exact)": accurate — Proposition 12's identity subtracts H(X | Y) exactly, with the O(log n) confined to the marginal bracket.
- Proposition 13: Definition 10's bound at the same t; Jensen direction; event inclusion; the c_U(t + n) ≤ T(n) condition is the right one for USamp_t (Definition 10, line 875: draw k ∈ [O(n)], r ∈ {0,1}^t, d ∈ {0,1}^k, run U for t steps).
- Remark 5: equal probabilities under bijections; two applications of T in the conditional term, one in the marginal; the exchanged direction by φ^{−1}, ψ^{−1}.
- Remark 6: Lemma 6 and Definition 10 at the same time p(t_S); e depends on the code of S; "the universal-witness clause of Theorem 4 with the process D removed" (line 1005; the clause itself is line 899) accurate.
- Labels: every item in the joint carries **Proved** (Remark 6: "Proved; known in substance"); every displayed formula has a *Plain reading*; no [Speculation]/[Unverified] on any proposition.
- Cross-references: Proposition 9 (line 839) in Proposition 10; Lemma 11's constant c in Lemma 12 and 11(c); Lemma 12 in 11(a); Lemmas 4, 5, 7 where cited; Theorem 4(⇐) in 11(b); Definition 10 and Proposition 12 in 13; Lemma 6 in 13's converse and Remark 6; "Section 7" for symmetry of information (lines 442, 611, 757–769); Corollary 2 (line 919) as named in Corollary 1.
- Sources: HILNO Definition 21 (lines 1259–1268) matches Definition 10's description of USamp; HILNO Proposition 22 (lines 1271–1273) states Ω(1/(n · 2^k)) when pK^t(x | y) ≤ k, matching "≥ 1/(a n 2^k)". Kashefi–Kerenidis §1 (lines 96–98) and Definition 2 (157–165): distributionally one-way functions are Impagliazzo–Luby's [10] and were proved equivalent to one-way functions — the paper's description of IL's theorem is accurate (only the "this is" of MINOR-3 is not). LOZ Theorem 5 (lines 329–334) = Theorem 30 (1246–1251), Lemma 31 (1255–1266): "optimal coding theorem" as attributed in Remark 6; the reference entry (line 1181) names exactly these parts.

---

## Sources read, with line ranges

- `ENTROPY_PRODUCTION.md`: 7–22 (Conventions); 96–170 (§2, Definitions 1–5, Lemma 1); 196–262 (Lemmas 2–8); 329–337 (Proposition 1 statement); 349–359 (Theorem 2 statement); 428–436 (Lemma 11); 713–717 (Proposition 7 statement); 837 (the "Hidden splits further" paragraph); 839–852 (Proposition 9); 853–1006 (the joint, in full); 1007 (first line of "The arrow and its observer", not further); 1087 (Appendix row 17); 1147, 1168, 1172, 1181, 1194 (reference entries for Bogdanov–Trevisan, Impagliazzo–Luby, Kashefi–Kerenidis, LOZ, Zvonkin–Levin); grep hits only for "symmetry of information", "Levin", "Theorem 1(c)".
- `sources/hilno_eprint2023-424.txt`: 1240–1300 (Lemma 19, Lemma 20, Definition 21, Proposition 22, start of the proof of Lemma 20); grep for "Jensen" (no hit).
- `sources/kashefi_kerenidis2007_arxiv0511266.txt`: 90–100 (§1), 150–172 (Definition 2 and its lead-in), 340–348, 1030–1031 (reference [10]).
- `sources/lu_oliveira_zimand_2022_arxiv2204.08312.txt`: 329–346 (Theorem 5), 1246–1266 (Theorem 30, Lemma 31); grep for "Jensen" (no hit).
- Numerical checks: `.venv/bin/python` script (entropy identity on random Markov and non-Markov joints; Bernoulli product; the backward-factor example; Jensen direction; 1/ln 2), run once, outputs quoted above.

---

## Audit items [Unverifiable here]

- Novelty of Proposition 11(a) and of Proposition 13's Jensen step: HILNO and LOZ contain no "Jensen"; that is absence in the on-disk set only. [Unverifiable here]
- Impagliazzo–Luby 1989: not on disk; the paper cites it via Kashefi–Kerenidis, consistent with the reference entry (line 1168). What IL's original proves beyond KK07's summary is unverifiable here.
- "Levin's universality" (Remark 6): Zvonkin–Levin 1970 not on disk; the reference entry cites it via HILNO for symmetry of information, not for universality. [Unverifiable here]
- "Folklore" for Lemma 12 and for Proposition 11(b): no source named; standard, but unverifiable from disk.
- GKLO22 Lemma 21, behind Lemma 11 and therefore Lemma 12: not reopened (Lemma 11 was refereed earlier).
- c_U (Proposition 13): the paper does not fix the machine model in which "running in time T(n)" is measured; constant-factor simulation of the fixed U holds for multi-tape Turing machines and RAMs, not for a single-tape model. [Inference]

---

## In plain words

Everything new in this stretch of Section 8.2 is right: the Markov-chain example, the rule for how dissipation adds up when processes run in sequence or side by side, the exact bookkeeping of lost bits, and the bound that turns security against inverters into dissipation. I rebuilt each argument on my own before reading the paper's proofs, and in every case the paper's mechanism and its constants agree with mine; where they differ, the paper's constants are the safer, looser ones, apart from two places where the paper writes a slack a little more tightly than its own proof gives, both noted in the findings. What needs fixing is small and clerical: in a few places the paper states a bound without saying at what clock setting it holds, though the results it leans on say so; one sentence points to the wrong earlier result to justify a claim that has a one-line direct justification; one sentence says the paper's result "is" a classical theorem when it is a looser cousin of it; one mean bound says "log n" where "log t" is what is proved; two of the plain-language readings say something slightly different from the formula above them; and a remark adds running times where the paper's own convention multiplies one of them by a constant. Each fix is a clause or a phrase; none changes a conclusion. Total work: an hour of editing, no new mathematics.

---

## Reproduce

The numbers quoted above (entropy identity on random Markov and non-Markov joints, the Bernoulli product, the backward-factor example, the Jensen direction, 1/ln 2) come from the script below; run it with the project interpreter, `.venv/bin/python checks.py`, runtime under one second, no dependencies beyond numpy.

```python
import numpy as np, math
rng = np.random.default_rng(1)
def H(p):
    p = p[p>0]; return float(-(p*np.log2(p)).sum())
# 1. Entropy identity: H(X,Y)+H(Y,Z)-H(X,Z) = H(Y)+H(Y|X,Z)+I(X;Z|Y)
def ent_terms(pxyz):
    pxy = pxyz.sum(2); pyz = pxyz.sum(0); pxz = pxyz.sum(1); py = pxyz.sum((0,2))
    lhs = H(pxy.ravel())+H(pyz.ravel())-H(pxz.ravel())
    HY = H(py); HY_XZ = H(pxyz.ravel()) - H(pxz.ravel())
    I_XZ_Y = H(pxy.ravel()) + H(pyz.ravel()) - H(py) - H(pxyz.ravel())
    return lhs, HY, HY_XZ, I_XZ_Y
# Markov chain: p(x) F(y|x) G(z|y)
for trial in range(3):
    kx,ky,kz = 4,5,3
    px = rng.dirichlet(np.ones(kx)); F = rng.dirichlet(np.ones(ky), size=kx); G = rng.dirichlet(np.ones(kz), size=ky)
    pxyz = px[:,None,None]*F[:,:,None]*G[None,:,:]
    lhs,HY,HY_XZ,I = ent_terms(pxyz)
    print(f"Markov trial {trial}: lhs={lhs:.6f}  H(Y)+H(Y|X,Z)={HY+HY_XZ:.6f}  I(X;Z|Y)={I:.2e}")
# non-Markov
pxyz = rng.dirichlet(np.ones(4*5*3)).reshape(4,5,3)
lhs,HY,HY_XZ,I = ent_terms(pxyz)
print(f"non-Markov: lhs={lhs:.6f}  H(Y)+H(Y|X,Z)={HY+HY_XZ:.6f}  diff={lhs-HY-HY_XZ:.6f}  I(X;Z|Y)={I:.6f}")
# deterministic F => H(Y|X,Z)=0
F = np.eye(4,5)[:, :5]; F = np.zeros((4,5)); 
for i in range(4): F[i, rng.integers(5)] = 1
G = rng.dirichlet(np.ones(3), size=5); px = rng.dirichlet(np.ones(4))
pxyz = px[:,None,None]*F[:,:,None]*G[None,:,:]
print("deterministic F: H(Y|X,Z) =", round(ent_terms(pxyz)[2], 12))
# 2. Rounding arithmetic (Prop 10)
for L in [1,2,3,7,10,100,1000]:
    print(f"L={L}: (1-1/(4L))^L = {(1-1/(4*L))**L:.5f} >= 3/4: {(1-1/(4*L))**L >= 0.75};  (1-1/(2L))^L={(1-1/(2*L))**L:.5f}")
B=7; L=8; b = B + math.log2(L) + 2
print("b = B+log L+2 =", b, "; 2^{-b+B} =", 2**(-b+B), "; 1/(4L) =", 1/(4*L))
# 3. Backward factor example: states 0..m, P(i->i+1)=2^-B0, P(i->0)=1-2^-B0 (i<m), P(m->0)=1, start at 0
B0 = 3; m = 6; k = 20
P = np.zeros((m+1,m+1))
for i in range(m): P[i,i+1] = 2.0**-B0; P[i,0] = 1-2.0**-B0
P[m,0] = 1.0
pi = np.zeros(m+1); pi[0]=1
pis=[pi.copy()]
for _ in range(k): pi = pi@P; pis.append(pi.copy())
Q = pis[k-1][m]*P[m,0]/pis[k][0]   # backward prob of being at m at time k-1 given at 0 at time k
print(f"entry bits B0={B0}: min backward factor Q(m|0) = {Q:.3e} = 2^{math.log2(Q):.2f};  2^-B0 = {2.0**-B0:.3e};  bound 2^-(B0(k+1)) = {2.0**(-B0*(k+1)):.3e}")
# 4. Jensen direction: E[2^-K] >= 2^-E[K]
K = rng.integers(1,40,size=1000).astype(float)
print("E[2^-K] =", np.mean(2.0**-K), " 2^-E[K] =", 2.0**-np.mean(K), " E[2^-K] >= 2^-E[K]:", np.mean(2.0**-K) >= 2.0**-np.mean(K))
# 5. tail integral constants
print("1/ln2 =", 1/math.log(2))
```
