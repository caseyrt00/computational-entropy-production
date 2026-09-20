# Thread B37: attack on Obstruction A (the block partition), one bounded attempt

Date: 2026-09-15, Fable. Source read: Kabanets–Kolokolova 2025, Theorem 4.3 and its proof in full
(`pass16/sources/kk_eccc_tr25-089.txt`, from the line "Theorem 4.3." through eq. (23) and the choice of
`s(n,t)`). Brief: B36 called Obstruction A "an accounting, not a barrier, no oracle argument found".
Question: does the moment/average form of our hypothesis (BEM_skew: an exponential-moment bound on the
SoI defect for every samplable pair distribution) let a partition argument reach logarithmic usefulness,
i.e. a BPP natural property with usefulness `n − O(log n)`?

## Outcome in one paragraph

**No, and the reason is structural, not bookkeeping.** KK25's Theorem 4.3 converts a chain rule into a
natural property by cutting `x` into `ℓ` blocks, using the chain rule to find one block with a short
conditional description, and finding that description by brute force. Poly time forces the blocks to
have length `O(log t)`, so `ℓ = n / O(log t)`. Two costs are then unavoidable and each is linear in `n`
for polynomial `t`: (a) the union bound that makes a random string reject needs a margin of `2 log ℓ`
bits *per block*, `2ℓ log ℓ = Ω(n)` in total; (b) the chain rule's error is `O(log n)` per string,
`ℓ · O(log n) = Ω(n)` in total. Removing (b) entirely does not help: with zero chain-rule error, a string
compressible by only `O(log n)` bits has its saving spread over `ℓ` blocks as `O(log n)/ℓ` bits per
block, a fraction of a bit, which no block-local test can see against the `O(1)`-bit fluctuation of a
random block. **A logarithmic global saving cannot be localised to a block.** So every partition
argument with poly-time block search has usefulness `n − Ω(n / log t)` at best, and the `2^{O(n/log n)}`
of KK25's Appendix B is the same fact read from the other side (log-many blocks, exponential search).
Obstructions A and B are therefore one wall, not two; B36 was right that no oracle argument attaches to
A, and wrong that A is an accounting. The only escape from the partition is a *search algorithm* for
short descriptions of `Θ(n / log n)`-bit blocks, which is meta-complexity search — and an average-case
hypothesis of ours can supply worst-case-sound search only through a worst-case-to-average-case
reduction for MINKT of Hirahara's kind (FOCS 2018 [cited from memory; on the audit list]), whose
hypothesis is *errorless* average-case easiness. That is the errorless/error-prone gap of §7.5 again.
The moment form buys nothing here: Markov on `2^{Σ}` trades exceptional mass `2^{−k}` for defect `k`,
so worst-case control of the strings of complexity `≤ s` costs defect `≈ s`, which is vacuous. The
attempt is closed as a clean negative with the mechanism named.

## 1. The proof of Theorem 4.3, reduced to its two constraints

Given `x ∈ {0,1}^n` with `K^t(x | y) ≤ s`, cut `x = x_1 … x_ℓ` into blocks of length `n/ℓ`. The chain
rule (KK25 eq. (16) at error `ℓ · O(log n) + δ`) gives

    Σ_i pK^{poly(t)}(x_i | y, x_{<i})  ≤  s + ℓ · O(log n) + δ,

so by averaging some block has conditional description length `≤ S := (s + ℓ·O(log n) + δ)/ℓ`. The
algorithm finds it by brute force over all programs of length `≤ S ≤ n/ℓ`, cost `2^{n/ℓ} · poly(t)`.

*Plain reading: if the whole string is a little compressible, at least one small piece is, and small
pieces can be searched exhaustively.*

**Constraint C1 (poly time).** `2^{n/ℓ} ≤ poly(t)` forces `n/ℓ ≤ c log t`, i.e. `ℓ ≥ n / (c log t)`.

**Constraint C2 (largeness).** A random `z` must be rejected with probability `≥ 1/2`. The algorithm
accepts if *any* block is `S`-compressible, so all `ℓ` blocks must be incompressible at once; by KK25's
Lemma 2.1 a random block is `(n/ℓ − 2 log ℓ)`-compressible with probability `≤ 4/ℓ²`, and the union
bound over `ℓ` blocks gives failure `≤ 4/ℓ`. That requires `S ≤ n/ℓ − 2 log ℓ`, KK25 eq. (23).

Substituting `S` and clearing `ℓ`:

    s  ≤  n − 2ℓ log ℓ − ℓ · O(log n) − δ(2n, 2t).

*Plain reading: the usefulness is the string length minus a tax per block. There are `n / log t`
blocks, so the tax is linear in `n`.*

## 2. Why neither tax can be removed

**The `2ℓ log ℓ` tax is the union bound.** It exists because the property is "some block is short". Any
property of that shape needs every block of a random string to look random, hence a per-block margin
that grows with the number of blocks. With `ℓ = n / (c log t)` this is `Ω(n · log n / log t)`, linear
for polynomial `t`.

