# Thread B36: is the worst-case problem the hub? (the cheapest open item from B31)

Date: 2026-09-15. Reading task. Question inherited from `b31_instance_checkers.md` §4.2 and §7: does

  (i) BPP natural property for conditional pK^t, usefulness `n − O(log n)`, largeness ≥ 1/2
  ⇒ (ii) `Gap_{τ,δ} McpK^tP ∈ promise-BPP`  ⇒ (iii) errorless scheme computing `pK^t(x | y)` on
  samplable pairs  ⇒ (iv) `H_pK`

go through at **logarithmic** gap, so that both directions of the characterization become available?

**Sources read this session, all local, nothing from memory.** All citations give the printed page
and the line number in the extracted text under `pass16/sources/`.

| source | what was read | status |
|---|---|---|
| Kabanets & Kolokolova, ECCC TR25-089 (`kk_eccc_tr25-089.txt`) | §1 pp. 2–3 (incl. fn. 2); §2.2 Defs 2.3, Lemmas 2.4/2.5 + Remark 2.6 (ll. 568–618); §2.3 Defs 2.7/2.10/2.11 (ll. 626–700); §2.4 Defs 2.12/2.13, Lemmas 2.14/2.15/2.16, Cors 2.17/2.19, Def 2.18 (ll. 705–828), **all proofs**; **§3.3 Theorem 3.4 with its full proof** (ll. 1119–1215); §4.1 Thm 4.1 proof and **§4.2 Thm 4.3 with its full proof** (ll. 1250–1385); §6.3 Thm 6.3 and §6.4 (ll. 1556–1630); §8 (l. 1887 ff.) | **Read (local)** |
| Hirahara, CCC 2022 (`hirahara_ccc2022_lipics234-26.txt`) | §2.1 Lemmas 2.1/2.2 + the DP sketch (ll. 470–600); §3 Defs 3.1/3.3/3.5, Facts 3.2/3.4 (ll. 800–856); **§4 Theorem 4.1 with its full proof** (ll. 858–965); §6.1 Def of GapMINcKT + **Prop 6.2 with proof** (ll. 1240–1300); §7 Def 7.4 + **Lemma 7.5 with proof** (ll. 1740–1800); **§8 in full**: Def 8.1, Thm 8.2, Lemma 8.3 + proof, Lemma 8.4, Thms 8.5/8.6/8.7 + proofs, **proof of Thm 8.2** (ll. 1911–2155) | **Read (local)** |
| GKLO22, CCC 2022 (`gklo_ccc2022.txt`) | §1.1 Thm 1 (l. 321); §1.3.1.4–1.3.3 incl. the "no PRG needed" passage (ll. 483–600); §2.1 defs of K^t/pK^t and Lemma 2.1 (ll. 540–575); Defs 4/5, **Lemma 6 + proof** (ll. 684–735); §3.2 **Lemma 22 + proof**, Lemma 23 (ll. 1179–1300); §3.3 **Lemma 24/25** (ll. 1307–1330); §3.4 **Lemma 26 statement and the full proof of Item 1** (ll. 1334–1490); §3.7 Lemma 31 (l. 1780); §4.6 + Remark 52 (ll. 2755–2800); §5.1.2 **Def 59 and Lemma 60 + proof** (ll. 3059–3120) | **Read (local)** |
| HILNO, eprint 2023/424 | Theorems 1 and 3 statement lines only (ll. 217, 368), used for placement, not for any step | **Read (local), partial** |

No web fetches were needed.

---

## 0. Outcome in one paragraph

**The briefed chain fails at (ii) ⇒ (iii), and it does not matter, because the chain is unnecessary.**
Hirahara's Theorem 8.2 item 1 ⇒ item 2 runs through Theorem 4.1 and Theorem 8.6, and Theorem 8.6
runs through **Lemma 8.3**, the Longpré–Watanabe search algorithm, whose object is *the
lexicographically first shortest program* for `x`. `pK^t` has no such object — its program may depend
on the random string — so that step does not transport, and Hirahara's only conditional gap problem
(Proposition 6.2) is a *weaker* promise problem carrying the computational depth of the conditioning
string inside its yes-side. Both failures are moot: **Kabanets–Kolokolova Theorem 3.4 (§3.3, p. 21,
l. 1124) already proves (i) ⇒ symmetry of information for conditional `pK^t` directly**, for every
number of strings ℓ, with additive error `ℓ·O(log N) + δ(2N, 2t)`, with **no derandomization
assumption** and with the hypothesis being a natural property for conditional **K^t** (weaker than
for `pK^t`). Its proof is fully parametric in δ; KK25 only ever instantiate it at δ linear, because
that is what their Theorem 6.3 equivalence needs. Instantiated at **ℓ = 2, y = ε, δ(n,t) = O(log n)**
it delivers exactly the hypothesis `(H1)` of the paper's Proposition 2(a), hence **BEM_skew
pointwise**. So the worst-case problem *is* a hub for the forward direction, at logarithmic gap,
and B31's Gap 1 (largeness amplification) and Gap 2 (yes-side search) both disappear — for the
forward direction only. What does **not** follow is `(i) ⇒ H_pK`: there is no route, and B31.2's
`H_pK ⇒ (i)` still carries the average-over-y versus per-y largeness mismatch, so `H_pK` and `(i)` are
two **incomparable** sufficient conditions for `BEM_skew`, not a chain. The characterization question
therefore changes shape: from `BEM_skew ⇒? H_pK` to `BEM_skew ⇒? (i)`, which is verbatim
Kabanets–Kolokolova's §8 technical challenge, now pinned at *logarithmic* usefulness. Two
independent obstructions block that converse, with different accountings: KK25 Theorem 4.3 (block
partition: `Θ(n)` loss even at δ = 0, and it needs the *multi-string* chain rule, which two-string SoI
is not known to give — their fn. 2) and KK25 Appendix B (computational depth `O(n/log n)`, B31.5).

---

## 1. Item 1 — the KK25 objects, stated exactly

### Definition 2.11 (Natural Property for Conditional K^t), KK25 p. 12, l. 686, verbatim

> A natural property for conditional `K^t` on n-bit strings with usefulness `s(n,t)` is a predicate
> `P : {0,1}^* × {0,1}^* × 1^* → {0,1}` satisfying the following: For some polynomial p, we have for
> all large `n, m ∈ N` and `t ≥ p(n+m)` that
> 1. for all `x ∈ {0,1}^n` and `y ∈ {0,1}^m`, if `K^t(x | y) ≤ s(n,t)`, then `P(x, y, 1^t) = 1`, and
> 2. **for all** `y ∈ {0,1}^m`, `Pr_{x ∈ {0,1}^n}[P(x, y, 1^t) = 0] ≥ 1/2`.
>
> A BPP-computable natural property for conditional `K^t` is defined similarly to that for `K^t`
> above.

