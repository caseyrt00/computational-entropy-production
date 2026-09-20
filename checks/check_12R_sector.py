"""Pass 16 check prompted by correspondence with S. Takesue: rule 12R on a periodic ring of N sites.
Independent implementation (not pass 02's code). Second-order rule: cur' = f(l,c,r) XOR prev,
f = rule 12 = c AND NOT l, which is Shiraishi-Takesue 2025 eq. (1).
Claims checked, for N = 8..11 by complete enumeration of all 4^N states:
  (a) the longest cycle has length exactly 3^(N-1);
  (b) every state on that cycle has exactly one site with (prev,cur) = (0,0), always the same site;
  (c) the median cycle length over states (the pass-05 statistic).
(a)+(b) is their theorem "12R is ergodic on the sector with one pinned (0,0) site" seen on a ring.
Run: .venv/bin/python check_12R_sector.py   (N=8..11, ~1 min)"""
import numpy as np, json, sys, time
def run(N):
    M = 1 << N; mask = M - 1
    cur = np.arange(M, dtype=np.int64)
    l = ((cur << 1) | (cur >> (N - 1))) & mask          # left neighbour of each site
    f = cur & ~l & mask                                  # rule 12: c AND NOT l
    # state index s = prev*M + cur ; next = (cur, f(cur) XOR prev)
    prev = np.repeat(np.arange(M, dtype=np.int64), M)
    curr = np.tile(cur, M)
    nxt_cur = f[curr] ^ prev
    perm = curr * M + nxt_cur
    # cycle lengths over all states
    seen = np.zeros(M * M, dtype=bool); lengths = np.zeros(M * M, dtype=np.int64)
    longest = 0; longest_start = -1
    for s in range(M * M):
        if seen[s]: continue
        path = []; x = s
        while not seen[x]:
            seen[x] = True; path.append(x); x = perm[x]
        L = len(path); lengths[path] = L
        if L > longest: longest, longest_start = L, s
    med = int(np.median(lengths))
    # walk the longest cycle, record which sites are (0,0)
    zero_sites = None; x = longest_start
    for _ in range(longest):
        p, c = divmod(int(x), M)
        z = frozenset(i for i in range(N) if not ((p >> i) & 1) and not ((c >> i) & 1))
        zero_sites = z if zero_sites is None else (zero_sites if zero_sites == z else 'VARIES')
        if zero_sites == 'VARIES': break
        x = perm[x]
    return dict(N=N, states=M * M, longest=longest, three_pow_Nm1=3 ** (N - 1),
                longest_is_3powNm1=(longest == 3 ** (N - 1)),
                zero_sites_on_longest=(sorted(zero_sites) if zero_sites != 'VARIES' else 'VARIES'),
                median_over_states=med)
out = []
for N in range(8, 12):
    t = time.time(); r = run(N); r['seconds'] = round(time.time() - t, 1); out.append(r); print(r, flush=True)
json.dump(out, open('check_12R_sector.json', 'w'), indent=1)
