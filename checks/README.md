# checks/

Three exhaustive computations from the paper's research phase, kept because the paper's
reference list and audit trail mention them. **None of them feeds a number in the paper.**
They need `numpy`; each writes its JSON next to itself (run each from inside this directory).

- `05-hn-short-interval-check.py` / `.json` — exact enumeration of the Håstad–Näslund
  Lemma 10.1 bad-key event for primes on a short interval, against a uniform baseline.
- `check_12R_sector.py` / `.json` — rule 12R (second-order reversible elementary cellular
  automaton) on a periodic ring, N = 8…11, all 4^N states: the longest cycle has length 3^(N−1)
  and one frozen site — the Shiraishi–Takesue 2025 ergodic sector seen on a ring.
- `hardcore_attempt_check.py` / `.json` — exhaustive checks of the Applebaum–Ishai–Kushilevitz
  randomized-encoding identities on tiny instances, and of a discrete-log padding statistic,
  each with its baseline.