The "similarly" refers to Definition 2.10 (p. 12, l. 672): BPP-computable means a randomized
polynomial-time `A` with `Pr_A[A = 1] ≥ 0.9` on every compressible input, and
`Pr_x[Pr_A[A = 0] ≥ 0.9] ≥ 1/2`.

*Plain reading: a fast test that says "yes" on every string that has a short program given `y`, and
says "no" on at least half of all random strings — for every `y`, not on average over `y`.*

**Typing.** Definition 2.11 is for **conditional K^t**, deterministic. There is no separate KK25
definition of a natural property for conditional `pK^t`; every KK25 theorem in this area takes a
property for conditional `K^t` as its *hypothesis* and produces a `pK^t` statement as its
*conclusion*. Since `pK^t(x|y) ≤ K^t(x|y) + O(1)`, a property for `pK^t` would be the stronger object;
the brief asks for the `pK^t` version and the answer below needs only the `K^t` version, so **the
result proved here is stronger than briefed** on this axis.

**Largeness and usefulness required.** Largeness exactly `1/2` (per-`y`), usefulness `s(n,t)` a
parameter. Below we take `s(n,t) = n − δ(n,t)` with `δ` monotone non-decreasing (KK25's convention,
p. 12, l. 699).

### Definition 2.18 (Gap McpK^tP), KK25 p. 14, l. 807, verbatim

> For a polynomial τ and a function `δ : N × N → N`, define `Gap_{τ,δ} McpK^tP` as the following
> promise problem:
> `Π_yes = {(x, y, 1^s, 1^t) | pK^t(x|y) ≤ s}`,
> `Π_no  = {(x, y, 1^s, 1^t) | pK^{τ(t)}(x|y) > s + δ(|x|, t)}`.

*Plain reading: given a string, a helper string, a length budget and a time budget, say whether the
string has a short probabilistic program — you are allowed to be wrong when the truth sits inside a
window of width δ.*

### Lemma 2.15, KK25 p. 13, l. 733, verbatim

> If, for some polynomial τ and a function `δ : N → N`, `Gap_{τ,δ} McK^tP ∈ promise-P`, then there is
> a P-computable natural property for conditional `K^t(x|y)` on n-bit strings `x` with usefulness
> `s(n,t) = n − δ(n,t) − 2`.

Proof (read): run the gap algorithm at `s(n,t) = n − δ(n,t) − 2`; usefulness is `Π_yes`, largeness is
the counting bound `K(x|y) > n − 2` for half of `x`, **for every `y`**. Direction: worst-case algorithm
⇒ property. `K^t` throughout, both sides deterministic.

### Lemma 2.16, KK25 p. 14, l. 747, verbatim

> Assume that `E ⊄ io-SIZE[2^{o(n)}]`. If there is a P-computable natural property for conditional
> `K^t(x|y)` on n-bit strings `x` with usefulness `s(n,t) = n − δ(n,t)`, then for some polynomial τ,
> we have `Gap_{τ,δ'} McK^tP ∈ promise-P`, where `δ'(n,t) = δ(2n, 2t) + O(log(nt))`.

Proof (read): feed the direct-product generator `DP^k_x` into the property at conditioning `z ∘ y`,
with `k = σ + c log n + δ(2n,2t)`; if the property accepts `DP^k_x(z)` with probability ≥ 0.6 then by
Lemma 2.4 it is a distinguisher and `K^{p(t)}(x|y) ≤ k + O(log(nt)) = σ + δ'(n,t)`, so the instance is
not in `Π_no`. **Direction: property ⇒ worst-case algorithm. The statement is parametric in δ.** It
uses per-`y` largeness at the *adversarial* conditioning string `z ∘ y`, and it uses the derandomized
reconstruction Lemma 2.4 (which is where `E ⊄ io-SIZE` enters).

### Corollary 2.19, KK25 p. 14, l. 815, verbatim

> The following are equivalent:
> • For any `C > 1`, there is a polynomial τ such that `Gap_{τ,δ} McpK^tP ∈ promise-BPP`, for
>   `δ(n,t) ≤ n/C`.
> • For any constant `D > 1`, there is a BPP-computable natural property for conditional `K^t(x|y)`
>   on n-bit strings `x` with usefulness `s(n,t) = n − n/D`.
>
> *Proof sketch.* By similar arguments, we can prove analogs of Lemma 2.15 and Lemma 2.16 for the
> case of `Gap_{τ,δ} McpK^tP` and BPP-computable natural properties for conditional `K^t`. For the
> analog of Lemma 2.16, we do not assume `E ⊄ io-SIZE[2^{o(n)}]`, and use Lemma 2.5.

**What it delivers and what it does not.** Corollary 2.19 is stated **only at linear gap**
`δ ≤ n/C` and linear usefulness `n − n/D`, and its proof is a sketch. It is **not** the parametric
statement. The parametric statement is Lemma 2.16, which at `δ(n,t) = O(log n)` gives
`δ'(n,t) = O(log n) + O(log(nt)) = O(log(nt))` — a **logarithmic** gap. The linearity in Corollary 2.19
is an artifact of the instantiation KK25 needed for their Theorem 6.3, not a limit of the method.
Both `characterization_attempt.md` §1 and `b31_instance_checkers.md` §4.2 cited Corollary 2.19 /
Theorem 6.3 and recorded the gap as linear; that reading was correct about the corollary and
misleading about the machinery. **Correction, logged in §7 below.**

Reading-status note: `Gap_{τ,δ}McpK^tP` is for **conditional pK^t**; the natural properties in
Definitions 2.10/2.11 are for `K^t` and conditional `K^t`; Lemma 2.15 and Lemma 2.16 are both entirely
in the deterministic `K^t` world; only Corollary 2.19 (sketch) and Theorem 3.4 (full proof) cross into
`pK^t`.

---

## 2. Item 2 — Hirahara Theorem 8.2, the proof of 1 ⇒ 2, and what transports

### Theorem 8.2, Hirahara p. 26:32, l. 1944, verbatim (all items)

