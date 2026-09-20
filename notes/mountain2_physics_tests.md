# Mountain 2: is there a falsifiable prediction for "NP-hardness as a physical principle"?

Agent research note, pass 20. Date: 2026-09-15.
Scope: the seven questions in the ticket. Context read first: `pass16/ENTROPY_PRODUCTION.md` §1, §1.4,
§2.6, §8.4, §8.5, Appendix A.1/A.2, References; `pass20/SYNTHESIS.md` (including the Fable viability
review appended to it).

**Headline, stated plainly.** For the *law* — "no fast physical process solves NP-complete problems" —
there is no direct falsifiable prediction, and the sources say why in their own words. But the survey
turned up more than "nobody has one":

1. **One live experiment is a genuine test of the law, by an indirect route, and it was written down in
   June 2026.** Fox, Karamchedu and Mygdalas prove that semiclassical gravity solves NP-complete
   problems in polynomial time, and read that as a physical argument *against* semiclassical gravity.
   The gravitationally-induced-entanglement (GIE / Bose–Marletto–Vedral) experiment, not yet performed,
   is the lab measurement that bears on it. A clean null result there is evidence gravity is classical,
   which by their theorem puts NP in P. **That could come out wrong.** It is the best candidate found.
   Two qualifiers travel with it: joining the theorem to the experiment is this note's [Inference], not
   their sentence; and the underlying "non-linearity ⇒ NP easy" step is established only for error-free
   dynamics (Aaronson §5 says so; Fox et al. never mention noise).
2. **Several already-performed measurements could have gone the other way and did not**: precision tests
   of the linearity of quantum mechanics (Weinberg parameter), and Aaronson's own soap-bubble
   experiment. Both test *necessary conditions* of the law rather than the law itself.
3. **The one completed falsification in the whole literature is on the candidate side, and it was
   falsified by an algorithm, not by a physics measurement**: the Pappu et al. "physical one-way
   function" claim that the device "admits no compact mathematical representation" is false for
   integrated optical PUFs, which are polynomial-time PAC-learnable even with injected noise.
4. **The thermodynamic side gives no quantity that is large iff a task is hard, and there is a theorem
   saying it cannot.** Kolchinsky–Wolpert: the thermodynamic complexity of an output is bounded by a
   *constant* while its Kolmogorov complexity is unbounded.
5. **Constructor theory supplies the missing template** — how a "task is impossible" principle is
   tested — but its impossibilities carry no resource bound, so "impossible for any *fast* process" is
   not a statement of the theory's type.

---

## (a) Read status ledger

Conventions of the paper apply: **Read** names the parts read; **fetched (targeted)** means a WebFetch
answered a prompt against the source and I did not read the text myself; **abstract-only**;
**[Unverified — cited from memory]**.

