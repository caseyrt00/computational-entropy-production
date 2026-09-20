# B30 — Which physical quantity, measurable in a laboratory, is a complexity meter?

Date: 2026-09-15. Thread B30. ~26 web searches, 7 targeted full-text or ar5iv extractions, one PDF
read locally with `pdftotext`.

Context read first, in this order: `pass20/MOUNTAIN2_VERDICT.md` (whole file),
`pass20/research/b26_physical_heuristica.md` §0 (reading ledger), §8 (the table), §9 (verdict),
§10 (threads — B30 is defined there), and `pass20/research/mountain2_compression_tests.md` §0.5
(the compressor inequality, load-bearing for §6 below).

**The question B26 handed over.** B26 found that the one-way-function principle's stock of ruled-out
physical theories has exactly one inhabitant wearing two costumes, and that the inhabitant is
**complexity metering**. But the stock has no falsifying *observation*: the chain ends at a
computation, because nobody can measure circuit complexity. So: **which physical quantity, measurable
in a laboratory, is provably or plausibly a complexity meter** — a functional of a physical state or
process whose value tracks circuit complexity, time-bounded Kolmogorov complexity `K^t`, or logical
depth, on a class of instances rich enough to contain a candidate one-way function?

**Answer in one line.** **None, and the reason is a theorem rather than a gap in the literature:** a
complexity meter is *exactly* a distinguisher between pseudorandom and Haar-random states, so under
the principle itself every efficiently measurable quantity must fail — and the literature has been
steadily proving the individual cases (`pseudoentanglement` 2022, `pseudomagic` 2024, **`pseudochaotic
dynamics` — the pseudo-OTOC theorem — July 2025**). The single observable that was both measured at
scale and open closed negative fourteen months ago. §8 gives the verdict and the one experiment that
would still mean something.

---

## 0. Reading status per source

| # | source | status | what was taken |
|---|---|---|---|
| S1 | Kolchinsky & Wolpert, *Thermodynamic costs of Turing Machines*, arXiv 1912.04685v3 / Phys. Rev. Research **2**, 033312 (2020) | **Read** — full PDF pulled and converted with `pdftotext` (2815 lines); abstract, §I introduction, §I C, the Eq. (1)/(2)/(3)/(26) passages, and the coin-flipping-vs-dominating comparison read verbatim; **full-text grep run for `depth`, `logical depth`, `time-bounded`, `resource-bounded`, `running time`, `computation time`** | Eqs. (1), (2), (3), (26); the non-computability caveat; the physical-Church–Turing sentence; the grep result (§2e) |
| S2 | Aaronson, Bouland, Fefferman, Ghosh, Vazirani, Zhang, Zhou, *Quantum Pseudoentanglement*, arXiv 2211.00747, ITCS 2024 | **Read via ar5iv** — abstract verbatim, Corollary 1.0.1 verbatim, §3.4 AdS/CFT passages verbatim | the Θ(n) vs ω(log n) gap; the quantum-secure-OWF assumption; the Ryu–Takayanagi sentence |
| S3 | Lee, Kwon, Cho, *Pseudochaotic many-body dynamics as a pseudorandom state generator*, Nature Communications **16** (2025), doi 10.1038/s41467-025-62081-6 | **Read via PMC open-access full text, twice** — abstract verbatim; construction (RSED); Theorem 1 statement; level-statistics remark; experimental remark; **second targeted pass specifically to locate where LWE is invoked** (answer: not in Theorem 1) | the pseudo-OTOC theorem — the load-bearing new source of this note |
| S3b | Haferkamp, Kothakonda, Faist, Eisert, Yunger Halpern, *Linear growth of quantum circuit complexity*, Nature Physics **18**, 528 (2022), arXiv 2106.05305 | **Summary only** (abstract + institutional press description) | complexity of random circuits grows linearly until saturating at a gate count exponential in the qubit number — turns §2(c) reason 1 into theorem-vs-theorem |
| S4 | Crutchfield & Shalizi, *Thermodynamic depth of causal states*, Phys. Rev. E **59**, 275 (1999) / SFI WP 1998, arXiv cond-mat/9808147 | **Summary only** (search-level; abstract and secondary description) | the "dive = reverse-time Shannon entropy rate" result; the unspecified-macrostate objection |
| S5 | Ji, Liu, Song, *Pseudorandom Quantum States*, CRYPTO 2018 / ePrint 2018/544 | **Summary only** (search-level; same status as in B26 §0) | the PRS definition (poly copies, poly-time quantum distinguisher); PRS from post-quantum PRFs |
| S6 | Craps, Evnin, Pascuzzi, *A relation between Krylov and Nielsen complexity*, PRL **132**, 160402 (2024), arXiv 2311.18401 | **Abstract verbatim** (ar5iv/abs fetch) | the direction of the inequality: Krylov time-average **upper-bounds** Nielsen, under a custom penalty schedule |
| S7 | *Explicit connections between Krylov and Nielsen complexity*, arXiv 2511.15799 / Phys. Rev. D (2026) | **Summary only** | Krylov = squared length of a straight-line trajectory; saturation only for small precursors |
| S8 | Gärttner et al., *Measuring out-of-time-order correlations…in a trapped-ion quantum magnet*, Nature Physics **13**, 781 (2017) | **Summary only** | >100 ions, Penning trap, time-reversal protocol, up to 8-body correlations |
| S9 | Mi et al., *Information scrambling in quantum circuits*, Science **374**, 1479 (2021), arXiv 2101.08870 | **Summary only** | 53-qubit Sycamore; operator spreading (classically easy) vs operator entanglement (hard) |
| S10 | Google Quantum AI, *Quantum Echoes* (OTOC, Nature, Oct 2025) | **Summary only** (research blog + press) | 65-qubit subsystem of 105-qubit Willow; claimed ~13,000× over best classical simulation; "verifiable quantum advantage" |
| S11 | Brydges, Elben, Jurcevic, Vermersch, Maier, Lanyon, Zoller, Blatt, Roos, *Probing Rényi entanglement entropy via randomized measurements*, Science **364**, 260 (2019) | **Summary only** | partitions up to 10 qubits, trapped Ca ions |
| S12 | Gu, Leone, Ghosh, Eisert, Yelin, Quek, *Pseudomagic Quantum States*, PRL **132**, 210602 (2024) | **Summary only** | magic can be computationally hidden; magic-dominated phase provably intractable |
| S13 | Oliviero, Leone et al., *Measuring magic on a quantum processor*, npj Quantum Information **8** (2022), arXiv 2204.00015 | **Summary only** | stabilizer 2-Rényi entropy measured by randomized measurements on `ibmq_quito`, `ibmq_casablanca` |
| S14 | Grewal, Iyer, Kretschmer, Liang, *Low-Stabilizer-Complexity Quantum States Are Not Pseudorandom*, ITCS 2023, arXiv 2209.14530 | **Summary only** | efficient distinguisher for stabilizer fidelity ≥ 1/k using O(k¹²) copies; ω(log n) T-gates necessary for PRS |
| S15 | Belin, Myers, Ruan, Sárosi, Speranza, *Does Complexity Equal Anything?*, PRL **128**, 081602 (2022), arXiv 2111.02429 | **Summary only** | an *infinite class* of bulk observables reproduces late-time linear growth + switchback |
| S16 | Brown, Roberts, Susskind, Swingle, Zhao, *Complexity Equals Action*, arXiv 1509.07876; *Complexity, action, and black holes*, arXiv 1512.04993; PRL **116**, 191301 | **Summary only** | C = A/(πħ) on the Wheeler–DeWitt patch |
| S17 | Hayden & Wang, *What exactly does Bekenstein bound?*, Quantum **9**, 1664 (2025), arXiv 2309.07436 | **Summary only** | capacities of the Unruh channel obey the bound; **zero-bits are not constrained by it** |
| S18 | Ibnouhsein, *Thermodynamic Signature of Logical Depth in Quantum Circuits*, Found. Phys. **55**, 71 (2025), arXiv 2508.03203 | **Abstract only** (Springer paywalled; abstract from search + arXiv listing) | "logical depth factor" L_d ≈ 1.615 on two 4-branch circuits; ancilla-based protocol proposed |
| S19 | Ghafari et al., *Dimensional Quantum Memory Advantage in the Simulation of Stochastic Processes*, PRX **9**, 041013 (2019) | **Summary only** | photonic; memory in the polarization of one photon (qubit) vs a classical 3-level system |
| S20 | Schuster, Haferkamp, Huang, *Random unitaries in extremely low depth*, arXiv 2407.07754, Science (2025) | **Summary only** | PRUs in poly(log n) depth in 1D, poly(log log n) all-to-all; "low complexity, short-range entanglement, yet indistinguishable from unitaries with exponential complexity" |
| S21 | *Quantum pseudoresources imply cryptography*, arXiv 2504.15025; *Near-Term Pseudorandom and Pseudoresource Quantum States*, arXiv 2504.17650 | **Summary only** | the general pseudoresource template; pseudocoherence, pseudopurity, pseudoimaginarity |
| S22 | *Measuring Spectral Form Factor in Many-Body Chaotic…*, arXiv 2403.16935 | **Summary only** | "the naive Hadamard test method … suffers from an exponentially small signal-to-noise ratio in general" |
| S23 | Parker, Cao, Avdoshkin, Scaffidi, Altman, *A Universal Operator Growth Hypothesis*, PRX **9**, 041017 (2019) | **[Unverified — cited from memory]**, not fetched this session | the definition of Krylov complexity from the Lanczos coefficients |
| S24 | Nielsen, Dowling, Gu, Doherty, *Quantum computation as geometry*, Science **311**, 1133 (2006); *The geometry of quantum computation*, quant-ph/0701004 | **[Unverified — cited from memory]**, abstract listing seen only | geodesic length in a right-invariant penalty metric |
| S25 | Lloyd & Pagels, *Complexity as thermodynamic depth*, Annals of Physics **188**, 186 (1988) | **[Unverified — cited from memory]**, seen only through S4 and secondary description | depth as entropy difference; designed to be an *effectively computable* observable |
| S26 | Bennett, *Logical depth and physical complexity* (1988) | **[Unverified — cited from memory]**, seen only through secondary description | depth at significance s = least runtime of a program within s bits of minimal |
| S27 | Zurek, *Algorithmic randomness and physical entropy*, Phys. Rev. A **40**, 4731 (1989) | **Summary only** (search-level) | physical entropy S = H + K |
| S28 | *Quantum Circuit Complexity as a Physical Observable*, J. Applied Mathematics and Physics **13** (2025), doi 10.4236/jamp.2025.131004 | **Abstract only.** **Low-credibility venue (SCIRP).** Recorded to be dismissed, not relied on | claims circuit complexity is self-adjoint, gauge-invariant, measurable |
| S29 | Yao 1982 / Blum–Micali 1984 / HILL 1999 (classical PRGs from OWFs) | **[Unverified — cited from memory]**, textbook-level, not fetched | the classical analogue of the master no-go (§6) |
| S30 | Baez & Stay, *Algorithmic thermodynamics* (2010) | **[Unverified — cited from memory]**, not fetched | a formal Gibbs-ensemble analogy, no experimental programme |

