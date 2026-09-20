# Reading note: Shiraishi & Takesue, "Complete Ergodicity in One-Dimensional Reversible Cellular Automata"

J. Stat. Phys. 192, 165 (2025), DOI 10.1007/s10955-025-03529-3, CC-BY. arXiv 2408.06691.
Source: `sources/shiraishi_takesue_2025_arxiv2408.06691.pdf` (+ `.txt`). Read 13 Sep 2026: abstract, §1, §2 in full,
§8 Open problems, §9 Discussion, reference list; §3–§7 (the rule-by-rule proofs, ~3500 lines) skimmed by heading only.
Read in pass 17.

## What the paper is

- Object: **semi-infinite one-way CA**. Site 1 is driven by a fixed k-cycle; site n ≥ 2 is updated by a permutation
  chosen by the state of site n−1 (eqs. 8–9). "One-way" means *spatial*: a cell depends only on itself and its left
  neighbour. Not "one-way function". No overlap with our meaning of the phrase.
- "Reversible" = every site update is a permutation (trivially invertible by induction from site 1).
- "Ergodic" = site n has period exactly k^n. Result: all ergodic rules for k = 3 (12 rules), 4 (none), 5 (118,320 rules),
  proved analytically; non-ergodic ones confirmed numerically.
- Seed of the paper: **rule 12R** (second-order ERCA) has a sector, with the two boundary sites fixed at (0,0), that holds
  a single orbit of length 3^N. That is the only ERCA content.

## What it is not (for the ERCA draft, `pass11/DRAFT_reversible_rules.md`)

- No periodic rings. §9 says explicitly that CA with periodic boundary conditions can never be completely ergodic, which
  is why they moved to the semi-infinite setting. Our statistic (median cycle length over states on a ring of size N, all
  256 second-order rules) is not computed, not discussed.
- No cycle-length tables, no enumeration of ERCA beyond the 12R sector.
- Cites Takesue 1987 (PRL) and Hattori–Takesue 1991; does **not** cite Takesue 1989 or 1990.
- Zero on Kolmogorov complexity (the single "Kolmogorov" is KAM), hardness, entropy, one-way functions.

**Verdict: not prior art for any claim in the ERCA draft.** Adjacent result on one rule. Cite it when 12R is mentioned.

## One cross-link worth a sentence [Inference, from our own data]

Pass 11's master table records rule 12R's recurrence time on periodic rings as 81, 243, 729 at N = 8, 10, 12 — i.e.
3^{N/2}, growing ×3 per two sites (`pass11/master_table.csv`, row 12). Their semi-infinite site n has period 3^n.
Same base 3, half the exponent on a ring of N sites. Plausibly the ring sector splits into two interleaved 12R
sub-chains; not checked. Could be asked in the reply; not a claim.

## Status codes for the HANDOFF audit list

Read (partial: proofs skimmed). Read-status upgrade for the ERCA draft's bibliography: add as "adjacent, read".
