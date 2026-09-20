# Audit: Wolfram, "Computational Foundations for the Second Law of Thermodynamics" (Feb 3, 2023)

Purpose: confirm or refute a prior unverified claim that Wolfram states the
"thermodynamic irreversibility for computationally bounded observers <-> one-way functions"
thesis "almost word for word" and flags the exact gap.

Written 2026-09-09. All quotation marks below that are not around a verbatim quote are Wolfram's
own scare quotes, reproduced because they carry his hedging.

## Provenance and reading discipline

- Part 1 (the target): https://writings.stephenwolfram.com/2023/02/computational-foundations-for-the-second-law-of-thermodynamics/
  Fetched by direct HTTP (200, 360,058 bytes). Tags stripped -> ~27,100 words of body text.
- Part 2: "A 50-Year Quest: My Personal Journey with the Second Law of Thermodynamics" (Feb 2023,
  ~19,850 words). Fetched and stripped.
- Part 3: "How Did We Get Here? The Tangled History of the Second Law of Thermodynamics"
  (Jan 2023, ~37,200 words). Fetched and stripped.
- All three were combined into the book "The Second Law: Resolving the Mystery of the Second Law of
  Thermodynamics", Wolfram Media, 2023, 584 pp.

WHAT I READ IN FULL, in part 1: sections 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13 (all except the
conservation-law arithmetic images), 14, 15. That covers everything bearing on questions 1-7.
WHAT I SKIMMED in part 1: section 5 (Ergodicity and Global Behavior) — read for its recurrence and
state-transition-graph claims, not line by line; and sections 16-20 (Class 4 / mechanoidal phase,
bulk molecular biology, thermodynamics of spacetime, quantum mechanics, the future of the Second
Law) — read only far enough to confirm they are physics extensions with no complexity-theoretic
content. That confirmation is backed by a keyword grep over the complete stripped text for:
one-way, cryptograph, encrypt, decrypt, NP, polynomial, complexity theory, hash.
PARTS 2 AND 3: keyword-grepped in full, and every hit read in its surrounding context. Not read end
to end.
NOT INSPECTED anywhere: the ~200 generated images of cellular-automaton runs, which carry much of
the "evidence"; the text describes what they show and I relied on the text.

Reproduce: `strip_html.py` in this directory converts a saved page to text
(`python3 strip_html.py page.html page.txt`); headings come out as lines beginning `### `.

## Exact section headings of part 1 (in order, for relocating claims)
1. The Mystery of the Second Law
2. The Core Phenomenon of the Second Law
3. The Road from Ordinary Thermodynamics
4. Reversibility, Irreversibility and Equilibrium
5. Ergodicity and Global Behavior
6. How Random Does It Get?
7. The Concept of Entropy
8. Why the Second Law Works
9. Textbook Thermodynamics
10. Towards a Formal Proof of the Second Law
11. Maxwell's Demon and the Character of Observers
12. The Heat Death of the Universe
13. Traces of Initial Conditions
14. When the Second Law Works, and When It Doesn't
15. The Second Law and Order in the Universe
16. Class 4 and the Mechanoidal Phase
17. The Mechanoidal Phase and Bulk Molecular Biology
18. The Thermodynamics of Spacetime
19. Quantum Mechanics
20. The Future of the Second Law

---

## 1. THE THESIS

Stated in "The Mystery of the Second Law", restated in "The Core Phenomenon of the Second Law", and
given its fullest form in "Why the Second Law Works". In his framing: the Second Law is a
consequence of the interplay between computational irreducibility in the underlying dynamics and
the computational boundedness of observers like us.

The mechanism as he gives it:
- The microscopic dynamics is deterministic and (in physics) reversible, and computationally
  irreducible: no shortcut predicts it faster than running it.
- A computationally bounded observer cannot see through that irreducibility, so the state looks
  random to the observer.