Anything below not attributed to a source is `[Inference]` and is marked.

---

## 1. The organizing constraint: what a "complexity meter" is, and the trichotomy

Before any candidate. This sorts every row of the final table and it is the reason the verdict is
negative. `[Inference]` — the trichotomy is ours; the ingredients are S3, S5, S15.

**Definition (operational complexity meter).** A complexity meter is a laboratory procedure that is
handed an **unknown** state or process as a black box — you may prepare copies of it, evolve it,
measure it — and returns a number that tracks its circuit complexity (or `K^t` of its output). The
two words that do all the work are **unknown** and **black box**. A functional you can evaluate with
pencil and paper once you have been told the Hamiltonian is not a meter; it is a calculation.

*Plain reading: a meter is a thing you point at an object you know nothing about, and it tells you
how hard that object was to make. A formula that needs the recipe as an input is not a meter, because
if you already have the recipe you already know how hard the thing was to make.*

**ELI5.** Imagine two sealed boxes. One contains a jigsaw someone assembled in five minutes from a
kit; the other contains one assembled over a year from hand-cut pieces. A complexity meter is a
device you wave at a sealed box that says "five minutes" or "a year". The claim of the one-way-function
principle is that nature contains no such device — and the theorems below say that every instrument
anyone has actually built in a laboratory is provably not one.

**Every candidate falls into one of three buckets.**

- **Bucket 1 — functionals of a *known* dynamics.** Krylov complexity, spread complexity, OTOCs,
  Nielsen geometric complexity. Each is defined from `(H, O, t)` or from a unitary `U` you already
  hold. If you know `H` you can compute the number without a laboratory; if you do not know `H` the
  number is not even defined. These never take the black-box object as input, so they are not meters
  in the sense above, whatever else they are good for. The OTOC case is the sharpest: the standard
  measurement protocol (Gärttner 2017, S8; Google Quantum Echoes 2025, S10) is a **time-reversal echo
  — you must physically apply `U†`**, i.e. hold the dynamics in your hand.
- **Bucket 2 — genuine black-box functionals, estimable from poly many copies in poly time.**
  Rényi-2 entropy via swap tests or randomized measurements, entanglement entropy, purity, stabilizer
  Rényi entropy (magic), any expectation value, and — given oracle access to `U` and `U†` — the OTOC.
  These are real meters in form. Under quantum-secure one-way functions they are all provably not
  meters in fact, and this is definitional, not a coincidence: see §4.
- **Bucket 3 — readouts requiring exponential resources, or a non-boundary observer.** Complexity =
  volume / action, Zurek's `K` term, Bennett's logical depth, thermodynamic complexity in
  Kolchinsky–Wolpert's dominating realization, the spectral form factor. Not lab-measurable by
  construction. This is the Bouland–Fefferman–Vazirani loophole from B26 — the hypothesis is that
  *gravity does the exponential work for you* — and it is the only escape from buckets 1 and 2.

**Consequence, stated now so nothing below is a surprise.** The buckets are exhaustive and the escape
in bucket 3 is by inefficiency. So the search for a lab-measurable complexity meter is not a search
through a big space with one lucky corner; it is a search that the principle itself forbids
succeeding. Every time an observable is measured well enough to matter, a pseudo-X theorem follows.
**This is Aaronson 2005 §10's asymmetry appearing for the third time in this folder** — once in
`MOUNTAIN2_VERDICT.md` (no direct test of the law), once in `b26` §9 (the stock has no falsifying
observation), and now one level further down: not one *instrument* either.

---

## 2. Q1 — the proposed meters, one at a time

### (a) Complexity = volume, complexity = action

**What is claimed.** Complexity = volume (Susskind 2014; Stanford–Susskind 2014
**[Unverified — cited from memory for the exact references]**): for a two-sided eternal AdS black
hole,

    C(|ψ⟩)  ≈  V / (G_N · ℓ)

*Plain reading: the number of elementary gates you would need to build the boundary quantum state,
starting from a simple reference state, is proportional to the spatial volume of the wormhole
connecting the two sides — a length times an area, divided by two constants of nature.*

Complexity = action (S16, Brown–Roberts–Susskind–Swingle–Zhao, PRL 116, 191301): `C = A/(πħ)`, where
`A` is the gravitational action of the Wheeler–DeWitt patch.

*Plain reading: same claim, but the bulk quantity is the action of a spacetime region rather than the
volume of a slice.*

**What exactly is claimed to equal circuit complexity.** The *quantum computational complexity of the
boundary state*: the minimum number of elementary gates taking a fixed simple reference state to
`|ψ⟩` within a tolerance. Three things are left unspecified in every version: the gate set, the
tolerance, and the reference state. Each changes the answer by more than a constant.

**Is anything measurable? No, and worse than no.** Three independent reasons.
1. The volume of a maximal bulk slice and the action of a WDW patch are *bulk* quantities. Reading
   one off requires the holographic dictionary, and BFV 2019's whole point (B26 §8) is that if that
   dictionary were efficiently computable, the resulting complexity meter would break quantum-secure
   pseudorandomness. In their own word the meter is "non-physical".
2. Susskind's reply (arXiv 2003.01807, *Horizons Protect Church–Turing*; abstract only, via B26) is
   that horizons stop the readout reaching the boundary at all.
3. **The dual is not even pinned down.** S15 (Belin–Myers–Ruan–Sárosi–Speranza, PRL 128, 081602):
   there is an *infinite class* of bulk gravitational observables on codimension-one or -zero regions
   that all exhibit the two diagnostic properties — late-time linear growth and the switchback effect
   — so "any observable from this class has the potential to serve as a gravitational dual for the
   circuit complexity of boundary states". Follow-ups are literally titled *Complexity equals (almost)
   anything*. `[Inference]` A quantity with an infinite family of candidate definitions, none of them
   measurable, is not an instrument reading; it is a family of conjectures about an unmeasured number.

**Bucket 3. Verdict: the one hypothetical meter with a real theorem behind it (BFV), and it is
unmeasurable by construction.**

### (b) Krylov complexity

**What it is.** Given a Hamiltonian `H` and an operator `O`, run the Lanczos algorithm on the nested
commutators to build an orthonormal "Krylov basis"; the operator's wavefunction spreads along that
chain, and Krylov complexity is its mean position. Parker–Cao–Avdoshkin–Scaffidi–Altman, PRX 9,
041017 (2019) (S23, **[Unverified — cited from memory]**) conjecture that the Lanczos coefficients
grow linearly in chaotic systems, giving exponential growth of `K`.

*Plain reading: line up a ladder of increasingly complicated observables built out of the
Hamiltonian, watch how far up the ladder the system's dynamics has pushed a simple starting
observable, and call that distance the complexity.*

