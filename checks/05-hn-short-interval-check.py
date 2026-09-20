#!/usr/bin/env python
"""Research 05 companion: exact enumeration of the Hastad-Naslund Lemma 10.1 bad-key event
   bad(p') := exists s in [1,M], kappa in [-M,M] with gcd(s*P1 - kappa, p') >= D,   P1 = p' >> w,
for p' uniform on the short interval [2^t - 2^ell, 2^t) (odd p' only, as in the application),
against the baseline p' uniform on all odd t-bit integers.

Part A: w on both sides of ell.  Part B: D-scaling in case (a) (w < ell) vs case (b) (w > ell).
Part C: case (b) with the forced P1 = 2^(t-w)-1 vs random P1 values vs a primorial P1.
Part D: exact-formula check  Pr[gcd(N,p') >= D] vs (1/N) sum_{d|N, d>=D} phi(N/d).

Run:  .venv/bin/python .scratch/owf-entropy-paper/research/05-hn-short-interval-check.py
Runtime ~ 26 s (numpy).  Output: 05-hn-short-interval-check.json next to this file.
"""
import json, math, os, time
import numpy as np

rng = np.random.default_rng(0)
HERE = os.path.dirname(os.path.abspath(__file__))


def bad_fraction(pp, w, M, D):
    """Exact fraction of the int64 array pp that is bad. gcd(0, p') = p' >= D counts as bad."""
    P1 = pp >> w
    bad = np.zeros(pp.shape, dtype=bool)
    for s in range(1, M + 1):
        for kappa in range(-M, M + 1):
            N = s * P1 - kappa
            g = np.gcd(np.abs(N), pp)
            g = np.where(N == 0, pp, g)
            bad |= g >= D
    return float(bad.mean())


def odd_interval(lo, hi):
    a = np.arange(lo, hi, dtype=np.int64)
    return a[a % 2 == 1]


def bound_short(t, ell, w, M, D):
    """The bound proved in research/05 section 2.1 (odd-restricted constants)."""
    D1 = 2 * M * 2 ** min(w, t - w)
    return (3 * M * M * 2.0 ** (-(w - 1)) + 6 * M * M / D
            + 3 * M * M * (math.log(D1) + 1) * (2.0 ** (-(w - 1)) + 2.0 ** (-(ell - w)))
            + 12 * M ** 3 * 2.0 ** (-(ell - w)))