- "Looks random to us" is what we call heat, and what we score as high entropy. Hence the Second
  Law. He puts the same thing in mechanical-work language: to harness work you need predictability,
  and irreducibility removes predictability from a bounded observer's reach.
- Anti-thermodynamic behaviour is not impossible, merely not preparable and not detectable by a
  bounded observer. Setting up such an initial state would require inverting the irreducible
  computation.

Two structural features of the claim:
- It is explicitly OBSERVER-RELATIVE. He says the Second Law's validity depends on what observers
  like us can do, and that an alien observer, or our own future technology, might see differently.
  In "When the Second Law Works, and When It Doesn't" he states flatly that the assumption that the
  Second Law is universally valid is not true: rules that do not generate randomness (a solid, a
  chain of perfect linear springs, his class 1 and class 2 cellular automata) show no Second Law
  behaviour at all.
- It is a claim about GENERALITY, not about physics specifically. He argues the same phenomenon
  underlies general relativity and quantum mechanics in his Physics Project, and applies to any
  computationally irreducible system.

VERDICT vs the prior report. The thesis half of the "word for word" claim is substantively CORRECT.
Wolfram does assert that irreversibility-as-experienced is exactly the computational hardness of
inversion relative to a bounded observer. He does not use the one-way-function formalism or
vocabulary (section 7 below), so "word for word" overstates it: the concepts line up, the words do
not.

## 2. IS ANYTHING PROVED

Blunt answer: NO. Zero theorems, zero proofs. The essay is informal argument plus computational
illustration — cellular automaton runs, blob-size curves, block-entropy curves, histograms of
recurrence times, exhaustive enumerations of small rule spaces.

The one section that confronts this is "Towards a Formal Proof of the Second Law", and it is a
sketch of what a proof would have to look like, explicitly not a proof. Its content:
- He posits a state S, an "observer function" Theta that summarises/compresses S (his running
  example is run-length encoding), and an "evolution function" Xi = xi^t.
  *Plain reading: Theta is "the best summary the observer can make of the state"; Xi is "run the
  system forward t steps".*
- He writes the claim as: size of Theta[Xi[S]] >= size of Theta[S].
  *Plain reading: after the system runs, the observer's best summary of it gets bigger — the state
  compresses worse — which is what "entropy went up" means operationally.*
- He immediately concedes it is not provable now. His obstacles, in substance:
  (i) there is no "observer theory" — no formal characterisation of admissible Theta comparable to
      what Turing machines gave for computation. A full formal proof would need axioms about
      observers that, in his phrasing, do not have immediate foundations in existing mathematics,
      physics, or computation theory;
  (ii) lower-bounding the minimal size of a representation of xi^t (say as a Boolean circuit) is,
      by his own description, exceptionally difficult given the current state of computation theory;
      he has only circumstantial evidence, from small-case exhaustive search;
  (iii) many specific questions will be formally undecidable;
  (iv) the statement can only ever hold "typically", and defining "typically" via probability
      measures is circular inside his framework.
- On toy models he is dismissive in advance: if xi is simple enough to prove things about (his
  example is a finite automaton), he doubts the results would be useful or representative.

There is no formal statement anywhere in the essay with a proof, not even a lemma. The inequality
above is the only notation resembling a theorem statement, and it is offered as a target.

## 3. THE NP CONNECTION

Located precisely: LAST PARAGRAPH of "Why the Second Law Works", immediately before the section
"Textbook Thermodynamics". Two sentences. That is the entire NP discussion in the essay.

He first frames the Second Law as the dynamics "encrypting" the initial conditions such that no
computation available to the observer can feasibly "decrypt" them (his scare quotes). Then, the
only NP sentence:

> "as soon as one looks at 'inverting' coarse-grained results one is immediately faced with fairly
> classic NP problems from computational complexity theory."
> — Wolfram, "Why the Second Law Works"

Assessment:
- He claims a RESEMBLANCE, not NP-hardness. He does not say NP-hard, and does not say the inversion
  problem is complete for anything.
