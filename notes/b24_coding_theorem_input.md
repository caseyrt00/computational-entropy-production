# B24 — does LOZ22's coding theorem survive an auxiliary input? (reading note)

Date: 15 Sep 2026. Thread B24 (from E59, E60, E61). No paper edits; this is a reading note.

Source read: `passes/pass16/sources/lu_oliveira_zimand_2022_arxiv2204.08312.pdf` (Lu, Oliveira, Zimand,
*Optimal Coding Theorems in Time-Bounded Kolmogorov Complexity*, arXiv 2204.08312v1, 18 Apr 2022), §5.1
"Optimal Coding Theorem for pK^t": Theorem 30 and Lemma 31 with proof (p. 25), proof of Theorem 30
(p. 26). Read in full. (E59 and `theorem_reversibility.md` §Label say "§3"; the coding theorem's proof is
§5.1, pp. 25–26. Corrected here, not in the file.)

## Outcome in one paragraph

**Yes.** The decoder in LOZ22's proof of Theorem 30 uses the sampler in exactly one way: it holds the
sampler's code as part of a short advice string and *runs the sampler once on a random tape it has
computed*. Nothing else about the sampler enters the proof; the hash family of Lemma 31 depends only on
the sampler's running time `T` and the target probability `δ`, not on the sampler. Give the sampler an
auxiliary input `y` and give the decoder the same `y` on a separate tape (HILNO's convention for
`pK^t(x | y)`, p. 17), and every line goes through unchanged, with the same constant. The relativized
statement and its proof are written out in §3 below. So the one conditional step of the draft's
Proposition 8 and Corollary 1, and of Theorem R4 (⇐) in `passes/pass20/theorem_reversibility.md`, is
closed at the level of this note. **They may drop to Proved once §3 is pasted into the paper as a lemma
with its proof** (CLAUDE.md rule 2: "Proved" means a written proof in the report, not a relabel). Two
harmless wrinkles are recorded in §4. Owner's call on when to paste; no edit made here.

*Plain reading: the coding theorem says "if a fast random program lands on x with odds 1 in 2^k, then
x has a fast description of about k bits". The proof builds that description by handing the decoder
the program itself plus a short pointer into a random tape. If the program is allowed to look at a
hint y, the decoder just gets the same hint and runs the program the same way. Nothing in the proof
cared what the program was doing inside.*

## 1. What the theorem says, verbatim

Theorem 30 (p. 25), the restatement of Theorem 5:

> Suppose there is a randomized algorithm A for sampling strings such that A(1^n) runs in time T(n) and
> outputs a string x ∈ {0,1}^n with probability at least δ > 0. Then pK^t(x) = log(1/δ) + O(log T(n)),
> where t(n) = poly(T(n)) and the constant behind the O(·) depends on |A| and is independent of the
> remaining parameters.

The definition it is about (LOZ22 §1.2.3, p. 7, the display after "is defined as"):

> pK^t(x) = min { k : Pr_{w ∼ {0,1}^{t(|x|)}} [ ∃ M ∈ {0,1}^k, M(w) outputs x within t(|x|) steps ] ≥ 2/3 }.

*Plain reading: x has probabilistic description length k if, for two thirds of all random tapes w,
some k-bit program run on w prints x fast.*

The conditional version this paper uses (HILNO, p. 17, immediately after their Eq. (6)):

> These definitions can be extended to conditional Kolmogorov complexity in the natural way. For
> instance, in pK^t(x | y) the machine U is also given access to the input string y in Equation (6)
> above. For concreteness, we assume that y is given in a separate input tape.

## 2. The lines that carry the black-box property

All on pp. 25–26 of the PDF (`pdftotext -layout`, pages 25 and 26).

**(L1) Lemma 31's hypothesis on the sampler, p. 25.** The lemma is stated for an arbitrary function of
the random bits:

> Let M : {0,1}^T → {0,1}^* be a function computable in time T and let x ∈ Range(M) be such that
> Pr_{z ∼ {0,1}^T} [M(z) = x] ≥ δ.

and its conclusion is a hash family that does not depend on M at all:

> For any T ∈ N and δ ∈ [0,1], there exists a family of functions H = { H_w : {0,1}^ℓ → {0,1}^T }_{w ∈
> {0,1}^k} where k = poly(T) and ℓ = log(1/δ) + O(1) such that the following holds. […] It holds that
> Pr_{w ∼ {0,1}^k} [ ∃ v ∈ {0,1}^ℓ such that M(H_w(v)) = x ] ≥ 2/3. Moreover, given w ∈ {0,1}^k and
> v ∈ {0,1}^ℓ, H_w(v) can be computed in time poly(T).

The family is quantified *before* M ("there exists a family … such that … Let M …"): one family per
(T, δ) serves every M. That is the whole reason an auxiliary input costs nothing.

**(L2) The only use of M inside Lemma 31's proof, p. 25.** M is *run*, inside a nondeterministic check:

> note that given M and x, and using oracle access to H, checking whether there exists some
> v ∈ {0,1}^ℓ such that M(H(v)) = x can be done in NP. By the standard connection between the
> computation of an oracle-taking machine in PH and constant-depth circuits (see e.g., [RST15]), we get
> that there is an AC^0 circuit of size at most 2^{poly(T)} that takes H as input and checks whether it
> is good.

The circuit's size is governed by the running time of the check, poly(T); M and x are hard-wired into
the checker. Then a pseudorandom generator for AC^0 with seed length poly(T) supplies H_w.

**(L3) The sampler as a function of its coins, p. 26, first line of the proof of Theorem 30:**

> Let us view M := A(1^n) as a function that takes T := T(n) random bits and outputs x ∈ {0,1}^n with
> probability at least δ.

**(L4) The decoder, p. 26:**

> This means that for at least 2/3 of w ∈ {0,1}^{poly(T)}, there is some advice string
> α ∈ {0,1}^{log(1/δ)+O(log T)}, which encodes the number T, the code for A(1^n), the code for computing
> H_w using w, and some good v (which could depend on w), such that using α together with w we can
> recover x in time poly(T).

So the decoder is: read α; compute H_w(v) from w and v; run A(1^n) on the random tape H_w(v); print
the result. The sampler is a black box run once on a tape the decoder chose. Its code is carried in α,
which is why the constant "depends on |A|" — and that clause is the crux for B24: if y were *hard-wired*
into the sampler instead of given as input, |A| would grow by |y| and the bound would die. It survives
only because y is an input on a separate tape, for the sampler and for the decoder alike.

## 3. The relativized statement, with proof

**Lemma (coding theorem with an auxiliary input).** Let R be a randomized algorithm that, on input y,
runs in time T(n) and, for the pairs (x, y) in question, outputs x with probability at least δ = δ(x, y)
> 0. Then

    pK^t(x | y) ≤ log 1/δ + O(log T(n)),   t(n) = poly(T(n)),

where the constant behind the O(·) depends on |R| only and not on x, y, n, T or δ.

*Plain reading: if a fast program, shown y, lands on x with odds 1 in 2^k, then x has a fast description
of about k bits given y. Same theorem, one extra input, same constant.*

**Proof.** Fix (x, y). Set M_y(z) := R(y; z) for z ∈ {0,1}^T: the output of R on input y with random tape
z. Since R runs in time T it reads at most T bits of y, so M_y is a function computable in time T by a
machine that receives y as input; and Pr_z[M_y(z) = x] ≥ δ by hypothesis. Apply Lemma 31 with this M
and this x. The lemma's family H_w depends on (T, δ) only (L1), so it is the same family as before.
Inside the lemma's proof (L2), the NP check "∃ v : M_y(H(v)) = x" is run by a nondeterministic oracle
machine with M_y — that is, with R's code and with y — and with x hard-wired; it guesses v (ℓ bits),
reads H(v) (T bits), runs R on y with that tape (time T), and compares to x; its running time is
poly(T), so the AC^0 circuit has size 2^{poly(T)} exactly as before, and the pseudorandom generator and
its seed length are unchanged. Hence for at least 2/3 of w ∈ {0,1}^{poly(T)} there is a good v with
R(y; H_w(v)) = x.