**The `ℓ · O(log n)` tax is the chain rule's per-string error.** Even at zero error the argument fails
at logarithmic usefulness, and this is the load-bearing point: put `δ = 0` and error `0`, and take
`s = n − a log n`. Then `Σ_i pK(x_i | …) ≤ n − a log n`, so the *average* block saves `(a log n)/ℓ`
bits below its length `n/ℓ`. With `ℓ = n / (c log t)` that is `a c (log n)(log t)/n → 0` bits per
block. A random block already fluctuates by `O(1)` bits (Lemma 2.1's `4/ℓ²` is for a `2 log ℓ` margin;
at margin `0` the compressible fraction is constant). So no block-local statistic distinguishes "some
block saves a fraction of a bit" from "a random string". **The saving is real but not localisable.**
Conversely, to make the per-block saving at least `2 log ℓ` (the margin C2 needs), one must take
`ℓ ≤ a log n / (2 log ℓ) = O(log n)` blocks, which by C1 costs `2^{n/ℓ} = 2^{Ω(n / log n)}` time. That is
Appendix B's bound. **Obstructions A and B coincide.**

*Plain reading: to see a small saving you need big pieces; big pieces cannot be searched. To search
pieces you need them small; small pieces do not show the saving. There is no size that does both.*

## 3. Can the average form of our hypothesis escape the partition?

The partition exists only to make search feasible. The alternative is a *search algorithm* for short
conditional descriptions of `Θ(n / log n)`-bit strings, i.e. a meta-complexity search problem. Our
hypothesis is universal over samplable distributions, so it may be instantiated at the universal
distribution `U_t` (outputs of random short programs), where typical strings are exactly the
compressible ones. Three things follow, and none escapes:

1. **Average is not worst case.** A natural property must reject every string of complexity `≤ s`
   (soundness is worst-case over the compressible strings). Under `U_t`, strings of complexity `≤ s`
   each carry mass `≥ 2^{−s}/poly`, and there are up to `2^s` of them; a `1 − 1/q` average statement
   leaves `2^s/q` of them uncontrolled. Exponentially many.
2. **The moment form's tail does not close it.** BEM_skew gives `Pr_D[Σ⁺ > k + C log s] ≤ 2^{−k}` by
   Markov. Under `U_t`, worst-case control over all strings of complexity `≤ s` needs exceptional mass
   below `2^{−s}`, i.e. `k ≥ s`, at which point the guaranteed defect bound is `≈ s`: vacuous. The moment
   form buys exactly the HILNO `1 − 1/poly` statement plus a tail that is useless at the level needed.
3. **The known bridge needs errorless.** Worst-case soundness from an average-case hypothesis for a
   meta-complexity problem is the content of Hirahara's non-black-box worst-case-to-average-case
   reduction for MINKT (FOCS 2018) [cited from memory; audit], whose hypothesis is an *errorless*
   heuristic under the uniform distribution. Our hypothesis is of the error-prone kind (§7.5's divide,
   Prop. 5/6 of the paper). So the escape from the partition runs straight into the errorless/error-prone
   gap — the wall the instance checker was supposed to cross.

## 4. Barrier filter

Relativization: every step above relativizes (KK25 §4 and Appendix B relativize; Hirahara's Remark 6.4
is the oracle statement for the depth term). Natural proofs: not triggered; no lower bound is argued.
The conclusion is a limitation of a *method* (partition + brute force) plus an identification of what
any other method must supply (worst-case-sound search from an average hypothesis), not a barrier
theorem for the converse itself.

## 5. What this changes

- `b36_worst_case_hub.md` §9: "the block-partition wall is new … and has no oracle argument attached"
  — corrected: it is the same wall as the depth term, seen at the other end of the block-size
  trade-off. Forward correction only; the note is not edited.
- The paper's §7.5 (B38 edit 5, queued): name **one** obstruction for `BEM_skew ⇒? (i)`, not two:
  *a logarithmic saving cannot be localised by any partition, and any non-partition route needs
  worst-case-sound search from an average hypothesis, which is the errorless/error-prone gap.*
- Thread B37: closed, negative, mechanism named. No pass-sized attack on the converse remains at
  logarithmic usefulness by partition or by moment tails.

## 6. Divergent round before closing (targets)

1. **Usefulness `n − n^{ε}` instead of `n − O(log n)`.** With `ℓ = n^{1−ε}/…` blocks the taxes are
   `o(n)`; KK25's own regime is `n − n/C`. A moment bound with polynomial-in-`n^ε` slack is a different,
   weaker object; whether it still rules out one-way functions (Prop. 2(c) needs `O(log)`) is no — so
   the object would lose its meaning. Not worth a pass.
2. **Change the hypothesis to errorless.** Then Hirahara 2018 applies and the property follows; but
   that is `H_pK ⇒ (i)`-type, already B31.2, not the converse.
3. **Non-relativizing search.** The honest name of what is needed; no candidate.
4. **rK^t** (B39, running): changes the object, not the partition; the partition tax is the same.
Convergent pick: none on the converse; the paper states the single wall.