- [Inference] Read strictly, the natural formal content of "faced with fairly classic NP problems"
  is membership: inverting a coarse-graining is an NP search problem (guess a preimage microstate,
  verify in polynomial time). That is trivially true and carries no hardness whatsoever. He does
  not distinguish membership from hardness anywhere.
- He names NO specific NP-complete problem. Not SAT, not subset-sum, not preimage-finding. No
  reduction is sketched. No problem instance is defined.
- The preceding sentence is the only other complexity-theoretic gesture: he says the computational
  interpretation lets one translate Second Law indicators into questions in areas like computational
  complexity theory. A research aspiration, not a result.
- The empirical version lives in "How Random Does It Get?": he tried run-length encoding, block
  frequencies and block entropies, and an enumeration of simple cellular automata used as candidate
  decoders, plus a general appeal to statistics, machine learning and cryptography. None made
  significant progress. That is resistance-to-known-methods evidence and nothing more; per the
  program's own standing caveat, it cannot show hardness.

## 4. THE GAP HE CONCEDES

Located precisely: the parenthetical immediately following the NP sentence, same paragraph, end of
"Why the Second Law Works":

> "(Establishing NP completeness in a particular case remains challenging, just like establishing
> computation universality.)"
> — Wolfram, "Why the Second Law Works"

What he is conceding, unpacked:
- He has no NP-completeness result for any specific inversion problem arising from any specific
  rule and coarse-graining pair, and expects getting one to be hard.
- His analogy — "just like establishing computation universality" — says what kind of hardness he
  means: the construction burden of building a reduction gadget by gadget inside a specific
  cellular automaton rule. [Unverified — cited from memory] In his own programme the two celebrated
  universality proofs (Rule 110; the 2-state 3-colour Turing machine) each took years of intricate
  ad-hoc construction, which is presumably the comparison he intends.
- What he does NOT concede, and what a one-way-function programme must not inherit: NP-completeness
  is a WORST-CASE statement, and is therefore the wrong notion for a Second Law that is supposed to
  hold for typical initial conditions. The worst-case/average-case gap is unmentioned in the entire
  essay. So is the fact that P != NP does not imply one-way functions exist.

