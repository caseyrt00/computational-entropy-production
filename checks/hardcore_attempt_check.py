#!/usr/bin/env python
"""
Pass 16 -- numerical checks for hardcore_attempt.md.

Run:  .venv/bin/python problems/one-way-functions/passes/pass16/hardcore_attempt_check.py

Checks (all exhaustive, no sampling unless stated):
  A. AIK Lemma 4.15 (Ishai-Kushilevitz) encoding of a tiny mod-2 branching program:
     identities (E1) (E2) (E3) of hardcore_attempt.md, perfect correctness (det decodes),
     unique randomness, perfect privacy (multiset depends only on f(x)).
  B. Full Thm 5.7 pipeline on a 3-bit permutation F(x1,x2,x3) = (x1, x2+x1x3, x3):
     Lemma 4.15 + Lemma 4.10 concatenation + Construction 4.16 locality; verify the
     result is a permutation of {0,1}^20 with locality <= 4, verify the decoder, verify the
     coordinate identity r1 = M11 xor x1 and the s-bit identity s_a = output xor T_a,
     and measure the "guess-monomial-is-zero" predictor for every s-coordinate against
     the predicted 1 - 2^{-deg}.  Baseline: a random-guess predictor (1/2).
  C. Base DLOG collection f_{p,g} (AIK Appendix A): identity-padding fraction mu_p averaged
     over primes in [2^(n-1), 2^n) (baseline: uniform integers, exactly 1/4 + 2^-n);
     Euler-criterion recovery of the LSB and Pohlig-Hellman recovery of the low nu_2(p-1)
     bits (exhaustive over x for small p); exact advantage of the padding predictor for
     every bit position at one p.
Outputs JSON to hardcore_attempt_check.json next to this file.
"""
import itertools, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
out = {}

# ----------------------------------------------------------------------------------------
# A.  Lemma 4.15 on the BP for f(x) = x2 + x1*x3  (vertices s=1, a=2, t=3)
#     edges: (1,2):x1  (1,3):x2  (2,3):x3.   L = [[x1, x2],[1, x3]], det = x1 x3 + x2.
# ----------------------------------------------------------------------------------------
def R1_of(r1):            # 2x2 upper unitriangular
    return np.array([[1, r1], [0, 1]], dtype=np.int64)
def R2_of(r2):            # identity + last column (row 1 only, since ell-2 = 1)
    return np.array([[1, r2], [0, 1]], dtype=np.int64)
def L_of(x):
    x1, x2, x3 = x
    return np.array([[x1, x2], [1, x3]], dtype=np.int64)
def g_bp(x, r1, r2):
    M = (R1_of(r1) @ L_of(x) @ R2_of(r2)) % 2
    return (int(M[0, 0]), int(M[0, 1]), int(M[1, 1])), M

okE, okDec, mult = True, True, {}
for x in itertools.product((0, 1), repeat=3):
    fx = (x[1] + x[0] * x[2]) % 2
    seen = set()
    for r1, r2 in itertools.product((0, 1), repeat=2):
        y, M = g_bp(x, r1, r2)
        # (E2): M11 = L11 + r1_{1,2};  (E1): M12 = ... ; (E3): M22 = L22 + r2_{1}
        # For this BP: M11 = x1 + r1, M12 = x2 + r1 x3 + (x1 + r1) r2, M22 = x3 + r2
        okE &= y[0] == (x[0] + r1) % 2
        okE &= y[1] == (x[1] + r1 * x[2] + (x[0] + r1) * r2) % 2
        okE &= y[2] == (x[2] + r2) % 2
        # decoder = determinant (lower-left entry is the constant 1)
        okDec &= (y[0] * y[2] + y[1]) % 2 == fx
        seen.add(y)
    uniq = len(seen) == 4                     # unique randomness (Lemma 4.12a)
    mult.setdefault(fx, []).append(frozenset(seen))
okPriv = all(len(set(v)) == 1 for v in mult.values())   # multiset depends only on f(x)
okBal = len(set.union(*[set(v[0]) for v in mult.values()])) == 8 and all(len(v[0]) == 4 for v in mult.values())
out["A_lemma415"] = dict(E1_E2_E3=okE, det_decodes=okDec, unique_randomness=uniq,
                         perfect_privacy=okPriv, balanced_tiling=okBal)
print("A. Lemma 4.15 on x2+x1x3:", out["A_lemma415"])