> Assume that `E ⊄ i.o.SIZE(2^{εn})` for some constant `ε > 0`. In the following list, we have
> `1 ⟺ 2 ⟹ 3 ⟹ 4` and `3 ⟹ 5`.
> 1. `GapMINKT ∈ P`.
> 2. For every `D ∈ PSamp`, there exists a polynomial `t_0` such that `(K^t(-), D) ∈ AvgP` for every
>    polynomial `t ≥ t_0`.
> 3. `SoI` holds.
> 4. For every `D ∈ PSamp`, there exists a polynomial `t_0` such that `(K^t(-), D) ∈ HeurP` for every
>    polynomial `t ≥ t_0`.
> 5. `Gap_τ MINKT ∈ DTIME(2^{O(n/log n)})` for some function `τ(n,t) = 2^{O(n/log n)}`.

Definition 8.1 (p. 26:32, l. 1921): an *errorless heuristic scheme* for `K^t(-)` w.r.t. `D` outputs
`K^{t(n)}(x)` or `⊥` on every `x ∈ supp(D_n)`, fails with probability ≤ δ, runs in `poly(n/δ)`. Note:
it outputs the **value**, not a decision, and it is for **unconditional** `K^t`.

### The proof of 1 ⇒ 2 (Hirahara p. 26:35, l. 2137, verbatim)

> The implication from Item 2 to 1 is proved in [33]. **Theorems 4.1 and 8.6 prove the implication
> from Item 1 to 2.**

So `1 ⇒ 2` is the composite `GapMINKT ∈ P →[Thm 4.1] SoI`, then `SoI + GapMINKT ∈ P →[Thm 8.6]`
errorless scheme.

**Theorem 4.1** (p. 26:15, l. 858): *If `GapMINKT ∈ P` and `E ⊄ i.o.SIZE(2^{εn})` then SoI holds.* Its
proof (ll. 872–960) uses (a) **Fact 3.4** (p. 26:15, l. 834): `GapMINKT ∈ P` iff there is a
polynomial-time `K̃` and a polynomial `p` with `K^{p(t)}(x) − log p(t) ≤ K̃(x,1^t) ≤ K^t(x)` for every
`x` and every `t ≥ |x|`; and (b) **Lemma 2.2** (p. 26:9, l. 508), the *deterministic* reconstruction
for `DP_k`, which is stated under `E ⊄ i.o.SIZE(2^{εn})` and outputs a bound on `K^{p(ns/ε)}(x | D)`.

**Theorem 8.6** (p. 26:34, l. 2053): *If SoI holds and `GapMINKT ∈ P`, then for every `D ∈ PSamp`
there exist a polynomial `t` and an errorless heuristic scheme for `K^t(-)` w.r.t. `D`.* Its proof
uses three things:
- **Lemma 8.3** (p. 26:33, l. 1976), from Longpré–Watanabe: *If SoI holds, then there exist a
  polynomial `p` and a polynomial-time algorithm `M` such that for every `x` and every `t ≥ p(|x|)`
  such that `cd^{t,p(t)}(x) ≤ k`, on input `(x, 1^t, 1^{2^k})`, `M` outputs **the lexicographically
  first program of length `K^t(x)`** that outputs `x` in time `t`.* The proof enumerates all programs
  of length `≤ k + log q(t)` **taking `x` as input**, in time `poly(|x|, t, 2^k)`.
- **Lemma 8.4** (p. 26:33, l. 2016), cited to Hirahara STOC 2021: *If SoI holds, then for every
  `D ∈ PSamp` there is a polynomial `t` with `Pr_{x∼D_n}[cd^{t(n)}(x) > k] ≤ 2^{−k + log t(n)}`* — an
  **exponential** tail on computational depth over a samplable distribution.
- **the checker `C` of Lemma 7.5** (p. 26:29, l. 1752), which estimates `cd` using the `K̃` of Fact
  3.4; this is the **only** place `GapMINKT ∈ P` is consumed inside Theorem 8.6, and it is what turns
  the error-prone scheme of Theorem 8.5 into an errorless one.

### Where each of (a), (b), (c) is used, and whether it survives

**(a) The derandomization assumption `E ⊄ i.o.SIZE(2^{εn})`.** It enters at exactly one place:
Lemma 2.2, inside the proof of Theorem 4.1. **It drops.** GKLO22's Lemma 22 (p. 16:20, l. 1179) is
the same reconstruction with no assumption, at the price of concluding `pK^{Õ(t_D)·p_DP(n/ε)}(x|β) ≤
k + log p_DP(n t_D/ε)` instead of a `K^t` bound; KK25's Lemma 2.5 (p. 11, l. 608) is the same lemma in
their notation, and Remark 2.6 (l. 616) states the trade explicitly: the extra `t_D` dependence in
Lemma 2.4 "is due to the derandomization of a distinguisher `D` and the Goldreich–Levin list-decoding
algorithm … using the PRG from Theorem 2.2". GKLO22 say it in their own words (p. 16:9, l. 501, and
Remark 52, p. 16:43, l. 2755): *"For the Hadamard decoding step, we cannot derandomize the
Goldreich-Levin algorithm as we no longer have a PRG … Leaving randomness in, we now get an upper
bound on `pK^t(w)` … On the positive side, no average-case easiness assumptions are now needed for
this step."* and *"by using the probabilistic time-bounded Kolmogorov complexity measure `pK`, we
forgo the need for a PRG within the DPG reconstruction lemma."*

**(b) The deterministic nature of `K^t`.** Two uses, one benign and one fatal.
- *Benign:* Fact 3.4's `K̃` and Lemma 7.5's checker. Both transport: KK25 Lemma 2.14 (p. 13, l. 719)
  is the same sandwich equivalence for conditional `K^t`, and its proof (a binary/linear search on
  `s`) is measure-agnostic — it works verbatim for `Gap_{τ,δ}McpK^tP` and gives a poly-time `p̃K` with
  `pK^{τ(t)}(x|y) − δ ≤ p̃K(x,y,1^t) ≤ pK^t(x|y)`. **[Inference]**, since KK25 state Lemma 2.14 only
  for `K^t`.