| source | status |
|---|---|
| Aaronson, *NP-complete problems and physical reality*, arXiv quant-ph/0502072 | **Read.** §§3, 4, 4.1, 4.2, 5, 5.1, 6, 7, 8, 9, 10 read line by line this session from the local full text `pass16/sources/aaronson2005_quant-ph0502072.txt`. §§8.1 and 11 skimmed. |
| Aaronson 2016, *P =? NP*, footnote 20 | **Read** (the footnote, verbatim, from local `aaronson2016_pnp_survey.txt`). |
| Aaronson, Kardes, Hartle 2025, Suppes Lecture slides | **Read** (targeted: slides carrying "demon", "predict", "experiment", from the local `.txt`). Searched for a 2026 preprint: **none found**; still slides-only. |
| Wolfram 2023, *Computational foundations for the second law* | Prior full read is `pass04/wolfram2023.md` (owner's earlier session, part 1 read in full). This session: keyword grep of that note for falsifi/predict/experiment/test (4 hits, none a prediction) + **one fetched (targeted)** re-query of the live page for any testability passage. |
| Marletto, Deutsch, Vedral, *Tests of constructor theory*, arXiv 2606.07352v1 (5 Jun 2026) | **Read** §1, §1.1 ("Testing constructor theory"), §2.3 (BMV/GIE), the work-media passage in §3; grep across the whole text for refut/falsif/efficien/complexity/resource. §§2.4, 4–5 **skimmed by heading**. PDF pulled and converted locally. |
| Fox, Karamchedu, Mygdalas, *Semiclassical Gravity Efficiently Solves NP-Complete Problems*, arXiv 2606.14806v1 (11 Jun 2026) | **Read** abstract, §I, §II (the PECTT statement), §V Discussion incl. footnotes 9–12. §§III–IV (Schrödinger–Newton derivation, the algorithm) **skimmed by heading**. PDF pulled and converted locally. |
| Kolchinsky, Wolpert, *Thermodynamic costs of Turing machines*, Phys. Rev. Research 2:033312 (2020), arXiv 1912.04685 | **abstract-only** (fetched, verbatim quotes obtained). |
| Yadav, Caravelli, Wolpert, *Entropy production bounds for systems running computer programs*, PNAS Nexus (2026) | **fetched (targeted)**; not read by me. Bibliographic details as returned by the fetch; volume/page **[Unverified]**. |
| Wolpert, *The stochastic thermodynamics of computation*, arXiv 1905.05669 (J. Phys. A 2019) | **abstract-only** via search summary. |
| Pappu, Recht, Taylor, Gershenfeld, *Physical one-way functions*, Science 297:2026 (2002) | **abstract-only** (the "admits no compact mathematical representation" phrase is from the abstract). |
| Rührmair, Sehnke, Sölter, Dror, Devadas, Schmidhuber, *Modeling attacks on PUFs*, CCS 2010 (ePrint 2010/251) | **abstract-only** via search summary. |
| Rührmair et al., *Optical PUFs Reloaded*, ePrint 2013/215 | **abstract-only** via search summary. |
| Albright, Gelfand, Dixon, *Polynomial bounds for learning noisy optical PUFs and connections to LWE*, arXiv 2308.09199 (2023); journal version *Learnability of optical PUFs through the lens of LWE*, IEEE Trans. Inf. Forensics Secur. 20:886 (2025) | **abstract-only** (arXiv abstract fetched verbatim; journal version via search summary). |
| King et al., *Scaling advantage in approximate optimization with quantum annealing*, Phys. Rev. Lett. 134:160601 (2025), arXiv 2401.07184 | **abstract-only** via search summary. Author list beyond "King et al." **[Unverified]**. |
| Ringbauer et al., *Experimental simulation of closed timelike curves*, Nature Communications 5:4145 (2014) | **abstract-only** via search summary. |
| Bollinger et al. (⁹Be⁺) and Chupp–Hoare (²⁰¹Hg) linearity tests, PRL 1989/1990; cryogenic RF bound arXiv 2411.09611 (2024) | **abstract-only** via search summary; the numerical limits (4×10⁻²⁷, 2.0×10⁻²⁷ of binding energy per nucleon) are as reported in that summary and are **[Unverified]** against the papers. |
| Bérut et al. Nature 483:187 (2012); Toyabe et al. Nat. Phys. 6:988 (2010); Jun, Gavrilov, Bechhoefer PRL 113:190601 (2014) | **abstract-only** via search summary. What was measured (heat, work) confirmed; I did not open them. |
| Information engines with feedback delay: PRE 109:034121 (2024); "Imprecise Maxwell's demon with feedback delay" (2025); *Experimental realizations of information engines: beyond proof of concept*, arXiv 2501.13593 | **abstract-only** via search summaries. |
| Borsten, Kim, *Limits to computational acceleration imposed by QFT and quantum gravity*, arXiv 2604.00182 (2026) | **abstract-only** (fetched). |
| Bennett 1973; Landauer 1961; Crooks 1999; HILNO 2023 | already **Read** in pass 16; used here as already-read background, not re-read. |
| Bao, Bouland, Jordan (non-linear QM ⇒ NP easy); Abrams–Lloyd 1998; Aaronson–Watrous (P_CTC = PSPACE); Baker–Gill–Solovay; Razborov–Rudich | **[Unverified — cited from memory]**, except where reached through Fox et al., which is Read. Goes on the audit list. |

---

## 1. Aaronson 2005 §§3–9: which proposals are *tests*, and what is the status now

**What the paper actually does.** Eleven sections. Exactly **one** contains a physical measurement
performed by the author; everything else is theory, and the theory is of two kinds — complexity lower
bounds in a black-box model, and physics arguments about energy and precision.

### 1.1 The one real measurement: soap bubbles (§3)

This is the only place in the paper where an observation could have come out the other way and was made
to come out. The provocation is on the record: a newsgroup poster wrote

> "I'd be willing to make a gentleman's bet that no one can site [sic] a paper which describes an
> experiment that shows that the global minimum is not always achieved with soap bubbles."

Aaronson's answer (§3):

> "Though I was unable to find such a paper, I was motivated by this post to conduct the experiment
> myself. I bought two 8" × 9" glass plates… I concentrated on instances with 3 to 7 vertices…
> The result was fascinating to watch: with 3 or 4 pegs, the optimum tree usually is found. However, by
> no means is it always found, especially with more pegs."

He names the failure modes himself, and the one that is not explainable as error:

> "I also sometimes found triangular 'bubbles' of three Steiner vertices—which is much harder to
> explain, since such a structure could never occur in a Steiner tree."

**Reading.** This is a test of a **CANDIDATE** (soap films as a Steiner-tree solver), not of the law.
Its falsifier is clean and was live before the run: *soap films reliably reach the global Steiner
optimum, with the success rate not decaying as pegs are added.* It came out the other way, and the
paper says the mechanism generalises: "There are other proposed methods… such as spin glasses and
protein folding. All of these methods are subject to the same pitfalls of local optima and potentially
long relaxation times." On protein folding specifically he gives an argument, not a measurement:
proteins probably evolved not to have local optima, "but this also means that if we engineered an
artificial protein to represent a hard 3SAT instance, then there would be no particular reason for it
to fold as quickly or reliably as do naturally occurring proteins." **Status 2026:** I found no paper
reporting the engineered-3SAT-protein experiment. Protein folding remains NP-hard as a mathematical
model (HP lattice model) with no physical scaling experiment attached.

### 1.2 The proposals he treats as *tests of the assumption*, and their status

He does not label them "tests"; §10 makes the structure explicit instead. The assumption earns the
status of a physical principle if (1) there is evidence for it and (2) accepting it constrains new
theories. Sections 4–9 supply (1) by showing that plausible-looking routes fail *on physics*, and §10
converts (2) into four bullets. Those four bullets are the paper's falsifiable content.

| §  | proposal | is it a test? | status 2024–2026 | could a measurement have gone the other way? |
|---|---|---|---|---|
| 4 | quantum computing, brute-force search | no — a black-box lower bound (Bennett–Bernstein–Brassard–Vazirani, Grover tight) | unchanged | no; this is a theorem |
| 4.2 | quantum adiabatic algorithm | **yes, and he names the experiment**: "the crucial experiment (which has not yet been done) would be to compare the adiabatic algorithm head-on against simulated annealing and other classical heuristics" | **partly done.** King et al., PRL 134:160601 (2025) report a scaling advantage for quantum annealing over parallel tempering with isoenergetic cluster moves on 2D spin glasses — but for **approximate** optimization. Per the same literature, "a computational quantum advantage in exact optimization using quantum annealing hardware has so far remained elusive." D-Wave's March 2025 *Science* simulation claim is contested by a Flatiron tensor-network method. | **yes** — and it is the closest thing in the whole survey to Aaronson's own proposed experiment. Rule 7 caveat is permanent: it shows resistance to *known* classical algorithms. |
| 5 | non-linear corrections to Schrödinger | **yes, indirectly** — Abrams–Lloyd: any non-linear gate gives NP (and #P, and with arbitrary gates PSPACE) in polynomial time | precision linearity tests are real measurements; limits on the Weinberg parameter ~10⁻²⁷ of the binding energy per nucleon (⁹Be⁺, ²⁰¹Hg); improved cryogenic RF bound in 2024 (arXiv 2411.09611) | **yes.** A non-zero Weinberg parameter would have been a direct falsification of the assumption via Abrams–Lloyd. The numbers are **[Unverified]**. |
| 5.1 | hidden variables; Valentini non-equilibrium matter | no — his own result puts history-sampling at SZK, not NP | no non-equilibrium matter found (not searched this session) | in principle yes; no experiment run |
| 6 | relativity computing; analog computing; Malament–Hogarth | no — killed by energy and by the holographic bound | the holographic/Bekenstein bound is standing physics | no |
| 7 | quantum gravity | he poses it as a **benchmark for the theory**: "to anyone who wants a test or benchmark for a favorite quantum gravity theory… can you define Quantum Gravity Polynomial-Time?" | **this is the question Fox et al. 2026 answer for semiclassical gravity — see §6 below** | see §6 |
| 8 | closed timelike curves | no — a complexity characterisation | Ringbauer et al. (Nat. Commun. 2014) ran a photonic **simulation** of a Deutsch CTC. It is a simulation via entanglement and post-selection, not a CTC; no NP-hard speedup is obtained or claimed. It tests nothing about the law. | no |
| 9 | anthropic computing | no — a joke that turns into BPP_path / PostBQP = PP | unchanged | no |

### 1.3 The statement of the law that Aaronson himself makes falsifiable (§10)

Two pieces, both worth quoting, because together they are the template the paper (`ENTROPY_PRODUCTION.md`)
lacks.

**The finite, operational form** — this is a statement about a lab measurement:

> "Given an undirected graph G with 10⁸ vertices, there is no physical procedure by which you can decide
> in general whether G has a clique of size 10⁷, with probability at least 2/3 and after at most 10⁸⁰
> seconds as experienced by you."

*Plain reading: hand someone a concrete huge graph and a clock; the claim is that no machine, of any
kind, gives the right yes/no most of the time within a stated wall-clock time.* Falsified by exhibiting
the procedure. Not falsified by any negative result, ever — you cannot certify absence by experiment.

**The split that makes half of it testable:**

> "while the Second Law rests on an elementary fact about statistics, the NP Hardness Assumption rests on
> some of the deepest conjectures ever made, in the sense that it could be falsified by a purely
> mathematical discovery such as P = NP. So as a heuristic, it might be helpful to split the Assumption
> into a 'mathematical' component (P ≠ NP, NP ⊄ BQP, and so on), and a 'physical' component (there is no
> physical mechanism that achieves an exponential speedup for black-box search)."

**This is the structural answer to Mountain 2, in the source's own words.** The mathematical component
is an arithmetic sentence; no measurement decides it. The physical component *is* testable, and it is
the only half that is. Every candidate below that survives at all is a test of the physical half.

**The four derived predictions (§10)** — accepting the assumption commits you to:

> - "There are no nonlinear corrections to the Schrödinger equation, not even (for example) at a black
>   hole singularity."
> - "There are no closed timelike curves."
> - "Real numbers cannot be stored with unlimited precision (so in particular, there should be a finite
>   upper bound on the entropy of a bounded physical system)."
> - "No version of the anthropic principle that allows arbitrary conditioning on the fact of one's own
>   existence can be valid."

Each is a physics statement with a lab programme attached (bullet 1 and bullet 3 in particular), and
each is a **necessary condition** of the law: falsify one and the law falls with it. Bullet 1 is the one
with real numbers on it.

### 1.4 Aaronson 2016, footnote 20 (Read, verbatim)

> "I like to joke that, if computer scientists had been physicists, we'd simply have declared P ≠ NP to
> be an observed law of Nature, analogous to the laws of thermodynamics. A Nobel Prize would even be
> given for the discovery of that law. (And in the unlikely event that someone later proved P = NP, a
> second Nobel Prize would be awarded for the law's overthrow.)"

Note the falsifier he names is a *proof*, not a measurement. Consistent with §10.

### 1.5 Aaronson–Kardes–Hartle 2025 slides (Read, targeted)

The demon (slides 27 and neighbours):

> "We've constructed a toy situation where, if P=NP, then one could appear to reverse the Second Law of
> Thermodynamics, by building a Maxwell's Demon that collects all the gas in a box onto one side."
> "Normally, the entropy just gets transferred into the Demon's own memory (Szilard/Landauer/Bennett).
> But in our model scenario, we can use the P=NP assumption to 'uncompute' the Demon's memory."

And, decisively for this note, the slides pose the demarcation question that Fox et al. 2026 then answer:

> "Should there be an inductive bias against physical theories that predict 'computational
> superpowers'?"

No preprint as of 2026-09-15 (searched). Still slides-only.

---

## 2. Wolfram 2023: framework or prediction?

**Finding: framework only. No falsifiable prediction, and no passage claiming one.**

Two independent checks, both negative:

- The pass-04 read-note `passes/pass04/wolfram2023.md` (part 1 read in full in that session) contains
  **no occurrence** of "falsifi", and only four of "predict"/"experiment"/"test" — all four describing
  computational irreducibility ("no shortcut predicts it faster than running it"; "irreducibility
  removes predictability from a bounded observer's reach") or Wolfram's claim that Second-Law behaviour
  fails when a system "falls to a predictable fixed point". None is a prediction about a measurement.
- A targeted re-fetch of the live page this session returned: *"there are no explicit passages where the
  author proposes falsifiable predictions, experimental tests, or observable consequences that could
  prove his framework wrong."* The nearest passages are descriptive —

  > "And in practice what the Second Law asserts is that systems will tend to go from states where we can
  > recognize regularities to ones where we cannot."

  and the thesis statement —

  > "But in fact the core phenomenon of the Second Law is much more general, and in a sense purely
  > computational, depending only on the basic computational phenomenon of computational irreducibility,
  > together with the fundamental computational boundedness of observers like us."

**Reading.** Wolfram's account is an *explanation* of why the Second Law looks the way it does to a
bounded observer. It makes the same predictions as the standard account by construction — that is the
point of it. It therefore supplies no candidate for Mountain 2. It is worth recording that his position
and ours differ in one respect that matters: Wolfram's bounded observer is bounded by *irreducibility*
(no shortcut exists), ours by *polynomial time* (a shortcut may exist and be out of reach). His has no
one-way function in it, as the pass-04 note already established.

---

## 3. Constructor theory: is there a template for "impossible for any fast process"?

**Finding: there is a template for stating and testing an impossibility principle, and it is a good one.
There is no template for a *resource-bounded* impossibility. Constructor theory's impossibilities are
flat-out.**

### 3.1 What they say a test looks like (Marletto, Deutsch, Vedral 2026, §1.1, verbatim)

> "Testing the principles of constructor theory works in the same way as testing other principles of
> physics, such as the conservation of energy or the second law. One must test them not by direct
> falsification of their predictions, but by testing the subsidiary theories that comply with them, or
> by showing that given tasks that are ruled out by them are, in fact, possible."

And the mechanics, from the earlier *Constructor theory of information* (Deutsch–Marletto), as reported
in the search summary and consistent with the 2026 review:

> "A principle P is refuted if some law violating P survives experimental tests, whereas all rival laws
> conforming to P are refuted."

Supporting machinery in the review: "The principles of constructor theory are **meta-laws**: they are
obeyed by some dynamical laws (called 'subsidiary theories'), and violated by others… they do not refer
to constructors but rather to the possibility or impossibility of certain tasks."

**This is exactly the template the ticket asks for, and it is not ours to invent — it is standard.** A
principle of the form "task T is impossible" is never tested head-on. It is tested by the survival of
the dynamical theories that respect it, and refuted when a theory that violates it survives while its
rivals die. Concretely, for us: *the NP-hardness principle is refuted if a physical theory that permits
efficient NP-solving survives experimental test while the theories that forbid it are refuted.*

### 3.2 The worked example (§2.3): BMV / gravitationally induced entanglement

The 2026 review's central experimental proposal is the Bose–Marletto–Vedral test, and the review is
careful about its logic — which is the honest version of what a "test of a principle" buys you:

> "the experiment does not test interoperability alone. Instead, the logic is conditional: if
> entanglement between the probes is observed and all interactions are local, satisfy the
> interoperability condition, and are mediated solely by gravity, then the mediator cannot remain purely
> classical in the information-theoretic sense used in the theorem. Conversely, the absence of GIE in a
> carefully prepared experiment would raise several equally interesting possibilities. It could indicate
> that gravity is fundamentally classical, challenging the completeness of quantum theory at certain
> scales. Alternatively, gravity may indeed be quantum, but our current theoretical frameworks might be
> insufficient to predict this effect. Another possibility is that the principles of the constructor
> theory underlying the non-classicality witness are incorrect."

Note the honesty: a null result is a Duhem–Quine fan-out, not a clean refutation. The same will be true
of any test of our law.

### 3.3 Why the template does not carry a resource bound

Grepped the whole text for efficien / complexity / resource / time. The only place resources enter an
impossibility is energy conservation, not computation:

> "Given finite resources, executing the task T₊,₀ is impossible due to energy conservation, as it
> necessitates a change in the atom's energy."

Constructor theory's irreversibility result (Violaris–Marletto) is of the same type: "requiring that a
task is possible, but its inverse task is not" — a possible/impossible pair, with no clock. Constructor
theory's own second law is "scale-independent, dynamics-independent"; a complexity bound is by
construction neither scale- nor dynamics-independent, since "polynomial time" needs a notion of step
count. **[Inference]:** stating "some task is impossible for any *fast* process" is not a statement of
constructor theory's type, and nothing in the 2026 review extends the formalism to add one. If we wanted
the template, we would have to add a resource measure to the constructor, which is a research programme,
not a citation.

---

## 4. Landauer / Maxwell-demon experiments: has anyone measured a *computational* cost?

**Finding: no. Every experiment in this family measures heat or work. The demon's inference is one bit
and is trivially computable. No experiment anywhere makes the *time* or *compute* of reversal the
measured quantity, and there is a theorem-shaped reason why doing so would not help.**

What the canonical experiments measure:

| experiment | measured quantity |
|---|---|
| Toyabe et al., Nat. Phys. 6:988 (2010) | work / free-energy gain from information-to-energy conversion; validates a generalized Jarzynski equality |
| Bérut et al., Nature 483:187 (2012) | mean dissipated **heat** during erasure, shown to saturate kT ln 2 for long cycles |
| Jun, Gavrilov, Bechhoefer, PRL 113:190601 (2014) | **work** to reduce the number of macrostates by 2, in a virtual double-well built by a feedback trap |
| information engines with feedback delay, PRE 109:034121 (2024); "imprecise demon with delay" (2025) | work/cycle and efficiency as functions of **physical delay time**, level spacing, cycle time, measurement error |

The delay literature is the closest anyone comes to putting a clock on the demon, and it is not close:
the delay is the *latency of the apparatus*, a wall-clock parameter in the physical dynamics. It is not
the cost of a computation, and nothing in the feedback rule is hard — these demons compare a position to
a threshold. The review *Experimental realizations of information engines: beyond proof of concept*
(arXiv 2501.13593) is the current survey; nothing in the hits proposes a demon whose feedback requires
solving anything.

**The structural reason, from sources already Read in pass 16.** Bennett 1973: any computation can be
made logically reversible by keeping a history tape, dissipating "considerably less than kT of energy per
logical step". So heat is not a proxy for computational difficulty — you can always pay bits of tape
instead of joules. Our own Appendix A.1 row 17 already records this as the gap: Landauer heat and
Zurek's description-length cost are "a different object", matched only by "the same word 'reversal'".

There is also a live dispute about whether the demon is even a computation story. Norton, *Maxwell's
Demon Does Not Compute*, and the 2025 argument that "the entropy cost that thwarts the Demon comes from
the need to measure… rather than from computational erasure" (arXiv 2503.18186 / PhilSci 24936) both say
the exorcism runs through measurement, not computation. **abstract-only.** If they are right, the demon
is a weaker peg for our frame than §8.3 of the paper assumes. Worth one sentence of hedging there.

**What an experiment of the shape we want would have to be.** [Speculation] Build a demon whose feedback
rule requires inverting a candidate one-way function on the measured microstate, and measure whether the
extractable work falls short of the mutual-information bound by an amount that grows with the security
parameter. Nobody has proposed this. It would not prove hardness (rule 7), and by Bennett it would test
the demon's *implementation*, not the law.

---

## 5. Physical one-way functions and PUFs: the one claim that was actually falsified

**Finding: yes, there is a clean "prediction that can fail" here, it was stated, and it failed. It is a
CANDIDATE-level claim, and it was falsified by an algorithm, not by a physics measurement. That is the
shape of every falsification available in this area.**

**The claim (Pappu, Recht, Taylor, Gershenfeld, Science 2002, abstract):** the mesoscopic speckle
structure gives identifiers that are "inexpensive to fabricate, prohibitively difficult to duplicate,
**admit no compact mathematical representation**, and are intrinsically tamper-resistant."

"Admits no compact mathematical representation" is a falsifiable prediction with a clean falsifier:
*exhibit a compact model that predicts responses to fresh challenges from polynomially many
challenge-response pairs.*

**The falsifications.**

- Rührmair, Sehnke, Sölter, Dror, Devadas, Schmidhuber, CCS 2010 (ePrint 2010/251): machine-learning
  modeling attacks break "standard Arbiter PUFs and Ring Oscillator PUFs of arbitrary sizes, and XOR
  Arbiter PUFs, Lightweight Secure PUFs, and Feed-Forward Arbiter PUFs of up to a given size and
  complexity", using logistic regression and evolution strategies. **abstract-only.**
- Rührmair et al., *Optical PUFs Reloaded*, ePrint 2013/215: the first integrated optical PUF prototype
  "can be attacked by machine learning techniques if the employed scattering structure is linear and if
  the raw interference images of the PUF are available to the adversary." **abstract-only.**
- Albright, Gelfand, Dixon, arXiv 2308.09199 (2023), journal version IEEE TIFS 20:886 (2025), abstract
  verbatim: "It is shown that a class of optical physical unclonable functions (PUFs) can be learned to
  arbitrary precision with arbitrarily high probability, **even in the presence of noise**, given access
  to polynomially many challenge-response pairs and polynomially bounded computational power, under mild
  assumptions about the distributions of the noise and challenge vectors." The motivation is the
  similarity between integrated Pappu-style optical PUFs and **Learning With Errors** — and the finding
  is that the PUF sits on the *easy* side of that analogy, because the noise structure does not deliver
  LWE's hardness.

**Three readings that matter for us.**

1. The prediction was falsified **by a learning algorithm**, i.e. by mathematics applied to data, not by
   a physical measurement. This is the same asymmetry Aaronson names in §10: hardness claims die of
   mathematical discoveries.
2. The 2023/2025 result is the most interesting item in this section for the paper, because it is a case
   where a *physical device's* security was reduced to a *computational* assumption (LWE) and then shown
   to fall on the wrong side of it. The direction of explanation is physics ← complexity, which is the
   direction our Conventions permit. It is the closest published thing to "a physical system whose
   one-wayness is a theorem about a computational problem".
3. It is CANDIDATE-level throughout. No PUF paper claims or tests "no fast process inverts this"; they
   claim "the attacks we know fail", which is rule-7 territory by construction. The field's own response
   to each break is to build a new device ("ML-resistant amorphous silicon PUFs", "photonic PUFs
   resilient to ML attacks", 2024–2025), which is the behaviour of a candidate under attack, not of a law
   under test.

---

## 6. 2020–2026: proposals for an experimental test of complexity as a physical law

**Finding: one strong item, found in this session, published June 2026. Plus the quantum-advantage
programme, which tests a different law and points the other way.**

### 6.1 The strong item: Fox, Karamchedu, Mygdalas, arXiv 2606.14806 (11 Jun 2026)

Abstract, verbatim:

> "Assuming the gravitational field is classical and that it couples to quantum fields via the
> semiclassical Einstein field equations, we show that the weak-field dynamics of a massive and
> non-relativistic qubit can in principle be used to solve an NP-complete problem in polynomial time. We
> attribute this vast computational power to the non-linear dynamics afforded by the semiclassical
> Einstein field equations. Consequently, the above two assumptions entail a violation of the Physical
> Extended Church–Turing Thesis, which we regard as evidence for the quantization of gravity."

They state the principle as a principle (§II, verbatim):

> "**Physical Extended Church–Turing Thesis (PECTT).** No physical procedure can decide an NP-complete
> problem in polynomially many steps."
>
> "While motivated from computer science, this thesis is largely a postulate about the physical world as
> it articulates what can and cannot be computed efficiently by physical devices. Thus, in the context of
> demarcating different physical theories, the PECTT dictates that a candidate theory should be deemed
> implausible if it can be exploited to efficiently solve an NP-complete problem."

And the conclusion (§V):

> "if the PECTT is taken seriously as a principle of physics, then any candidate theory of gravity must
> respect it. In this way, the PECTT, and computational complexity more broadly, provides not just a
> constraint, but a guiding principle in the search for a consistent theory of quantum gravity."

**Why this is the best candidate for Mountain 2.** It executes the constructor-theory template of §3
exactly, for our principle, with a *live* experiment at the end of the chain:

- Principle: PECTT.
- Subsidiary theory that violates it: semiclassical gravity (any consistent non-linear matter–gravity
  coupling; their Theorem 2 is general).
- The measurement: gravitationally induced entanglement (BMV/GIE), not yet performed, nanogram masses,
  named by Marletto–Deutsch–Vedral as "yet-to-be-performed" and "particularly promising… making it more
  experimentally feasible".
- **The falsifiable prediction: a carefully prepared GIE experiment will see entanglement.** If it
  robustly does not, and locality and the other controls hold, gravity is classical; and if it is
  classical with the semiclassical EFEs, NP-complete problems are efficiently solvable and the principle
  is false.

**This is a statement about a lab measurement that could come out wrong.** It is the only one found.

**Attribution, precisely. [Inference]** Fox et al. prove PECTT ⇒ ¬(classical gravity with semiclassical
EFEs). They do **not** write the further step "therefore GIE/BMV is the experimental test of the PECTT";
that step is mine. What is theirs: they cite Marletto and Vedral, Phys. Rev. Lett. 119:240402 (2017) —
the entanglement-witness paper behind BMV — as their reference [9], in the sentence "despite many
ongoing experiments (e.g., [9–12]), there is no definitive experimental evidence that gravity is
quantized." So they place BMV-type experiments as the live empirical question their theorem bears on;
joining the two into a falsification chain is the synthesis of this note, and the table's "who proposed
it" column is marked accordingly.

**The noise caveat, which rows 1 and 2 both inherit, and which neither source closes.** The mechanism in
both rows is the same — non-linear dynamics ⇒ NP easy, via Abrams–Lloyd and its generalisation
(Bao–Bouland–Jordan, stated as Theorem 2 in Fox et al. and so **cited via Fox et al. [Read]**, not from
memory). Aaronson 2005 §5, which I read, flags exactly the gap:

> "But what if we allow error, as any physically reasonable model of computation must? In this case,
> while it might still be possible to solve NP-complete problems in polynomial time, I am not convinced
> that Abrams and Lloyd have demonstrated this… the standard quantum error-correction theorems break
> down, since just as a tiny probability of success can be magnified exponentially during the course of a
> computation, so too can a tiny probability of error."

I grepped the whole of Fox et al. for error / noise / precision / robust / decoher. **The only hit is the
expansion of "BPP".** They do not address noise tolerance. So rows 1 and 2 carry the qualifier: *the
implication "non-linearity ⇒ NP efficiently solvable" is established for error-free dynamics; whether it
survives realistic noise is open, per Aaronson §5, and Fox et al. do not close it.* Rows 1 and 2 are
therefore one mechanism in two substrates, not two independent tests. Note also (their footnote 7 region,
p. 9) that they argue the relevant state is "a highly non-uniform superposition state" for which "the
gravitational effects of the SN equation are large", i.e. they claim a regime where the effect is not
suppressed; whether the existing ~10⁻²⁷ linearity bounds of row 2 already constrain Schrödinger–Newton
in that regime is not discussed in the parts I read, and is **open in this note**.

**The caveats, in the authors' own words, which must travel with it.** §V lists the escape routes:
"either gravity is not classical, or gravity is classical, but the semiclassical EFEs do not correctly
describe the matter-gravity coupling"; and footnote 11: "if the dynamics are such that the density matrix
of a quantum state evolves linearly and stochastically (as in Oppenheim's post-quantum theory), then our
conclusions do not hold." Marletto et al. add their own fan-out for a null GIE result (quoted in §3.2).
So the prediction is falsifiable in Popper's sense but not decisive in practice — which is, note, also
true of the Second Law's own lab tests.

They also note Kent et al. reach the same mechanism and read it the opposite way — as a route to
"experimentally accessible computational advantages beyond standard quantum theory". Same physics,
opposite prior. That disagreement is itself evidence that the principle is doing work: it is the thing
that decides which reading you take.

### 6.2 Quantum advantage as a test of the Extended Church–Turing Thesis — a different law, opposite sign

BosonSampling and random-circuit sampling are framed by their authors as experimental challenges to the
ECT thesis ("classical computers can efficiently implement any reasonable model of computation"). Status
as of 2026: the claims move, repeatedly, because the classical side improves. Sycamore's 2019 10,000-year
estimate fell to days (IBM), then to 304 seconds on Sunway with PEPS-based simulators, with the largest
PEPS simulations now reaching 10×10 qubits at depth 42, beyond Sycamore. Zuchongzhi 3.0 (PRL 134:090601,
2025) restates the claim at 105 qubits. D-Wave's March 2025 *Science* simulation claim is contested by a
Flatiron tensor-network result, with D-Wave disputing the scope. The validation problem is acknowledged
in the field's own words: one must show the device produces "a correct boson sampling distribution rather
than a pathological classically simulatable one."

**Two things to take from this for the paper.**

- It is the *only* place where a physical experiment is routinely presented as a test of a
  complexity-theoretic law, and the pattern of the last seven years is that the falsifications run in one
  direction only — the classical algorithm improves and the claim retreats. That is rule 7 in the field's
  own history. It is evidence about how such a test behaves, and it is not encouraging.
- **It points the other way from our frame, and this is a check the paper should run.** These experiments
  argue that the class of fast *physical* processes is larger than BPP. Theorems 1 and 2 are stated over
  polynomial-time samplable distributions and a pK^t observer — a classical, probabilistic-polynomial
  class throughout (Definition 2, HILNO's eq. (6), the LOZ coding theorem). **[Inference]:** if one takes
  the quantum-advantage experiments at face value, then "fast process" in the physical reading of §8 is
  BQP-samplable, and the paper's objects are the wrong class for the physical parallel. This does not
  touch the theorems — they are about samplers, and are true regardless — but it does touch §8.5's
  "two ends of one scale" reading, which silently identifies the physical and the BPP notions. One
  sentence in §6 (Modelling choices) naming this would be honest and cheap.

### 6.3 Others found, and what they are not

- Borsten and Kim, arXiv 2604.00182 (2026), *Limits to computational acceleration imposed by QFT and
  quantum gravity*: "An observer and a computer able to withstand energy scales up to order E can
  accelerate computation at most O(1)E e-folds per unit time." **abstract-only.** A physics *bound on
  speedup*, not a test; NP-hardness is not used as a principle; no falsifiable prediction stated.
- *The quantum-extended Church–Turing thesis in quantum field theory*, arXiv 2309.09000, and *Horizons
  protect Church–Turing*, arXiv 2003.01807, and *Constraints on physical computers in holographic
  spacetimes*, arXiv 2304.09900 — all theoretical consistency results, no experiments. **Not read**;
  titles only, from search. Recorded for the audit list, not used.
- Searches for "no-go theorem NP-hard nature experiment" 2023–2026 returned nothing with an experiment
  attached beyond the above.

---

## 7. Thermodynamics: is any measurable quantity large iff a task is hard?

**Finding: no, and there is a published theorem that says the natural candidate is constant.** This is
the cleanest negative in the note, and it deserves to be in the paper.

### 7.1 The theorem that kills the natural candidate

Kolchinsky and Wolpert, *Thermodynamic costs of Turing machines*, Phys. Rev. Research 2:033312 (2020),
abstract, verbatim:

> "the thermodynamic complexity of any desired output is bounded by a constant (unlike the conventional
> Kolmogorov complexity)"

and

> "the expected amount of generated heat is infinite"

*Plain reading: they define the exact thermodynamic analogue of Kolmogorov complexity — the least heat
any physical realisation of a universal Turing machine must generate to produce a given output — and it
is O(1) for every output, while K is unbounded. Heat does not track description length. And the expected
heat, on the natural input distribution, does not even converge.*

**This is the structural reason in one line.** The object our paper needs to be physically measurable —
a description-length cost — provably has no heat shadow. Appendix A.1 row 17 already calls Landauer heat
and Zurek cost "a different object"; Kolchinsky–Wolpert turn that from a modelling remark into a theorem.

**[Inference], and flagged because the source is abstract-only.** I attribute the constant bound to
Bennett's mechanism — keep the history tape and pay in bits instead of joules, so heat stays O(1) while
description cost grows. **That explanation is my guess, not their text.** Their "thermodynamic
complexity" is a minimum over inputs for a particular realization, and the constant may come from the
choice of input rather than from reversibility. The *finding* (heat O(1), K unbounded) stands as quoted;
the *mechanism* is unverified and must be checked against the paper before it is used anywhere.

### 7.2 The current bounds, and what they actually depend on

- Yadav, Caravelli, Wolpert, *Entropy production bounds for systems running computer programs*, PNAS
  Nexus (2026). **fetched (targeted), not read by me.** The bound is **mismatch cost**,
  MC(p) = D(p‖q) − D(Gp‖Gq): KL divergence between the actual initial distribution and the
  thermodynamically optimal prior for the computational map G, minus the same after the map. It depends
  on *distribution mismatch and the state-space structure*, and the fetch's verdict is explicit: the
  bounds are "independent of computational time and depend instead on input distribution mismatch and
  state-space structure", and "The paper makes no claims that computational hardness (time/space
  complexity) correlates with entropy production." Worst-case scaling is "at least linearly with the
  difference between maximum and minimum value of f(x)", where f is average heat flow per state — a
  property of the heat landscape, not of the problem's difficulty.
- The prediction/dissipation family (Still; Crutchfield school; "thermodynamic cost of inference",
  modularity dissipation): the bound is *non-predictive information stored about the drive*. Large
  dissipation means the system keeps statistically irrelevant bits, not that its task is hard. **All
  abstract-only.**
- Wolpert's 2019 review and the 2022–2023 "combining lower bounds" line: strengthen the second law by
  decomposing a complex system; again no complexity dependence.

### 7.3 What it would take, stated precisely

**[Speculation, and this is the object the ticket is asking for.]** The quantity we would need is a
dissipation D(P, n) attached to a *physical* process P on inputs of size n such that

> D(P, n) = ω(log n) for some fast physical process P  ⟺  one-way functions exist,

i.e. an observable version of Theorem 2's left-hand side. Three obstructions, in descending order of
severity, and all three are load-bearing:

1. **Bennett's escape.** Any computation can be made reversible at O(1) heat by keeping a history tape.
   So no heat-like D can be forced large by computational difficulty. Kolchinsky–Wolpert make this
   quantitative: thermodynamic complexity is O(1). Any D that works must therefore be a
   *description-length* quantity, not a heat quantity.
2. **σ is measurable by the bounded observer exactly when it vanishes.** [Inference], conditional on
   Liu–Pass 2020 as read in `pass04/liupass2020.md`. The paper's σ is log D(x,y) − log m_R(x,y), with
   m_R built from pK^t. The tempting claim is "a bounded observer cannot compute pK^t, so cannot measure
   its own entropy production, and physics has no analogue of that." **That claim is wrong, and its
   correction is sharper.** Liu–Pass: one-way functions exist **iff** K^poly is *mildly* hard on average
   — meaning no probabilistic polynomial-time algorithm computes K^t on at least a 1/p(n) fraction of
   n-bit strings. Contrapositive: with no OWF, a bounded observer *can* compute K^t on all but a
   1/p(n) fraction. So in the no-OWF worlds the observer can estimate its own description cost on most
   strings, and σ is average-case measurable — which is the same world in which Theorem 2 says σ is
   O(log n), i.e. in which the arrow is not there. **The arrow is measurable by the observer exactly
   when it vanishes, and unmeasurable exactly when it exists.** That is not a defect of the frame; it is
   the frame's content restated, and it is a better sentence for §8.2 than a claimed disanalogy.
   Two hedges: Liu–Pass is about K^t, ours about pK^t, and the pass-04 note explicitly warns that the
   two statements it compares "are different statements and nothing here connects them"; and the
   direction quantified over ("some fast process" vs "most strings") is not literally the same
   quantifier. Verify against HILNO Proposition 1 before this goes into the paper.
3. **The arithmetic barrier.** Even a perfect measurement of D on any finite family decides nothing,
   because "one-way functions exist" is an asymptotic arithmetic sentence. See §8 below.

No source proposes such a D. The searches for a dissipation quantity tied to cryptographic hardness
returned only entropy-production *estimation* methods (quantum dots, milestoning, fluctuating currents),
which measure dissipation in physical systems with no computational content.

---

## 8. The structural reason, in the sources' words

Assembled, because the ticket asks for the default finding to be defended rather than asserted.

1. **The law is half arithmetic, and no measurement decides an arithmetic sentence.** Aaronson 2005 §10:
   the assumption "could be falsified by a purely mathematical discovery such as P = NP", where the
   Second Law could not, because it "rests on an elementary fact about statistics". His own fix is to
   split off a 'physical' component; only that half is testable.
2. **Our paper already says the same thing in its own vocabulary and should say it louder.** §1.4:
   Theorems 1 and 2 hold in every one of Impagliazzo's five worlds. Which world we are in is open. A
   measurement cannot select a world, because the worlds differ on an asymptotic statement about all
   polynomial-time algorithms, and no finite apparatus quantifies over that class. This is the same wall
   as CLAUDE.md rule 7, arrived at from the physics side.
3. **Principles of this type are never tested directly, and that is normal.** Marletto–Deutsch–Vedral:
   "One must test them not by direct falsification of their predictions, but by testing the subsidiary
   theories that comply with them, or by showing that given tasks that are ruled out by them are, in
   fact, possible." So the absence of a direct test is not a defect specific to our law; it is the
   generic situation for conservation of energy and the second law too. **What our law lacks is not a
   direct test — it is a stock of subsidiary theories it discriminates between.** Fox et al. 2026 is the
   first entry in that stock. That reframing is the most useful thing in this note.
4. **The thermodynamic quantity cannot be made to track hardness.** Bennett 1973 plus Kolchinsky–Wolpert
   2020: heat is O(1); description length is not.
5. **Our own σ is unmeasurable by the observer it is defined for.** §7.3 item 2 above. [Inference]

---

## (c) Ranked table of candidate falsifiable predictions

Ranked by how close each comes to "a lab measurement that could come out wrong, bearing on the law."

| # | candidate | law or candidate | what observation falsifies it | who proposed it | status | fit to Theorem 1/2 objects |
|---|---|---|---|---|---|---|
| 1 | **PECTT via semiclassical gravity → GIE/BMV experiment.** "A carefully prepared gravitationally-induced-entanglement experiment will observe entanglement." If gravity is classical and couples by the semiclassical EFEs, NP-complete problems are efficiently solvable. | **LAW** | A robust null GIE result with locality and mediation controls holding ⇒ gravity classical ⇒ (with semiclassical EFEs) NP ⊆ P, principle false. Equally, any demonstration of the Abrams–Lloyd/Bao–Bouland–Jordan algorithm on a real non-linear substrate. | Theorem: Fox, Karamchedu, Mygdalas, arXiv 2606.14806 (Jun 2026), via Bao–Bouland–Jordan (their Thm 2) and Abrams–Lloyd. Experiment: Bose–Marletto–Vedral; Fox et al. cite Marletto–Vedral PRL 119:240402 as an "ongoing experiment" on gravity's quantization but **do not state the falsification chain — joining them is this note's [Inference]**. | Experiment **not yet performed**; nanogram masses; theory chain published Jun 2026. Authors name escape routes: non-semiclassical couplings, Oppenheim's linear-stochastic post-quantum gravity. Kent et al. read the same physics as an opportunity, not a violation. **Noise caveat (shared with row 2): the "non-linearity ⇒ NP easy" step is error-free only; Aaronson §5 says the noise-tolerant version is undemonstrated, and Fox et al. never mention noise.** | **Does not touch them.** Tests the physical bridge (what any fast physical process can do), not σ, pK^t or samplable D. Relevant to §8.5's "two ends of one scale" and to §6's modelling choices, not to Theorems 1–3. |
| 2 | **No non-linear correction to the Schrödinger equation.** A non-zero Weinberg parameter would give NP, #P (and with arbitrary gates PSPACE) in polynomial time. | **LAW** (a necessary condition of it) | Detect a non-linear term. Current limits ~10⁻²⁷ of the binding energy per nucleon (⁹Be⁺; ²⁰¹Hg), improved 2024 (arXiv 2411.09611). | Aaronson 2005 §5 and §10 bullet 1, from Abrams–Lloyd; experiments by the precision-spectroscopy community | **Performed, repeatedly, and could have come out the other way.** Limits tighten; no violation. Numbers **[Unverified]**. Same noise caveat as row 1, from the same §5. | Does not touch them. Same reason as row 1. **Rows 1 and 2 are one mechanism (non-linear QM) in two substrates, not two independent tests** — count them once. This is the strongest *already-performed* measurement bearing on the law. |
| 3 | **Soap films do not reliably find the global Steiner tree.** | **CANDIDATE** (one substrate) | Soap films reach the global optimum reliably, with success rate not decaying as pegs are added. | Aaronson 2005 §3, run by him | **Performed (2004–05); came out for the law.** Optimum "by no means always found, especially with more pegs"; impossible triangular structures observed. | Does not touch them. It is a measurement about one analog device, not about the class of fast processes. Its value is as the only hands-on datum in the literature. |
| 4 | **Head-to-head: adiabatic/annealing hardware vs best classical heuristics on the same random instances.** Aaronson's "crucial experiment (which has not yet been done)". | **CANDIDATE** (one hardware family) | Polynomial scaling to *exact* optima on an NP-hard family, beating the best classical solver, sustained as n grows. | Aaronson 2005 §4.2; partially executed by King et al., PRL 134:160601 (2025) vs PT-ICM | **Partly done.** Scaling advantage reported for **approximate** optimization only; exact-optimization advantage "remains elusive"; D-Wave's 2025 *Science* claim contested by Flatiron tensor networks. | Does not touch them. **Rule 7 applies permanently**: resistance to known algorithms, not hardness. |
| 5 | **PUF unclonability: "admits no compact mathematical representation."** | **CANDIDATE** (one device class) | Exhibit a model predicting fresh responses from polynomially many CRPs. | Pappu, Recht, Taylor, Gershenfeld, Science 2002 | **FALSIFIED.** Rührmair et al. CCS 2010 (arbiter, XOR, ring-oscillator); *Optical PUFs Reloaded* 2013 (integrated linear optical); Albright–Gelfand–Dixon 2023/2025 (poly-time PAC-learnable **even with noise**, motivated by an LWE analogy the device fails to inherit). | Closest *published* thing to a physical system whose one-wayness is reduced to a computational assumption — the direction physics ← complexity that our Conventions allow. But falsified **by an algorithm**, not by a measurement: the same asymmetry Aaronson §10 names. |
| 6 | **Quantum-advantage experiments as tests of the Extended Church–Turing thesis.** | **LAW — but a different law, and the opposite direction** | A classical algorithm reproducing the sampler's distribution at the claimed size and fidelity. | Aaronson–Arkhipov (BosonSampling) **[Unverified — cited from memory]**; Google/USTC implementations; Zuchongzhi 3.0 PRL 134:090601 (2025) | **Live, contested, and moving one way.** Sycamore 10,000 yr → days (IBM) → 304 s (Sunway PEPS, now past Sycamore's size); D-Wave 2025 contested; the field names its own "validation problem". | **This is the one row that bears on the paper's objects — as a warning.** If physical fast processes are BQP-samplable, then Definition 2's poly-time sampler and the pK^t observer are the wrong class for the *physical* reading of §8. The theorems are untouched; §8.5's identification of the two notions is not. Recommend one sentence in §6. |
| 7 | **CTC computing.** "There are no closed timelike curves" (Aaronson §10 bullet 2). | LAW (necessary condition) | Find or build a CTC. | Aaronson 2005 §8, §10 | **No test exists.** Ringbauer et al. (Nat. Commun. 2014) simulated a Deutsch CTC photonically via entanglement + post-selection — a simulation, not a CTC; no NP-hard speedup obtained or claimed. | Does not touch them. Record as "tests nothing", against any temptation to cite it as evidence. |
| 8 | **Constructor-theoretic tests: BMV, and the Violaris–Marletto irreversibility demonstrations.** | LAW-shaped, but for *different* principles (interoperability, locality, constructor-theoretic second law) | Per Marletto–Deutsch–Vedral: a subsidiary theory violating the principle survives while conforming rivals are refuted. | Deutsch 2013; Marletto–Deutsch 2015; Marletto–Deutsch–Vedral arXiv 2606.07352 (2026) | Framework mature; BMV not yet performed; thermodynamic demonstrations performed. | **The template we should borrow, not a test we can use.** Constructor-theoretic impossibilities carry no resource bound; "impossible for any fast process" is not a statement of the theory's type, and the 2026 review adds no complexity measure. |
| 9 | **Thermodynamic cost bounds: mismatch cost, thermodynamic complexity, prediction/dissipation bounds.** | neither | Measure heat below the stated bound. (Tests thermodynamics, not complexity.) | Kolchinsky–Wolpert PRR 2:033312 (2020); Yadav–Caravelli–Wolpert PNAS Nexus (2026); Still/Crutchfield school; Wolpert 2019 review | Bounds proved; measurable; **provably not hardness-tracking.** "Thermodynamic complexity of any desired output is bounded by a constant (unlike the conventional Kolmogorov complexity)". | **The decisive negative.** This is the theorem that forbids the object we want on the heat side, and it should be cited in Appendix A.1 row 17, which currently states the same thing as a modelling remark. |
| 10 | **Landauer / Maxwell-demon experiments.** | neither | Measure erasure heat below kT ln 2. | Landauer 1961; Bérut 2012; Toyabe 2010; Jun–Gavrilov–Bechhoefer 2014; feedback-delay engines 2024–25 | All performed; all confirm. **Every measured quantity is heat or work; the demon's inference is one bit.** The "delay" in delayed-feedback engines is apparatus latency, not compute. | Does not touch them, and by Bennett 1973 cannot be made to. Note also the live dispute (Norton; arXiv 2503.18186) that the demon is a *measurement* story, not a computation story — a hedge §8.3 should carry. |
| 11 | **Wolfram 2023, computational second law.** | neither | — | Wolfram 2023 | **No falsifiable prediction proposed.** Framework only; two independent checks (pass-04 note; targeted re-fetch) agree. | Does not touch them. By construction it reproduces standard thermodynamics for a bounded observer; no one-way function appears. |

---

## Recommendations for the paper, cheap and specific

1. **Read Kolchinsky–Wolpert 2020, then add it to Appendix A.1 row 17.** Row 17 currently says Landauer
   heat and Zurek cost are "a different object" — a modelling remark. The abstract says thermodynamic
   complexity is O(1) while Kolmogorov complexity is not, which would turn the remark into a theorem.
   **Rule 3: the source is abstract-only here. Read the relevant sections before citing**, and drop my
   Bennett-tape explanation of the constant unless their text supports it.
2. **§8.2: not a disanalogy — a restatement, and a better sentence.** Do *not* write "the bounded
   observer cannot measure its own σ, and physics has no analogue". Liu–Pass makes that false in the
   no-OWF worlds. Write instead: *the arrow is measurable by the bounded observer exactly when it
   vanishes, and unmeasurable exactly when it exists.* [Inference], conditional on Liu–Pass 2020
   (`pass04/liupass2020.md`), and hedged on K^t vs pK^t — verify against HILNO Prop. 1 first.
3. **§6 (Modelling choices): one sentence naming the BQP question.** The paper's "fast process" is a
   classical polynomial-time sampler. If the quantum-advantage experiments are taken at face value, the
   *physical* class of fast processes is larger. The theorems do not depend on it; §8.5's reading does.
4. **§8.5: report Fox et al. 2026 as the one concrete instance of Aaronson's "constrains new physical
   theories" criterion.** It is exactly the payoff Aaronson §10 point (2) predicted, published a year
   after the Suppes lecture posed the demarcation question, and it is the only live experimental chain
   found. Report it as theirs, as the paper reports the AKH demon as theirs.
5. **Do not claim a falsifiable prediction of our own.** Nothing found supports one, and §8 above gives
   the reason in three published voices. If Mountain 2 is to be answered rather than reported, the
   answerable form is: *supply a subsidiary theory that our law discriminates against.* Fox et al. did
   that for gravity. The analogous move for one-way functions specifically — not just for NP-hardness —
   has not been made by anyone, and is the open question worth recording.

## Audit list additions

Bao–Bouland–Jordan is **cited via Fox et al. [Read]** (their Theorem 2, stated in full there), not from
memory; corrected from the first draft of this note.

Cited from memory or title-only, not used in any argument above beyond naming: Aaronson–Arkhipov 2011;
Abrams–Lloyd 1998; Aaronson–Watrous (P_CTC = PSPACE); arXiv 2309.09000; arXiv
2003.01807; arXiv 2304.09900; Norton, *Maxwell's Demon Does Not Compute*. Numerical limits on the
Weinberg parameter and the King et al. author list are **[Unverified]**.