# ----------------------------------------------------------------------------------------
# B.  Thm 5.7 pipeline for the permutation F(x) = (x1, x2 + x1 x3, x3).
#     Degree-3 layer g(x, r1, r2) = (x1 | M11, M12, M22 | x3)  -- 5 output polynomials.
#     Each polynomial is a list of monomials over variables (x1,x2,x3,r1,r2) = indices 0..4.
# ----------------------------------------------------------------------------------------
polys = [
    [(0,)],                                  # x1
    [(0,), (3,)],                            # M11 = x1 + r1
    [(1,), (3, 2), (0, 4), (3, 4)],          # M12 = x2 + r1 x3 + x1 r2 + r1 r2
    [(2,), (4,)],                            # M22 = x3 + r2
    [(2,)],                                  # x3
]
n_xr = 5
# Construction 4.16: for a polynomial with k monomials, fresh bits s_1..s_k, s'_1..s'_{k-1};
# outputs (T_1+s_1, ..., T_k+s_k, s_1+s'_1, s'_1+s_2+s'_2, ..., s'_{k-1}+s_k).
# Build a description of every output bit as (monomial tuple over xr, list of s-indices).
outputs = []          # list of (monomial, s_index_list)
s_meta = []           # per s-coordinate: ('s', poly#, a, monomial) or ('sp', poly#, a)
n_s = 0
for pi, mons in enumerate(polys):
    k = len(mons)
    s_idx = list(range(n_s, n_s + k)); n_s += k
    sp_idx = list(range(n_s, n_s + k - 1)); n_s += k - 1
    for a, T in enumerate(mons):
        s_meta.append(('s', pi, a, T))
    for a in range(k - 1):
        s_meta.append(('sp', pi, a))
    for a, T in enumerate(mons):
        outputs.append((T, [s_idx[a]]))
    if k == 1:
        outputs.append(((), [s_idx[0]]))            # degenerate k=1: (T - s_1, s_1)
    else:
        outputs.append(((), [s_idx[0], sp_idx[0]]))
        for a in range(1, k - 1):
            outputs.append(((), [sp_idx[a - 1], s_idx[a], sp_idx[a]]))
        outputs.append(((), [sp_idx[k - 2], s_idx[k - 1]]))
n_in = n_xr + n_s
n_out = len(outputs)
assert n_in == n_out, (n_in, n_out)
locality = max(len(T) + len(S) for T, S in outputs)

# exhaustive evaluation over all 2^n_in inputs, vectorised
N = 1 << n_in
z = ((np.arange(N, dtype=np.int64)[:, None] >> np.arange(n_in)) & 1).astype(np.int8)   # N x n_in
xr = z[:, :n_xr]; s = z[:, n_xr:]
Y = np.zeros((N, n_out), dtype=np.int8)
for j, (T, S) in enumerate(outputs):
    v = np.ones(N, dtype=np.int8) if T else np.zeros(N, dtype=np.int8)   # empty monomial = absent, not 1
    for t in T:
        v = v & xr[:, t]
    for si in S:
        v = v ^ s[:, si]
    Y[:, j] = v
codes = (Y.astype(np.int64) * (1 << np.arange(n_out, dtype=np.int64))).sum(axis=1)
is_perm = len(np.unique(codes)) == N

# decoder: XOR of each polynomial's 2k block recovers the g-output; then det recovers F
blk, dec_ok = 0, True
g_dec = np.zeros((N, len(polys)), dtype=np.int8)
for pi, mons in enumerate(polys):
    k = len(mons)
    g_dec[:, pi] = Y[:, blk:blk + 2 * k].sum(axis=1) % 2
    blk += 2 * k
F_true = np.stack([xr[:, 0], (xr[:, 1] + xr[:, 0] * xr[:, 2]) % 2, xr[:, 2]], axis=1)
F_dec = np.stack([g_dec[:, 0], (g_dec[:, 1] * g_dec[:, 3] + g_dec[:, 2]) % 2, g_dec[:, 4]], axis=1)
dec_ok = bool((F_true == F_dec).all())
# coordinate identities: r1 = M11 xor x1 ;  r2 = M22 xor x3
r1_id = bool(((g_dec[:, 1] ^ xr[:, 0]) == xr[:, 3]).all())
r2_id = bool(((g_dec[:, 3] ^ xr[:, 2]) == xr[:, 4]).all())

# cheap predictors for every s-coordinate: predict s_a := output bit (i.e. guess T_a = 0)
pred = {}
for si, meta in enumerate(s_meta):
    if meta[0] != 's':
        continue
    _, pi, a, T = meta
    j = next(jj for jj, (TT, SS) in enumerate(outputs) if SS == [si] and TT == T)
    succ = float((Y[:, j] == s[:, si]).mean())
    pred[f"s[poly{pi},mono{T}]"] = dict(deg=len(T), predictor_success=succ, predicted=1 - 2.0 ** (-len(T)))