**Is there a theorem relating it to circuit complexity? Yes, and the direction matters.** S6
(Craps–Evnin–Pascuzzi, PRL 132, 160402, 2024): the time average of Krylov complexity "controls an
**upper bound** on Nielsen complexity with a specific custom-tailored penalty schedule adapted to the
Krylov basis". S7 (arXiv 2511.15799, PRD): Krylov complexity of a Hermitian operator equals the
squared length of a *straight-line* trajectory on the unitary manifold, and that length upper-bounds
Nielsen complexity, **saturating only when the straight line happens to be a minimal geodesic** —
established only in the limit of small precursors, otherwise evidential.

`[Inference]` Read as a meter this is the *useful* direction and it still fails. Small Krylov would
certify small Nielsen, which is exactly what a PRS distinguisher needs (it needs to catch the cheap
state, not the expensive one). But three things block it: the penalty schedule is custom-tailored to
the Krylov basis, so "Nielsen complexity" there is not standard circuit complexity; saturation is not
proved in general, so the bound is one-way and can be vacuous; and — decisively — **Krylov complexity
is a function of `H`, which the meter is not allowed to know.**

**Has it been measured? Not directly — and the qualification matters.** The Lanczos coefficients are
fixed by the moments of the operator autocorrelation function `⟨O(t)O⟩`, which *is* measured
routinely in every one of the platforms below. So Krylov complexity is **inferable in principle from a
measured two-point function**, with the precision demanded of those moments growing with `n`. What
does not exist is a direct measurement. The bucket-1 verdict is unchanged either way: reconstructing
the Lanczos chain still presupposes you know which `H` and which `O` you are talking about. What
exists concretely:
- *Protocols proposed, not executed*: a quantum Gram–Schmidt circuit that orthogonalises the Krylov
  basis; arXiv 2605.07668 (2026) *Bridging Krylov Complexity and Universal Analog Quantum Simulator*;
  arXiv 2403.06391 *Towards verifications of Krylov complexity*. All summary-level.
- *A different Krylov thing that has run on hardware*: Sample-Based Krylov Quantum Diagonalization
  (arXiv 2510.26951) on trapped-ion and superconducting processors, N = 4–20. That is a
  numerical-linear-algebra Krylov **subspace** method for finding ground-state energies. It is not a
  measurement of Krylov **complexity**. Do not let the word do double duty.

**Bucket 1. Verdict: not a meter — it needs the Hamiltonian — and it has never been measured.
Its pseudo-X status is open only because nobody has bothered; see §5.**

### (c) OTOCs and scrambling

**What is measured.** `F(t) = ⟨W†(t) V† W(t) V⟩` and relatives.

*Plain reading: poke the system in one place, let it evolve, poke it somewhere else, run the evolution
backwards, and see how badly the second poke spoiled the first. The faster that spoiling spreads, the
more the system is "scrambling" — smearing local information across everything.*

**Measured, repeatedly, at real scale.** S8: Gärttner et al., Nature Physics 13, 781 (2017) —
**more than 100 ions** in a Penning trap, long-range Ising, time reversal of the many-body dynamics,
multiple-quantum-coherence spectrum, up to 8-body correlations. NMR, 4 qubits, Li et al. 2017
**[Unverified — cited from memory]**. S9: Mi et al., Science 374, 1479 (2021) — **53-qubit Sycamore**,
separating operator spreading (captured by an efficient classical model) from operator entanglement
(exponentially hard to simulate). S10: Google's *Quantum Echoes*, Nature, October 2025 — **65-qubit
subsystem of the 105-qubit Willow chip**, a deterministic OTOC value rather than a sampled bitstring,
claimed ≈13,000× faster than the best classical simulation, marketed as the first "verifiable quantum
advantage". By any measure this is the most seriously measured complexity-adjacent observable in
physics.

**Does OTOC decay track circuit complexity? No — two independent reasons, and the second is new.**

1. **Timescales (old, standard — and now theorem against theorem).** OTOCs saturate at the scrambling
   time `t_* ≈ (β/2π) log N`. Circuit complexity keeps growing linearly until `t ~ e^S`, and this is no
   longer a conjecture: Haferkamp, Kothakonda, Faist, Eisert & Yunger Halpern, *Linear growth of
   quantum circuit complexity*, Nature Physics **18**, 528 (2022), arXiv 2106.05305, prove for random
   circuits built from Haar-random two-qubit gates that complexity grows linearly in the gate count
   until saturating at a threshold exponential in the number of qubits (summary-level; abstract and
   press description only). *Plain reading: scrambling finishes after a time that grows like the
   logarithm of the system size; complexity keeps climbing for a time that grows like the exponential
   of it — and both halves of that sentence are now proved. An instrument that has already saturated
   cannot report on what happens over the next e^S of the history.* Roberts–Yoshida, *Chaos and
   complexity by design*, JHEP 04 (2017) 121 relate OTOC decay to `k`-designs — not to complexity
   (summary-level).
2. **The pseudo-OTOC theorem (new, July 2025) — S3.** Lee, Kwon & Cho, *Pseudochaotic many-body
   dynamics as a pseudorandom state generator*, Nature Communications 16 (2025). Abstract verbatim:
   *"Quantum chaos is central to understanding quantum dynamics and is crucial for generating random
   quantum states, a key resource for quantum information tasks. In this work, we introduce a new
   class of quantum many-body dynamics, termed pseudochaotic dynamics. Although distinct from chaotic
   dynamics, out-of-time-ordered correlators, the key indicators of quantum chaos, fail to distinguish
   them. Moreover, pseudochaotic dynamics generates pseudorandom states that are computationally
   indistinguishable from Haar-random states."*
   The construction is **random subsystem-embedded dynamics (RSED)**: embed a `k`-qubit unitary into
   an `n`-qubit system via random isometries; `k = ω(log n)` suffices. **Theorem 1**: individual RSED
   realisations exhibit negligible OTOCs with probability `1 − negl(n)` when the embedded operator's
   matrix elements scale as `O(2^{−k/2})`.

   **Where the cryptography enters — checked directly against the full text, because the dependency
   graph matters and a first reading got it wrong.** **Theorem 1 is unconditional.** It is a statement
   about random isometries and needs no cryptographic assumption; the OTOC-blindness is a
   *sample-complexity* fact, not a hardness one. The mechanism is the one §1 predicts: a chaotic
   system's OTOC is `~2^{−n}` and RSED's is `~2^{−k}` with `k = ω(log n)`, both far below the
   `Ω(1/poly(n))` error floor of any poly-time estimator on poly-many copies, so the difference is
   simply invisible. **Sub-exponential LWE is invoked later and only for the efficient
   implementation** — the paper's sentence: *"The first and last steps apply quantum secure pseudorandom
   function and permutation in the entire system with polylog(n) depth circuits under the assumption of
   the sub-exponential hardness of the Learning with Errors (LWE) problem."* — i.e. to realise the
   random isometries in polylog depth, and for the pseudorandom-state claim about the outputs.

   *Plain reading: the fact that no OTOC measurement can tell these two systems apart does not depend
   on any unproven cryptographic assumption. It is a counting fact about how few copies you have.
   Cryptography is needed only to build the fake cheaply.*

   This makes the result **stronger** than a cryptographically-conditional one, and it should be
   carried into the paper that way: the observable is dead as a meter whether or not LWE is hard.

   *Plain reading: you can build a system that is not chaotic at all — it is a small chaotic core
   wrapped in a random change of coordinates — and no OTOC measurement will ever tell it apart from a
   genuinely chaotic one, unless you can break lattice cryptography.*

3. A third reason, from the protocol itself: measuring an OTOC requires **applying `U†`**. The
   experimenter supplies the inverse dynamics. That is bucket 1, and it is the same observation
   b26 §8 made about Yoshida–Kitaev decoding: reverse-*with*-the-action, not reverse-from-output.

**Bucket 1 for the protocol, bucket 2 for the estimand. Verdict: measured at 65–100+ qubits, and
proved not a meter in 2025.**

### (d) Nielsen geometric complexity

**What it is.** Nielsen–Dowling–Gu–Doherty, Science 311, 1133 (2006) (S24,
**[Unverified — cited from memory]**): put a right-invariant Riemannian metric on `SU(2ⁿ)` that
charges more for many-body directions than for one- and two-body ones; complexity is the length of the
minimal geodesic from the identity to the target unitary.

*Plain reading: think of every possible quantum operation as a point in a curved landscape where
"easy" directions are cheap to walk and "hard" directions are expensive. The complexity of an
operation is the length of the shortest path to it.*

**Any proposal to measure it? Nothing credible.** One paper claims circuit complexity is a bona fide
physical observable — self-adjoint, gauge-invariant, with a measurement theory and uncertainty
relations (S28, JAMP 13, 2025). **The venue is SCIRP**, and the claim, taken at face value, would
contradict the PRS no-go of §4 unless its "complete protocols for measuring complexity" are
inefficient — in which case it is bucket 3 and says nothing new. Recorded so a later reader does not
have to re-find it; not relied on anywhere below.

**Bucket 1. Verdict: not a meter — geodesic length is a functional of the unitary you already hold —
and no measurement exists.**