A SECOND, DEEPER GAP is conceded elsewhere and is arguably the binding one: the absence of an
observer theory ("Towards a Formal Proof of the Second Law"; and "Maxwell's Demon and the Character
of Observers", where he says a metatheory of observers must devolve to a rather human question).
Without a formal class of admissible Theta, no inequality about Theta can be a theorem.

VERDICT vs the prior report: CONFIRMED, but flattered by the prior description. He does flag the
exact gap — in one parenthetical of about twenty words. It is an aside, not an analysis. That he
"flags the gap" is true; that he characterises it is not.

## 5. THE OBSERVER

QUALITATIVE ONLY. No parameters, no resource bounds, no quantification anywhere in the essay.

- Operative definition: an observer is computationally bounded — it cannot involve unbounded amounts
  of computation — and additionally reduces the detail of the outside world to a smaller
  representation that fits in the observer's mind and supports decisions. In the Physics Project
  extension he adds a second attribute: the observer takes itself to be persistent in time.
- He is explicit that the lack of quantification is deliberate. In "Why the Second Law Works" he
  says one could imagine a detailed model of an observer or its apparatus, but the details do not
  matter; all that matters is that the observer is computationally bounded.
- He never writes a complexity class, a polynomial bound, a circuit-size bound, a memory bound, or
  any numeric budget. No "poly(n)" or equivalent occurs.
- He names the missing formalisation "observer theory", says it does not exist, and proposes it as
  the analogue of what Turing machines are for computation.
- The only Theta actually instantiated in the essay is run-length encoding, used illustratively,
  plus block-frequency entropy and a brute-force enumeration of simple CAs as candidate detectors.
- One requirement he does state, in "Why the Second Law Works", is that the coarse-graining itself
  must be bounded: the argument assumes one is not inventing an elaborate coarse-graining procedure
  specially set up to pick out collections of states with special behaviour. He does not formalise
  this, and it is the same missing-definition problem in a second place.

Consequence for a programme that wants a theorem: Wolfram supplies no definition to build on. The
observer-side formalisation (PPT adversary, circuit family, security parameter, distribution over
inputs) would be entirely the programme's own contribution.

## 6. CELLULAR AUTOMATA — WHAT HE USES, WHAT HE MEASURES

### Rules
- RULE 30 (elementary CA). The recurring exemplar of intrinsic randomness generation, referenced
  throughout from "The Core Phenomenon of the Second Law" onward. Used QUALITATIVELY only: the
  pattern looks random, no known method finds regularities in it. No measurement in this essay is
  performed on rule 30.
- A reversible 1D "PARTICLE CELLULAR AUTOMATON": a block cellular automaton, block size 2, plus a
  3-colour "delayed particle" variant he says he first studied in 1986. THIS, not rule 30, is the
  workhorse for every quantitative measurement in the essay. It is reversible and self-inverse, and
  conserves particle number (his energy analogue).
- 2D block CAs functionally identical to a discrete-velocity lattice-gas model; hard-sphere and
  hard-square gas simulations. Used to argue a continuous chain from "real physics" down to CAs.
- Enumerations: all 288 3-colour reversible block CAs that fix the all-white state; the 1800
  reversible 3-colour nearest-neighbour ordinary CAs out of 134,217,728; the 6 reversible elementary
  rules, all trivial; and, for reversible block CAs generally, (k^b)^(k^b) rules of which (k^b)!
  are reversible.
- SECOND-ORDER REVERSIBLE CAs: he notes one can construct reversible second-order variants of all
  256 elementary rules, and that they are equivalent to 4-colour first-order nearest-neighbour
  rules. He does NOT name 37R or any specific R-rule, and does not use second-order rules for any
  measurement. [Verified by grep: the string "37R" does not occur in the essay.]

### Measured quantities
- Maximum "blob" size (largest run of adjacent particles) vs time — his order parameter.
- Run-length-encoding compressed length vs time.
- Block frequencies (size 1, size 2) and the block entropy -sum p_i log p_i for blocks of a given
  length, shown converging to constant equilibrium values.
- Coarse-grained entropy under a hierarchy of coarse-grainings — see the definition caveat below.
- Recurrence times and within-cycle fluctuation statistics — see below.
- State transition graphs for small sizes: size 4 (2 x 3^4 = 162 states), size 6, size 10.
- In "Textbook Thermodynamics": energy distributions from token-event-graph collision models,
  shown converging to the exponential Maxwell-Boltzmann form; and particle speeds in a 2D
  hard-sphere gas converging to the Maxwellian form. These are the essay's only contact with
  conventional statistical mechanics results, and they are simulations reproducing known results.

### HIS DEFINITION OF COARSE-GRAINED ENTROPY IS NOT THE TEXTBOOK ONE — worth flagging
In "The Concept of Entropy" he sets up the standard idea (entropy = log of the number of microstates
consistent with a macrostate; a fully specified microstate gives entropy zero) but the quantity he
actually plots is different. He takes ONE coarse-grained initial condition, expands it into all
compatible microstates (his worked example: 6 particles, colour ignored, 2^6 = 64 microstates),
evolves each, and counts HOW MANY DISTINCT COARSE-GRAINED STATES ARE REACHABLE at each step — a
branching count in a multiway graph. Coarse-grained entropy is then the log of that count. He
reports it grows rapidly, then saturates and fluctuates, and notes that once equilibrium is
approached the multiway graph starts MERGING as well as branching.
[Inference] This is a reachable-set / multiway-branching measure, not the Boltzmann count of a
macrostate's volume. It is not obviously the same quantity, and a programme that cites his entropy
curves should not assume it is. He also, at the end of that section, openly de-emphasises the whole
construction: he says coarse-graining and entropy are a rather indirect way of getting at the core
phenomenon, which he takes to be simply that the system produces effective randomness.

Coarse-graining schemes he uses: (i) drop particle colour, keep occupancy; (ii) particle density in
blocks of increasing size, applied after the fact to a single microscopic run; (iii) restrict
attention to one block of cells and ignore the rest (he notes the rest "seeps in" quickly);
(iv) 3x3 blocks of average velocity, for the 2D vortex case.

### RECURRENCE — his data cuts BOTH ways, and he denies it is causal
Numbers he states in the text:
- "delayed particle" rule, 121st initial condition: period 7022 steps.
- size-30 particle CA, width-17 initial blob: recurrence time 155,150 steps.
- size-30, width-13 initial blob: 861,930 steps — the longest in his scan.
- distribution of recurrence times over initial conditions: falls off approximately exponentially
  with a definite tail; mean more than 50,000 steps.
- an "expanding into vacuum" case: becomes essentially periodic with period 70 after 979 steps.
- a light-particle structure that drifts ~1 position per 1300 steps and returns at recurrence time
  46,836 steps.
Within-cycle fluctuations, width-17 blob, 155,150-step cycle: most blob-size fluctuations are small
(linear and log histograms shown); at HALF the recurrence time there is a fluctuation reproducing a
blob as wide as the initial condition, lasting about 280 steps; runner-up width-15 fluctuations are
roughly equally spaced through the cycle.

DIRECTION A (short cycles look ordered). In "Traces of Initial Conditions" he says that where the
behaviour looks much more structured, sometimes this is just because there is a short recurrence
time. In "Ergodicity and Global Behavior" he says thermodynamic-like behaviour is quite often
overwhelmed by freezing, fluctuations and recurrences.

DIRECTION B (long cycles ALSO look ordered — the opposite correlation). Also in "Ergodicity and
Global Behavior", from the size-10 state-transition graph he observes that most of the LONGEST,
closest-to-ergodic cycles look simple and deliberate all the way through, and that the more typical
random-looking behaviour is on SHORTER cycles. Then, a few paragraphs later, he notes that
reversible block CAs WITHOUT particle conservation reach equilibrium FASTER and have FEWER, LONGER
cycles in their state transition graphs.

HIS OWN CONCLUSION: he denies any causal link. At the end of "Ergodicity and Global Behavior" he
states that the approach to equilibrium is its own computational phenomenon, not directly related
to long cycles or to ergodicity. He also argues ergodicity is neither sufficient (an ergodic system
could still spend a long time in visibly organised "counting down" states) nor necessary
(effectively-random sampling gives the same averages without visiting every state).

[Inference] For the related programme that measured apparent entropy tracking recurrence time
rather than irreducibility: Wolfram's denial is an ASSERTION, not a measurement. He never plots
apparent entropy against recurrence time, and never separates a recurrence-time variable from an
irreducibility proxy. His own reported observations point in both directions at once (A and B
above), which is what one would expect if cycle length is confounded with something else in his
data. Nothing he shows contradicts the programme's finding, and nothing he shows supports his own
denial either.

### Other admitted departures from clean Second Law behaviour
- Exact conserved quantities leave permanent traces: particle number, and the parity of the count
  of light/dark cells ("Traces of Initial Conditions").
- "Light particle walls" — a pair of light particles can trap dark particles between them. He works
  out the trapping fractions as rational functions of the separation s: for d = 2 dark particles,
  (s-3)/(s-1) of the Binomial[s,d] configurations get trapped; for d = 3, (s-3)(s-4)/(s(s-1)); for
  d = 4, (s-4)(s-5)/(s(s-1)). Such walls can survive 200,000 steps and significantly slow
  degradation to randomness. These are the essay's only closed-form results and they are elementary
  combinatorics about a specific rule, not statements about the Second Law.
- Long-time tails: power-law rather than exponential decay of correlations, visible in his CA
  approximation to a hard-sphere gas, which he attributes to a computationally reducible
  hydrodynamic layer above the irreducible microscopic layer.
- "Pockets of computational reducibility" always exist inside an irreducible system — his argument
  being that if they did not, that fact could itself be used to reduce the irreducibility. A
  hydrodynamic vortex survives 3x3 coarse-graining in his 2D model.
- Reversible CAs where a random initial block simplifies by "radiating information out": if the
  observer ignores the radiation to infinity, entropy appears to DECREASE. He states this openly in
  "The Second Law and Order in the Universe".

## 7. ONE-WAY FUNCTIONS

He does NOT use the term. Verified by grep over the complete text: "one-way function" does not
occur; "one-way" occurs twice, both non-cryptographic (the one-way transition from order to
disorder of a scrambled egg; a "one-way membrane" as a Maxwell's-demon device). "hash" does not
occur. "P vs NP" does not occur in part 1's body.

Cryptography appears only as metaphor, in two places:
- "How Random Does It Get?": cryptography is listed alongside statistics and machine learning among
  the toolboxes that fail to find regularities; he says the encoding associated with the evolution
  seems too strong to break (his scare quotes on "encoding" and "break").
- "Why the Second Law Works": the dynamics "encrypts" the initial conditions so that no computation
  available to the observer can feasibly "decrypt" them (his scare quotes).

DOES HE DISTINGUISH "EXPENSIVE TO INVERT" FROM "INFORMATION DESTROYED"? Yes, sharply, and it is one
of the strongest things in the essay. It is the point of "Reversibility, Irreversibility and
Equilibrium" and it returns in "The Heat Death of the Universe":
- Information is never destroyed under reversible dynamics. The past remains in principle
  determinable from the future; what makes it inaccessible is that recovering it takes irreducibly
  much computation, vastly more than observers like us can muster.
- He demonstrates the point with a reversible particle CA run outward in both directions from a
  simple middle state: randomness increases FORWARD AND BACKWARD. So the arrow of time cannot come
  from the dynamics; it comes from which initial states we can prepare and which regularities we
  can detect.
- He separates out the class-1/class-2 case, where the rules genuinely do destroy information fast
  and the system falls to a predictable fixed point — and says Second Law behaviour does not occur
  there.

So the "expensive to invert, not destroyed" distinction is exactly his framing. What is absent is
everything that would turn it into a one-way-function statement: no efficiently-computable forward
direction stated as a complexity condition, no negligible inversion probability, no security
parameter, no distribution over inputs, no average-case anything.

## 8. CRITICISM

Searched 2026-09-09 (several WebSearch query formulations, including by the names of physicists and
complexity theorists likely to respond). RESULT: I found NO substantive published critique by a
physicist or complexity theorist of this essay or of the book. That absence is itself the finding.
What exists:

- PUBLICATION VENUE. The essay was republished as a paper: "Computational Foundations for the Second
  Law of Thermodynamics", Complex Systems 33(2), 2024
  (https://www.complex-systems.com/abstracts/v33_i02_a01/). Complex Systems is the journal Wolfram
  founded in 1987 and which Wolfram Media publishes. [Inference] Publication there should not be
  cited as independent peer review.
- The only located review is a book review on ResearchGate (publication 377235360, Dec 2023). I did
  not read it — ResearchGate gates the PDF. Its visible summary language is descriptive, not
  adversarial. [Unverified]
- No critique found from Aaronson, Carroll, Hossenfelder or Woit. One search snippet indicates
  Hossenfelder holds a broadly SIMILAR position (irreducible complexity as the source of the
  experienced Second Law) rather than an opposing one. [Unverified — search snippet only, primary
  source not read.]
- [Speculation] The standard objections a referee would raise, none of them yet published, are easy
  to reconstruct and the programme should pre-empt them: (i) observer-relative entropy is old — this
  is close to the Jaynes subjective-entropy position, and coarse-graining dependence of entropy is a
  long-running debate; (ii) "computationally bounded" without a resource bound is not a definition;
  (iii) computational irreducibility has no formal definition with a theorem attached; (iv) no
  worst-case/average-case distinction anywhere; (v) his plotted coarse-grained entropy is a
  multiway reachable-set count, not the Boltzmann quantity (section 6 above).

## 9. PRIOR ART FOUND WHILE SEARCHING — higher value than the criticism search

None of these are in Wolfram's essay. All are closer to the programme's actual target than Wolfram
is. Flagged for the audit list.

### Weinberger 2005 — WITHDRAWN NP-completeness result. Read the abstract in full.
Edward D. Weinberger, "Computational Complexity as a Source of Thermodynamic Irreversibility",
arXiv:nlin/0505017 [nlin.CD], submitted 2005-05-07, WITHDRAWN BY THE AUTHOR 2006-10-11. The arXiv
page carries only "This paper has been withdrawn by the author" — NO REASON IS GIVEN.

Claimed content, per the abstract: a Fredkin-Toffoli-style billiard-ball computer embedded in a
hard-sphere gas. TRUE/FALSE is encoded by whether a given sphere trajectory is followed; a set of
"routing" spheres follows the same trajectory for all inputs and collides with the signal
trajectories at pre-specified points. The NP-complete question is: does there exist a set of inputs
producing a specified final configuration? Forward simulation is linear in N; the inverse question
is claimed NP-complete. He then argues the asymmetry as N -> infinity justifies the Stosszahlansatz
used in deriving the Boltzmann equation.

[Inference] Two things make this the single most instructive item found:
1. THE INSTANCE IS DESIGNED. The routing spheres are placed so as to implement a circuit. This is a
   worst-case statement about a hand-built gas and says nothing about a typical gas from a typical
   initial condition — which is what the Second Law is about. This is exactly the gap Wolfram never
   mentions, made concrete.
2. THE AUTHOR WITHDREW IT 17 months later, without stating why. Finding out why — via the v1 PDF,
   or any later Weinberger publication — is cheap and should happen before the programme builds an
   argument of the same shape.

### Others (not read)
- "A one-way function from thermodynamics and applications to cryptography" (surfaced via search;
  ResearchGate 225731105). Title is directly on point: an explicitly cryptographic one-way function
  derived from thermodynamics. [Unverified — not read, authors and venue not established.]
- Stephen Wolfram, "P vs. NP and the Difficulty of Computation: A Ruliological Approach",
  2026-01-30. CHECKED AND CLEARED: fetched, stripped (~17,750 words), headings and keywords scanned.
  It is an exhaustive-enumeration ruliology of small Turing machines — runtime distributions across
  s=1..3, k=2 machines, absolute lower bounds, space complexity, nondeterministic/multiway machines,
  ending in "What Does It All Mean for P vs. NP?". Keyword counts over the full text: "Second Law" 0,
  "one-way" 0, "cryptograph" 0, "average-case" 0, "NP-complete" 0, "thermodynam" 1. It does NOT
  need its own audit for this programme.

## 10. THE COMPANION ESSAYS

### Part 2: "A 50-Year Quest" — this is where the cryptography actually is
Headings: When I Was 12 Years Old...; Becoming a Physicist; Statistical Mechanics and Simple
Programs; Computational Irreducibility and Rule 30; Where Does Randomness Come From?; Hydrodynamics,
and a Turbulent Tale; Getting to the Continuum; The Second Law in A New Kind of Science; The Physics
Project—and the Second Law Again; Discovering Class 4; The End of a 50-Year Journey; Appendix.

In "Computational Irreducibility and Rule 30":
- His 1983-84 "Statistical Mechanics of Cellular Automata" paper already invoked NP-completeness: he
  says he suggested there, with a reference to NP completeness, that it might be common for there to
  be no computational shortcut to cellular automaton evolution.
- His 1984 Scientific American caption already said CA patterns can be applied to encrypt messages
  by converting text into an apparently random form. He explicitly ties this to the 2023 thesis,
  saying he later described the Second Law as being about "encrypting" initial conditions to produce
  effective irreversibility.
- MOST RELEVANT TO A ONE-WAY-FUNCTION PROGRAMME: in 1984 at the Institute for Advanced Study he and
  the mathematician John ("Jack") Milnor tried to invent a PUBLIC-KEY cryptosystem based on cellular
  automata — i.e. a trapdoor one-way function built from CA dynamics. They drafted a paper. They
  failed. His summary: they could not figure it out, it has basically still not been figured out,
  and maybe it is actually impossible. He then says the idea of encrypting initial data and turning
  it into effective randomness is nevertheless a crucial part of his computational foundations of
  thermodynamics.
  [Inference] This is a 40-year-old negative result, by the same author, on the CONSTRUCTIVE half of
  the very connection the programme is pursuing. It proves nothing, but it is directly on-topic
  prior experience and belongs on the audit list.
- In "Where Does Randomness Come From?": the tools he threw at rule 30 — combinatorics, dynamical
  systems theory, logic minimisation, statistical analysis, computational complexity theory, number
  theory — plus Connection Machine, Cray, and a Celerity C1200 that computed a
  length-40,114,679,273 repetition period. All negative. This is the evidence base behind the 2023
  claims, and it is entirely resistance-to-known-methods.
- Charles Bennett is credited in the acknowledgements as someone he discussed applying computation
  theory (and Chaitin's ideas) to physics with in the early 1980s. No Bennett result is used.

### Part 3: "How Did We Get Here?"
~37,200 words, almost entirely history of physics (Carnot through Boltzmann, Gibbs, Planck,
Einstein, the ergodic-theory tradition, and a survey of what textbooks said). No cryptography, no
NP-completeness, no one-way functions. One passage is worth recording, in "What the Textbooks Said:
The Evolution of Certainty": discussing Planck's 1903 chapter titled "Proof", which grounds the
Second Law in the empirical fact that nobody has built a perpetual motion machine, Wolfram remarks
parenthetically that this is more than a little reminiscent of P != NP, which through computational
irreducibility is related to the Second Law. That is an assertion of a relationship with no argument
attached, and it is the only P vs NP statement in the trilogy.

## 11. WHAT THE PROGRAMME CAN AND CANNOT TAKE FROM WOLFRAM

CAN take:
- Priority framing. The informal thesis is his, publicly, in embryo since 1984-85 and in full since
  2023. A writeup that does not cite him will look like it missed the obvious prior art.
- The two-directional reversibility argument as a clean demonstration that irreversibility is not in
  the dynamics.
- The observation that the coarse-graining must itself be computationally bounded or the claim is
  vacuous — a constraint the programme's own definitions will need.
- His catalogue of what fails empirically (compression, block entropies, CA-enumeration decoders),
  as a starting list of adversaries a candidate construction must resist.
- His catalogue of exceptions (conservation laws, particle walls, long-time tails, radiating-out
  cases where apparent entropy decreases) as a list of things any general theorem must exclude.

CANNOT take:
- Any definition. There is no formal definition of observer, of boundedness, or of computational
  irreducibility.
- Any theorem, lemma, or proof. There are none.
- Any hardness result. The NP remark is a resemblance, with no problem, no reduction, no class.
- Any average-case statement. The concept does not appear in any of the three essays.

[Speculation] The most defensible position for the programme: Wolfram is the correct citation both
for the IDEA and for the fact that NOBODY HAS FORMALISED IT — he says so himself in "Towards a
Formal Proof of the Second Law", and the twenty-word parenthetical in "Why the Second Law Works" is
the entirety of his engagement with the complexity-theoretic obstacle.