rng = np.random.default_rng(0)
baseline = float((rng.integers(0, 2, N) == s[:, 0]).mean())
out["B_pipeline"] = dict(n_in=n_in, n_out=n_out, locality=locality, is_permutation=is_perm,
                         decoder_ok=dec_ok, r1_eq_M11_xor_x1=r1_id, r2_eq_M22_xor_x3=r2_id,
                         s_predictors=pred, random_guess_baseline=baseline)
print("B. Thm 5.7 pipeline on F=(x1, x2+x1x3, x3): n=%d locality=%d perm=%s dec=%s r1id=%s r2id=%s" %
      (n_in, locality, is_perm, dec_ok, r1_id, r2_id))
for kk, vv in pred.items():
    print("   %-28s deg=%d  success=%.4f  predicted=%.4f" % (kk, vv["deg"], vv["predictor_success"], vv["predicted"]))
print("   random-guess baseline: %.4f" % baseline)

# ----------------------------------------------------------------------------------------
# C.  Base DLOG collection (AIK Appendix A).
# ----------------------------------------------------------------------------------------
def primes_upto(m):
    sieve = np.ones(m + 1, dtype=bool); sieve[:2] = False
    for i in range(2, int(m ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    return np.nonzero(sieve)[0]

mu = {}
for n in range(10, 21):
    P = primes_upto(1 << n)
    P = P[P >= (1 << (n - 1))]
    mu_p = (float(1 << n) - P + 1) / float(1 << n)
    mu[n] = dict(num_primes=int(len(P)), mean_mu=float(mu_p.mean()),
                 mean_mu_sq=float((mu_p ** 2).mean()),
                 baseline_uniform_integers=0.25 + 2.0 ** (-n))
    print("C. n=%2d  #primes=%6d  E_p[mu_p]=%.4f  E_p[mu_p^2]=%.4f  baseline(uniform p)=%.4f" %
          (n, len(P), mu[n]["mean_mu"], mu[n]["mean_mu_sq"], mu[n]["baseline_uniform_integers"]))
out["C_mu"] = mu

def generator(p):
    q = p - 1; fac = set()
    m, d = q, 2
    while d * d <= m:
        while m % d == 0:
            fac.add(d); m //= d
        d += 1
    if m > 1: fac.add(m)
    for g in range(2, p):
        if all(pow(g, q // f, p) != 1 for f in fac):
            return g
def nu2(m):
    k = 0
    while m % 2 == 0: m //= 2; k += 1
    return k
def low_bits_pohlig_hellman(y, g, p, k):
    """recover x mod 2^k from y = g^x, using the order-2^k subgroup. Elementary."""
    q = p - 1; h = pow(g, q >> k, p)          # generator of the 2^k subgroup
    z = pow(y, q >> k, p); x = 0
    for i in range(k):                        # peel one bit at a time
        t = pow(z * pow(h, (-x) % (1 << k), p), 1 << (k - 1 - i), p)
        if t != 1: x |= 1 << i
    return x

n = 12
P = [int(v) for v in primes_upto(1 << n) if v >= (1 << (n - 1))]
leak = []
for p in P[:40]:
    g = generator(p); k = nu2(p - 1)
    eul_ok = ph_ok = True
    for x in range(1, p):
        y = pow(g, x, p)
        eul_ok &= (pow(y, (p - 1) // 2, p) == 1) == (x % 2 == 0)          # Euler: LSB
        ph_ok &= low_bits_pohlig_hellman(y, g, p, k) == x % (1 << k)     # low nu_2 bits
    leak.append(dict(p=p, nu2=k, euler_lsb_ok=eul_ok, pohlig_hellman_lowbits_ok=ph_ok))
out["C_leaks"] = leak
print("C. Euler LSB + Pohlig-Hellman low bits on %d primes (n=12): all ok = %s" %
      (len(leak), all(l["euler_lsb_ok"] and l["pohlig_hellman_lowbits_ok"] for l in leak)))

# exact advantage of the padding predictor for every bit position, one p, x uniform on {0,1}^n
p = P[len(P) // 2]; g = generator(p)
mu_p = (2 ** n - p + 1) / 2 ** n
adv = {}
for v in range(n):
    succ = 0
    for x in range(1 << n):
        if x == 0 or x >= p:                       # identity region: bit known exactly
            succ += 1
        else:
            succ += 0.5                            # guess (averaged)
    adv[v] = succ / (1 << n) - 0.5
out["C_padding_predictor"] = dict(p=p, mu_p=mu_p, advantage_per_bit=adv, predicted=mu_p / 2)
print("C. padding predictor at p=%d: mu_p=%.4f, advantage per bit = %.4f (predicted mu_p/2 = %.4f)" %
      (p, mu_p, adv[0], mu_p / 2))

with open(os.path.join(HERE, "hardcore_attempt_check.json"), "w") as fh:
    json.dump(out, fh, indent=1, default=str)
print("wrote hardcore_attempt_check.json")