def divisors(n):
    ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i * i != n:
                ds.append(n // i)
        i += 1
    return sorted(ds)


def phi(n):
    r, m, p = n, n, 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            r -= r // p
        p += 1
    if m > 1:
        r -= r // m
    return r


out = {}
t0 = time.time()

# ---------- Part A ----------
t, ell, M, D = 24, 14, 2, 64          # c = ell/t = 0.583
short = odd_interval(2 ** t - 2 ** ell, 2 ** t)
full = odd_interval(2 ** (t - 1), 2 ** t)   # all odd t-bit integers (exact, 2^22 values)
A = []
for w in [4, 6, 8, 10, 12, 14, 16, 18, 20]:
    A.append(dict(w=w, side="a (w<=ell)" if w <= ell else "b (w>ell)",
                  short=bad_fraction(short, w, M, D),
                  full_baseline=bad_fraction(full, w, M, D),
                  P1_values_short=int(len(np.unique(short >> w))),
                  bound_2_1=(bound_short(t, ell, w, M, D) if w <= ell else None)))
out["A"] = dict(t=t, ell=ell, M=M, D=D, n_short=int(len(short)), n_full=int(len(full)), rows=A)

# ---------- Part B: D-scaling ----------
B = []
for w in [8, 18]:
    for Dv in [8, 16, 32, 64, 128, 256, 512]:
        B.append(dict(w=w, D=Dv, short=bad_fraction(short, w, M, Dv),
                      full_baseline=bad_fraction(full, w, M, Dv)))
out["B"] = dict(t=t, ell=ell, M=M, rows=B)

# ---------- Part C: fixed P1 vs random P1 vs primorial P1 ----------
t, ell, M, D = 30, 18, 2, 32
C = []
for w in [20, 22, 24]:
    P0 = odd_interval(2 ** w - 2 ** ell, 2 ** w)          # the P0 range forced by the short interval
    forced = 2 ** (t - w) - 1
    rows = dict(w=w, t_minus_w=t - w, forced_P1=forced,
                forced=bad_fraction(forced * 2 ** w + P0, w, M, D))
    rand = [bad_fraction(int(P) * 2 ** w + P0, w, M, D)
            for P in rng.integers(2 ** (t - w - 1), 2 ** (t - w), size=40)]
    rows["random_P1_mean"] = float(np.mean(rand))
    rows["random_P1_max"] = float(np.max(rand))
    prim = 1
    for q in [2, 3, 5, 7, 11, 13]:
        if prim * q < 2 ** (t - w):
            prim *= q
    rows["primorial_P1"] = prim
    rows["primorial"] = bad_fraction(prim * 2 ** w + P0, w, M, D)
    C.append(rows)
out["C"] = dict(t=t, ell=ell, M=M, D=D, rows=C)

# ---------- Part D: exact formula for a fixed N ----------
w = 22
P0 = odd_interval(2 ** w - 2 ** ell, 2 ** w)
pp = (2 ** (t - w) - 1) * 2 ** w + P0
Drows = []
for N in [255, 2 * 255 - 1, 2 * 255 + 1, 210]:
    for Dv in [8, 32, 128]:
        emp = float(np.mean(np.gcd(N, pp) >= Dv))
        # odd p' only: condition on residues coprime to 2 -> use phi over odd part; N odd here
        formula = sum(phi(N // d) for d in divisors(N) if d >= Dv) / N
        Drows.append(dict(N=N, D=Dv, empirical=emp, formula=formula))
out["D"] = dict(t=t, ell=ell, w=w, rows=Drows)

out["runtime_s"] = round(time.time() - t0, 1)
with open(os.path.join(HERE, "05-hn-short-interval-check.json"), "w") as f:
    json.dump(out, f, indent=1)

print(f"Part A  t={out['A']['t']} ell={out['A']['ell']} M={M} D={out['A']['D']}  "
      f"|short|={out['A']['n_short']} |full|={out['A']['n_full']}")
print(f"{'w':>3} {'side':>12} {'#P1':>6} {'Pr[bad] short':>14} {'Pr[bad] full':>13} {'bound 2.1':>10}")
for r in A:
    b = "-" if r["bound_2_1"] is None else f"{r['bound_2_1']:.3g}"
    print(f"{r['w']:>3} {r['side']:>12} {r['P1_values_short']:>6} {r['short']:>14.5f} {r['full_baseline']:>13.5f} {b:>10}")
print("\nPart B  D-scaling (Pr*D shown)")
print(f"{'w':>3} {'D':>4} {'short':>9} {'short*D':>9} {'full':>9} {'full*D':>9}")
for r in B:
    print(f"{r['w']:>3} {r['D']:>4} {r['short']:>9.5f} {r['short']*r['D']:>9.3f} {r['full_baseline']:>9.5f} {r['full_baseline']*r['D']:>9.3f}")
print(f"\nPart C  t={t} ell={ell} M={M} D={D}: w>ell, P1 fixed by the interval vs random P1 vs primorial P1")
for r in C:
    print(f"w={r['w']} t-w={r['t_minus_w']} forced P1={r['forced_P1']}: Pr={r['forced']:.5f} | "
          f"random P1 mean={r['random_P1_mean']:.5f} max={r['random_P1_max']:.5f} | "
          f"primorial P1={r['primorial_P1']}: Pr={r['primorial']:.5f}")
print("\nPart D  Pr[gcd(N,p')>=D] empirical vs (1/N) sum_{d|N,d>=D} phi(N/d)")
for r in Drows:
    print(f"N={r['N']:>4} D={r['D']:>4} empirical={r['empirical']:.5f} formula={r['formula']:.5f}")
print(f"\nruntime {out['runtime_s']} s")
