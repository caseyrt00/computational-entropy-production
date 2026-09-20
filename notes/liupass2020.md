# Liu–Pass 2020 — read notes (primary source, read directly)

**Citation.** Yanyi Liu (Cornell) and Rafael Pass (Cornell Tech), *On One-way Functions and Kolmogorov
Complexity*, FOCS 2020, pp. 1243–1254, DOI 10.1109/FOCS46700.2020.00118. Read from the Cryptology
ePrint Archive version, paper 2020/423, dated 24 September 2020. **Pages 1–5 read directly from the
PDF** (title, abstract, §1 Introduction, §1.1 Related Work, start of §1.2 Proof outline). Later
sections not yet read; anything below drawn only from those pages is marked.

---

## 1. The theorem

**Theorem 1.1.** The following are equivalent:
- One-way functions exist;
- `K^poly` is mildly hard-on-average.

And the paper states the stronger form: **for every polynomial `t(n) ≥ (1+ε)n` with `ε > 0` constant,
mild average-case hardness of `K^t` is equivalent to the existence of one-way functions.**

*Plain reading: unbreakable codes are possible exactly when one particular counting question is hard.
The question is "how short is the shortest quick program that prints this string?" You do not have to
answer it perfectly. You only have to fail on a small but noticeable slice of random strings. If every
fast algorithm fails on such a slice, codes are possible. If some fast algorithm succeeds on nearly
all of them, no code is safe.*

## 2. The definitions, precisely

**`K^t(x)`, time-bounded Kolmogorov complexity.** The length of the shortest program that outputs `x`
**within time `t(|x|)`** when run on a fixed universal Turing machine `U`.

Difference from the neighbours:
- **plain `K`** has no efficiency requirement on the program at all. The paper says this is unappealing
  from a computational point of view, and `K^t` exists to fix exactly that.
- **`K^poly`** means: there exists *some* polynomial `t` for which the statement holds.
- Levin's `Kt` is a different object (it charges for time inside the score). This paper uses `K^t`, not
  `Kt`. **This distinction matters and was checked.**

**Mildly hard-on-average (mildly HoA).** There is a polynomial `p(·) > 0` such that every probabilistic
polynomial-time algorithm **fails to compute `K^t(·)` on at least a `1/p(n)` fraction of `n`-bit strings
`x`**, for all sufficiently large `n`.

So, precisely:
- **distribution:** the **uniform** distribution over `n`-bit strings.
- **adversary class:** PPT, probabilistic polynomial time.
- **failure requirement:** only an inverse-polynomial *fraction* need be hard. This is a very weak
  hardness hypothesis, which is what makes the equivalence strong.
- **heuristics may err.** The paper is explicit that it needs hardness against heuristics that can give
  wrong answers, not just "errorless" heuristics that output ⊥ when unsure. It flags this as a much
  weaker property than errorless hardness, with a random-3SAT example showing why the two differ.

## 3. Direction and difficulty

The proof outline (§1.2) starts with **OWFs from average-case `K^poly` hardness**: if `K^t` is mildly
average-case hard for some polynomial `t`, then a **weak** one-way function exists, which is then
amplified to a standard one. The converse direction (OWFs ⟹ average-case hardness of `K^poly`) builds
on prior work showing OWFs imply `K^poly` is **worst-case** hard (Kabanets–Cai; Allender et al.), and
strengthens worst-case to average-case. Full proof sections not yet read.

## 4. Adjacent results in the same paper

- **Theorem 1.2.** If `K^poly` is mildly HoA, then for every constant `d` it is also mildly HoA to
  `(d log n)`-approximate. So any efficient algorithm that beats the trivial approximation by a little
  breaks OWFs.
- **Decisional version.** With `MINK^t[s]` the set of `x` with `K^t(x) ≤ s(|x|)`, and `s(n) = n − c log n`,
  mild average-case hardness of that language under the uniform distribution is likewise equivalent to
  OWFs. Useful: it turns the bridge target into a **decision** problem.
- **Constructive vs existential.** For the OWF direction it suffices to assume hardness of the
  *constructive* version (also output a minimal-length program), giving an equivalence between the two
  in the average-case regime.
- **Universal extrapolation.** Via Impagliazzo–Levin 1990, infeasibility of universal extrapolation is
  equivalent to mild average-case hardness of `K^poly`. A second, differently-flavoured handle on the
  same object.

## 5. What an application must supply — the operative question for this program

To use the theorem to conclude **one-way functions exist**, one must supply:

> a polynomial `t(n) ≥ (1+ε)n`, and an argument that **no probabilistic polynomial-time algorithm can
> compute `K^t(x)` for a uniformly random `n`-bit string `x`, except on at most a `1 − 1/p(n)` fraction**,
> for some polynomial `p` and all large `n`.

That is the whole input. Nothing about circuits, nothing about NP-completeness.

## 6. Physics

**Nothing.** Pages 1–5 contain no discussion of thermodynamics, entropy, the second law, physics, or
observers in any physical sense. The framing is entirely cryptographic and complexity-theoretic. A
targeted search for a physics connection to this line of work is still outstanding.

## 7. Bearing on the bridge, stated carefully

**Encouraging.** The distribution Liu–Pass requires is the **uniform** one. Pass 03's anchor fact is
that a second-order reversible CA is a bijection, so a uniform prior over microstates is preserved
exactly, forever. The thermodynamic side therefore hands over a uniform distribution for free, which is
the distribution the theorem wants. That removes one obstruction I had expected in thread B2.

**But the gap is not closed, and it is not small.** [Inference] Liu–Pass needs *"PPT cannot compute
`K^t` of a uniformly random string"*. The thermodynamic side gives *"a bounded observer cannot invert a
coarse-graining"*. **These are different statements** and nothing here connects them:

- computing `K^t(x)` is a question about `x`'s shortest fast description; inverting a coarse-graining is
  a search for a preimage. Neither obviously reduces to the other.
- Liu–Pass's random object is a uniform **string**; our uniform object is a **microstate**, and what
  the observer actually sees is a coarse-grained **observation sequence**, which is not uniform.
- The failure fraction needed is only `1/p(n)`, which is weak and therefore favourable — but it is a
  statement about *all* PPT algorithms, which no measurement can establish (the permanent caveat).

So the honest status: **Liu–Pass is a genuine far half of a bridge, the distribution matches, and the
near half does not exist yet.** Constructing it means finding a reduction from coarse-grained inversion
to computing `K^t`, or replacing the thermodynamic statement with one about `K^t` directly.

## 8. Still to check

- Formal definitions in §2 and the full proofs (pages 6+ not read).
- Follow-up work by Liu–Pass and others (`Kt` vs `K^t` versions, worst-case-to-average-case, other
  primitives). Hirahara and Santhanam are cited as adjacent; Santhanam's MCSP equivalence is
  *conditional* on a new conjecture whereas this equivalence is **unconditional** — the paper is
  explicit about that contrast.
- Whether anyone has connected this line to thermodynamics. Nothing found in the paper itself.