- *Fatal:* **Lemma 8.3**. Its object is "the lexicographically first program of length `K^t(x)` that
  outputs `x` in time `t`", a single string `d_{x,t}`, and SoI is applied to the pair `(d_{x,t}, x)`.
  `pK^t(x)` has **no such witness**: `pK^t_λ(x|y) ≤ s` means `Pr_{r}[K^t(x | r, y) ≤ s] ≥ λ`, and the
  length-`s` program may be a different string for each `r` (GKLO22 p. 16:10, l. 528: *"the `pK^t`
  definition resembles the definition of AM, where Merlin provides a Kolmogorov description of a
  given string, **based on Arthur's randomness**"*). One can try to search for `d_{x,t,r}` at a sampled
  `r`, but then the SoI one needs is symmetry of information for `K^t(· | r)` at a random `r`, which
  is not what SoI for `pK^t` says. **No transport in the texts, and no obvious repair.** This is the
  step that kills (ii) ⇒ (iii) as briefed.

**(c) The unconditional (no `y`) nature of the problem.** Theorem 8.2 is entirely about
`GapMINKT` and `K^t(-)` with no conditioning string. Hirahara's only conditional version is
**Proposition 6.2** (p. 26:21, l. 1248): *Assume SoI holds. If `GapMINKT ∈ P` then there is a
polynomial τ with `Gap_τ MINcKT ∈ P`* — where `Gap_τ MINcKT` (p. 26:21, l. 1240) has
`Π_yes = {(x,y,1^t,1^s) : K^t(x|y) ≤ s − cd^{t,τ(|x|,|y|,t)}(y)}`. **The yes-side is weakened by the
computational depth of the conditioning string.** That is strictly weaker than KK25's
`Gap_{τ,δ}McK^tP`, whose yes-side is `K^t(x|y) ≤ s` outright. So even granting (b), Hirahara's
machinery does not deliver a conditional gap problem of the KK25 shape, and `Gap McpK^tP` from
Corollary 2.19 is not the hypothesis Theorem 8.2 item 1 asks for.

**One piece that does transport, and is worth recording.** Lemma 8.4's role — "depth is small on
samplable inputs" — has an **unconditional** `pK^t` analogue: GKLO22 **Lemma 60** (p. 16:48, l. 3084),
*Small Probabilistic Sampling Depth for Samplable Distributions*:
`E_{x∼D^m_n}[pK^t(x) − pK^{t'}(x)] ≤ O(log m + log T(n) + a(n) + log t')`, proved from the
**unconditional** source coding theorem for `pK^t` (their Lemma 24, p. 16:22, l. 1307:
`pK^{p(T(n))}(x) ≤ log(1/D_n(x)) + O(log T(n)) + a(n)`). No SoI, no derandomization. But Lemma 60 is in
**expectation**; Hirahara's Lemma 8.4 is an **exponential tail**, and Markov from an `O(log t)`
expectation gives only `Pr[depth > k] ≤ O(log t)/k`, which is not enough for a heuristic *scheme*
(`k = O(log(n/δ))` at failure δ). **[Inference]** the exponential tail is nevertheless available:
for fixed `r`, `#{x : K^{t'}(x|r) ≤ s} < 2^{s+1}`, so
`D({x : K^{t'}(x|r) ≤ log(1/D(x)) − k}) ≤ (n + O(1))·2^{−k}`; averaging over `r` and Markov gives
`Pr_{x∼D}[pK^{t'}(x) < log(1/D(x)) − k] ≤ (3/2)(n+O(1))2^{−k}`, and combining with Lemma 24 gives
`Pr_{x∼D}[pK^{p(T)}(x) − pK^{t'}(x) > k + O(log T)] ≤ poly(n)·2^{−k}`. This is my derivation, not in
any of the three texts; it is labelled and goes on the audit list. It is not load-bearing below.

---

## 3. Item 3 — the gap-matching, precisely

| object | gap | source |
|---|---|---|
| Hirahara `Gap_τ MINKT`, Theorem 8.2 item 1 | `Π_no : K^{τ(\|x\|,t)}(x) > s + **log τ(\|x\|,t)**` — **additive logarithmic** | Def 3.3, p. 26:14, l. 824 |
| KK25 Corollary 2.19 | `δ(n,t) ≤ n/C` — **linear** | p. 14, l. 815 |
| KK25 Lemma 2.16 (parametric) | `δ'(n,t) = δ(2n,2t) + O(log(nt))`; at `δ = O(log n)`, `δ' = O(log(nt))` — **logarithmic** | p. 14, l. 747 |

**Answer to the question as posed.** The `1 ⇒ 2` step of Theorem 8.2 needs a **log**-gap hypothesis:
`GapMINKT ∈ P` means `Gap_τ MINKT ∈ P` for some polynomial τ, and the gap is `log τ`, logarithmic. A
*linear*-gap algorithm does **not** satisfy it: Fact 3.4's sandwich would become
`K^{p(t)}(x) − n/C ≤ K̃ ≤ K^t(x)`, and every counting step in Theorem 4.1 (e.g. the threshold
`θ := |w| + |w'| − 2 − log p(t')`, l. 906) would lose `2^{n/C}`, which is fatal.

**But the chain does not fail there,** because Corollary 2.19's linearity is not forced. Its
underlying Lemma 2.16 is parametric, and at usefulness `n − O(log n)` it delivers `δ' = O(log(nt))`.
So **(i) ⇒ (ii) at logarithmic gap is available** — modulo the caveat that KK25 give only a proof
*sketch* for the `pK^t`/BPP analogue (Corollary 2.19), and that sketch has one substantive point
which their Theorem 3.4 handles explicitly and which I checked there: on the yes-side the `pK^t`
random string `r` must be absorbed into the property's conditioning string, because Equation (6) of
Lemma 2.16 (`K^{2t}(DP^k_x(z) | z,y) ≤ K^t(x|y) + c log n`) is a statement about **deterministic**
`K^t`. Theorem 3.4's proof does exactly this (l. 1155: "by the definition of `pK^t`, this means that,
for at least 2/3 of random strings `r ∈ {0,1}^{2t}`, `K^{2t}(… | r, y, z_1,…,z_ℓ) ≤ σ`", and then `A`
is applied at conditioning `r ∘ y ∘ z_1 ∘ … ∘ z_ℓ`).

**So the chain fails at (ii) ⇒ (iii), not at (i) ⇒ (ii)** — and for the reasons in §2(b)/(c), not for
a gap reason.

---

## 4. Item 4 — (iii) ⇒ (iv): what `L` actually is, and whether a `pK^t` scheme decides it

GKLO22's language (proof of Lemma 26 Item 1, p. 16:22, l. 1352):

    L := {(u, v, w, w', 1^s) | ∃ M ∈ {0,1}^s, M(w, w') prints uv in |w| steps, and s = |u|+|v|−10}

with `D` uniform on `u ∼ U_{nk+k}`, `v ∼ U_{mk'+k'}`, `w ∼ U_{2t}`, `w' ∼ U_τ`.

**Exactly which object `L` is.** `M` is a **deterministic** program taking `(w, w')` on its input
tapes and running for `|w| = 2t` steps. So

    L(u,v,w,w',1^s) = 1  ⟺  K^{2t}(uv | w, w') ≤ s.