### (e) Thermodynamic depth and logical depth

**Thermodynamic depth (Lloyd–Pagels 1988, S25).** The depth of a macrostate is `−k` times the entropy
difference between the distribution over trajectories that could have produced it and the macrostate
itself. It was designed explicitly to be an *effectively computable observable*, in contrast to
Bennett's logical depth.

**It was killed in 1999 — S4, Crutchfield & Shalizi, Phys. Rev. E 59, 275.** Two findings:
(i) the measure depends on a choice of macroscopic states, and neither Lloyd–Pagels nor any follow-up
said how to choose them; (ii) **the rate of increase of thermodynamic depth — the "dive" — is the
system's reverse-time Shannon entropy rate**, so *"depth only measures degrees of macroscopic
randomness, not structure"*.

*Plain reading: the quantity Lloyd and Pagels proposed as a measure of how much history is congealed
in an object turns out to be a measure of how noisy the object is. A fair coin has maximal depth.*

`[Inference]` That is fatal for meter duty in the direction we care about: a cryptographic PRG's
output is maximally *noisy-looking*, so thermodynamic depth is maximal on exactly the object a meter
is supposed to catch.

**Logical depth (Bennett 1988, S26, [Unverified — cited from memory]).** The depth of `x` at
significance level `s` is the least running time of a program `p` with `|p| ≤ K(x) + s` that outputs
`x`.

*Plain reading: not how short the shortest description is, but how long you have to wait for a
near-shortest description to produce the thing. Random noise is shallow (print it literally, instantly);
a simple pattern is shallow; something with a long computational history is deep.*

**Is there a theorem that logical depth is not thermodynamically measurable? The task asked whether
Kolchinsky–Wolpert 2020 covers depth. Read this session (S1). The answer is no — and stating it
precisely matters, because `MOUNTAIN2_VERDICT.md` item 3 currently leans on this paper at
abstract-only.**

What K–W actually prove (quoted / transcribed from the PDF):

- **Heat function of the coin-flipping realisation, Eq. (1):**
  `Q_coin(x) = kT ln2 · [ ℓ(x) − K(φ_U(x)) ] + O(1)`
  *Plain reading: the heat released by running program `x` on a physically reversible realisation of a
  universal computer is proportional to how much longer `x` is than the shortest program producing the
  same output.*
- **Thermodynamic complexity is a constant, Eq. (26):** `min_{x : φ_U(x) = y} Q_coin(x) = O(1)`,
  because `min ℓ(x) = K(y)` by definition. Their sentence: *"for the coin-flipping realization, the
  minimal heat required by the UTM to compute `y` is bounded by a constant … this is a fundamental
  difference between thermodynamic complexity … and Kolmogorov complexity, which is unbounded as one
  varies over `y`."* Same constant-bound conclusion for the dominating realisation (§V C).
  *Plain reading: the minimum heat you must pay to produce any output at all is bounded by a number
  that does not depend on the output. Heat does not track how hard the output is to describe, because
  you can always pay the minimum by feeding in the shortest program.*
- **Heat function of the dominating realisation, Eq. (2):** `Q_dom(x) = kT ln2 · K(x | φ_M(x))`, and
  Eq. (3): `Q_dom(x) ≤ Q(x) + O(1)` for **every computable realisation** `Q`.
  *Plain reading: the best physically-buildable machine's heat, on input `x`, equals the length of the
  shortest description of the input given the output.* — This is directly the reverse-conditional
  description length our `σ` uses, which is why it is worth recording exactly.
- **But the dominating realisation is not constructible.** Verbatim: *"while the dominating
  realization is better than any computable realization, in the sense of Eq. (3), it itself is not
  computable. This is because its heat function is defined in terms of the conditional Kolmogorov
  complexity, which is not a computable function."*
- **Their own no-meter sentence, §I C**, verbatim: *"`K_U` is an uncomputable function. This implies
  that if the physical Church-Turing thesis is true, then no real-world physical system can take any
  desired string `x` as input and produce the value of `K_U(x)` as output."*

**Does any of it touch depth? No.** Full-text grep of the 2815-line conversion for `depth`,
`logical depth`, `time-bounded`, `resource-bounded`, `running time`, `computation time` returns
**exactly one hit** for `depth`, and it is the phrase *"this example is analyzed in more depth below,
in Section VI"* — prose. **No time-bounded complexity, no logical depth, and no notion of runtime as
a thermodynamic cost appears anywhere in the paper.** So:

> **Correction to `MOUNTAIN2_VERDICT.md` item 3, for the HANDOFF.** Kolchinsky–Wolpert's constant
> bound is about **heat** and about **unbounded-time `K`**. It closes the thermodynamic route to
> Kolmogorov complexity. It does **not** cover logical depth, and it does **not** cover `K^t` — their
> `Q_dom = kT ln2 · K(x|y)` has no time bound in it, so it is not the object Theorem 1/2 or Liu–Pass
> use. The paper is still exactly the right citation for appendix row 17 (`"a different object"`
> becomes a theorem), and the sentence to quote is the physical-Church–Turing one above rather than
> the abstract's.

**Is logical depth connected to a measurable relaxation time?** One paper only, and it is weaker than
its title: S18, Ibnouhsein, *Thermodynamic Signature of Logical Depth in Quantum Circuits*, Found.
Phys. 55, 71 (2025) [abstract only]. Deep conditionally-branching circuits are compared with shallow
uniform ones under progressive decoherence, at matched halting probability and physical resources;
branching architectures induce greater entropy flow, captured by a "logical depth factor" `L_d`; the
demonstration is two 4-branch circuits with `L_d ≈ 1.615`; an ancilla-based controlled-phase protocol
is proposed for near-term hardware. `[Inference]` Three reasons this is not a meter: `L_d` is a
proxy invented for the paper, not Bennett's depth; two hand-built circuits are not a class, let alone
one containing a one-way function; and the experimenter designs the circuits, so it is bucket 1.

`[Inference] — and this is the reason depth is the wrong target regardless.` A pseudorandom
generator's output `y = G(s)` is **shallow** in Bennett's sense: `G` is fast, and `s` together with a
description of `G` is a near-minimal program, so a near-shortest description produces `y` quickly. A
uniformly random string is also shallow (print it literally). **So logical depth assigns the same
verdict — shallow — to the two objects the one-way-function question is entirely about.** Depth is
orthogonal to `K^t` hardness. The meter question is Liu–Pass in physical dress, and depth is not in
it.

