# Reading note: Takesue, "Ergodic properties and thermodynamic behavior of ERCA. I. Basic properties"

J. Stat. Phys. 56, 371–402 (1989). Source: `sources/takesue1989_ergodic_I.pdf`
+ `.txt`. Read 13 Sep 2026: abstract, §1, §2 (model, symmetries), §5 (phase space structure) in full, §6, references;
§3–§4 (conserved quantities; 40 pages of tables) by heading. Closes B8.

## What it contains that bears on the ERCA draft

- **Definition.** ERCA = second-order reversible elementary CA, two Boolean variables per site, periodic ring of N sites.
  Same object as ours. Reflection and Boolean conjugation give **88 equivalence classes** of the 256 rules (p. 371, §2).
- **§5, p. 393 (the sentence that matters):** "the distributions of cycle lengths were obtained for the 88 classes with
  N ≤ 13." So the exact enumeration of all rules on rings to N = 13 was done in 1989.
- **What he reported from it:** number of cycles grows like 2^N to 4^N (O(2^N) for rules with no conservation law; Fig. 4:
  30R, 75R, 155R); "the mean or maximal cycle length shows a rich variety of N dependence from constant to exponential."
  **No per-rule table** of cycle statistics appears in the paper; cycle data are in Figs. 3–4 only. Statistics named:
  number of cycles, mean cycle length (expected value), maximal cycle length. **Median over states: not mentioned.**
- **Additive rules:** maximal cycle length computed to N < 29 via the superposition basis (p. 392). 90R and 165R: maximal
  cycle length "globally linear in N", so the number of cycles is O(4^N/N) — consistent with our 3·4^N/(4N) count.
- **Interpretation:** exponential number of cycles ⇒ finite ERCA not ergodic in the strict sense; argued not fatal for
  thermodynamic behaviour (p. 394–395). Rule 45 (first-order, reversible for odd N, not time-reversal invariant) has mean
  cycle length o(2^N) — used as the contrast case.
- Cites Martin–Odlyzko–Wolfram 1984 [23] for the algebraic method on additive rules.

## Consequence for the draft's first claim

The enumeration is his (1989, all classes, N ≤ 13). Not new. What the paper does **not** contain: a tabulation per rule;
the state-weighted median; the split of the family by rule shape (skeleton/perturbation) with the growth-rate table;
anything at N > 13 for non-additive rules; the sampled walks to N = 24 for 30R/37R; the predictability/solver part.
The draft must cite p. 393 and describe its enumeration as a reproduction of his with a different statistic and a
different organisation, not as new.