Decoder (L4, with the extra tape): the advice α encodes T, the code of R, the code for computing H_w
from w, and v; |α| = log(1/δ) + O(log T) with the O(·) depending on |R| only. Given α, the random tape w
and y on its separate input tape (HILNO's convention, §1), the universal machine computes H_w(v) in
time poly(T), runs R on input y with random tape H_w(v), and prints the result, which is x for at
least 2/3 of w. By the definition of pK^t(x | y), pK^t(x | y) ≤ |α| for t = poly(T). ∎

**What the lemma feeds.** The bound is in R's *own* output probability δ = Pr[R(y) = x]. In the
draft's Proposition 8, R(y) samples D(· | y) exactly, so δ = D(x | y) and pK^t(x | y) ≤ log 1/D(x | y) +
O(log n); Lemma 5 supplies pK^t(y) ≤ log 1/D_2(y) + O(log n); summing, σ^rev_D(x, y) ≤ O(log n) on every
support pair, the statement of Proposition 8, with Corollary 1 its contrapositive. In Theorem R4 (⇐),
the hypothesis is domination, S(x | y) ≥ D(x | y)/n^c, so δ ≥ D(x | y)/n^c and the lemma gives
pK^t(x | y) ≤ log 1/D(x | y) + c log n + O(log n), which is what the proof of (⇐) in
`theorem_reversibility.md` uses. Both proofs invoke the lemma pointwise, for every (x, y) in the support,
which is how the lemma is stated. The time bound: the lemma's t is poly(T_R(n)), and pK^t's random
tape has length t(|x|), so t must also be at least the polynomial in n that covers |y|; both are
polynomials in n since |y| ≤ poly(n), and the draft already enlarges t_D to cover R's running time.

## 4. Two wrinkles, both harmless

1. Lemma 31 states ℓ = log(1/δ) + O(1); the proof of Theorem 30 says ℓ = log(1/δ) + O(log T). Either
   gives |α| = log(1/δ) + O(log T), because T itself is encoded in O(log T) bits. No effect.
2. LOZ22's definition of pK^t draws the random string of length t(|x|); HILNO's conditional version
   draws it the same way with y on a separate tape. The advice α does not encode n; the decoder
   needs n only to run R(y), and can read it from |y| or from T. If the owner prefers, encode n in α
   at a cost of O(log n) ≤ O(log T) bits. No effect.

## 5. What this does downstream

- **Proposition 8 and Corollary 1 (draft §8.2, E60):** the "Proved-conditional on the coding theorem
  holding with the sampler given y as input" label can become **Proved** once §3 is written into the
  paper as a lemma (suggested placement: after Lemma 5, as its conditional form, with the label
  Proved and the read-status "LOZ Theorem 30 and Lemma 31, pp. 25–26, Read; the auxiliary-input form is
  this paper's, by the proof above"). The audit-list entry from E60 is then resolved.
- **Theorem R4 (⇐), `theorem_reversibility.md`:** same; its §Label paragraph names this note as the
  closer. (⇒) was already Proved. Then R4 is a Proved biconditional and the novelty audit E59 asked for
  becomes the only thing between it and the paper.
- **E61's organizing remark B26.1** was conditional on B24; it is now conditional only on R4's
  bookkeeping check.
- **Not touched:** the general conditional coding theorem (for every samplable pair distribution,
  whether or not D(· | y) is samplable given y) remains equivalent to NP ⊆ BPP [HILNO Theorem 4, item 2];
  this note is the special case with an efficient conditional sampler *given*, which is all the paper
  uses.

## 6. Read-status ledger

| Source | What was read | Status |
|---|---|---|
| Lu–Oliveira–Zimand 2022, arXiv 2204.08312v1 | §5.1 in full: Theorem 30, Lemma 31 and its proof (p. 25), proof of Theorem 30 (p. 26); §1.2.3 definition of pK^t (p. 7) | Read (on disk, `pass16/sources/lu_oliveira_zimand_2022_arxiv2204.08312.pdf`) |
| HILNO 2023, ePrint 2023/424 | p. 17, Eq. (6) and the conditional convention; p. 18, Theorem 7 | Read (on disk) |
| `passes/pass20/theorem_reversibility.md` | Theorem R4, proof of (⇐), §Label | Read |
| `passes/pass16/ENTROPY_PRODUCTION.md` | Proposition 8, its label paragraph and proof, Corollary 1 (lines 753–769 at sha 0f50595d…) | Read |

No numerical claims in this note; nothing to rerun.