**Bucket 3 (logical depth, Zurek's K, thermodynamic complexity in the dominating realisation);
bucket 2 but measuring the wrong thing (thermodynamic depth). Verdict: closed, by two different
theorems, in two different ways.**

### (f) Crutchfield's statistical complexity / computational mechanics

**What it is.** Group histories into *causal states*: two pasts are equivalent when they induce the
same conditional distribution over futures. The resulting minimal predictive machine is the
ε-machine, and the statistical complexity is `C_μ = H[causal states]` — the Shannon entropy of the
stationary distribution over them.

*Plain reading: how many bits of memory about the past you must carry in order to predict the future
as well as it can be predicted. Not how complicated the data looks — how big a machine you need to
keep up with it.*

**Measurable? Yes, in two senses.** Classically, by ε-machine reconstruction from a time series.
Quantum-mechanically it has been measured: S19, Ghafari et al., PRX 9, 041013 (2019) — a photonic
implementation in which the memory about the past is carried in the **polarization of a single
photon** (one qubit) where the optimal classical simulator needs a three-level system; an earlier
photonic demonstration is Palsson et al., Science Advances 3, e1601302 (2017) (summary-level). Scale:
a single qubit of memory, a handful of time steps. This is a real lab measurement of a complexity-named
quantity, and that is precisely why it needs a precise disqualification.

**Why it is not `K^t` — the task asked for "precisely why". Four reasons, in increasing severity.**
1. **Wrong kind of object.** `C_μ` is a statistic of a *stationary stochastic process*. `K^t(x)` is a
   property of a *single string*. One is an entropy of a distribution; the other is a description
   length of an individual.
2. **No time bound anywhere.** `C_μ` has no resource parameter. `K^t`'s entire content is the
   resource parameter — that is what separates it from `K` and what makes Liu–Pass's equivalence with
   one-way functions possible.
3. **Opposite orderings on the crypto-relevant pair.** `C_μ` is zero for an i.i.d. source and zero for
   a trivially periodic one; a finite-state pseudorandom generator has `C_μ ≈` its state-register
   length. So on the pair (true randomness, pseudorandomness) `C_μ` goes **up** for the pseudorandom
   object while `K^t` goes **down**. `[Inference]` That looks at first like a distinguisher, and for a
   *toy* generator it genuinely is: a linear congruential generator has a small ε-machine and would be
   caught. But a cryptographically secure generator's ε-machine has on the order of `2^{seed}` causal
   states, and **reconstructing it from a polynomial-length record is exactly the distinguishing
   problem the generator is designed to defeat.** So the estimator `Ĉ_μ` computed from any feasible
   record returns the same value on a secure PRG stream as on true randomness. `C_μ` is a bucket-2
   observable and dies the bucket-2 death.
4. **Computability.** `C_μ` is computable given the process. `K` is not computable at all; `K^t` is
   computable only in exponential time. Different kinds of object, not different values of one object.

**Bucket 2. Verdict: measured (photonic, one qubit of memory, 2017/2019); a genuine structural
measure; not a `K^t` meter, and not a PRS distinguisher.**

### (g) Zurek's physical entropy `S = H + K`

**What it is.** Zurek, Phys. Rev. A 40, 4731 (1989) (S27): for an observer holding a measurement
record `d`,

    S_d  =  H_d  +  K(d)

*Plain reading: the entropy of a system, as seen by someone who has already written down some
measurements, is the ignorance that is still left over plus the length of the shortest description of
what they wrote down. The second term is the bookkeeping that stops a record-keeping demon from
beating the second law.*

**Any proposal for measuring the `K` term? None, and there is a theorem about why.** `K` is
uncomputable, and S1's own sentence is the physical statement of the obstruction: *if the physical
Church–Turing thesis is true, no real-world physical system can take `x` as input and output `K_U(x)`*.
Everything in the literature that calls itself a measurement of `K` is a **compressor**, and by
`mountain2_compression_tests.md` §0.5 a code word is a program, so

    pK^t(d) ≤ C(d) + O(1)

*Plain reading: whatever a real compressor achieves is an upper bound on the shortest fast program's
length — never a lower bound. A compressor can tell you a thing is simple; it can never tell you a
thing is complicated.*

`[Inference]` Zurek's `K` term is a consistency device that makes the second law come out right for
an observer who keeps records; it is not, and was never presented as, an instrument reading.

**Bucket 3. Verdict: not measurable, with a theorem (S1) saying so in physical language.**

### (h) Bekenstein-bound saturation as a compressibility test

**What it is.** `S ≤ 2πkRE/(ħc)` — a bound on the entropy of matter of energy `E` in a region of
radius `R`, often glossed as "the maximum information that can be stored".

**Why it is not a meter — two reasons, one of them a 2025 theorem.**
1. It bounds **entropy** — the logarithm of a number of states, or a von Neumann entropy — not the
   description length of a particular state. A state saturating the bound is one whose *ensemble* is
   maximally spread; it says nothing about whether that particular state was cheap to prepare.
   `[Inference]` And entropy is precisely the quantity that pseudoentanglement (§4) proves can be
   faked: a state with `ω(log n)` entanglement entropy across every cut is indistinguishable from one
   with `Θ(n)`. So a "maximal information density" test is a test of the one quantity that has already
   been shown not to be a meter.
2. S17, Hayden & Wang, *What exactly does Bekenstein bound?*, Quantum 9, 1664 (2025) [summary only]:
   they test the information-storage reading operationally, via channel capacity. Classical and
   quantum capacities of the Unruh channel obey the bound — but **zero-bits and their associated
   information-processing capability are not constrained by it**. The bound does not universally
   constrain information processing.

**Bucket 2 in form (entropy is measurable), but it measures a quantity proved fakeable. Verdict:
not a meter.**

---

## 3. Q2 — experimental status: what has actually been measured, and could it distinguish PRS from Haar

The operational test, stated once: **a complexity meter is exactly a PRS distinguisher.** If an
instrument returns different numbers on a pseudorandom state (built by a poly-size circuit) and a
Haar-random state (exponential complexity), it distinguishes the two ensembles, and by S5 (Ji–Liu–Song)
that refutes the existence of pseudorandom states, hence of quantum-secure one-way functions.

| what was measured | system | size | year | could it distinguish PRS from Haar? |
|---|---|---|---|---|
| OTOC / multiple-quantum coherences, via Hamiltonian time reversal | trapped ions, Penning trap, long-range Ising | **>100 ions**; up to 8-body correlations | 2017 (S8) | **No — proved.** S3 Theorem 1 (pseudochaotic RSED, LWE). Poly-copy estimation floor `Ω(1/poly n)` hides the decay. |
| OTOC, separating operator spreading from operator entanglement | superconducting, Sycamore | **53 qubits** | 2021 (S9) | **No — same theorem.** |
| OTOC ("Quantum Echoes"), deterministic observable, quantum-advantage claim | superconducting, Willow | **65 of 105 qubits**, ≈13,000× vs best classical sim | 2025 (S10) | **No — same theorem**, published three months before this measurement was announced. The advantage claim is about *simulating* the dynamics classically, not about reading complexity off an unknown state. |
| Rényi-2 entanglement entropy, randomized measurements | trapped Ca ions | partitions **up to 10 qubits** | 2019 (S11) | **No — proved.** S2 Corollary 1.0.1: pseudoentangled ensembles with a `Θ(n)` vs `ω(log n)` gap across all cuts, from any quantum-secure OWF. |
| Stabilizer 2-Rényi entropy ("magic"), randomized measurements | IBM `ibmq_quito`, `ibmq_casablanca` | a few qubits | 2022 (S13) | **No — proved.** S12, pseudomagic (PRL 132, 210602). |
| Statistical complexity `C_μ` / quantum ε-machine | photonic | memory = **1 qubit** (vs classical 3-level) | 2017, 2019 (S19) | **No** — §2(f), reason 3; and it is not a `K^t` quantity at all. |
| **Cross-entropy benchmarking (XEB) / Porter–Thomas output statistics** | superconducting, Sycamore | **53 qubits** | 2019 | **No.** Sampling in the computational basis is efficient, so a PRS reproduces the Haar statistics — bucket 2, definitionally not a meter. Against a *known* circuit (which is how XEB is actually used) it is bucket 1. Listed because it is the field's most-measured Haar-likeness statistic and the omission would look like an oversight |
| Krylov complexity | — | — | — | **Never measured directly.** See §2(b) for the qualification: the Lanczos coefficients are fixed by the moments of the operator autocorrelation `⟨O(t)O⟩`, which *is* measured routinely, so Krylov complexity is inferable in principle from a measured two-point function — with precision demands that grow with `n`. Bucket-1 verdict unchanged. |
| Spectral form factor | randomized-measurement protocols proposed | — | 2024 (S22) | **Not efficiently measurable**: the naive Hadamard test has exponentially small signal-to-noise. See §5. |
| Circuit complexity, complexity=volume, `K`, logical depth | — | — | — | **Never measured; not measurable.** Bucket 3. |

`[Inference]` **Stated carefully, because the loose version of this sentence is wrong.** It is tempting
to say the one-way-function principle has already been tested at 100+ ions and 65 qubits. It has not,
and §1 says why: in every OTOC experiment above the experimenter *holds the dynamics* and physically
applies `U†`, so these are bucket 1 and were never candidate meters even before S3. The defensible
sentence, and the one that should go in the paper, is narrower and still worth saying: **physics has
built the instrument at scale, and the theorem shows the instrument cannot read complexity even when
handed oracle access to `U` and `U†`.** That is a real strengthening — the no-go survives giving the
observer more power than a meter is allowed — and it is the honest form of the claim.

---

## 4. Q3 — the no-go results

### 4.1 The master no-go, which is definitional

S5, Ji–Liu–Song (CRYPTO 2018): a **pseudorandom state (PRS)** ensemble is a keyed family `{|φ_k⟩}`
such that (i) `|φ_k⟩` is preparable in polynomial time, and (ii) **no polynomial-time quantum
adversary given polynomially many copies distinguishes `|φ_k⟩` from a Haar-random state.** PRS exist
if quantum-secure one-way functions do (provable elementary construction from post-quantum
pseudorandom functions; the binary-phase conjecture was proved by Brakerski–Shmueli 2019).

*Plain reading: if one-way functions exist, then a computer can cheaply prepare states that no
efficient experiment — none, ever, on polynomially many copies — can tell apart from the most
complicated states that exist.*

**Therefore:** a laboratory measurement is (a) a physically implementable, hence efficient, quantum
procedure, applied to (b) polynomially many copies. **Every lab-measurable quantity returns the
Haar-random value on a PRS.** That is the theorem the task asked for — "a measurable quantity cannot
distinguish pseudorandom from Haar states" — and it is not a deep separate result; it is what PRS
*means*. The content is entirely in the existence of PRS, which follows from quantum-secure OWFs.

Two strengths should be kept apart, because the table's "proved not / conjectured not / open" column
is about the second:

- **(A) Definitional.** "Any efficient estimator returns the Haar value on a PRS." Automatic for every
  bucket-2 observable, the moment PRS exist. No named theorem needed.
- **(B) Named pseudo-X.** "Here are two efficiently preparable, computationally indistinguishable
  ensembles whose *true* values of X differ by a named gap." This is strictly more informative — it
  exhibits the low-X object — and it is what gets published.

### 4.2 The named pseudo-X theorems

| result | the gap | assumption | source |
|---|---|---|---|
| **Pseudoentanglement** | entanglement entropy `Θ(n)` vs `ω(log n)` **across all cuts simultaneously**, and simultaneously a PRS ensemble | any **quantum-secure one-way function** | S2, Cor. 1.0.1, ITCS 2024 |
| **Public-key pseudoentanglement** | volume-law vs near-area-law ground states of local Hamiltonians, indistinguishable | **LWE** | arXiv 2311.12017 (summary only) |
| **Pseudomagic** | large vs small non-stabilizerness (stabilizer Rényi entropy) | quantum-secure OWF / PRS | S12, PRL 132, 210602 (2024) |
| **Pseudochaotic dynamics = pseudo-OTOC** | genuinely chaotic vs a `k = ω(log n)` core in a random isometry; OTOCs negligible w.p. `1−negl(n)` | **Theorem 1 is unconditional** (random isometries + the poly-copy estimation floor). Sub-exponential LWE is needed only to implement the isometries in polylog depth and for the PRS claim | S3, Theorem 1, Nat. Commun. (2025) |
| **Pseudorandom density matrices** | mixed-state analogue | PRS | PRX Quantum 6, 020322 (2025) (summary only) |
| **Pseudocoherence, pseudopurity, pseudoimaginarity; general pseudoresources** | gaps as large as `Θ(n)` vs `0` for some resources | pseudorandomness / OWF; conversely **pseudoresources imply EFI pairs, hence quantum commitments** | S21, arXiv 2504.15025, 2504.17650 (summary only) |
| **Low-depth PRUs** | poly(log n)-depth 1D circuits, only short-range entanglement, indistinguishable from exponential-complexity unitaries | PRU assumptions | S20, Science (2025) |

S2's own sentence on the gravity application, verbatim from §3.4: *"It is natural to ask if this
connection between entanglement and geometry already implies the dictionary is exponentially hard to
compute."*

`[Inference]` That is the same move BFV made for complexity = volume, applied one rung down to
Ryu–Takayanagi. **Pseudoentanglement kills the entropy readout of the dictionary the way BFV kills the
volume readout.** Both are in B26's "gap" — cryptographic consequences with no known NP consequence.

### 4.3 The one positive result — a meter does exist, on a class that excludes everything we care about

S14, Grewal–Iyer–Kretschmer–Liang (ITCS 2023): an efficient algorithm distinguishes a Haar-random
`n`-qubit pure state from any state with **stabilizer fidelity ≥ 1/k**, using `O(k¹² log(1/δ))` copies
and `O(n k¹²  log(1/δ))` time (or `O(k³)` queries with access to the state-preparation unitary and its
inverse). Corollary: **`ω(log n)` T-gates are necessary** for any Clifford+T circuit to prepare a
pseudorandom state.

*Plain reading: there is a real complexity meter — it catches any state that is close to a state a
classical computer can simulate. And the theorem tells you exactly where it stops working: as soon as
the state has more than a logarithmic number of genuinely quantum gates in it.*

`[Inference]` This is the shape of every escape. Partial meters exist, and the class they work on is
always provably disjoint from the class a one-way function would produce. It is worth recording
because it shows the negative results are sharp, not vacuous.

---

## 5. Q4 — the inverse question: the family of pseudo-X results the principle predicts

The principle predicts: **for every efficiently measurable observable X, a pseudo-X result.** So the
right way to audit the literature is as a scoreboard.

| observable X | pseudo-X status | measured in a lab? |
|---|---|---|
| entanglement entropy / Rényi entropies | **proved** (2022/2024) | **yes** — 10 qubits, 2019 |
| non-stabilizerness / magic | **proved** (2024) | **yes** — IBM, few qubits, 2022 |
| OTOC / scrambling | **proved** (July 2025) | **yes** — 100+ ions 2017, 53 qubits 2021, 65 qubits 2025 |
| coherence, purity, imaginarity | **proved** (pseudoresources, 2025) | yes, routinely |
| any expectation value / any efficient estimator | **proved, definitionally** (§4.1) | yes, by definition |
| circuit complexity itself | **proved** (that is what PRS *is*) | **no** |
| **Krylov complexity / spread complexity** | **open** — no pseudo-Krylov theorem found in ~4 targeted searches | **no** — protocols only |
| **spectral form factor / level statistics** | **open, and pointing the other way** — see below | **no**, not efficiently |
| Nielsen complexity | not applicable — undefined for an unknown state | no |
| complexity = volume / action | **proved contrapositively** (BFV 2019, B26) | no, and not measurable |

**Is there an observable that is (a) lab-measured and (b) still open? As of July 2025, no — and the
case that closed is the important one.** OTOC was exactly that observable. It was measured at serious
scale three times over eight years, it is the flagship of Google's 2025 quantum-advantage claim, and it
was the one chaos diagnostic with no no-go attached. Lee–Kwon–Cho closed it. **If B30 had been run in
June 2025, the answer to this question would have been "yes, OTOC — open in the query-access model",
and the recommended experiment would have been the one the theorem now says is pointless.** The
qualifier matters and is not a hedge: §1's trichotomy would have called OTOC bucket 1 regardless, since
the protocol requires applying `U†`. What was open in June 2025 was the narrower question — given
oracle access to `U` and `U†`, does the OTOC separate low from high complexity — and that is what
closed. Recorded as a calibration note: the negative direction here is not an absence of results, it is
a live research programme that keeps arriving on schedule.

**Two near-misses, recorded because they show the mechanism rather than an exception.**

1. **Spectral form factor.** S3 notes that pseudochaotic RSED has *"exponential degeneracies"*
   deviating from Wigner–Dyson level statistics, while the spectral form factor *"closely follows"*
   the embedded subsystem's behaviour. So the SFF is **not fooled** by their construction — a genuine
   asymmetry with the OTOC. `[Inference]` But the escape is by inefficiency, not by insight: S22
   states that the naive Hadamard test for `Tr U(t)` has *exponentially small signal-to-noise*, because
   `Tr U(t)/2ⁿ` is exponentially small for a scrambling `U`. **An observable escapes the no-go exactly
   when it is not efficiently estimable** — which is bucket 3, which is the BFV loophole again. Not a
   counterexample to §1; an instance of it. `[Speculation]` If someone found an efficient SFF estimator
   on a class including RSED, that would be a PRS distinguisher and hence a refutation of
   sub-exponential LWE — so one should expect the estimator not to exist, and a "pseudo-SFF" theorem
   for a modified construction is a natural next paper.
2. **Krylov complexity.** Both halves are missing: no pseudo-Krylov theorem, and no measurement.
   `[Inference]` A pseudo-Krylov theorem should be easy and is probably not worth anyone's time,
   because Krylov complexity is bucket 1 — it is a functional of a Hamiltonian you were given, so the
   cryptographic question does not even arise until someone defines a Krylov complexity of an *unknown*
   dynamics accessible only through poly-many queries. `[Speculation]` If someone does define that, the
   S3 machinery applies almost verbatim, since RSED's embedded `k`-qubit core would dominate any
   query-accessible Lanczos reconstruction.

---

## 6. Q5 — the classical side

**The classical master no-go is the same statement with the quantum removed.** A pseudorandom generator
(Blum–Micali 1984; Yao 1982; from any one-way function by HILL 1999) is a polynomial-time map
`G : {0,1}ⁿ → {0,1}^{poly(n)}` whose output no polynomial-time statistical test distinguishes from
uniform (S29, **[Unverified — cited from memory]**, textbook-level). **A classical laboratory
instrument applied to a physical record is a polynomial-time statistical test.** So under the one-way-
function principle, no classical efficient measurement of a record distinguishes a pseudorandom record
from a random one, and in particular none of them reads off `K^t`.

*Plain reading: the classical version of §4.1. If one-way functions exist, a data stream can be
produced by a tiny program and still pass every test any instrument can run in reasonable time.*

**Proposed classical measurements of `K` or of depth of a physical record: all are compressors.**
Normalized compression distance (Cilibrasi–Vitányi), CTM/BDM (Zenil et al.), Lempel–Ziv entropy-rate
estimators in physics, and the recent time-series work (e.g. compression-based estimation of liquid
diffusion coefficients, PRL 133, 068001 (2024), summary-level). **All of them give upper bounds only**,
and the reason is one line from this folder's own §0.5 (`mountain2_compression_tests.md`): a code word
*is* a program, so `pK^t(x) ≤ C(x) + O(1)`. Three consequences, restated here for completeness because
they bound what any classical "complexity measurement" can ever mean:

- Compressor **failure** proves nothing — CLAUDE.md rule 7, permanent.
- Compressor **success** on `(z, f(z))`, to `O(log n)` bits on a `1/poly(n)` fraction, **is an
  inverter** (Lemma 8) — the inverter is the result; the measurement is a side effect.
- Therefore the only classical "complexity meter" that could ever exist would announce itself by
  breaking a candidate one-way function, not by producing a number.

**Algorithmic thermodynamics** (Baez–Stay 2010, S30, **[Unverified — cited from memory]**) is a formal
analogy — Gibbs ensembles over programs weighted by length, runtime and output — not an experimental
programme. No experiment has been proposed or run.

**The closest thing to a classical theorem in the right shape is S1's Eq. (2) and it cuts both ways.**
`Q_dom(x) = kT ln2 · K(x | φ_M(x))`: the heat of the best physically-buildable machine on input `x`
equals the conditional Kolmogorov complexity of the input given the output — *literally the reverse-
conditional description length our `σ` is built from.* But (i) the realisation achieving it is not
computable, so it is not buildable; (ii) the complexity is unbounded-time `K`, not `K^t`, so it is not
our object; and (iii) the quantity an experimenter actually controls — the minimum heat over inputs
producing a desired output — is `O(1)`, independent of the output. `[Inference]` So: heat tracks
description length **along the input**, and is blind to it **across outputs**. That is a sharper
version of `MOUNTAIN2_VERDICT.md` item 3 than the abstract supports, and it should replace it.

---

## 7. The table

Columns as specified, plus the bucket of §1. "PRS-distinguisher status" is the (B)-strength named
result where one exists, the (A)-strength definitional statement otherwise.

| observable | bucket | claimed to track | theorem linking it to computational complexity (or none) | measured? (system, size, year) | PRS-distinguisher status | verdict as a complexity meter |
|---|---|---|---|---|---|---|
| **Complexity = volume** (Susskind; Stanford–Susskind) | 3 | circuit complexity of the boundary state | **Conjecture only** (no gate set, tolerance or reference state fixed). BFV 2019: efficient dictionary + CV ⇒ meter ⇒ breaks PRS ⇒ no qOWF. S15: an *infinite class* of bulk observables shares the diagnostics, so the dual is not pinned down | **No.** Bulk quantity; Susskind 2003.01807 argues horizons block the readout | **Would be a distinguisher if it existed** — that is BFV's whole argument | **Hypothetical meter with a real theorem, unmeasurable by construction.** The only genuine gap entry (B26) |
| **Complexity = action** (Brown et al., PRL 116, 191301) | 3 | same | same conjecture, different bulk region (WDW patch) | **No** | same | same |
| **Krylov complexity** (Parker et al. 2019) | 1 | operator growth / "complexity of evolution" | **Yes, one-directional**: S6 (PRL 132, 160402) — time-averaged Krylov **upper-bounds** Nielsen complexity under a penalty schedule custom-tailored to the Krylov basis; S7 — saturation only for small precursors. Not standard circuit complexity | **Not directly.** Protocols proposed (2024–2026); SKQD on hardware is a different object. Inferable in principle from the measured autocorrelation `⟨O(t)O⟩`, whose moments fix the Lanczos coefficients, at precision growing with `n` | **Open** — no pseudo-Krylov theorem exists | **Not a meter: it is a functional of a Hamiltonian you are given.** Open only because the question has not been asked |
| **OTOC / scrambling** | 1 (protocol needs `U†`), 2 (estimand) | scrambling; often loosely "complexity" | **Yes, negative, twice.** (i) OTOC saturates at `t_*~log N` while complexity grows linearly to `t~e^S` — the latter now a theorem (Haferkamp et al., Nat. Phys. 18, 528, 2022); Roberts–Yoshida tie OTOCs to `k`-designs, not complexity. (ii) **S3 Theorem 1** | **Yes — the best-measured case.** >100 ions Penning trap 2017; 53-qubit Sycamore 2021; **65-qubit Willow 2025** | **Proved not — unconditionally** for poly-sample OTOC estimation (S3 Thm 1); LWE only for efficient implementation and the PRS statement | **Killed, July 2025.** Was the last measured-and-open candidate, and the no-go holds even given oracle access to `U`, `U†` |
| **Nielsen geometric complexity** | 1 | circuit complexity (continuum version) | It *is* a definition of circuit complexity, not a link to one | **No.** One low-credibility claim of measurability (S28, SCIRP) — recorded, dismissed | **Would be a distinguisher by definition** | **Not a meter: geodesic length in the unitary you already hold** |
| **Thermodynamic depth** (Lloyd–Pagels 1988) | 2 | "physical complexity", computably | **Yes, negative**: S4 — the dive equals the reverse-time Shannon entropy rate, so depth measures macroscopic randomness, not structure; and the macrostate choice is unspecified | Not as such (it is an entropy rate in disguise, and those are measured constantly) | **Proved not** — it is maximal on noise, which is the wrong direction | **Killed in 1999** |
| **Bennett logical depth** (1988) | 3 | computational history | **No link to a lab quantity.** S1 does **not** cover it: full-text grep finds no `depth`, no time-bounded complexity, no runtime cost. S18 offers a *proxy* `L_d` on two hand-built 4-branch circuits | **No** | **[Inference]** irrelevant: a PRG output is shallow and true randomness is shallow, so depth does not separate the crypto-relevant pair | **Not measurable, and the wrong target anyway** |
| **Thermodynamic complexity / heat** (Kolchinsky–Wolpert 2020) | 3 | `K` of the output | **Yes, negative and sharp** (read this session): thermodynamic complexity of any output is `O(1)`, Eq. (26); `Q_dom(x)=kT ln2·K(x\|φ(x))` but the dominating realisation is **not computable**; and their own line — no real physical system can output `K_U(x)` if the physical Church–Turing thesis holds | Every Landauer/demon experiment measures heat; none measures this | **Proved not** (for `K`; `K^t` untouched) | **Closed. The cleanest theorem in the whole note** |
| **Statistical complexity `C_μ`** (Crutchfield) | 2 | predictive memory of a *process* | **No link to `K^t`.** Four precise reasons, §2(f): process vs string; no time bound; opposite ordering on (random, pseudorandom); computable vs not | **Yes** — photonic quantum ε-machine, memory = **1 qubit** vs classical 3-level, 2017/2019 | **Proved not** by the definitional route: a secure PRG's ε-machine has `~2^{seed}` causal states, so `Ĉ_μ` from any feasible record matches true randomness `[Inference]` | **A real structural measure of something else** |
| **Zurek physical entropy `S=H+K`** (1989) | 3 | the `K` term is description length | **No measurement proposal exists**; S1's physical-Church–Turing sentence is the obstruction; every candidate is a compressor, hence an upper bound (§0.5) | **No** | **Proved not** (same as the row above) | **A bookkeeping device, not an instrument** |
| **Bekenstein saturation / max. information density** | 2 | "maximal information" ⇒ incompressibility | **No.** It bounds entropy/capacity, not description length. S17: zero-bits are not constrained by the bound | Entropy is measured routinely; saturation is not a test anyone runs | **Proved not** — entropy is exactly what pseudoentanglement fakes (S2) | **Not a meter; it constrains the wrong quantity** |
| **Entanglement entropy / Rényi-2** | 2 | "complexity" via RT / holography | **Yes, negative**: S2 Cor. 1.0.1, gap `Θ(n)` vs `ω(log n)` across all cuts, from any quantum-secure OWF | **Yes** — trapped ions, partitions up to **10 qubits**, 2019 | **Proved not** (2022/2024) | **Killed.** The template for every later pseudo-X |
| **Stabilizer Rényi entropy (magic)** | 2 | non-classicality / "complexity" | **Yes, negative**: S12 pseudomagic (PRL 132, 210602, 2024). **Partial positive**: S14 — efficient distinguisher for stabilizer fidelity `≥1/k`, and `ω(log n)` T-gates necessary for PRS | **Yes** — IBM `ibmq_quito`/`ibmq_casablanca`, few qubits, 2022 | **Proved not** in general; **proved yes** on the stabilizer-fidelity-`≥1/k` class | **Killed in general; a real meter on a class that excludes one-way functions** |
| **Spectral form factor / level statistics** | 3 (not efficiently estimable) | chaos, indirectly complexity | None. S3 reports RSED's *"exponential degeneracies"* deviate from Wigner–Dyson, so the SFF is **not fooled** | **No** — S22: naive Hadamard test has exponentially small signal-to-noise | **Open**, but it escapes by inefficiency, not insight `[Inference]` | **The one observable that dodges S3 — and only because you cannot measure it** |
| **Compression of a classical record** (NCD, CTM/BDM, LZ) | 2 (classical) | `K`, `K^t` | **Yes, and it is an inequality, not a link**: `pK^t(x) ≤ C(x)+O(1)` (§0.5). Success on `(z,f(z))` **is an inverter** (Lemma 8); failure proves nothing (rule 7) | Yes, constantly, in a dozen fields | **Proved not**, classically: PRG output passes every poly-time test (S29) | **Upper bounds only, permanently** |

---

## 8. Verdict

**Is there any lab-measurable observable for which "is it a complexity meter" is open rather than
known-negative?** **No — not one, as of July 2025.** The reason is structural and was visible before
the search began: a complexity meter is, by definition, a distinguisher between pseudorandom and
Haar-random states, so if quantum-secure one-way functions exist then *every* quantity estimable by an
efficient procedure on polynomially many copies is provably not a meter, and the literature has been
converting that definitional fact into named theorems one observable at a time — pseudoentanglement
(2022) for entanglement entropy, pseudomagic (2024) for non-stabilizerness, pseudoresources (2025) for
coherence, purity and imaginarity, and **pseudochaotic dynamics (Lee–Kwon–Cho, Nature Communications,
July 2025) for the out-of-time-order correlator, which was the last candidate that had been both
measured at scale and left open.** The quantities that survive — complexity = volume and action,
Zurek's `K`, Bennett's logical depth, Kolchinsky–Wolpert's dominating heat function, the spectral form
factor — survive exactly because they are *not efficiently measurable*: a bulk volume behind a horizon,
an uncomputable function, a non-constructible realisation, an exponentially small trace. That is the
Bouland–Fefferman–Vazirani loophole restated as a rule: **an observable escapes the no-go precisely by
being unmeasurable, which is why the one-way-function principle's stock of ruled-out physical theories
has entries but no falsifying observation.** Three of the candidates on B26's divergent list are worse
than unmeasurable — they are the wrong quantity: thermodynamic depth was proved in 1999 to be a
reverse-time entropy rate, logical depth assigns "shallow" to both a pseudorandom stream and true
randomness so it cannot separate the pair the principle is about, and Bekenstein saturation constrains
entropy, which is the one quantity pseudoentanglement proves can be faked. **What experiment would
still make something a test of the principle?** Only one shape survives, and it is not a meter: an
experiment whose *success* is an inversion rather than a reading. Concretely — run the S3
pseudochaotic construction on the hardware its authors name (Rydberg arrays or trapped ions, "a few
dozens of qubits"), measure the OTOC alongside a genuinely chaotic control, and publish the null
separation as the first *deliberate* demonstration that the instrument cannot read complexity rather
than an accidental one; then attempt, and report the failure of, an efficient estimator of the spectral
form factor on that same ensemble, since `[Speculation]` an efficient SFF estimator separating them
would plausibly yield a PRS distinguisher and so bear on sub-exponential LWE. Both are null-result
experiments by construction, which is the honest form of the claim: **a complexity meter announces
itself by breaking a candidate one-way function, never by producing a number**, so the principle's only
observational signature is the continued absence of the instrument — and after 2017, 2019, 2021, 2022
and 2025 that absence is an experimental record with 100 ions and 65 qubits in it, not a philosophical
position. One correction the record now forces: S3's Theorem 1 is **unconditional**, so the OTOC's
failure as a meter does not rest on any cryptographic assumption at all — the instrument is blind
whether or not one-way functions exist, and cryptography is needed only to build the fake cheaply.

---

## 9. For the paper, and threads

**Paper edits (owner decides; none applied here).**

- **Appendix row 17 / §8.2 — correction to `MOUNTAIN2_VERDICT.md` item 3.** Kolchinsky–Wolpert 2020,
  now read: quote the physical-Church–Turing sentence (*"no real-world physical system can take any
  desired string `x` as input and produce the value of `K_U(x)` as output"*) rather than the abstract's
  constant-bound line, and state the three-part reading of §6: heat tracks description length along the
  input (`Q_dom = kT ln2 · K(x|φ(x))`) and is blind to it across outputs (`min Q = O(1)`), and the
  realisation achieving the first is non-computable. **Add the caveat the abstract hides, in exactly
  these words so that nobody re-reads the abstract and re-overclaims: Kolchinsky–Wolpert's result is
  about heat and about unbounded-time `K`; `K^t` and logical depth do not appear in the paper at all
  (full-text grep, §2e).**
- **§8.5, after the BFV paragraph.** One paragraph: the principle predicts a family of pseudo-X results
  and the family is arriving — pseudoentanglement 2022, pseudomagic 2024, pseudochaotic/pseudo-OTOC
  2025 — with the §7 table's five rows as the evidence and S2's Ryu–Takayanagi sentence quoted. This is
  the closest the principle has to a *confirmed prediction*, and it should be stated as that and not
  more: the theorems follow from the assumption, so they are consistency, not confirmation.
- **§6 / §8.5.** One sentence, in the careful form of §3's closing note and **not** the loose one: the
  OTOC has been measured at >100 ions (2017), 53 qubits (2021) and 65 qubits (2025), and S3 proves
  unconditionally that no such measurement can detect low complexity **even when the observer is handed
  oracle access to `U` and `U†`** — which is more power than a complexity meter is allowed. Do *not*
  write that physics has already tested the principle three times: those experiments hold the dynamics,
  so they are bucket 1 and were never candidate meters.
- **Do not** claim that any observable is a candidate meter. The §8 verdict is negative and should be
  written negatively.

**Threads.**

- **B31 is being written concurrently** (`b31_instance_checkers.md`); not touched by this note.
- **B32 (reading).** Read S3 (Lee–Kwon–Cho) §§2–4 and the Theorem 1 proof line by line — it is the
  load-bearing new source of this note and is currently at PMC-summary level. Also S2 §3.4 in full,
  and S14 (Grewal et al.) for the exact class boundary, which is the sharpest statement anywhere of
  where a real meter stops working.
- **B33 (the small theorem worth writing).** `[Speculation]` **"Pseudo-SFF"**: S3's construction is
  *not* fooled by level statistics. Either (i) modify RSED so the spectral form factor is also fooled,
  or (ii) prove that no efficient SFF estimator exists on that ensemble under LWE. Either outcome
  sharpens §1's claim that escape from the no-go is always by inefficiency, and (ii) is probably the
  easier and the more useful.
- **B34 (classical, and it connects to B22/R1).** The classical statement of §4.1 — "a laboratory
  instrument is a statistical test, therefore no classical instrument reads `K^t`" — is one paragraph
  and belongs next to Theorem 2's disconfirmability clause in §0.5. It is the classical twin of the
  PRS no-go and the paper currently has neither stated.
- **B35 (divergent, on the target again).** Every candidate in this note was a *state or process*
  functional. The round that has not been run: **do not ask for a meter at all.** B26 diverged on
  which theory inverts one-way functions; B30 diverged on which quantity meters complexity; both
  funnelled to the same wall. The un-run target is the *inverse of the inverse*: which physical
  situation would force a **one-way function to exist** — i.e. which physical theory, if true, would
  *prove* the principle rather than refute it (candidate directions with no judgment: horizons as
  complexity-hiding devices per Susskind 2003.01807; the KPT interior code which *assumes* the
  principle, B26 row 12; black-hole complementarity as a cryptographic commitment; measurement-induced
  phase transitions as a hardness threshold; the thermodynamic-uncertainty-relation literature). A
  physical theory that *implies* one-way functions exist would be the first entry in a stock nobody has
  built, and it is a different target from everything in passes 16–20.

## 10. Audit list additions (copy to HANDOFF §8)

| item | current status | what is needed |
|---|---|---|
| Lee–Kwon–Cho, Nat. Commun. 16 (2025), pseudochaotic dynamics | PMC full-text summary; abstract verbatim; Theorem 1 statement second-hand | read §§2–4 and the Theorem 1 proof |
| Ji–Liu–Song, CRYPTO 2018 | **summary only** in both B26 and B30 — and it is load-bearing in both | read the PRS definition and the qOWF ⇒ PRS theorem verbatim |
| Aaronson et al., pseudoentanglement, ITCS 2024 | ar5iv: abstract, Cor. 1.0.1, §3.4 verbatim; rest unread | read §3.4 in full for the AdS/CFT claim's exact scope |
| Crutchfield–Shalizi, PRE 59, 275 (1999) | summary only | read; the "dive = reverse-time entropy rate" result is quoted second-hand |
| Lloyd–Pagels 1988; Bennett 1988; Zurek 1989 | **[Unverified — cited from memory]** | read at least Bennett's definition of depth at significance `s` before the §2(e) `[Inference]` is used in the paper |
| Parker et al., PRX 9, 041017 (2019) | **[Unverified — cited from memory]** | read the definition of Krylov complexity |
| Nielsen et al., Science 311, 1133 (2006) | **[Unverified — cited from memory]** | low priority; the row's verdict does not depend on the details |
| Roberts–Yoshida, JHEP 04 (2017) 121 | summary only | read for the exact `k`-design statement, used in §2(c) reason 1 |
| Haferkamp, Kothakonda, Faist, Eisert, Yunger Halpern, Nat. Phys. **18**, 528 (2022) | summary only | read the theorem statement; it is the half of §2(c) reason 1 that is now proved rather than conjectured |
| Yao 1982 / Blum–Micali / HILL 1999 | **[Unverified — cited from memory]**, textbook-level | cite properly if §6 goes in the paper |
| Baez–Stay, *Algorithmic thermodynamics* (2010) | **[Unverified — cited from memory]** | low priority; recorded only to say no experiment exists |
| Grewal–Iyer–Kretschmer–Liang, ITCS 2023 | summary only | read for the exact class boundary (`stabilizer fidelity ≥ 1/k`, `O(k¹²)` copies) |
| S28, JAMP 13 (2025), "circuit complexity as a physical observable" | abstract only; **low-credibility venue** | do not cite; recorded so it is not re-found and mistaken for a result |