*It is conditional `K^t` at time `2t`, with the drawn random string `w` and the conditioning string
`w'` both on the conditioning tape.* The `pK` value is the **probability of this event over `w`**:
by GKLO22's own definition (p. 16:9, l. 553, "`pK^t_λ(x|y) ≤ s` if and only if
`Pr_{r∼{0,1}^t}[K^t(x|r,y) ≤ s] ≥ λ`", with the random string on a separate input tape),

    pK^{2t}(uv | w') ≤ s  ⟺  Pr_w[ L(u,v,w,w',1^s) = 1 ] ≥ 2/3,

which is precisely the step GKLO22 take at l. 1470. So: **`L` is neither "pK^t of the pair given `w'`"
nor "`K^t` relative to a fixed `w`" in the loose sense — it is the inner deterministic event whose
`w`-probability is the conditional `pK^t`.** B31's typing remark (§4.1: "`L` quantifies over
deterministic programs `M`, so B31.2 produces a natural property for conditional `K^t`, not for
`pK^t`") is confirmed exactly.

**Does an errorless scheme for `pK^t(x|y)` decide `L`?** **No, not per-`w`.** Knowing
`pK^{2t}(uv | w')` tells you the threshold at which the `w`-probability crosses 2/3; it says nothing
about the particular `w` in the instance. `L` is decided by an errorless scheme for *conditional
`K^t`* on the samplable distribution over pairs `(uv, w ∘ w')`, which is a different (and, by
`pK ≤ K + O(1)`, stronger) object than the one (iii) supplies.

**[Inference] But an errorless scheme for conditional `pK^t` does substitute for `B` inside
GKLO22's proof**, which is what the chain actually wants. Define
`B̃(u, v, w', 1^s) := 1` iff the scheme's output on `(uv, w')` is `≤ s` or `⊥` (the one-sided
conversion of their Lemma 6, p. 16:13, l. 717). Then:
- *yes-side*: if `pK^{2t}(uv|w') ≤ s` then `B̃ = 1` (errorlessness), which is all the final step needs
  (l. 1452: "if for all `z, z'`, `Pr_w[… ∈ L] ≥ 2/3` then `Pr[B = 1] ≥ (2/3)(1 − 1/n)`" becomes an
  equality-free implication);
- *counting*: GKLO22's `Pr[(u,v,w,w',1^s) ∈ L] ≤ 2^{−10}` (l. 1400) is replaced by GKLO22's Lemma 2.1
  (probabilistic incompressibility, KK25 p. 10, l. 568):
  `Pr_{u,v}[pK^{2t}_{2/3}(uv | w') ≤ |uv| − 10] ≤ 3·2^{−10}`. The constant 3 changes `2^{−10} + 3/n` to
  `3·2^{−10} + (failure)`, and Markov still gives ≤ 1/10 for 9/10 of `w'`;
- *hybrid*: `B̃` is a randomized poly-time algorithm with advice `(v, w', 1^s)`, so Lemma 22 applies
  unchanged.
So (iii) ⇒ "GKLO22 Lemma 26(1) holds" **[Inference]**, even though (iii) ⇏ (iv) literally. Since the
paper's Proposition 2(a) consumes only the Lemma-26 inequality, this is enough for `BEM_skew` — but
it is a *different* statement from `H_pK`, and §5 shows it is not needed at all.

**Secondary [Inference], recorded and not load-bearing.** The same substitution works with a
**worst-case** `Gap_{τ,δ}McpK^tP ∈ promise-BPP` algorithm in place of `B`, if the threshold constant
`10` in `s = |u|+|v|−10` is replaced by `C log(nt)` for a large constant `C`: the counting bound
becomes `Pr[pK^{τ(2t)}(uv|w') ≤ s + δ] ≤ 3·2^{−(C log(nt) − δ)}`, small for `δ = O(log(nt))` and `C`
large; off-promise instances are exactly the ones this bound covers; and the conclusion is SoI for
`pK^t` with an extra additive `O(log(nt))`, which the paper's `(H1)` already tolerates. *This confirms
B31's guess that the worst-case problem is the hub, by a route that does not use Hirahara at all.*
It is superseded by §5, which cites a published theorem instead.

---

## 5. The finding: (i) ⇒ BEM_skew, directly, at logarithmic error

### KK25 Theorem 3.4 (§3.3, p. 21, l. 1124), verbatim

> **Theorem 3.4 (Chain Rule for Conditional `pK^t`).** Suppose that there is a BPP-computable natural
> property `A` for conditional `K^t` on n-bit inputs with usefulness `s(n,t) = n − δ(n,t)`. Then there
> exist constants `c_0, c_1 ∈ N` such that for all sufficiently large `x_1, …, x_ℓ ∈ {0,1}^*`, for any
> `ℓ ∈ N`, for every `y ∈ {0,1}^*`, and for every `t ≥ (N + |y|)^{c_0}`, where `N = Σ_{i=1}^ℓ |x_i|`,
> we have
>
>     pK^t(x_1, …, x_ℓ | y) ≥ Σ_{i=1}^ℓ pK^{t^{c_1}}(x_i | y, x_1, …, x_{i−1}) − ℓ·O(log N) − δ(2N, 2t).

Its preamble (l. 1119): *"The difference from Theorem 3.3 above is that (1) **no circuit lower bound
for E (derandomization assumption) is needed**, and (2) a natural property for conditional `K^t` can
be BPP-computable (rather than P-computable)."*

**The proof is fully parametric in δ** (read in full, ll. 1130–1215). The only places δ appears are
`s := M − δ(M, 2t)` with `M = Σk_i ≤ 2N`, and the final accounting. The engine is: the property
rejects `U_{k_1}∘…∘U_{k_ℓ} ∘ r ∘ y ∘ z_1 ∘…∘ z_ℓ` with probability ≥ 0.45 **for every** `r, y, z`
(per-conditioning largeness, Definition 2.11(2)); if `σ ≤ s` it accepts the DP-generator hybrid with
probability ≥ 0.6; the `ℓ`-step hybrid argument then hands a `0.05/ℓ`-distinguisher to **Lemma 2.5**
(the derandomization-free `pK^t` reconstruction), giving
`pK^{q(t)}(x_i | y, x_1,…,x_{i−1}) ≤ k_i + O(log N)`; setting `k_i` just below that forces `σ > s`.

### Proposition B36.1

**Label: Proved-conditional** on KK25 Theorem 3.4 as read, plus the Definition-2.11 time-parameter fix
of §6 below.

Let `A` be a BPP-computable natural property for conditional `K^t` in the sense of KK25 Definition
2.11, with usefulness `s(n,t) = n − δ(n,t)` for some `δ(n,t) = O(log n)` and largeness `1/2`. Then:

**(a)** There are constants `c_0, c_1` such that for every `x, y ∈ {0,1}^n` and every
`t ≥ (2n)^{c_0}`,

    pK^t(x, y) ≥ pK^{t^{c_1}}(x) + pK^{t^{c_1}}(y | x) − O(log n).

*Plain reading: describing the pair costs at least as much as describing the first string and then
the second given the first, up to a logarithmic slack, when the two parts are given polynomially more
time.*

**(b)** Hence `(H1)` and `(H2)` of the proof of the paper's Proposition 2(a) hold with
`p(t) := t^{c_1}` and loss `O(log n) ≤ O(log s)`, and therefore **`BEM_skew` holds pointwise**, with
the bounds of Proposition 2(a): `Σ⁺_{s,P}(x,y) ≤ O(log s)` and `Σ⁻_{s,P}(x,y) ≤ O(log s)` for all
`s ≥ p_0(n)` and every pair, hence `E_D[2^{Σ^±}] ≤ s^{O(1)}` under **every** distribution on pairs.

**Proof.** (a) is KK25 Theorem 3.4 at `ℓ = 2`, `y = ε`, `x_1 = x`, `x_2 = y`, `N = 2n`, and
`δ(n,t) = O(log n)`, so that `δ(2N, 2t) = O(log N) = O(log n)` and `ℓ·O(log N) = O(log n)`; the total
error is `O(log n)`. Apply it also with the roles of `x` and `y` exchanged to get the mirror
inequality. (b) is the derivation inside the paper's proof of Proposition 2(a), which consumes only
`(H1)`, `(H2)` and Lemma 11/Lemma 4; the source of `(H1)` is irrelevant to it. ∎

**Three things this buys, all from B31's own list.**
1. **Largeness `1/2` suffices.** Theorem 3.4 takes Definition 2.11 as given; no amplification from
   `1/2` to `1 − 1/poly` is needed anywhere. **B31's Gap 1 is gone (forward direction).**
2. **The property is used only as a distinguisher, never to supply yes-answers.** Its accepting side
   is used to derive a *contradiction*, and its rejecting side is used on uniform strings.
   **B31's Gap 2 is gone (forward direction).**
3. **No derandomization, and the hypothesis is the weaker `K^t` property.** The brief asked for a
   property for conditional `pK^t`; Theorem 3.4 needs only one for conditional `K^t`, which is
   implied by it since `pK^t ≤ K^t + O(1)`. So the result is stronger than briefed on that axis.

### What this does *not* do

`(i) ⇒ H_pK` is **not** established, and no route to it appeared. `H_pK ⇒ (i)` is B31.2, which still
carries the mismatch B31 identified (an errorless scheme for `(L, D)` gives largeness only on average
over `(w, w')`, while Definition 2.11(2) demands it for every conditioning string). **So `H_pK` and
`(i)` are two incomparable sufficient conditions for `BEM_skew`, not a chain**, and the sandwich in
the paper's §7.6 gains a second, parallel top rather than a lower one:

    DistNP ⊆ AvgBPP  ⇒  H_pK      ⇒  BEM_skew  ⇒  no io-OWF
    (i) BPP nat. prop. for cond. K^t at n − O(log n)  ⇒  BEM_skew            [Prop. B36.1]

---

## 6. The Definition 2.11 time-parameter wrinkle (flagged, with a fix)

In Theorem 3.4's proof the property `A` is invoked as `A(−, 1^{2t})` at input length `M` with
conditioning string `r ∘ y ∘ z_1 ∘ … ∘ z_ℓ` of length `m' ≥ |r| = 2t`. Definition 2.11 requires the
time parameter to satisfy `t ≥ p(n + m)` for the property's polynomial `p` — here `2t ≥ p(M + m')`
with `m' ≥ 2t`, which is impossible for any `p(x) ≥ x + 1`. The same wrinkle is inherited by KK25's
own Theorem 6.3, which composes Theorem 3.4 with Theorem 4.3.

**[Inference] Fix.** Invoke `A` at time parameter `t'' := p(M + m')` instead of `2t`. The yes-side
survives because `K^{t''}(· | r,y,z) ≤ K^{2t}(· | r,y,z)` whenever `t'' ≥ 2t`, which holds since
`p(x) ≥ x`; the largeness side is unaffected (it is a counting statement for every time parameter);
Lemma 2.5's conclusion picks up `t''` in place of `2t` inside its polynomial, which stays polynomial
in `t` since `m' = poly(t, N)`; and `δ(M, t'') = δ(M, 2t)` for any δ that depends on its first argument
only, which is the case for `δ(n,t) = O(log n)` as well as for KK25's own `δ(n,t) = n/C`.

**The wrinkle does not discriminate the logarithmic instance from KK25's linear one.** It is a
convention issue about how Definition 2.11's `t ≥ p(n+m)` interacts with a conditioning string whose
length is itself tied to `t`, and it bites Theorem 6.3 exactly as much as it bites Proposition B36.1.
It goes on the audit list.

---

## 7. The converse, and the two obstructions (do not merge them)

The characterization question is now `BEM_skew ⇒? (i)`. KK25 have **two** routes from a symmetry-of-
information statement to a natural property, and both are stuck, with **different accountings**.

**Obstruction A — the block partition (KK25 Theorem 4.3, §4.2, p. 23, l. 1298; read with proof).**
From the chain rule for conditional `pK^t` with error `δ(2n,2t)`, partition `x` into `ℓ` blocks of
length `n/ℓ`, brute-force `pK^{poly(t)}` on one block by random sampling in time `2^{n/ℓ}·poly(t)`.
Polynomial time forces `n/ℓ = O(log t)`, i.e. `ℓ = n/(c log t)`. The resulting usefulness (l. 1370) is

    s(n,t) ≤ n − 2ℓ·log ℓ − ℓ·O(log n) − δ(2n, 2t),

and with `ℓ = n/(c log t)` the middle two terms alone are `Θ(n/c)`. **Even at `δ = 0` the loss is
linear in `n`.** So this route cannot produce usefulness `n − O(log n)` regardless of how good the
input chain rule is. Two further requirements: it needs the chain rule for **super-constant ℓ**, and
KK25 state (p. 2, l. 168 and fn. 2) that *"for super-constant ℓ, unlike in the time-unbounded case of
`K`, SoI for `K^t` (the chain rule for two strings) does not seem to imply the multi-string chain rule
by induction on ℓ … The reason is a polynomial blowup in the time bounds for `K^t` on the right-hand
side of SoI after each inductive step."* `BEM_skew` is a **two-string** statement. So Obstruction A is
two obstructions stacked: linear loss, and two-string ⇏ multi-string.

**Obstruction B — the computational depth term (KK25 Appendix B; B31.5).** The other route gets a
natural property from SoI via Hirahara's computational depth lemma, and stops at
`2^{O(n/log n)}`-time at a superpolynomial instance-dependent time bound `t* ≤ 2^{n^ε}`, because the
depth bound is `O(n/log n)`. B31.5 argues (by analogy with Hirahara's Remark 6.4) that improving that
depth term to `O(log n)` is relativization-barred.

**These are not the same wall.** Obstruction A's `Θ(n)` comes from `ℓ` blocks × `O(log t)` error each,
an accounting internal to the partition; Obstruction B's `O(n/log n)` comes from the telescoping
average over time bounds (GKLO22 Lemma 31, p. 16:29, l. 1780, and KK25 Lemma B.1). They land at the
same order of magnitude by different routes, and B31.5's relativization argument attaches to B, not to
A. **A proof of `BEM_skew ⇒ (i)` at logarithmic usefulness must beat both, or find a third route.**
Recording them as one wall would be wrong; I am not asserting that the relativization barrier applies
to Obstruction A, because the block-partition loss is an algorithmic accounting and no oracle argument
was found for it.

---

## 8. The step table

`c-K^t` = conditional `K^t`; `c-pK^t` = conditional `pK^t`. "Needed after Thm 3.4?" asks whether the
step is still required once Proposition B36.1 is in hand.

| # | step | source (page, line) | needs derandomization? | needs deterministic `K^t`? | needs no conditioning string? | survives `pK^t` + `y`? | needed after Thm 3.4? |
|---|---|---|---|---|---|---|---|
| 1 | (i) ⇒ (ii), parametric | KK25 Lemma 2.16 (p. 14, l. 747) | **yes**, via Lemma 2.4 | in the conclusion only | no — it is conditional throughout | **yes** — Cor 2.19 / Lemma 2.5 remove the derandomization; yes-side needs `r` absorbed into the conditioning (done in Thm 3.4) | no |
| 1′ | (i) ⇒ (ii), as KK25 state it | KK25 Cor 2.19 (p. 14, l. 815) | no | hypothesis is a `c-K^t` property | no | yes, but **linear gap only**, and proof is a sketch | no |
| 2 | (ii) ⇒ SoI | Hirahara Thm 4.1 (p. 26:15, l. 858) via Fact 3.4 + Lemma 2.2 | **yes**, via Lemma 2.2 | Fact 3.4's `K̃` is `K^t` | **yes** — `GapMINKT` is unconditional | Lemma 2.2 → GKLO Lemma 22 [ok]; Fact 3.4 → KK25 Lemma 2.14 analogue **[Inference]**; conditional version only as Prop 6.2 with a depth term in `Π_yes` | no |
| 3 | SoI ⇒ error-prone scheme | Hirahara Thm 8.5 (p. 26:33, l. 2022) via Lemma 8.3 + Lemma 8.4 | no | **yes — Lemma 8.3 needs the lex-first shortest program** | yes | **NO** — `pK^t` has no single witness program (GKLO22 p. 16:10, l. 528) | no |
| 4 | + `GapMINKT ∈ P` ⇒ errorless scheme (= (ii) ⇒ (iii)) | Hirahara Thm 8.6 (p. 26:34, l. 2053) via Lemma 7.5's checker | inherits step 2's | inherits step 3's | yes | **NO**, inherits step 3's failure; and the checker would need a conditional gap problem Hirahara does not have | no |
| 4a | depth is small on samplable inputs | Hirahara Lemma 8.4 (p. 26:33, l. 2016) | no (but assumes SoI) | yes | yes | **partly** — GKLO22 Lemma 60 (p. 16:48, l. 3084) is the unconditional `pK^t` analogue, but in **expectation**; the exponential tail is **[Inference]**, §2 | no |
| 5 | (iii) ⇒ (iv) = decides `L` | GKLO22 proof of Lemma 26(1) (p. 16:22, l. 1352) | no | `L` **is** a `c-K^t` event; `pK` is its `w`-probability | no | **does not decide `L` per-`w`**; **does** substitute for `B` in the Lemma-26 proof **[Inference]**, §4 | no |
| 6 | **(i) ⇒ SoI for `c-pK^t` at `O(log)` error** | **KK25 Thm 3.4 (p. 21, l. 1124)** | **no** | hypothesis is a `c-K^t` property; conclusion is `c-pK^t` | no | **yes — this is the transport, already published** | **this is the step** |
| 7 | SoI for `pK^t` ⇒ `BEM_skew` | paper Prop. 2(a) | no | no | n/a (paper uses `y = ε`) | yes | yes |
| 8 | converse: SoI ⇒ (i) | KK25 Thm 4.3 (p. 23, l. 1298) | no | no | no | yes, but **`Θ(n)` loss even at `δ = 0`**, and needs multi-string ℓ | **open — Obstruction A** |
| 8′ | converse via depth | KK25 App. B (Thm B.2, Lemma B.1) | no | yes | yes | `2^{O(n/log n)}` only | **open — Obstruction B** |

---

## 9. Item 5 — verdict

**No, the briefed chain does not go through, and the question it was asking is answered anyway by a
route that skips it.** Step (ii) ⇒ (iii) fails, for two independent reasons that have nothing to do
with the gap: Hirahara's Theorem 8.2 item 1 ⇒ item 2 is the composite of Theorem 4.1 and Theorem 8.6,
and Theorem 8.6 runs through **Lemma 8.3**, whose object is the lexicographically first shortest
*deterministic* program for `x` — an object `pK^t` does not have, since its program may differ for
each random string — while Hirahara's only conditional gap problem, Proposition 6.2's
`Gap_τ MINcKT`, weakens its yes-side by the computational depth of the conditioning string and so is
not the `Gap McpK^tP` that Corollary 2.19 supplies; the derandomization assumption, by contrast,
drops cleanly (it enters only through Lemma 2.2 inside Theorem 4.1, and GKLO22's Lemma 22 / KK25's
Lemma 2.5 replace it with no assumption, exactly as GKLO22 say in Remark 52). The gap question itself
comes out in our favour and was a red herring: Hirahara's `GapMINKT` gap is *logarithmic* (`log τ`,
Definition 3.3), KK25's Corollary 2.19 is *linear*, but Corollary 2.19's linearity is an artifact of
the instantiation KK25 needed for Theorem 6.3 — the underlying **Lemma 2.16 is parametric in δ** and
at usefulness `n − O(log n)` delivers `δ' = O(log(nt))`, a logarithmic gap. None of this is needed,
because **Kabanets–Kolokolova Theorem 3.4 already proves the whole forward direction in one step**:
a BPP-computable natural property for conditional `K^t` with usefulness `n − δ(n,t)` implies the chain
rule for conditional `pK^t` for every `ℓ` with error `ℓ·O(log N) + δ(2N,2t)`, with no derandomization
assumption, and its proof is parametric in δ; at `ℓ = 2`, `y = ε`, `δ = O(log n)` it is exactly the
hypothesis `(H1)` that the paper's Proposition 2(a) consumes, and hence gives **`BEM_skew`
pointwise** (Proposition B36.1, **Proved-conditional** on Theorem 3.4 as read plus the Definition-2.11
time-parameter fix of §6). Largeness `1/2` suffices and the property is used only as a distinguisher,
so B31's Gap 1 and Gap 2 both vanish **in the forward direction**; the hypothesis needed is the
*weaker* `K^t` property rather than the `pK^t` one the brief asked for. But this is **not**
`(i) ⇒ H_pK`: no route to `H_pK` from `(i)` appeared, `H_pK ⇒ (i)` (B31.2) still carries the
average-over-`y` versus per-`y` largeness mismatch, and so `H_pK` and `(i)` are two **incomparable**
sufficient conditions for `BEM_skew` rather than a chain — the paper's sandwich gains a second,
parallel top, it does not lower the existing one. The characterization question accordingly changes
from `BEM_skew ⇒? H_pK` to `BEM_skew ⇒? (i)`, which is Kabanets–Kolokolova's §8 technical challenge
verbatim, now pinned at *logarithmic* usefulness; and that converse is blocked by **two** obstructions
that must not be merged — Theorem 4.3's block partition, which loses `Θ(n)` even at `δ = 0` and needs
a multi-string chain rule that two-string SoI is not known to give (their footnote 2), and Appendix
B's `O(n/log n)` computational depth term, which is the wall B31.5 identified. **The failure is
therefore not the same wall B31.5 named; B31.5's depth/relativization wall is one of two, and the
block-partition wall is new to this note and has no oracle argument attached to it.**

---

## 10. Corrections and audit list

**Correction (logged, per CLAUDE.md; earlier reports not edited).**
`characterization_attempt.md` §1 recorded KK25's contribution as "(Thm 6.3) the multi-string chain
rule for conditional `pK^t` **with error N/D** is equivalent to `Gap_{τ,δ}McpK^tP ∈ promise-BPP` for
`δ ≤ n/C'` — a *linear* gap", and §4 item 2 concluded that a linear-error moment bound would be needed
to make KK25's machinery apply. `b31_instance_checkers.md` §4.2 likewise cited Lemmas 2.15/2.16 and
Corollary 2.19 and recorded the gap as linear. **Both are correct about Theorem 6.3 and Corollary 2.19
and wrong about the machinery:** KK25 **Theorem 3.4** (one direction of Theorem 6.3) is parametric in
δ and, at `δ = O(log n)`, gives the two-string, logarithmic-error, conditional-`pK^t` symmetry of
information directly — the object `characterization_attempt.md` §1 described as living "in exactly the
regime they call missing". What is actually missing is only the **converse** at that regime.

**Audit list additions.**
1. The exponential tail on probabilistic sampling depth derived in §2 (Kraft-over-`r` from GKLO22
   Lemma 24) — **[Inference]**, my derivation, in none of the three texts. Not load-bearing.
2. The Definition 2.11 time-parameter wrinkle of §6 and the proposed fix — **[Inference]**. It affects
   KK25's own Theorem 6.3 equally. Worth a one-line check against the published version of KK25 if one
   appears.
3. The `pK^t` analogue of KK25 Lemma 2.14 (sandwich equivalence for `Gap McpK^tP`) — **[Inference]**;
   KK25 state Lemma 2.14 only for `K^t`. Used only in the step table, not in Proposition B36.1.
4. The worst-case shifted-threshold variant of GKLO22's Lemma 26 in §4 — **[Inference]**, secondary,
   superseded by Theorem 3.4.

## 11. Next threads (divergent round before converging)

1. **Ask whether Theorem 3.4 at `δ = O(log n)` also gives the same-time object.** Its RHS sits at
   `t^{c_1}`, so no — but the exponent `c_1` comes from Lemma 2.5's polynomial, and GKLO22's
   fine-grained track (Theorem 2, Remark 52) refines `poly(t)` to `Õ(t)`. A quasi-linear time skew is
   not the same-time object but is closer than anything in §7.2 of the paper.
2. **Attack Obstruction A directly.** The `2ℓ log ℓ + ℓ·O(log n)` loss in Theorem 4.3 is an accounting,
   not a barrier. Ask whether a non-uniform partition, or a partition into `O(1)` blocks with a
   different brute force, trades the `Θ(n)` for something sublinear. No oracle argument was found
   against it.
3. **Ask what `BEM_skew` gives that a chain rule does not.** `BEM_skew` is an exponential-moment
   statement over samplable pairs; Theorem 4.3 consumes a *pointwise worst-case* chain rule. The
   moment form may be the wrong input shape for the converse, and a distributional analogue of
   Theorem 4.3 (natural property from an average-case chain rule) is not in KK25.
4. **Unrelated field, for the divergent requirement:** the block-partition loss `ℓ·O(log t)` is exactly
   the per-symbol overhead of a block code, and the question "can `ℓ` blocks be decoded with `o(ℓ)`
   total overhead" is the rate/redundancy trade of a universal code. Whether any coding-theoretic
   construction (arithmetic coding, Lempel–Ziv parsing with a shared dictionary) removes the per-block
   `O(log t)` is not something any of the three papers considers.
5. **Write the paper edit.** §7.6 gains Proposition B36.1 as a second top, and §7.5's sharpened
   question becomes `BEM_skew ⇒? (i)`, with the two obstructions named separately.

Convergent pick: item 5 is bookkeeping and cheap; item 2 is the only one with a chance of moving the
converse, and it is a proof attempt, not a reading task. Item 3 is the reframing most likely to be
right and is untested.
