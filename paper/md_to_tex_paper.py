"""Typeset ENTROPY_PRODUCTION.md as LaTeX: markdown -> ENTROPY_PRODUCTION.tex (pure ASCII).

Typesetting only: no wording, number, label, tag or citation is altered.  Unlike the ERCA note, this
paper writes its mathematics as Unicode text in the prose (33 backtick spans exist, all filenames in
the references), so the object classified by hand is the *fragment*: every run of mathematics in the
prose is an entry of MATH / RAW / PROSE below, matched longest-first at word boundaries.  Whatever the
dictionaries do not cover is caught afterwards by a leftover check that fails the build: any residual
mathematical character, lone variable letter, function application or digit-letter join in the prose
is a hard error, never a guess.  The 52 displayed formulas are a second hand-written dictionary
(DISPLAY), keyed by their exact source text; an unknown display is a hard error.

Usage (from this directory):
    ../../../../.venv/bin/python md_to_tex_paper.py
Then:  tectonic --keep-logs ENTROPY_PRODUCTION.tex
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'ENTROPY_PRODUCTION.md')
OUT = os.path.join(HERE, 'ENTROPY_PRODUCTION.tex')

# --------------------------------------------------------------------------------------------
# 1. The fragment dictionaries.  Keys are source text with runs of whitespace collapsed to one
#    space and trailing , . ; : removed.  MATH values are inline-math bodies ($...$ is added);
#    RAW values are final LaTeX (prose allowed); PROSE keys look mathematical but are prose
#    (item labels, identifiers, equation-label references) and are set as ordinary text.
# --------------------------------------------------------------------------------------------


MATH = {          # inline mathematics: value is the body of $...$
    'c = C + 4': 'c = C + 4',
    'E_D[σ^rev_D] > C log n': r'\mathrm{E}_D[\sigma^{\mathrm{rev}}_D] > C \log n',
    'BEM_skew ⇒ NP ⊆ BPP': r'\mathrm{BEM}_{\mathrm{skew}} \Rightarrow \mathrm{NP} \subseteq \mathrm{BPP}',
    'no io-OWF ⇒ BEM': r'\text{no io-OWF} \Rightarrow \mathrm{BEM}',
    'DistNP ⊆ HeurP ⇒ BEM': r'\mathrm{DistNP} \subseteq \mathrm{HeurP} \Rightarrow \mathrm{BEM}',
    '⟨ω⟩ > 0': r'\langle\omega\rangle > 0',
    't = cs ≥ p_0(n)': r't = cs \ge p_0(n)',
    '(0^m, 0^m)': '(0^m, 0^m)',
    '(1)⇔(3)': '(1)\\Leftrightarrow(3)',
    '(1/(2q)) · Ω(1 / (q n^{c+1})) = 1 / poly(n)': '(1/(2q)) \\cdot \\Omega(1 / (q n^{c+1})) = 1 / \\mathrm{poly}(n)',
    '(1/(n + d)) · (2/3) · 2^{−pK^t(x)}': '(1/(n + d)) \\cdot (2/3) \\cdot 2^{-\\mathrm{pK}^t(x)}',
    '(3/2)²(n + d)²': '(3/2)^{2}(n + d)^{2}',
    '(BEM ⇒ NP ⊆ BPP)': '(\\mathrm{BEM} \\Rightarrow \\mathrm{NP} \\subseteq \\mathrm{BPP})',
    '(f(z), z)': '(f(z), z)',
    '(M, x, 1^{T^{2c}})': '(M, x, 1^{T^{2c}})',
    '(n, t)': '(n, t)',
    '(no io-OWF ⇒ BEM)': '(\\text{no io-OWF} \\Rightarrow \\mathrm{BEM})',
    '(p, q) ↦': '(p, q) \\mapsto',
    '(x, y)': '(x, y)',
    '(x, y) := ((z, w), R_z(w) 0^n)': '(x, y) := ((z, w), R_z(w) 0^n)',
    '(x, y) ~ D': '(x, y) \\sim D',
    '(x, y) ∈ supp D': '(x, y) \\in \\operatorname{supp} D',
    '(x_0, y_0)': '(x_0, y_0)',
    '(x_0, y_0) ∈ supp D': '(x_0, y_0) \\in \\operatorname{supp} D',
    '(y, x)': '(y, x)',
    '(z, f(z))': '(z, f(z))',
    '(z, w)': '(z, w)',
    '(z, w) ← P': '(z, w) \\leftarrow P',
    '(z, w, ℓ)': '(z, w, \\ell)',
    '(z, x)': '(z, x)',
    '0.81 ≥ 2/3': '0.81 \\ge 2/3',
    '1 − 1/n^2': '1 - 1/n^2',
    '1 − 1/poly': '1 - 1/\\mathrm{poly}',
    '1 − 1/q': '1 - 1/q',
    '1 − 2/q': '1 - 2/q',
    '1 − 2^{−Ω(N)}': '1 - 2^{-\\Omega(N)}',
    '1 − p(n)': '1 - p(n)',
    '1/(2q)': '1/(2q)',
    '1/2': '1/2',
    '1/3': '1/3',
    '1/n^2': '1/n^2',
    '1/q': '1/q',
    '1/q(n)': '1/q(n)',
    '1/q′(n)': "1/q'(n)",
    '1/ε': '1/\\varepsilon',
    '1^n': '1^n',
    '2/3': '2/3',
    '2/q': '2/q',
    '2^n': '2^n',
    '2^s': '2^s',
    '2^{+pK^t(y | x)}': '2^{+\\mathrm{pK}^t(y \\mid x)}',
    '2^{n − o(n)}': '2^{n - o(n)}',
    '2^{n/2}': '2^{n/2}',
    '2^{n−5}': '2^{n-5}',
    '2^{O(log s)} = s^{O(1)}': '2^{O(\\log s)} = s^{O(1)}',
    '2^{−E_D[σ]} ≤ E_D[2^{−σ}] ≤ (3/2)^2 (n + d)^2': '2^{-\\mathrm{E}_D[\\sigma]} \\le \\mathrm{E}_D[2^{-\\sigma}] \\le (3/2)^2 (n + d)^2',
    '2^{−k}': '2^{-k}',
    '2^{−n/2}': '2^{-n/2}',
    '2^{−o(n)}': '2^{-o(n)}',
    '2^{−pK^t(x | y)}': '2^{-\\mathrm{pK}^t(x \\mid y)}',
    '2^{−pK^t(x | y)} = D(x | y) · n^{±O(1)}': '2^{-\\mathrm{pK}^t(x \\mid y)} = D(x \\mid y) \\cdot n^{\\pm O(1)}',
    '2^{−pK^t(y)}': '2^{-\\mathrm{pK}^t(y)}',
    '2^{−T(n)}': '2^{-T(n)}',
    '2^{−σ(x,y)} = m_R(x, y) / D(x, y)': '2^{-\\sigma(x,y)} = m_R(x, y) / D(x, y)',
    '2^{−σ^rev_D} = m_R / D': '2^{-\\sigma^{\\mathrm{rev}}_D} = m_R / D',
    '2^{−σ_t} = m_R / m_F': '2^{-\\sigma_t} = m_R / m_F',
    '2n': '2n',
    '2n/(ε(n) log n)': '2n/(\\varepsilon(n) \\log n)',
    '3/4': '3/4',
    '[n, A(n)]': '[n, A(n)]',
    'a > 0': 'a > 0',
    'A_t': 'A_t',
    'A_t := limsup_n E_n(t)': 'A_t := \\limsup_n E_n(t)',
    'AvgBPP': '\\mathrm{AvgBPP}',
    'B_1 = pK^t(x | y) − log 1/D(x | y)': 'B_1 = \\mathrm{pK}^t(x \\mid y) - \\log 1/D(x \\mid y)',
    'B_1 = pK^t(z | f(z)) − log |f^{−1}(f(z))|': 'B_1 = \\mathrm{pK}^t(z \\mid f(z)) - \\log |f^{-1}(f(z))|',
    'B_1 ≤ log p_0(n)': 'B_1 \\le \\log p_0(n)',
    'B_1 ≤ pK^t(x | y) ≤ n + d': 'B_1 \\le \\mathrm{pK}^t(x \\mid y) \\le n + d',
    'B_2 = pK^t(f(z)) − log 1/D_2(f(z))': 'B_2 = \\mathrm{pK}^t(f(z)) - \\log 1/D_2(f(z))',
    'B_2 = pK^t(y) − log 1/D_2(y)': 'B_2 = \\mathrm{pK}^t(y) - \\log 1/D_2(y)',
    'B_2 ≤ c_D log n': 'B_2 \\le c_D \\log n',
    'B_2 ≤ pK^t(y) ≤ n + d': 'B_2 \\le \\mathrm{pK}^t(y) \\le n + d',
    'BEM': '\\mathrm{BEM}',
    'BEM ⇒ BEM_skew': '\\mathrm{BEM} \\Rightarrow \\mathrm{BEM}_{\\mathrm{skew}}',
    'BEM^O': '\\mathrm{BEM}^O',
    'BEM_skew': '\\mathrm{BEM}_{\\mathrm{skew}}',
    'BEM_skew ⇒ no io-OWF': '\\mathrm{BEM}_{\\mathrm{skew}} \\Rightarrow \\text{no io-OWF}',
    'BEM_skew^O': '\\mathrm{BEM}_{\\mathrm{skew}}^O',
    'BPP ⊇ P': '\\mathrm{BPP} \\supseteq \\mathrm{P}',
    'C': 'C',
    'c': 'c',
    'c = 7a': 'c = 7a',
    'c log n': 'c \\log n',
    'c ≥ 1': 'c \\ge 1',
    'C(f⁻¹) ≤ 10·C(f)': 'C(f^{-1}) \\le 10\\cdot C(f)',
    'c_0': 'c_0',
    'c_0 log n': 'c_0 \\log n',
    'c_D': 'c_D',
    'c_f': 'c_f',
    'c_f log n': 'c_f \\log n',
    'D': 'D',
    'd': 'd',
    'D = (z, f(z))': 'D = (z, f(z))',
    'D = {D_n}': 'D = \\{D_n\\}',
    'D(f(z) | z)': 'D(f(z) \\mid z)',
    'D(G) ≥ 1 − 2/q': 'D(G) \\ge 1 - 2/q',
    'D(G) ≥ 1 − 2/q(n)': 'D(G) \\ge 1 - 2/q(n)',
    'D(S)': 'D(S)',
    'D(S) · E[2^{σ_t} | S] ≤ |S|² n^{O(1)} / 2^n ≤ n^{O(1)}': 'D(S) \\cdot \\mathrm{E}[2^{\\sigma_t} \\mid S] \\le |S|^{2} n^{O(1)} / 2^n \\le n^{O(1)}',
    'D(x | y)': 'D(x \\mid y)',
    'D(x | y) = D_n(x, y) / D_2(y)': 'D(x \\mid y) = D_n(x, y) / D_2(y)',
    'D(x, y)': 'D(x, y)',
    'D(x, y) = 2^{σ^rev_D(x,y)} m_R(x, y)': 'D(x, y) = 2^{\\sigma^{\\mathrm{rev}}_D(x,y)} m_R(x, y)',
    'D(x, y) = D(x | y) D_2(y)': 'D(x, y) = D(x \\mid y) D_2(y)',
    'D(y | x) = D_n(x, y) / D_1(x)': 'D(y \\mid x) = D_n(x, y) / D_1(x)',
    'D(z | f(z)) = 1 / |f^{−1}(f(z))|': 'D(z \\mid f(z)) = 1 / |f^{-1}(f(z))|',
    'D_1(x)': 'D_1(x)',
    'D_1(z) = 2^{−n}': 'D_1(z) = 2^{-n}',
    'D_1, D_2': 'D_1, D_2',
    'D_2': 'D_2',
    'D_2(f(z)) = |f^{−1}(f(z))| 2^{−n}': 'D_2(f(z)) = |f^{-1}(f(z))| 2^{-n}',
    'D_2(y)': 'D_2(y)',
    'D_m(G) ≥ (1/4) μ': 'D_m(G) \\ge (1/4) \\mu',
    'D_n': 'D_n',
    'DistNP ⊆ AvgBPP': '\\mathrm{DistNP} \\subseteq \\mathrm{AvgBPP}',
    'DistNP ⊆ AvgP': '\\mathrm{DistNP} \\subseteq \\mathrm{AvgP}',
    'DistNP ⊆ HeurBPP': '\\mathrm{DistNP} \\subseteq \\mathrm{HeurBPP}',
    'DistNP ⊆ HeurP': '\\mathrm{DistNP} \\subseteq \\mathrm{HeurP}',
    'DistNP^O ⊆ AvgBPP^O': '\\mathrm{DistNP}^O \\subseteq \\mathrm{AvgBPP}^O',
    'DistNP^O ⊆ AvgP^O': '\\mathrm{DistNP}^O \\subseteq \\mathrm{AvgP}^O',
    'DistNP^O ⊆ HeurP^O ⊆ HeurBPP^O': '\\mathrm{DistNP}^O \\subseteq \\mathrm{HeurP}^O \\subseteq \\mathrm{HeurBPP}^O',
    'D′': "D'",
    'e(N) ≤ o(N)': 'e(N) \\le o(N)',
    'E[ #{ (z, w) ∈ P : pK^t(x | y) ≤ log N − log t − 6 } ] ≤ N/4': '\\mathrm{E}[\\, \\#\\{ (z, w) \\in P : \\mathrm{pK}^t(x \\mid y) \\le \\log N - \\log t - 6 \\} \\,] \\le N/4',
    'E[ #{ (z, w) ∈ P : pK^t(y) ≤ n − 6 } ] ≤ N/4': '\\mathrm{E}[\\, \\#\\{ (z, w) \\in P : \\mathrm{pK}^t(y) \\le n - 6 \\} \\,] \\le N/4',
    'E[#bad] ≤ (3/2) · (N/(32t)) · 2(t + 1) ≤ (6/32) N < N/4': '\\mathrm{E}[\\#\\mathrm{bad}] \\le (3/2) \\cdot (N/(32t)) \\cdot 2(t + 1) \\le (6/32) N < N/4',
    'E[#bad] ≤ (3/2) · 2^{n−5} · (t + |M_t|) ≤ (3/32) N < N/4': '\\mathrm{E}[\\#\\mathrm{bad}] \\le (3/2) \\cdot 2^{n-5} \\cdot (t + |M_t|) \\le (3/32) N < N/4',
    'E[2^{−σ_t}]': '\\mathrm{E}[2^{-\\sigma_t}]',
    'E[ν_{(z,w)}(R_z(w) 0^n)] ≤ 2^{−n}': '\\mathrm{E}[\\nu_{(z,w)}(R_z(w) 0^n)] \\le 2^{-n}',
    'E_D[ max(−B_1, 0) ] ≤ L + 1/ln 2 ≤ L + 2': '\\mathrm{E}_D[\\, \\max(-B_1, 0) \\,] \\le L + 1/\\ln 2 \\le L + 2',
    'E_D[ max(−B_2, 0) ] ≤ L + 2': '\\mathrm{E}_D[\\, \\max(-B_2, 0) \\,] \\le L + 2',
    'E_D[2^{+σ_t}] = Σ D · m_F / m_R ≤ p_D(n) n^{c_D} Σ_{supp D} m_F': '\\mathrm{E}_D[2^{+\\sigma_t}] = \\sum D \\cdot m_F / m_R \\le \\allowbreak p_D(n) n^{c_D} \\sum_{\\operatorname{supp} D} m_F',
    'E_D[2^{+σ_t}] ≤ n^C': '\\mathrm{E}_D[2^{+\\sigma_t}] \\le n^C',
    'E_D[2^{+σ_t}] ≥ (1/2) · n^{a+1} · 2^{−d−4} ≥ n^a': '\\mathrm{E}_D[2^{+\\sigma_t}] \\ge (1/2) \\cdot n^{a+1} \\cdot 2^{-d-4} \\ge n^a',
    'E_D[2^{+σ_t}] ≥ n^{C+1}': '\\mathrm{E}_D[2^{+\\sigma_t}] \\ge n^{C+1}',
    'E_D[2^{±σ_t}]': '\\mathrm{E}_D[2^{\\pm\\sigma_t}]',
    'E_D[2^{Σ⁺_{s,P}}] ≤ s^C': '\\mathrm{E}_D[2^{\\Sigma^{+}_{s,P}}] \\le s^C',
    'E_D[2^{Σ⁺_{s,P}}] ≥ n^{kC+1}': '\\mathrm{E}_D[2^{\\Sigma^{+}_{s,P}}] \\ge n^{kC+1}',
    'E_D[2^{Σ⁻_{s,P}}] ≤ s^C': '\\mathrm{E}_D[2^{\\Sigma^{-}_{s,P}}] \\le s^C',
    'E_D[2^{−σ}] = Σ_{supp D} m_R': '\\mathrm{E}_D[2^{-\\sigma}] = \\sum_{\\operatorname{supp} D} m_R',
    'E_D[2^{−σ}]': '\\mathrm{E}_D[2^{-\\sigma}]',                      # the 228-word abstract (B48, 20 Sep 2026)
    'E_D[2^{−σ}] ≥ m_R(x_0, y_0) ≥ n^{−2c_0}': '\\mathrm{E}_D[2^{-\\sigma}] \\ge m_R(x_0, y_0) \\ge n^{-2c_0}',
    'E_D[σ] ≥ −O(log n)': '\\mathrm{E}_D[\\sigma] \\ge -O(\\log n)',
    'E_D[σ^rev_D]': '\\mathrm{E}_D[\\sigma^{\\mathrm{rev}}_D]',
    'e_F': 'e_F',
    'e_F(x, y) := pK^t(x) + pK^t(y | x) − pK^{ct}(x, y)': 'e_F(x, y) := \\mathrm{pK}^t(x) + \\mathrm{pK}^t(y \\mid x) - \\mathrm{pK}^{ct}(x, y)',
    'E_n(t)': 'E_n(t)',
    'e_R': 'e_R',
    'e_R(x, y) := pK^t(y) + pK^t(x | y) − pK^{ct}(x, y)': 'e_R(x, y) := \\mathrm{pK}^t(y) + \\mathrm{pK}^t(x \\mid y) - \\mathrm{pK}^{ct}(x, y)',
    'E_{D_m}[2^{σ_t}] ≥ (μ/4) · |M_t| / (2^{O(1)} t) = μ² 2^n / (2^{O(1)} t)': '\\mathrm{E}_{D_m}[2^{\\sigma_t}] \\ge (\\mu/4) \\cdot |M_t| / (2^{O(1)} t) = \\mu^{2} 2^n / (2^{O(1)} t)',
    'E_{D_m}[2^{σ_{t_k}}] ≥ 2^{n − o(n)}': '\\mathrm{E}_{D_m}[2^{\\sigma_{t_k}}] \\ge 2^{n - o(n)}',
    'E_{D′}[2^{−σ_t}] = E_D[2^{+σ_t}]': "\\mathrm{E}_{D'}[2^{-\\sigma_t}] = \\mathrm{E}_D[2^{+\\sigma_t}]",
    'E_{x ~ D(· | y)} [ 2^{−pK^t(x | y)} / D(x | y) ] = Σ_x 2^{−pK^t(x | y)} ≤ (3/2)(n + d)': '\\mathrm{E}_{x \\sim D(\\cdot \\mid y)} [\\, 2^{-\\mathrm{pK}^t(x \\mid y)} / D(x \\mid y) \\,] = \\sum_x 2^{-\\mathrm{pK}^t(x \\mid y)} \\le (3/2)(n + d)',
    'E|P ∖ G| ≤ N/2': '\\mathrm{E}|P \\setminus G| \\le N/2',
    'F': 'F',
    'f': 'f',
    'f : {0,1}^n → {0,1}^n': 'f : \\{0,1\\}^n \\to \\{0,1\\}^n',
    'F(z, w, ℓ)': 'F(z, w, \\ell)',
    'G': 'G',
    'G = G_q ⊆ supp D': 'G = G_q \\subseteq \\operatorname{supp} D',
    'G ⊆ P': 'G \\subseteq P',
    'good(z)': '\\mathrm{good}(z)',
    'HeurBPP': '\\mathrm{HeurBPP}',
    'HeurP ⊆ HeurBPP': '\\mathrm{HeurP} \\subseteq \\mathrm{HeurBPP}',
    'i': 'i',
    'i = 1, …, i_max(n)': 'i = 1, \\dots, i_{\\max}(n)',
    'i ≤ i(t) := max{ i_T : T^{2c} ≤ t } ≤ (1/c) log log t': 'i \\le i(t) := \\max\\{ i_T : T^{2c} \\le t \\} \\le (1/c) \\log \\log t',
    'i ≥ 1': 'i \\ge 1',
    'i(t) < i_max(n)': 'i(t) < i_{\\max}(n)',
    'i_max(n) = (1/7a) · log(an/log n)': 'i_{\\max}(n) = (1/7a) \\cdot \\log(an/\\log n)',
    'j ∈ {1, …, n + d}': 'j \\in \\{1, \\dots, n + d\\}',
    'K': 'K',
    'k': 'k',
    'k = ⌈log |f^{−1}(y)|⌉ + c log n': 'k = \\lceil\\log |f^{-1}(y)|\\rceil + c \\log n',
    'k ≥ max(j, k_0)': 'k \\ge \\max(j, k_0)',
    'K(x | y)': 'K(x \\mid y)',
    'K(x | y) − K(y | x)': 'K(x \\mid y) - K(y \\mid x)',
    'K(x) − K(y)': 'K(x) - K(y)',
    'K^t': 'K^t',
    'k_0': 'k_0',
    'kT': 'kT',
    'kT ln 2': 'kT \\ln 2',
    'L = log(3(n + d)/2)': 'L = \\log(3(n + d)/2)',
    'L = log(3(n + d)/2) ≤ log n + 2': 'L = \\log(3(n + d)/2) \\le \\log n + 2',
    'log 1/D': '\\log 1/D',
    'log 1/D(x | y)': '\\log 1/D(x \\mid y)',
    'log 1/D(x, y)': '\\log 1/D(x, y)',
    'log 1/D_2(y)': '\\log 1/D_2(y)',
    'log 1/δ': '\\log 1/\\delta',
    'log log n': '\\log \\log n',
    'log log t': '\\log \\log t',
    'log n': '\\log n',
    'log |S| + O(log n)': '\\log |S| + O(\\log n)',
    'log(1/D(S))': '\\log(1/D(S))',
    'log(1/μ)': '\\log(1/\\mu)',
    'log(an/log n)': '\\log(an/\\log n)',
    'M': 'M',
    'm = 2n': 'm = 2n',
    'M ~ {0,1}^j': 'M \\sim \\{0,1\\}^j',
    'm(n)': 'm(n)',
    'm(n) ≠ n': 'm(n) \\ne n',
    'm^j': 'm^j',
    'm^{k_0} ≥ t_D': 'm^{k_0} \\ge t_D',
    'm_F': 'm_F',
    'm_F ≥ D(x, y) / (p n^{c_D})': 'm_F \\ge D(x, y) / (p n^{c_D})',
    'm_F(y, x) = 2^{−pK^t(y) − pK^t(x | y)} = m_R(x, y)': 'm_F(y, x) = 2^{-\\mathrm{pK}^t(y) - \\mathrm{pK}^t(x \\mid y)} = m_R(x, y)',
    'm_R': 'm_R',
    'm_R ≥ D(x, y) / (p n^{c_D})': 'm_R \\ge D(x, y) / (p n^{c_D})',
    'm_R(x, y)': 'm_R(x, y)',
    'm_R(x, y) = 2^{−pK^t(y) − pK^t(x | y)}': 'm_R(x, y) = 2^{-\\mathrm{pK}^t(y) - \\mathrm{pK}^t(x \\mid y)}',
    'm_R(x_0, y_0) ≥ n^{−2c_0}': 'm_R(x_0, y_0) \\ge n^{-2c_0}',
    'm_R(y, x) = m_F(x, y)': 'm_R(y, x) = m_F(x, y)',
    'M_t': 'M_t',
    'M_t := S_{n,i(t)}': 'M_t := S_{n,i(t)}',
    'max(n, m(n)) + d': '\\max(n, m(n)) + d',
    'N': 'N',
    'n': 'n',
    'n + c log n − 2 − L': 'n + c \\log n - 2 - L',
    'n + d': 'n + d',
    'N := |P| = μ 2^{2n}': 'N := |P| = \\mu 2^{2n}',
    'N = pq': 'N = pq',
    'n ≥ d': 'n \\ge d',
    'N/(32t)': 'N/(32t)',
    'n^C': 'n^C',
    'n^{log* n}': 'n^{\\log^{*} n}',
    'n^{O(1)}': 'n^{O(1)}',
    'n^{−2c_0}': 'n^{-2c_0}',
    'n^{−O(1)} ≤ E_D[2^{−σ}] ≤ O(n²)': 'n^{-O(1)} \\le \\mathrm{E}_D[2^{-\\sigma}] \\le O(n^2)',
    'no io-OWF^O': '\\text{no io-OWF}^O',
    'NP': '\\mathrm{NP}',
    'coNP/poly': '\\mathrm{coNP}/\\mathrm{poly}',      # B46: Bogdanov and Trevisan 2006 entry
    'NP ⊄ BPP': '\\mathrm{NP} \\not\\subseteq \\mathrm{BPP}',
    'NP ⊆ BPP': '\\mathrm{NP} \\subseteq \\mathrm{BPP}',
    'NP ⊆ BPP ⇒ BEM ⇒ no io-OWF': '\\mathrm{NP} \\subseteq \\mathrm{BPP} \\Rightarrow \\mathrm{BEM} \\Rightarrow \\text{no io-OWF}',
    'NP^O': '\\mathrm{NP}^O',
    'NP^O ⊄ BPP^O': '\\mathrm{NP}^O \\not\\subseteq \\mathrm{BPP}^O',
    'O': 'O',
    'O ∈ A_{t_k}': 'O \\in A_{t_k}',
    'O(1)': 'O(1)',
    'O(log n)': 'O(\\log n)',
    'O(log t)': 'O(\\log t)',
    'O(log)': 'O(\\log)',
    'o(n)': 'o(n)',
    'O(t) + O(n)': 'O(t) + O(n)',
    'O_a': 'O_a',
    'O_a = F + A': 'O_a = F + A',
    'P': 'P',
    'p': 'p',
    'P := M_t × {0,1}^n': 'P := M_t \\times \\{0,1\\}^n',
    'p = max(p_0, t_D)': 'p = \\max(p_0, t_D)',
    'P = NP': '\\mathrm{P} = \\mathrm{NP}',
    'P ≠ NP': '\\mathrm{P} \\ne \\mathrm{NP}',
    'P ≥ id': 'P \\ge \\mathrm{id}',
    'p ≥ t_D': 'p \\ge t_D',
    'p(cs + O(n))': 'p(cs + O(n))',
    'p(cs)': 'p(cs)',
    'p(n)': 'p(n)',
    'p(n) = 2^{−6an/log n}': 'p(n) = 2^{-6an/\\log n}',
    'p(n) · |S_{n,i−1}|': 'p(n) \\cdot |S_{n,i-1}|',
    'p(q)': 'p(q)',
    'P(s)': 'P(s)',
    'P(s) ≥ s': 'P(s) \\ge s',
    'p(t)': 'p(t)',
    'P[x(+t) | λ(+t)] / P[x(−t) | λ(−t)] = exp(−βQ)': 'P[x(+t) \\mid \\lambda(+t)] / P[x(-t) \\mid \\lambda(-t)] = \\exp(-\\beta Q)',
    'p_0': 'p_0',
    'p_0 ≥ n': 'p_0 \\ge n',
    'p_D': 'p_D',
    'p_D, C': 'p_D, C',
    'P_F(+ω) / P_R(−ω) = e^{ω}': 'P_F(+\\omega) / P_R(-\\omega) = e^{\\omega}',
    'P_F(ω) / P_R(−ω) = e^ω': 'P_F(\\omega) / P_R(-\\omega) = e^{\\omega}',
    'PA': '\\mathrm{PA}',
    'pK^p(x | y) ≤ log 1/D(x | y) + log p': '\\mathrm{pK}^p(x \\mid y) \\le \\log 1/D(x \\mid y) + \\log p',
    'pK^p(y | x) ≤ log 1/D(y | x) + log p': '\\mathrm{pK}^p(y \\mid x) \\le \\log 1/D(y \\mid x) + \\log p',
    'pK^s(z) + pK^s(f(z) | z) ≤ n + d + c_f log n': '\\mathrm{pK}^s(z) + \\mathrm{pK}^s(f(z) \\mid z) \\le n + d + c_f \\log n',
    'pK^t': '\\mathrm{pK}^t',
    'pK^t(x | y)': '\\mathrm{pK}^t(x \\mid y)',
    'pK^t(x | y) ≤ log 1/D(x | y) + log p_D(n)': '\\mathrm{pK}^t(x \\mid y) \\le \\log 1/D(x \\mid y) + \\log p_D(n)',
    'pK^t(x | y) ≤ |x| + d': '\\mathrm{pK}^t(x \\mid y) \\le |x| + d',
    'pK^t(x | y) ≥ log 1/D(x | y) − O(log n)': '\\mathrm{pK}^t(x \\mid y) \\ge \\log 1/D(x \\mid y) - O(\\log n)',
    'pK^t(x) + pK^t(y | x) ≤ 2n + O(1)': '\\mathrm{pK}^t(x) + \\mathrm{pK}^t(y \\mid x) \\le 2n + O(1)',
    'pK^t(x) − pK^t(y)': '\\mathrm{pK}^t(x) - \\mathrm{pK}^t(y)',
    'pK^t(x) ≤ 2n + d': '\\mathrm{pK}^t(x) \\le 2n + d',
    'pK^t(x) ≤ log 1/D_1(x) + c_D log n': '\\mathrm{pK}^t(x) \\le \\log 1/D_1(x) + c_D \\log n',
    'pK^t(x) ≤ log 1/δ + O(log T(n))': '\\mathrm{pK}^t(x) \\le \\log 1/\\delta + O(\\log T(n))',
    'pK^t(x) ≤ |x| + d': '\\mathrm{pK}^t(x) \\le |x| + d',
    'pK^t(x_0 | y_0) ≤ c_0 log n': '\\mathrm{pK}^t(x_0 \\mid y_0) \\le c_0 \\log n',
    'pK^t(y | x)': '\\mathrm{pK}^t(y \\mid x)',
    'pK^t(y | x) ≤ log 1/D(y | x) + log p_D(n)': '\\mathrm{pK}^t(y \\mid x) \\le \\log 1/D(y \\mid x) + \\log p_D(n)',
    'pK^t(y | x) ≤ O(1)': '\\mathrm{pK}^t(y \\mid x) \\le O(1)',
    'pK^t(y) + pK^t(x | y)': '\\mathrm{pK}^t(y) + \\mathrm{pK}^t(x \\mid y)',
    'pK^t(y) ≤ k': '\\mathrm{pK}^t(y) \\le k',
    'pK^t(y) ≤ log 1/D_2(y) + c_D log n': '\\mathrm{pK}^t(y) \\le \\log 1/D_2(y) + c_D \\log n',
    'pK^t(y_0) ≤ c_0 log n': '\\mathrm{pK}^t(y_0) \\le c_0 \\log n',
    'pK^t(z | f(z)) ≤ log |f^{−1}(f(z))| + c log n': '\\mathrm{pK}^t(z \\mid f(z)) \\le \\log |f^{-1}(f(z))| + c \\log n',
    'pK^t(z | y) ≤ k': '\\mathrm{pK}^t(z \\mid y) \\le k',
    'pK^t(z) ≤ n + d': '\\mathrm{pK}^t(z) \\le n + d',
    'pK^t_α': '\\mathrm{pK}^t_{\\alpha}',
    'pK^{O(qt/α)}_β(x) ≤ pK^t_α(x) + O(log(q/α))': '\\mathrm{pK}^{O(qt/\\alpha)}_{\\beta}(x) \\le \\mathrm{pK}^t_{\\alpha}(x) + O(\\log(q/\\alpha))',
    'pK^{p(cs)}(y) + pK^{p(cs)}(x | y) − log p(cs) ≤ pK^{cs}(x, y) ≤ pK^s(x) + pK^s(y | x) + O(log s)': '\\mathrm{pK}^{p(cs)}(y) + \\mathrm{pK}^{p(cs)}(x \\mid y) - \\log p(cs) \\le \\mathrm{pK}^{cs}(x, y) \\le \\mathrm{pK}^s(x) + \\mathrm{pK}^s(y \\mid x) + O(\\log s)',
    'pK^{p(n)}(x | y) ≤ log 1/D(x | y) + log p(n)': '\\mathrm{pK}^{p(n)}(x \\mid y) \\le \\log 1/D(x \\mid y) + \\log p(n)',
    'pK^{P(s)} ≤ pK^s': '\\mathrm{pK}^{P(s)} \\le \\mathrm{pK}^s',
    'pK^{P(s)}(f(z)) ≥ log 1/D_2(f(z)) − 2 − L': '\\mathrm{pK}^{P(s)}(f(z)) \\ge \\log 1/D_2(f(z)) - 2 - L',
    'pK^{P(s)}(z | f(z)) > log |f^{−1}(f(z))| + c log n': '\\mathrm{pK}^{P(s)}(z \\mid f(z)) > \\log |f^{-1}(f(z))| + c \\log n',
    'pK^{p_0(n)}(x | y) ≤ log 1/D(x | y) + log p_0(n)': '\\mathrm{pK}^{p_0(n)}(x \\mid y) \\le \\log 1/D(x \\mid y) + \\log p_0(n)',
    'pK^{t′}(x | y) ≤ pK^t(x | y)': "\\mathrm{pK}^{t'}(x \\mid y) \\le \\mathrm{pK}^t(x \\mid y)",
    'pK^{t′}(x) ≤ pK^t(x)': "\\mathrm{pK}^{t'}(x) \\le \\mathrm{pK}^t(x)",
    'Pr[ 2^{−pK^t(x|y)} / D(x|y) ≥ 2^{α} (3/2)(n + d) ] ≤ 2^{−α}': '\\Pr[\\, 2^{-\\mathrm{pK}^t(x|y)} / D(x|y) \\ge 2^{\\alpha} (3/2)(n + d) \\,] \\le 2^{-\\alpha}',
    'Pr[ limsup_k A_{t_k} ] ≥ 1/3': '\\Pr[\\, \\limsup_k A_{t_k} \\,] \\ge 1/3',
    'Pr[ |G| ≥ N/4 ] ≥ 1/3': '\\Pr[\\, |G| \\ge N/4 \\,] \\ge 1/3',
    'Pr[A_t] ≥ limsup_n Pr[E_n(t)] ≥ 1/3': '\\Pr[A_t] \\ge \\limsup_n \\Pr[E_n(t)] \\ge 1/3',
    'Pr[Q(y) = (z, w)] ≤ (t + 1)/(N − t) ≤ 2(t + 1)/N': '\\Pr[Q(y) = (z, w)] \\le (t + 1)/(N - t) \\le 2(t + 1)/N',
    'Pr_D[ 2^{−σ} ≥ 2^{α} (3/2)^2 (n + d)^2 ] ≤ 2^{−α}': '\\Pr_D[\\, 2^{-\\sigma} \\ge 2^{\\alpha} (3/2)^2 (n + d)^2 \\,] \\le 2^{-\\alpha}',
    'Pr_r[Q prints y] ≤ Pr_r[touch (z, w)] + ν_{(z,w)}(y)': '\\Pr_r[Q \\text{ prints } y] \\le \\Pr_r[\\text{touch } (z, w)] + \\nu_{(z,w)}(y)',
    'Pr_z[ B_1 > c log n ] ≥ 3/4': '\\Pr_z[\\, B_1 > c \\log n \\,] \\ge 3/4',
    'Pr_z[ B_2 < −2 − L ] ≤ 1/4': '\\Pr_z[\\, B_2 < -2 - L \\,] \\le 1/4',
    'Pr_z[B_1 > c log n] ≥ 1 − 1/n': '\\Pr_z[B_1 > c \\log n] \\ge 1 - 1/n',
    'Pr_z[f(z) is a good image] ≥ 1/(2q)': '\\Pr_z[f(z) \\text{ is a good image}] \\ge 1/(2q)',
    'Pr_z[good(z)] = Σ_y D_2(y) · (fraction of good preimages of y)': '\\Pr_z[\\mathrm{good}(z)] = \\sum_y D_2(y) \\cdot (\\text{fraction of good preimages of } y)',
    'Pr_z[good(z)] ≥ 1/q(n)': '\\Pr_z[\\mathrm{good}(z)] \\ge 1/q(n)',
    'Pr_{y ~ D_2}[ pK^t(y) < log 1/D_2(y) − α − log(3(n + d)/2) ] ≤ 2^{−α}': '\\Pr_{y \\sim D_2}[\\, \\mathrm{pK}^t(y) < \\log 1/D_2(y) - \\alpha - \\log(3(n + d)/2) \\,] \\le 2^{-\\alpha}',
    'Pr_{z ~ D(· | y)}[B_1 < −α − L] ≤ 2^{−α}': '\\Pr_{z \\sim D(\\cdot \\mid y)}[B_1 < -\\alpha - L] \\le 2^{-\\alpha}',
    'Q': 'Q',
    'q': 'q',
    'q = ln(1/(1 − β))': 'q = \\ln(1/(1 - \\beta))',
    'q(n)': 'q(n)',
    'q(n) = n': 'q(n) = n',
    'q(n) = n^2': 'q(n) = n^2',
    'Q(y)': 'Q(y)',
    'q′': "q'",
    'r': 'r',
    'R_z(w)': 'R_z(w)',
    'R_z(x) := F(z, x, 1) ⋯ F(z, x, n)': 'R_z(x) := F(z, x, 1) \\cdots F(z, x, n)',
    'r′ ∈ {0,1}^{t′}': "r' \\in \\{0,1\\}^{t'}",
    'S': 'S',
    's': 's',
    's := max(p_0, t_D)': 's := \\max(p_0, t_D)',
    's ≤ n^k': 's \\le n^k',
    's ≥ n': 's \\ge n',
    's ≥ p_0(n)': 's \\ge p_0(n)',
    's ≥ p_0(n) ≥ n': 's \\ge p_0(n) \\ge n',
    's^C': 's^C',
    's^C ≤ n^{kC}': 's^C \\le n^{kC}',
    'S_{n,i(t)}': 'S_{n,i(t)}',
    'S_{n,i}': 'S_{n,i}',
    'SAT': '\\mathrm{SAT}',
    'supp D': '\\operatorname{supp} D',
    't': 't',
    't := max(p_D, t_D)': 't := \\max(p_D, t_D)',
    't = m^k': 't = m^k',
    't = p(n)': 't = p(n)',
    't = poly(T(n))': 't = \\mathrm{poly}(T(n))',
    't ≤ t′': "t \\le t'",
    't ≤ |M_t| = μ 2^n': 't \\le |M_t| = \\mu 2^n',
    't ≥ n': 't \\ge n',
    't ≥ p': 't \\ge p',
    't ≥ p(n)': 't \\ge p(n)',
    't ≥ p_0(n)': 't \\ge p_0(n)',
    't ≥ p_D(n)': 't \\ge p_D(n)',
    't ≥ t_D': 't \\ge t_D',
    't ≥ |x|': 't \\ge |x|',
    'T(n)': 'T(n)',
    't(n)': 't(n)',
    'T(n) ≥ n': 'T(n) \\ge n',
    't_D': 't_D',
    't_D = poly(T(n))': 't_D = \\mathrm{poly}(T(n))',
    't_D ≤ t': 't_D \\le t',
    't_k := m^k': 't_k := m^k',
    't_k ≥ max(p_D(m), t_D)': 't_k \\ge \\max(p_D(m), t_D)',
    'U': 'U',
    'u ↦ 2^{−u}': 'u \\mapsto 2^{-u}',
    'U(M, w)': 'U(M, w)',
    'U(p, r)': 'U(p, r)',
    'UP ∩ coUP ⊆ NP': '\\mathrm{UP} \\cap \\mathrm{coUP} \\subseteq \\mathrm{NP}',
    'USamp': '\\mathrm{USamp}',
    'USamp(1^n, 1^t, y)': '\\mathrm{USamp}(1^n, 1^t, y)',
    'w ~ {0,1}^{t(n)}': 'w \\sim \\{0,1\\}^{t(n)}',
    'W − ΔF': 'W - \\Delta F',
    'X': 'X',
    'x': 'x',
    'x ∈ supp D_1': 'x \\in \\operatorname{supp} D_1',
    'x, y ∈ {0,1}^n': 'x, y \\in \\{0,1\\}^n',
    'y': 'y',
    'y = R_z(w) 0^n': 'y = R_z(w) 0^n',
    'y_0': 'y_0',
    'y_ℓ': 'y_{\\ell}',
    'z': 'z',
    'z, w ∈ {0,1}^n': 'z, w \\in \\{0,1\\}^n',
    '{0,1}^n': '\\{0,1\\}^n',
    '{0,1}^n × {0,1}^n': '\\{0,1\\}^n \\times \\{0,1\\}^n',
    '{F(z, x, ℓ) : z ∈ M_t}': '\\{F(z, x, \\ell) : z \\in M_t\\}',
    '|f^{−1}(y)| / (2q)': '|f^{-1}(y)| / (2q)',
    'α': '\\alpha',
    'α = 2': '\\alpha = 2',
    'α = 2/3': '\\alpha = 2/3',
    'α ≥ 0': '\\alpha \\ge 0',
    'β = 0.9': '\\beta = 0.9',
    'δ': '\\delta',
    'ΔF': '\\Delta F',
    'ε': '\\varepsilon',
    'ε(n) → ∞': '\\varepsilon(n) \\to \\infty',
    'λ': '\\lambda',
    'μ': '\\mu',
    'μ := |M_t| / 2^n = p(n)^{i(t)}': '\\mu := |M_t| / 2^n = p(n)^{i(t)}',
    'ν_{(z,w)}': '\\nu_{(z,w)}',
    'Π₁': '\\Pi_{1}',
    'ρ_F(x_{−τ}) P[x(+t) | λ(+t)]': '\\rho_F(x_{-\\tau})\\, P[x(+t) \\mid \\lambda(+t)]',
    'ρ_R(x_{+τ}) = ρ_F(x_{+τ})': '\\rho_R(x_{+\\tau}) = \\rho_F(x_{+\\tau})',
    'ρ_R(x_{+τ}) P[x(−t) | λ(−t)]': '\\rho_R(x_{+\\tau})\\, P[x(-t) \\mid \\lambda(-t)]',
    'σ': '\\sigma',
    'σ = σ^rev_D': '\\sigma = \\sigma^{\\mathrm{rev}}_D',
    'σ^fwd_D := log(D / m_F)': '\\sigma^{\\mathrm{fwd}}_D := \\log(D / m_F)',
    'σ^rev_D': '\\sigma^{\\mathrm{rev}}_D',
    'σ^rev_D = B_1 + B_2': '\\sigma^{\\mathrm{rev}}_D = B_1 + B_2',
    'σ^rev_D = log(D / m_R)': '\\sigma^{\\mathrm{rev}}_D = \\log(D / m_R)',
    'σ^rev_D = s': '\\sigma^{\\mathrm{rev}}_D = s',
    'σ^rev_D − σ^fwd_D': '\\sigma^{\\mathrm{rev}}_D - \\sigma^{\\mathrm{fwd}}_D',
    'σ^rev_D − σ^fwd_D = log(D / m_R) − log(D / m_F) = log m_F − log m_R': '\\sigma^{\\mathrm{rev}}_D - \\sigma^{\\mathrm{fwd}}_D = \\log(D / m_R) - \\log(D / m_F) = \\log m_F - \\log m_R',
    'σ^rev_D ≤ O(log n)': '\\sigma^{\\mathrm{rev}}_D \\le O(\\log n)',
    'Σ_G m_F': '\\sum_G m_F',
    'Σ_P E[Pr_r[Q prints y]] ≤ t + |M_t|': '\\sum_P \\mathrm{E}[\\Pr_r[Q \\text{ prints } y]] \\le t + |M_t|',
    'Σ_P E[Pr_r[Q(y) = (z, w)]] ≤ 2(t + 1)': '\\sum_P \\mathrm{E}[\\Pr_r[Q(y) = (z, w)]] \\le 2(t + 1)',
    'Σ_P E[ν_{(z,w)}(y)] ≤ N 2^{−n} = |M_t|': '\\sum_P \\mathrm{E}[\\nu_{(z,w)}(y)] \\le N 2^{-n} = |M_t|',
    'Σ_P Pr_r[touch] ≤ t': '\\sum_P \\Pr_r[\\mathrm{touch}] \\le t',
    'Σ_Q Pr_r[Q prints y] ≥ 2/3': '\\sum_Q \\Pr_r[Q \\text{ prints } y] \\ge 2/3',
    'Σ_Q Pr_r[Q(y) = (z, w)] ≥ 2/3': '\\sum_Q \\Pr_r[Q(y) = (z, w)] \\ge 2/3',
    'σ_t': '\\sigma_t',
    'σ_t = ±O(log)': '\\sigma_t = \\pm O(\\log)',
    'σ_t = σ^rev_D − σ^fwd_D': '\\sigma_t = \\sigma^{\\mathrm{rev}}_D - \\sigma^{\\mathrm{fwd}}_D',
    'σ_t(f(z), z) = −σ_t(z, f(z))': '\\sigma_t(f(z), z) = -\\sigma_t(z, f(z))',
    'σ_t(x, y)': '\\sigma_t(x, y)',
    'σ_t(x, y) = σ^rev_D(x, y) − σ^fwd_D(x, y)': '\\sigma_t(x, y) = \\sigma^{\\mathrm{rev}}_D(x, y) - \\sigma^{\\mathrm{fwd}}_D(x, y)',
    'σ_t(y, x) = −σ_t(x, y)': '\\sigma_t(y, x) = -\\sigma_t(x, y)',
    'Σ_{|Q| ≤ k} Pr_r[Q prints y] ≥ 2/3': '\\sum_{|Q| \\le k} \\Pr_r[Q \\text{ prints } y] \\ge 2/3',
    'Σ⁺': '\\Sigma^{+}',
    'Σ⁺ ≤ σ': '\\Sigma^{+} \\le \\sigma',
    'Σ⁺_{s,P} ≤ O(log s)': '\\Sigma^{+}_{s,P} \\le O(\\log s)',
    'Σ⁺_{s,P} ≤ σ_s': '\\Sigma^{+}_{s,P} \\le \\sigma_s',
    'Σ⁺_{s,P}(x, y) ≤ O(log s)': '\\Sigma^{+}_{s,P}(x, y) \\le O(\\log s)',
    'Σ⁻(x, y) = Σ⁺(y, x)': '\\Sigma^{-}(x, y) = \\Sigma^{+}(y, x)',
    'Σ⁻_{s,P} ≤ O(log s)': '\\Sigma^{-}_{s,P} \\le O(\\log s)',
    'Σ⁻_{s,P} ≤ −σ_s': '\\Sigma^{-}_{s,P} \\le -\\sigma_s',
    'Σ⁻_{s,P}(x, y) ≤ O(log s)': '\\Sigma^{-}_{s,P}(x, y) \\le O(\\log s)',
    'ω': '\\omega',
    'Ω(1 / (n 2^k)) = Ω(1 / (n^{c+1} |f^{−1}(y)|))': '\\Omega(1 / (n 2^k)) = \\Omega(1 / (n^{c+1} |f^{-1}(y)|))',
    'Ω(1 / (q n^{c+1}))': '\\Omega(1 / (q n^{c+1}))',
    '…': '\\dots',
    'ℓ ≤ n': '\\ell \\le n',
    '⇒': '\\Rightarrow',
    '−O(log n)': '-O(\\log n)',
    '⊥': '\\bot',
    '⟨e^{−ω}⟩': '\\langle e^{-\\omega}\\rangle',
    '⟨ω⟩ ≥ 0': '\\langle\\omega\\rangle \\ge 0',
    # --- added 15 Sep 2026 for thread B21 (Definition 9, Proposition 3, Sections 7.5-7.6) ---
    'H_pK': '\\mathrm{H}_{\\mathrm{pK}}',
    'DistNP ⊆ AvgBPP ⇒ H_pK': '\\mathrm{DistNP} \\subseteq \\mathrm{AvgBPP} \\Rightarrow \\mathrm{H}_{\\mathrm{pK}}',
    'H_pK ⇒ BEM_skew': '\\mathrm{H}_{\\mathrm{pK}} \\Rightarrow \\mathrm{BEM}_{\\mathrm{skew}}',
    'L': 'L',
    '(L, D)': '(L, D)',
    '(L, D) ∈ AvgBPP': '(L, D) \\in \\mathrm{AvgBPP}',
    'L ∈ NP': 'L \\in \\mathrm{NP}',
    "(u, v, w, w')": "(u, v, w, w')",
    'K(x)': 'K(x)',
    'x ∼ D': 'x \\sim D',
    # --- added 15 Sep 2026 for thread B23 and Proposition 8 / Corollary 1 (E60) ---
    'BPP': '\\mathrm{BPP}',
    'R': 'R',
    'R(y)': 'R(y)',
    'D(· | y)': 'D(\\cdot \\mid y)',
    'y ∈ supp D_2': 'y \\in \\operatorname{supp} D_2',
    'σ^rev_D(x, y) ≤ O(log n)': '\\sigma^{\\mathrm{rev}}_D(x, y) \\le O(\\log n)',
    'E_D[σ^rev_D] ≤ O(log n)': '\\mathrm{E}_D[\\sigma^{\\mathrm{rev}}_D] \\le O(\\log n)',
    'E_D[2^{σ^rev_D}] ≤ n^{O(1)}': '\\mathrm{E}_D[2^{\\sigma^{\\mathrm{rev}}_D}] \\le n^{O(1)}',
    'E_D[2^{σ^rev_D}] ≤ 2^{O(log n)} = n^{O(1)}': '\\mathrm{E}_D[2^{\\sigma^{\\mathrm{rev}}_D}] \\le 2^{O(\\log n)} = n^{O(1)}',
    'T_R(n)': 'T_R(n)',
    '1/poly': '1/\\mathrm{poly}',
    '1/p(n)': '1/p(n)',
    'C log n': 'C \\log n',
    # --- added 15 Sep 2026 for Lemma 6, the coding theorem with an auxiliary input (E63) ---
    'y ∈ {0,1}^n': 'y \\in \\{0,1\\}^n',
    't = t(n) ≥ n': 't = t(n) \\ge n',
    'S(x | y)': 'S(x \\mid y)',
    'S(y)': 'S(y)',
    'x ∈ supp S(· | y)': 'x \\in \\operatorname{supp} S(\\cdot \\mid y)',
    '2^k': '2^k',
    'δ := S(x | y) > 0': '\\delta := S(x \\mid y) > 0',
    'T := t(n)': 'T := t(n)',
    'M_y : {0,1}^T → {0,1}^n': 'M_y : \\{0,1\\}^T \\to \\{0,1\\}^n',
    'M_y(z) := S(y; z)': 'M_y(z) := S(y; z)',
    'T': 'T',
    'M_y': 'M_y',
    'Pr_z[M_y(z) = x] ≥ δ': '\\Pr_z[M_y(z) = x] \\ge \\delta',
    'H = {H_w : {0,1}^ℓ → {0,1}^T}_{w ∈ {0,1}^k}': 'H = \\{H_w : \\{0,1\\}^\\ell \\to \\{0,1\\}^T\\}_{w \\in \\{0,1\\}^k}',
    'k = poly(T)': 'k = \\mathrm{poly}(T)',
    'ℓ = log 1/δ + O(1)': '\\ell = \\log 1/\\delta + O(1)',
    'Pr_z[M(z) = x] ≥ δ': '\\Pr_z[M(z) = x] \\ge \\delta',
    'w': 'w',
    'v': 'v',
    'v ∈ {0,1}^ℓ': 'v \\in \\{0,1\\}^\\ell',
    'M(H_w(v)) = x': 'M(H_w(v)) = x',
    'H_w(v)': 'H_w(v)',
    'poly(T)': '\\mathrm{poly}(T)',
    'M(H(v)) = x': 'M(H(v)) = x',
    'H': 'H',
    'AC^0': '\\mathrm{AC}^0',
    '2^{poly(T)}': '2^{\\mathrm{poly}(T)}',
    'H_w': 'H_w',
    'M = M_y': 'M = M_y',
    'H(v)': 'H(v)',
    'w ∈ {0,1}^k': 'w \\in \\{0,1\\}^k',
    'S(y; H_w(v)) = x': 'S(y; H_w(v)) = x',
    '|α| = log 1/δ + O(log T)': '|\\alpha| = \\log 1/\\delta + O(\\log T)',
    'O(·)': 'O(\\cdot)',
    'pK^{p(T)}(x | y) ≤ |α| = log 1/S(x | y) + O(log T)': '\\mathrm{pK}^{p(T)}(x \\mid y) \\le |\\alpha| = \\log 1/S(x \\mid y) + O(\\log T)',
    # --- added 15 Sep 2026 for B38 (E68): B31.6 in §7.3, the restated question of §7.5, Proposition 8 in §7.6, row 17 ---
    'pK^t(y)': '\\mathrm{pK}^t(y)',
    '2n + O(1)': '2n + O(1)',
    'Σ⁺_{s,P}': '\\Sigma^{+}_{s,P}',
    'i(P(s)) ≤ (1/c) log log P(s) = O(log log n)': 'i(P(s)) \\le (1/c) \\log \\log P(s) = O(\\log \\log n)',
    'M_{P(s)}': 'M_{P(s)}',
    'M_s': 'M_s',
    'E_{D_m}[2^{Σ⁺_{s,P}}] ≥ 2^{n − o(n)}': '\\mathrm{E}_{D_m}[2^{\\Sigma^{+}_{s,P}}] \\ge 2^{n - o(n)}',
    's ≥ t_D': 's \\ge t_D',
    'P_j(s) := s^j': 'P_j(s) := s^j',
    'j': 'j',
    'n − O(log n)': 'n - O(\\log n)',
    'ℓ = n/O(log t)': '\\ell = n/O(\\log t)',
    'Θ(n)': '\\Theta(n)',
    '2^{O(n/log n)}': '2^{O(n/\\log n)}',
    'O(n/log n)': 'O(n/\\log n)',
    '2^{o(n/log n)}': '2^{o(n/\\log n)}',
    '2t': '2t',
    'A(x, y, 1^t)': 'A(x, y, 1^t)',
    't ≥ p(|x| + |y|)': 't \\ge p(|x| + |y|)',
    'K^t(x | y) ≤ |x| − O(log |x|)': 'K^t(x \\mid y) \\le |x| - O(\\log |x|)',
    'c_0, c_1': 'c_0, c_1',
    't ≥ (2n)^{c_0}': 't \\ge (2n)^{c_0}',
    'p(t) := t^{c_1}': 'p(t) := t^{c_1}',
    'p_0(n) := (2n)^{c_0}': 'p_0(n) := (2n)^{c_0}',
    'log p(t)': '\\log p(t)',
    '(i) ⇒ BEM_skew': '\\text{(i)} \\Rightarrow \\mathrm{BEM}_{\\mathrm{skew}}',
    'n − δ(n, t)': 'n - \\delta(n, t)',
    'ℓ': '\\ell',
    'x_1, …, x_ℓ': 'x_1, \\ldots, x_\\ell',
    'N := Σ_i |x_i|': 'N := \\sum_i |x_i|',
    't ≥ (N + |y|)^{c_0}': 't \\ge (N + |y|)^{c_0}',
    'ℓ = 2': '\\ell = 2',
    'x_1 = x': 'x_1 = x',
    'x_2 = y': 'x_2 = y',
    'N = 2n': 'N = 2n',
    'δ(n, t) = O(log n)': '\\delta(n, t) = O(\\log n)',
    '2 · O(log 2n) + O(log 4n) = O(log n)': '2 \\cdot O(\\log 2n) + O(\\log 4n) = O(\\log n)',
    'O(log s)': 'O(\\log s)',
    'n − 10': 'n - 10',
    "(w, w')": "(w, w')",
    'K_U(x)': 'K_U(x)',
    '2^{n/2}': '2^{n/2}',
    '2^{n − o(n)}': '2^{n - o(n)}',
    # --- added 15 Sep 2026 for Definition 10, Theorem 4 and Corollary 2 in Section 8.2 (E70, thread B40) ---
    '⇐': '\\Leftarrow',
    't_S': 't_S',
    't_S(n) ≥ n': 't_S(n) \\ge n',
    'n^c': 'n^c',
    'Y': 'Y',
    'Y ⊆ supp D_2': 'Y \\subseteq \\operatorname{supp} D_2',
    'USamp_t(y) := USamp(1^n, 1^t, y)': '\\mathrm{USamp}_t(y) := \\mathrm{USamp}(1^n, 1^t, y)',
    '[O(n)]': '[O(n)]',
    'r ∈ {0,1}^t': 'r \\in \\{0,1\\}^t',
    'd ∈ {0,1}^k': 'd \\in \\{0,1\\}^k',
    'USamp_t(x | y)': '\\mathrm{USamp}_t(x \\mid y)',
    'Pr[USamp_t(y) = x]': '\\Pr[\\mathrm{USamp}_t(y) = x]',
    'c ≥ 0': 'c \\ge 0',
    'G ⊆ supp D_2': 'G \\subseteq \\operatorname{supp} D_2',
    'D_2(G) ≥ 1 − 1/n': 'D_2(G) \\ge 1 - 1/n',
    'y ∈ G': 'y \\in G',
    'σ^rev_D(x, y) ≤ c log n': '\\sigma^{\\mathrm{rev}}_D(x, y) \\le c \\log n',
    '1/n': '1/n',
    'b := 3a(1 + d)/2': 'b := 3a(1 + d)/2',
    'c′': "c'",
    'c″': "c''",
    'y ∈ Y': 'y \\in Y',
    'USamp_{p(t_S)}': '\\mathrm{USamp}_{p(t_S)}',
    'n^{c″}': "n^{c''}",
    'Y = supp D_2': 'Y = \\operatorname{supp} D_2',
    'pK^t(y) ≥ log 1/D_2(y) − log n − log(3(n + d)/2)': '\\mathrm{pK}^t(y) \\ge \\log 1/D_2(y) - \\log n - \\log(3(n + d)/2)',
    'α = log n': '\\alpha = \\log n',
    'pK^t(x | y) = σ^rev_D(x, y) − log D(x, y) − pK^t(y)': '\\mathrm{pK}^t(x \\mid y) = \\sigma^{\\mathrm{rev}}_D(x, y) - \\log D(x, y) - \\mathrm{pK}^t(y)',
    'k := pK^t(x | y)': 'k := \\mathrm{pK}^t(x \\mid y)',
    'USamp_t(x | y) ≥ 1/(a n 2^k) ≥ D(x | y) · n^{−(c+1)} · 2/(3(n + d)) · 1/(a n) ≥ D(x | y) / (b n^{c+3})':
        '\\mathrm{USamp}_t(x \\mid y) \\ge 1/(a n 2^k) \\ge D(x \\mid y) \\cdot n^{-(c+1)} \\cdot 2/(3(n + d)) \\cdot 1/(a n) \\ge D(x \\mid y) / (b\\, n^{c+3})',
    'n + d ≤ (1 + d) n': 'n + d \\le (1 + d) n',
    'S(x | y) ≥ D(x | y)/n^c > 0': 'S(x \\mid y) \\ge D(x \\mid y)/n^c > 0',
    'pK^{p(t_S)}(x | y) ≤ log 1/S(x | y) + O(log t_S) ≤ log 1/D(x | y) + c log n + O(log n)':
        '\\mathrm{pK}^{p(t_S)}(x \\mid y) \\le \\log 1/S(x \\mid y) + O(\\log t_S) \\le \\log 1/D(x \\mid y) + c \\log n + O(\\log n)',
    'σ^rev_D(x, y) ≤ (c + c_D + O(1)) log n =: c′ log n': "\\sigma^{\\mathrm{rev}}_D(x, y) \\le (c + c_D + O(1)) \\log n =: c' \\log n",
    'pK^{p(t_S)}(x | y)': '\\mathrm{pK}^{p(t_S)}(x \\mid y)',
    'p(t_S)': 'p(t_S)',
    'USamp_{p(t_S)}(x | y) ≥ 1/(a n 2^{pK^{p(t_S)}(x | y)}) ≥ D(x | y) / n^{c″}':
        "\\mathrm{USamp}_{p(t_S)}(x \\mid y) \\ge 1/(a n 2^{\\mathrm{pK}^{p(t_S)}(x \\mid y)}) \\ge D(x \\mid y) / n^{c''}",
    'σ^rev_D ≤ c log n': '\\sigma^{\\mathrm{rev}}_D \\le c \\log n',
    '1/q(n) + 1/n': '1/q(n) + 1/n',
    '1/q + 1/n': '1/q + 1/n',
    'D_2(Y) ≥ 1 − 1/q(n)': 'D_2(Y) \\ge 1 - 1/q(n)',
    'σ^rev_D ≤ c′ log n': "\\sigma^{\\mathrm{rev}}_D \\le c' \\log n",
    'Y_n': 'Y_n',
    'D_2(Y_n) ≥ 1 − 1/n': 'D_2(Y_n) \\ge 1 - 1/n',
    'y ∈ Y_n': 'y \\in Y_n',
    'σ^rev_D ≤ 2(n + d)': '\\sigma^{\\mathrm{rev}}_D \\le 2(n + d)',
    'log D(x, y) ≤ 0': '\\log D(x, y) \\le 0',
    'E_D[σ^rev_D] ≤ c′ log n + 2(n + d)/n ≤ (c′ + 1) log n': "\\mathrm{E}_D[\\sigma^{\\mathrm{rev}}_D] \\le c' \\log n + 2(n + d)/n \\le (c' + 1) \\log n",
    't = p′(n)': "t = p'(n)",
    'p = p′': "p = p'",
    'C = c′ + 1': "C = c' + 1",
    # --- added 18 Sep 2026 for the pass-22 referee corrections (E72, thread B41) ---
    'y*': 'y^*',                                                    # Theorem 0: prefix form conditions on y*
    'pK^t(x) ≥ 1': '\\mathrm{pK}^t(x) \\ge 1',                     # Three conventions (i)-(iii)
    'pK^t(x | y) ≥ 1': '\\mathrm{pK}^t(x \\mid y) \\ge 1',
    '⟨x, y⟩': '\\langle x, y\\rangle',
    't(2n)': 't(2n)',
    'M(w, y)': 'M(w, y)',
    'K^t(x | y, r) ≤ s': 'K^t(x \\mid y, r) \\le s',
    'n ≥ 2': 'n \\ge 2',                                            # Theorem 1
    '± O(log n)': '\\pm O(\\log n)',                                # Theorem 0, Proved; known
    'P(s) := p(c′s)': "P(s) := p(c's)",                             # Proposition 2(a)
    'c′ ≥ c': "c' \\ge c",
    '2^{Ω(n/log n)}': '2^{\\Omega(n/\\log n)}',                     # Section 7.5, Obstruction A
    'O(log n)/ℓ': 'O(\\log n)/\\ell',
    '9/10': '9/10',                                                 # Section 7.5, GKLO22 Lemma 26(2)
    'D(x | y)/K': 'D(x \\mid y)/K',                                 # Proposition 9 and its proof
    'p_R': 'p_R',
    't ≥ t_D + p_R(n)': 't \\ge t_D + p_R(n)',
    'pK^{p(T_R(n))}(x | y) ≤ log 1/D(x | y) + log K + O(log n)': '\\mathrm{pK}^{p(T_R(n))}(x \\mid y) \\le \\log 1/D(x \\mid y) + \\log K + O(\\log n)',
    't ≥ p_R(n) := p(T_R(n))': 't \\ge p_R(n) := p(T_R(n))',
    'x ↦ f(x)': 'x \\mapsto f(x)',                                  # the Markov-chain paragraph
    't ≥ t_D + p(t_S)': 't \\ge t_D + p(t_S)',                      # Theorem 4 (twice)
    't ≥ p′(n) := t_D + p(t_S(n))': "t \\ge p'(n) := t_D + p(t_S(n))",   # Corollary 2, proof
    # --- added 18 Sep 2026 for B42 (the How-to-read symbol table and the black-hole bullet) ---
    '2^{+σ_t}': '2^{+\\sigma_t}',
    '2^{−σ_t}': '2^{-\\sigma_t}',
    'Σ⁻': '\\Sigma^{-}',
    'SZK ⊆ BQP': '\\mathrm{SZK} \\subseteq \\mathrm{BQP}',
    'P = PSPACE': '\\mathrm{P} = \\mathrm{PSPACE}',
    # --- added 19 Sep 2026 for B43 (E73-E76): Proposition 10, the Composition block (Lemma 12,
    #     Proposition 11), Propositions 12-13, Remarks 5-6, the axiom paragraph of Section 8.4 ---
    '|S| ≤ n^{O(1)}': '|S| \\le n^{O(1)}',
    'π_0': '\\pi_0',
    'L ≤ n^{O(1)}': 'L \\le n^{O(1)}',
    '(s_0, …, s_L)': '(s_0, \\dots, s_L)',
    's_L': 's_L',
    'D_f(· | y)': 'D_f(\\cdot \\mid y)',
    'f^{−1}(y)': 'f^{-1}(y)',
    '1/K': '1/K',
    'D(x | y) = Π_{i<L} P̃_i(s_i | s_{i+1})': 'D(x \\mid y) = \\prod_{i<L} \\tilde{P}_i(s_i \\mid s_{i+1})',
    'P̃_i(s | s′) := π_i(s) P(s′ | s) / π_{i+1}(s′)': "\\tilde{P}_i(s \\mid s') := \\pi_i(s)\\, P(s' \\mid s) / \\pi_{i+1}(s')",
    'π_i := π_0 P^i': '\\pi_i := \\pi_0 P^i',
    'π_i': '\\pi_i',
    'P̃_i(s_i | s_{i+1})': '\\tilde{P}_i(s_i \\mid s_{i+1})',
    '2^{−B}': '2^{-B}',
    'B := (L + 2) B_0': 'B := (L + 2) B_0',
    'B_0': 'B_0',
    '(L + 2) B_0': '(L + 2) B_0',
    '2^{−B_0 L}': '2^{-B_0 L}',
    'π_L': '\\pi_L',
    's_L = y': 's_L = y',
    's_i': 's_i',
    'P̃_i(· | s_{i+1})': '\\tilde{P}_i(\\cdot \\mid s_{i+1})',
    '2^{−b}': '2^{-b}',
    'b := B + ⌈log L⌉ + 2': 'b := B + \\lceil \\log L \\rceil + 2',
    '(1 − 2^{−b+B}) = (1 − 1/(4L))': '(1 - 2^{-b+B}) = (1 - 1/(4L))',
    'D(x | y)(1 − 1/(4L))^L ≥ (3/4) D(x | y)': 'D(x \\mid y)(1 - 1/(4L))^L \\ge (3/4)\\, D(x \\mid y)',
    '4/3 ≤ 2': '4/3 \\le 2',
    'K = 2': 'K = 2',
    'x ~ X': 'x \\sim X',
    'y := F(x)': 'y := F(x)',
    'z := G(y)': 'z := G(y)',
    '(X, Y, Z)': '(X, Y, Z)',
    'D_F': 'D_F',
    'D_G': 'D_G',
    'D_{G∘F}': 'D_{G \\circ F}',
    '(y, z)': '(y, z)',
    '(x, z)': '(x, z)',
    'x, y, z ∈ {0,1}^n': 'x, y, z \\in \\{0,1\\}^n',
    't ≥ max(t_{D_F}, t_{D_G}, n)': 't \\ge \\max(t_{D_F}, t_{D_G}, n)',
    'H(Y | X, Z) = 0': 'H(Y \\mid X, Z) = 0',
    'H(Y | X, Z)': 'H(Y \\mid X, Z)',
    'S_F': 'S_F',
    'S_G': 'S_G',
    'D_F(· | y)': 'D_F(\\cdot \\mid y)',
    'D_G(· | z)': 'D_G(\\cdot \\mid z)',
    'n^a': 'n^a',
    'n^b': 'n^b',
    'n^{a+b}': 'n^{a+b}',
    'y ∈ supp Y': 'y \\in \\operatorname{supp} Y',
    'z ∈ supp Z': 'z \\in \\operatorname{supp} Z',
    'supp Z': '\\operatorname{supp} Z',
    'S_F ∘ S_G': 'S_F \\circ S_G',
    'D_{G∘F}(· | z)': 'D_{G \\circ F}(\\cdot \\mid z)',
    'σ^rev_{D_{G∘F}} ≤ O(log n)': '\\sigma^{\\mathrm{rev}}_{D_{G \\circ F}} \\le O(\\log n)',
    't ≥ t_{D_G} + p(t_{S_F} + t_{S_G})': 't \\ge t_{D_G} + p(t_{S_F} + t_{S_G})',
    'D′': "D'",
    'D × D′': "D \\times D'",
    '(⟨x, x′⟩, ⟨y, y′⟩)': "(\\langle x, x' \\rangle, \\langle y, y' \\rangle)",
    '(x′, y′) ~ D′': "(x', y') \\sim D'",
    '(x′, y′) ∈ supp D′': "(x', y') \\in \\operatorname{supp} D'",
    'σ_{GF}': '\\sigma_{GF}',
    'σ_F': '\\sigma_F',
    'σ_G': '\\sigma_G',
    'Δ := σ_{GF} − σ_F − σ_G': '\\Delta := \\sigma_{GF} - \\sigma_F - \\sigma_G',
    '−H(X, Z) + H(X, Y) + H(Y, Z) = H(Y) + H(Y | X, Z)': '-H(X, Z) + H(X, Y) + H(Y, Z) = H(Y) + H(Y \\mid X, Z)',
    'H(X, Y) = H(X, Y, Z) − H(Z | Y)': 'H(X, Y) = H(X, Y, Z) - H(Z \\mid Y)',
    'H(Y, Z) = H(Y) + H(Z | Y)': 'H(Y, Z) = H(Y) + H(Z \\mid Y)',
    'W := log 1/D_2(y) − pK^t(y)': 'W := \\log 1/D_2(y) - \\mathrm{pK}^t(y)',
    'ℓ := log(3(n + d)/2)': '\\ell := \\log(3(n + d)/2)',
    'Pr[W > α + ℓ] ≤ 2^{−α}': '\\Pr[W > \\alpha + \\ell] \\le 2^{-\\alpha}',
    'E[W] ≤ E[W⁺] = ∫_0^∞ Pr[W > s] ds ≤ ℓ + 1/ln 2':
        '\\mathrm{E}[W] \\le \\mathrm{E}[W^{+}] = \\int_0^\\infty \\Pr[W > s]\\, ds \\le \\ell + 1/\\ln 2',
    'E[pK^t(y)] ≥ H(Y) − ℓ − 2': '\\mathrm{E}[\\mathrm{pK}^t(y)] \\ge H(Y) - \\ell - 2',
    'E[Δ] ≤ H(Y) + H(Y | X, Z) + O(log t) − H(Y) + ℓ + 2 = H(Y | X, Z) + O(log t)':
        '\\mathrm{E}[\\Delta] \\le H(Y) + H(Y \\mid X, Z) + O(\\log t) - H(Y) + \\ell + 2 = H(Y \\mid X, Z) + O(\\log t)',
    'D_{G∘F}(x | z) = Σ_y D_G(y | z) D_F(x | y) ≤ n^{a+b} Σ_y S_G(y | z) S_F(x | y) = n^{a+b} · Pr[S_F(S_G(z)) = x]':
        'D_{G \\circ F}(x \\mid z) = \\sum_y D_G(y \\mid z)\\, D_F(x \\mid y) \\le n^{a+b} \\sum_y S_G(y \\mid z)\\, S_F(x \\mid y) '
        '= n^{a+b} \\cdot \\Pr[S_F(S_G(z)) = x]',
    'log (D × D′)(⟨x, x′⟩, ⟨y, y′⟩) = log D(x, y) + log D′(x′, y′)':
        "\\log (D \\times D')(\\langle x, x' \\rangle, \\langle y, y' \\rangle) = \\log D(x, y) + \\log D'(x', y')",
    'pK^t(y′ | y) ≤ pK^t(y′) + O(1)': "\\mathrm{pK}^t(y' \\mid y) \\le \\mathrm{pK}^t(y') + O(1)",
    'pK^{ct}(⟨y, y′⟩) ≤ pK^t(y) + pK^t(y′) + O(log t)':
        "\\mathrm{pK}^{ct}(\\langle y, y' \\rangle) \\le \\mathrm{pK}^t(y) + \\mathrm{pK}^t(y') + O(\\log t)",
    'y′': "y'",
    'pK^{ct}(⟨x, x′⟩ | ⟨y, y′⟩) ≤ pK^t(x | y) + pK^t(x′ | y′) + O(log t)':
        "\\mathrm{pK}^{ct}(\\langle x, x' \\rangle \\mid \\langle y, y' \\rangle) \\le \\mathrm{pK}^t(x \\mid y) + \\mathrm{pK}^t(x' \\mid y') + O(\\log t)",
    'E[σ_{D×D′}] ≥ E[σ_D] + E[σ_{D′}] − O(log n)':
        "\\mathrm{E}[\\sigma_{D \\times D'}] \\ge \\mathrm{E}[\\sigma_D] + \\mathrm{E}[\\sigma_{D'}] - O(\\log n)",
    'E[pK^t(⟨x, x′⟩ | ⟨y, y′⟩)] ≥ E[pK^t(x | y)] + E[pK^t(x′ | y′)] − O(log n)':
        "\\mathrm{E}[\\mathrm{pK}^t(\\langle x, x' \\rangle \\mid \\langle y, y' \\rangle)] \\ge \\mathrm{E}[\\mathrm{pK}^t(x \\mid y)] "
        "+ \\mathrm{E}[\\mathrm{pK}^t(x' \\mid y')] - O(\\log n)",
    'H(X | Y)': 'H(X \\mid Y)',
    '[−log(3(n + d)/2) − 2, c_D log n]': '[-\\log(3(n + d)/2) - 2,\\; c_D \\log n]',
    '−log(3(n + d)/2) − 2': '-\\log(3(n + d)/2) - 2',
    'E[σ^rev_D] = −H(X, Y) + E[pK^t(y)] + E[pK^t(x | y)] = (E[pK^t(y)] − H(Y)) + (E[pK^t(x | y)] − H(X | Y))':
        '\\mathrm{E}[\\sigma^{\\mathrm{rev}}_D] = -H(X, Y) + \\mathrm{E}[\\mathrm{pK}^t(y)] + \\mathrm{E}[\\mathrm{pK}^t(x \\mid y)] '
        '= (\\mathrm{E}[\\mathrm{pK}^t(y)] - H(Y)) + (\\mathrm{E}[\\mathrm{pK}^t(x \\mid y)] - H(X \\mid Y))',
    'Pr_x[A(f(x)) ∈ f^{−1}(f(x))] ≤ ε(n)': '\\Pr_x[A(f(x)) \\in f^{-1}(f(x))] \\le \\varepsilon(n)',
    'c_U (t + n) ≤ T(n)': 'c_U (t + n) \\le T(n)',
    'c_U': 'c_U',
    'H(X | f(X)) = 0': 'H(X \\mid f(X)) = 0',
    'E_D[σ^rev_D at time p(T)] ≤ E_x[ log 1/Pr[A(f(x)) = x] ] + O(log T)':
        '\\mathrm{E}_D[\\sigma^{\\mathrm{rev}}_D \\text{ at time } p(T)] \\le \\allowbreak \\mathrm{E}_x[\\, \\log 1/\\Pr[A(f(x)) = x] \\,] + O(\\log T)',
    't ≥ max(t_D, p(T))': 't \\ge \\max(t_D, p(T))',
    'E_x[ log 1/Pr[A(f(x)) = x] ] − H(X | f(X)) + O(log T) + c_D log n':
        '\\mathrm{E}_x[\\, \\log 1/\\Pr[A(f(x)) = x] \\,] - H(X \\mid f(X)) + O(\\log T) + c_D \\log n',
    'K(x) := pK^t(x | f(x))': 'K(x) := \\mathrm{pK}^t(x \\mid f(x))',
    'USamp_t(f(x))': '\\mathrm{USamp}_t(f(x))',
    'USamp_t': '\\mathrm{USamp}_t',
    '1/(a n 2^{K(x)})': '1/(a n\\, 2^{K(x)})',
    'c_U (t + n) ≤ T': 'c_U (t + n) \\le T',
    'E_x[2^{−K(x)}]/(a n) ≥ 2^{−E[K]}/(a n)': '\\mathrm{E}_x[2^{-K(x)}]/(a n) \\ge 2^{-\\mathrm{E}[K]}/(a n)',
    'ε ≥ 2^{−E[K]}/(a n)': '\\varepsilon \\ge 2^{-\\mathrm{E}[K]}/(a n)',
    'E[K] ≥ log 1/ε − log(a n)': '\\mathrm{E}[K] \\ge \\log 1/\\varepsilon - \\log(a n)',
    'H(X, Y) = H(X) = n': 'H(X, Y) = H(X) = n',
    'E[σ^rev_D] ≥ E[K] − H(X | f(X)) − log(3(n + d)/2) − 2':
        '\\mathrm{E}[\\sigma^{\\mathrm{rev}}_D] \\ge \\mathrm{E}[K] - H(X \\mid f(X)) - \\log(3(n + d)/2) - 2',
    'log 1/D(x, f(x)) = n': '\\log 1/D(x, f(x)) = n',
    'σ(x, f(x)) = pK^t(x | f(x)) + pK^t(f(x)) − n ≤ pK^t(x | f(x)) + d':
        '\\sigma(x, f(x)) = \\mathrm{pK}^t(x \\mid f(x)) + \\mathrm{pK}^t(f(x)) - n \\le \\mathrm{pK}^t(x \\mid f(x)) + d',
    'pK^{p(T)}(x | f(x)) ≤ log 1/Pr[A(f(x)) = x] + O(log T)':
        '\\mathrm{pK}^{p(T)}(x \\mid f(x)) \\le \\log 1/\\Pr[A(f(x)) = x] + O(\\log T)',
    '−log |f^{−1}(f(x))|': '-\\log |f^{-1}(f(x))|',
    'H(X | f(X))': 'H(X \\mid f(X))',
    'φ': '\\varphi',
    'ψ': '\\psi',
    'D^{φ,ψ}': 'D^{\\varphi,\\psi}',
    '(φ(x), ψ(y))': '(\\varphi(x), \\psi(y))',
    'D^{φ,ψ}(φ(x), ψ(y)) = D(x, y)': 'D^{\\varphi,\\psi}(\\varphi(x), \\psi(y)) = D(x, y)',
    'ψ(y)': '\\psi(y)',
    'φ(x)': '\\varphi(x)',
    'pK^{t+T+O(n)}(ψ(y)) ≤ pK^t(y) + O(1)': '\\mathrm{pK}^{t+T+O(n)}(\\psi(y)) \\le \\mathrm{pK}^t(y) + O(1)',
    'ψ^{−1}': '\\psi^{-1}',
    'φ^{−1}': '\\varphi^{-1}',
    'pK^{ct+2T+O(n)}(φ(x) | ψ(y)) ≤ pK^t(x | y) + O(1)':
        '\\mathrm{pK}^{ct+2T+O(n)}(\\varphi(x) \\mid \\psi(y)) \\le \\mathrm{pK}^t(x \\mid y) + O(1)',
    't_S(n)': 't_S(n)',
    'S(x | y) > 0': 'S(x \\mid y) > 0',
    'pK^{p(t_S)}(x | y) ≤ log 1/S(x | y) + O(log t_S)':
        '\\mathrm{pK}^{p(t_S)}(x \\mid y) \\le \\log 1/S(x \\mid y) + O(\\log t_S)',
    'USamp_{p(t_S)}(x | y) ≥ 2^{−pK^{p(t_S)}(x | y)}/(a n)':
        '\\mathrm{USamp}_{p(t_S)}(x \\mid y) \\ge 2^{-\\mathrm{pK}^{p(t_S)}(x \\mid y)}/(a n)',
    'E_D[σ^rev_D] ≥ −O(log n)': '\\mathrm{E}_D[\\sigma^{\\mathrm{rev}}_D] \\ge -O(\\log n)',
}

# final LaTeX, prose allowed: variables that sit inside a phrase, class names in prose
RAW = {
    'io-OWF exist ⇔ some samplable D has': r'io-OWF exist $\Leftrightarrow$ some samplable $D$ has',
    'A answers NP questions about F': '$A$ answers $\\mathrm{NP}$ questions about $F$',
    'A-answer': '$A$-answer',
    'A-queries': '$A$-queries',
    'F(z, x, ℓ) for z, x ∈ {0,1}^n and ℓ ∈ [n]': '$F(z, x, \\ell)$ for $z, x \\in \\{0,1\\}^n$ and $\\ell \\in [n]$',
    'F-query': '$F$-query',
    'H-theorem': '$H$-theorem',
    'k-bit': '$k$-bit',
    'length ≤ log N − log t − 6': 'length $\\le \\log N - \\log t - 6$',
    'length ≤ n − 6': 'length $\\le n - 6$',
    'length ≤ t': 'length $\\le t$',
    'levels ≤ i(t)': 'levels $\\le i(t)$',
    'levels ≤ i_T := (1/c) log log T': 'levels $\\le i_T := (1/c) \\log \\log T$',
    'levels ≤ i_T at lengths ≤ T': 'levels $\\le i_T$ at lengths $\\le T$',
    'm-bit': '$m$-bit',
    'O(1)-bit, O(n)-time': '$O(1)$-bit, $O(n)$-time',
    'P =? NP': '$\\mathrm{P} =? \\mathrm{NP}$',
    'P is not NP': '$\\mathrm{P}$ is not $\\mathrm{NP}$',
    'P versus NP': '$\\mathrm{P}$ versus $\\mathrm{NP}$',
    'P vs NP': '$\\mathrm{P}$ vs $\\mathrm{NP}$',
    'BQP-samplable': '$\\mathrm{BQP}$-samplable',
    'pK^t(y) ≤ k means Pr_r[ some program of length ≤ k prints y ] ≥ 2/3': '$\\mathrm{pK}^t(y) \\le k$ means $\\Pr_r[\\, \\text{some program of length} \\le k \\text{ prints } y \\,] \\ge 2/3$',
    'probability ≤ 1/(N − t)': 'probability $\\le 1/(N - t)$',
    'So A lies': 'So $A$ lies',
    'T-DNF': '$T$-DNF',
    'the P of HeurP': 'the $\\mathrm{P}$ of $\\mathrm{HeurP}$',
    'σ-form': '$\\sigma$-form',
    'ω = log(forward / reverse)': '$\\omega = \\log(\\text{forward} / \\text{reverse})$',
    # --- added 18 Sep 2026 (E72, thread B41) ---
    'circuit lower bound for E': 'circuit lower bound for $\\mathrm{E}$',   # Section 7.5, Hirahara's placement
    # --- added 19 Sep 2026 for B43: the inverter A of Proposition 13, the exponent e of Remark 6 and the
    #     bit count b of Proposition 10's proof, none of which can be a bare key ---
    'randomized A running in polynomial time T': 'randomized $A$ running in polynomial time $T$',
    'applied to A gives': 'applied to $A$ gives',
    'a constant e': 'a constant $e$',
    # a bare 'b' would also catch the (b) of "Theorem 3(b)", as 'c' already does with "Proposition 3(c)"
    'with b bits is drawn exactly with b fair coins': 'with $b$ bits is drawn exactly with $b$ fair coins',
}

# looks mathematical, is prose: item labels, identifiers, equation-label references
PROSE = {
    '(E1)',
    '(E2)',
    '(H1)',
    '(H2)',
    '(b)',
    '(c)',
    '(i)',
    '(ii)',
    '(iii)',
    '0704.1569',
    '2023/424',
    '21(3/4):219–253',
    '2308.06927v4',
    '2nd',
    '56(3/4):371–402',
    'Appendix B',
    'E27',
    'GKLO22',
    'LIPIcs 234:16',
    'LIPIcs 234:25',
    'LIPIcs 234:26',
    'Phys. Rev. E',
    'Physica D',
    'Step B',
    'TR21-161',
    'TR22-007',
    'TR25-089',
    'TR26-021',
    '[BCGL92]',
    '[GK22]',
    '[Hir22]',
    '[LM93]',
    '[LW95]',
    '§3b',
    '§IV C–D',
    'B21',            # thread B21 (references, 15 Sep 2026)
    # --- added 15 Sep 2026 for thread B23 (E60) ---
    'B23',            # thread B23
    # --- added 15 Sep 2026 for Lemma 6 (E63) ---
    'v1',             # arXiv version numbers in the reference list
    'v3',
    '2020/423',       # ePrint number, Liu and Pass 2020
    '§V',             # section numbers of Fox, Karamchedu and Mygdalas 2026 and of Kolchinsky and Wolpert 2020
    '§V.A',
    '§V.C',
    # --- added 15 Sep 2026 for B38 (E68) ---
    'B30',            # threads B30, B31, B36, B37 and their statements
    'B31',
    'B36',
    'B37',
    'Obstruction A',  # the two obstructions of §7.5
    'Obstruction B',
    '§II.B',          # Kolchinsky and Wolpert 2020
    'S2',             # entries of the reading ledger of research note B30 §0
    'S3',
    '2211.00747',     # arXiv numbers in the reference list
    '10.1038/s41467-025-62081-6',
    'ar5iv',          # the ar5iv rendering of arXiv papers
    'Theorem B.2',    # Kabanets and Kolokolova 2025, Appendix B
    'Lemma B.1',
    # --- added 15 Sep 2026 for Definition 10 (E70, thread B40) ---
    '[Lev86]',        # Bogdanov and Trevisan 2006 survey: their citation key for Levin 1986
    '§1.1.2',
    'arXiv cs/0606037',
    # --- added 18 Sep 2026 for B42 (E72: the How-to-read section, the black-hole bullet, Aaronson 2016a/b) ---
    '2016a',          # Aaronson 2016a / 2016b, the split reference
    '2016b',
    '[AMPS13]',       # Aaronson 2016b's citation keys, quoted in the reference list
    '[HH13]',
    'B26',            # thread B26 (reference list, Aaronson 2016b)
    # --- added 20 Sep 2026 for B46 (the nine formerly unread works, reference list) ---
    'TR08-005',       # Aaronson and Wigderson 2008, ECCC report number
    '2018/544',       # Ji, Liu and Song 2018, ePrint number
    # --- added 20 Sep 2026 for B48 (Appendix B: the oracle proofs; a bare B would trip the leftover check) ---
    'B.1',            # the headings B.1, B.2 (B.3 dropped in B48b, 20 Sep 2026, when Proposition 4's proof went back to 8.2); the body writes "Appendix B.k", caught by the 'Appendix B' key
    'B.2',
}

# the 32 distinct backtick spans: file names in the reference list, set in typewriter
TT = {
    # 'HANDOFF.md' dropped in B46 (20 Sep 2026): the audit-list references left the paper
    'passes/pass04/liupass2020.md',
    'passes/pass04/wolfram2023.md',
    'passes/pass11/takesue1990_relaxation.pdf',
    'passes/pass16/research/13-shiraishi-takesue-2025-read.md',
    'passes/pass16/research/14-takesue-1989-read.md',
    'passes/pass16/research/16-reversible-computing-audit.md',
    'passes/pass20/research/b24_coding_theorem_input.md',
    'passes/pass20/research/b30_complexity_meters.md',      # E68
    'passes/pass20/research/b31_instance_checkers.md',      # E68
    'passes/pass20/research/b36_worst_case_hub.md',         # E68
    'passes/pass20/wallA_attempt.md',                       # E68
    'passes/pass20/research/mountain2_physics_tests.md',
    'problems/one-way-functions/passes/pass16/sources/',
    'sources/aaronson2003_pnp_independent.pdf',
    'sources/aaronson2005_quant-ph0502072.pdf',
    'sources/aaronson2016_pnp_survey.pdf',
    'sources/aaronson2016_quantum_states_1607.05256.pdf',   # Aaronson 2016b (B42, 18 Sep 2026)
    'sources/aaronson_kardes_hartle2025_suppes_slides.pptx',
    'sources/ben-david_halevi_1992.ps',
    'sources/bennett1973_logical_reversibility.pdf',
    'sources/bennett_gacs_li_vitanyi_zurek1998_information_distance.pdf',
    'sources/birget2007_arxiv0704.1569.pdf',
    'sources/crooks1999_arxiv9901352.pdf',
    'sources/ebtekar_hutter2024_arxiv2308.06927.pdf',
    'sources/fredkin_toffoli1982_conservative_logic.pdf',
    'sources/gklo_ccc2022.pdf',
    'sources/goldreich2019_foundations_of_cryptography.pdf',
    'sources/grunwald_vitanyi2004_arxiv0410002.pdf',
    'sources/hilno_eprint2023-424.pdf',
    'sources/hirahara_ccc2022_lipics234-26.pdf',
    'sources/hmo_eccc_tr26-021.pdf',
    'sources/hn_ccc2022_lipics234-25.pdf',
    'sources/hn_eccc_tr21-161.pdf',
    'sources/jarzynski2006_arxiv0603185.pdf',
    'sources/kashefi_kerenidis2007_arxiv0511266.pdf',      # B43 (19 Sep 2026)
    'sources/kk_eccc_tr25-089.pdf',
    'sources/kolchinsky_wolpert2020_arxiv1912.04685.pdf',
    'sources/landauer1961_irreversibility.pdf',
    'sources/lu_oliveira_zimand_2022_arxiv2204.08312.pdf',
    'sources/',
    'sources/shiraishi_takesue_2025_arxiv2408.06691.pdf',
    'sources/takesue1989_ergodic_I.pdf',
    # B46 (20 Sep 2026): the nine formerly unread works and their secondary sources
    'sources/aaronson_wigderson2008_eccc_tr08-005.pdf',
    'sources/bogdanov_trevisan2006_wc2ac_sicomp.pdf',
    'sources/brown_myrvold_uffink2009_arxiv0809.1304.pdf',
    'sources/feigenbaum_fortnow1993_rsr.pdf',
    'sources/fortnow1994_relativization_beatcs.pdf',
    'sources/ji_liu_song2018_eprint544.pdf',
    'sources/razborov_rudich1997_natural.pdf',
    'sources/uffink_sep_boltzmann.txt',
}

# the 52 displayed formulas, keyed by their exact source text (lines stripped and joined)
DISPLAY = {
# --- How to read this paper (added 18 Sep 2026, B42) ---
'NP ⊆ BPP ⇒ BEM ⇒ no io-OWF (same-time defect; Theorem 3)\nDistNP ⊆ AvgBPP ⇒ H_pK ⇒ BEM_skew ⇒ no io-OWF (time-skewed defect; Propositions 7 and 8)\n(i) ⇒ BEM_skew (a second top; Proposition 13)\nopen: does no io-OWF force BEM? barriers on record: Propositions 9 and 10':
r"""\[
\begin{array}{@{}l@{\quad}>{\raggedright\arraybackslash}p{0.35\textwidth}@{}}
\mathrm{NP} \subseteq \mathrm{BPP} \;\Rightarrow\; \mathrm{BEM} \;\Rightarrow\; \text{no io-OWF} & (same-time defect; Theorem 3) \\
\mathrm{DistNP} \subseteq \mathrm{AvgBPP} \;\Rightarrow\; \mathrm{H}_{\mathrm{pK}} \;\Rightarrow\; \mathrm{BEM}_{\mathrm{skew}} \;\Rightarrow\; \text{no io-OWF} & (time-skewed defect; Propositions 7 and 8) \\
\text{(i)} \;\Rightarrow\; \mathrm{BEM}_{\mathrm{skew}} & (a second top; Proposition 13) \\[2pt]
\text{open: does no io-OWF force BEM?} & barriers on record: Propositions 9 and 10
\end{array}
\]""",
# --- section 1 ---
'some polynomial-time samplable process has mean production ≥ ω(log n) i.o. ⇔ one-way functions exist ⇒ P ≠ NP.':
r"""\[
\begin{aligned}
&\text{some polynomial-time samplable process has mean production} \ge \omega(\log n) \text{ i.o.} \\
&\qquad\Leftrightarrow\;\; \text{one-way functions exist} \;\;\Rightarrow\;\; \mathrm{P} \ne \mathrm{NP}.
\end{aligned}
\]""",
# --- section 2 ---
'pK^t(x) = min{ k : Pr_{r ~ {0,1}^{t(n)}} [ some p ∈ {0,1}^k has U(p, r) = x within t(n) steps ] ≥ 2/3 }.':
r"""\[
\mathrm{pK}^t(x) = \min\bigl\{\, k : \Pr_{r \sim \{0,1\}^{t(n)}} \bigl[\, \text{some } p \in \{0,1\}^k \text{ has } U(p, r) = x \text{ within } t(n) \text{ steps} \,\bigr] \ge 2/3 \,\bigr\}.
\]""",
'Pr_{z ~ {0,1}^n} [ A(f(z)) ∈ f^{−1}(f(z)) ] < 1 / q(n).':
r"""\[
\Pr_{z \sim \{0,1\}^n} \bigl[\, A(f(z)) \in f^{-1}(f(z)) \,\bigr] < 1 / q(n).
\]""",
'io-OWF exist ⇒ NP ⊄ BPP ⇒ P ≠ NP,':
r"""\[
\text{io-OWF exist} \;\;\Rightarrow\;\; \mathrm{NP} \not\subseteq \mathrm{BPP} \;\;\Rightarrow\;\; \mathrm{P} \ne \mathrm{NP},
\]""",
'm_R(x, y) := 2^{ −pK^t(y) − pK^t(x | y) }, m_F(x, y) := 2^{ −pK^t(x) − pK^t(y | x) }.':
r"""\[
m_R(x, y) := 2^{-\mathrm{pK}^t(y) - \mathrm{pK}^t(x \mid y)}, \qquad m_F(x, y) := 2^{-\mathrm{pK}^t(x) - \mathrm{pK}^t(y \mid x)}.
\]""",
'σ^rev_D(x, y) := log ( D(x, y) / m_R(x, y) )\n= [ pK^t(x | y) − log 1/D(x | y) ] + [ pK^t(y) − log 1/D_2(y) ].':
r"""\[
\begin{aligned}
\sigma^{\mathrm{rev}}_D(x, y) &:= \log \bigl( D(x, y) / m_R(x, y) \bigr) \\
&= \bigl[\, \mathrm{pK}^t(x \mid y) - \log 1/D(x \mid y) \,\bigr] + \bigl[\, \mathrm{pK}^t(y) - \log 1/D_2(y) \,\bigr].
\end{aligned}
\]""",
'Pr_{(x,y) ~ D} [ σ^rev_D(x, y) = s ] = 2^s · Σ_{(x,y) ∈ supp D : σ^rev_D(x,y) = s} m_R(x, y).':
r"""\[
\Pr_{(x,y) \sim D} \bigl[\, \sigma^{\mathrm{rev}}_D(x, y) = s \,\bigr] = 2^s \cdot \sum_{(x,y) \in \operatorname{supp} D \,:\, \sigma^{\mathrm{rev}}_D(x,y) = s} m_R(x, y).
\]""",
'ρ_F(x_{−τ}) P[x(+t) | λ(+t)] / ( ρ_R(x_{+τ}) P[x(−t) | λ(−t)] ) = e^{ +ω_F },':
r"""\[
\rho_F(x_{-\tau})\, P[x(+t) \mid \lambda(+t)] \;/\; \bigl( \rho_R(x_{+\tau})\, P[x(-t) \mid \lambda(-t)] \bigr) = e^{+\omega_F},
\]""",
# --- section 3 ---
'Σ_{x ∈ {0,1}^n} 2^{ −pK^t(x) } ≤ (3/2)(n + d).':
r"""\[
\sum_{x \in \{0,1\}^n} 2^{-\mathrm{pK}^t(x)} \le (3/2)(n + d).
\]""",
'Σ_{x ∈ {0,1}^n} 2^{ −pK^t(x | y) } ≤ (3/2)(n + d).':
r"""\[
\sum_{x \in \{0,1\}^n} 2^{-\mathrm{pK}^t(x \mid y)} \le (3/2)(n + d).
\]""",
'pK^t(x) ≤ log 1/D_1(x) + c_D log n,':
r"""\[
\mathrm{pK}^t(x) \le \log 1/D_1(x) + c_D \log n,
\]""",
'pK^{p(t)}(x | y) ≤ log 1/S(x | y) + O(log t).':
r"""\[
\mathrm{pK}^{p(t)}(x \mid y) \le \log 1/S(x \mid y) + O(\log t).
\]""",
'Pr_{x ~ D(· | y)} [ pK^t(x | y) < log 1/D(x | y) − α − log(3(n + d)/2) ] ≤ 2^{ −α },':
r"""\[
\Pr_{x \sim D(\cdot \mid y)} \bigl[\, \mathrm{pK}^t(x \mid y) < \log 1/D(x \mid y) - \alpha - \log(3(n + d)/2) \,\bigr] \le 2^{-\alpha},
\]""",
'2^{ −pK^t(y) } ≥ D_2(y) · n^{ −c_D } for every y ∈ supp D_2,\nPr_{y ~ D_2} [ 2^{ −pK^t(y) } > D_2(y) · 2^{ α } · (3/2)(n + d) ] ≤ 2^{ −α } for every α ≥ 0.':
r"""\[
\begin{gathered}
2^{-\mathrm{pK}^t(y)} \ge D_2(y) \cdot n^{-c_D} \quad \text{for every } y \in \operatorname{supp} D_2, \\
\Pr_{y \sim D_2} \bigl[\, 2^{-\mathrm{pK}^t(y)} > D_2(y) \cdot 2^{\alpha} \cdot (3/2)(n + d) \,\bigr] \le 2^{-\alpha} \quad \text{for every } \alpha \ge 0.
\end{gathered}
\]""",
'n^{ −2c_0 } ≤ E_{(x,y) ~ D} [ 2^{ −σ(x,y) } ] ≤ (3/2)^2 (n + d)^2,':
r"""\[
n^{-2c_0} \le \mathrm{E}_{(x,y) \sim D} \bigl[\, 2^{-\sigma(x,y)} \,\bigr] \le (3/2)^2 (n + d)^2,
\]""",
'E_{(x,y) ~ D} [ σ(x,y) ] ≥ −2 log ( 3(n + d)/2 ).':
r"""\[
\mathrm{E}_{(x,y) \sim D} \bigl[\, \sigma(x,y) \,\bigr] \ge -2 \log \bigl( 3(n + d)/2 \bigr).
\]""",
'Pr_{(x,y) ~ D} [ σ(x,y) < −α − 2 log ( 3(n + d)/2 ) ] ≤ 2^{ −α }.':
r"""\[
\Pr_{(x,y) \sim D} \bigl[\, \sigma(x,y) < -\alpha - 2 \log \bigl( 3(n + d)/2 \bigr) \,\bigr] \le 2^{-\alpha}.
\]""",
'E_D [ 2^{−σ} ] = Σ_{(x,y) ∈ supp D} m_R(x, y) ≤ Σ_y 2^{−pK^t(y)} Σ_x 2^{−pK^t(x | y)} ≤ (3/2)^2 (n + d)^2':
r"""\[
\mathrm{E}_D \bigl[\, 2^{-\sigma} \,\bigr] = \sum_{(x,y) \in \operatorname{supp} D} m_R(x, y) \le \sum_y 2^{-\mathrm{pK}^t(y)} \sum_x 2^{-\mathrm{pK}^t(x \mid y)} \le (3/2)^2 (n + d)^2
\]""",
'K(x, y) = K(y) + K(x | y) ± O(log n) = K(x) + K(y | x) ± O(log n),':
r"""\[
K(x, y) = K(y) + K(x \mid y) \pm O(\log n) = K(x) + K(y \mid x) \pm O(\log n),
\]""",
'K(x | y) − K(y | x) = K(x) − K(y) ± O(log n).':
r"""\[
K(x \mid y) - K(y \mid x) = K(x) - K(y) \pm O(\log n).
\]""",
'Pr_{(x,y) ~ D} [ pK^{p(n)}(x | y) ≤ log 1/D(x | y) + log p(n) ] ≥ 1 − 1/q(n).':
r"""\[
\Pr_{(x,y) \sim D} \bigl[\, \mathrm{pK}^{p(n)}(x \mid y) \le \log 1/D(x \mid y) + \log p(n) \,\bigr] \ge 1 - 1/q(n).
\]""",
# --- section 4 ---
'E_{(x,y) ~ D} [ σ^rev_D(x, y) ] ≤ C log n.':
r"""\[
\mathrm{E}_{(x,y) \sim D} \bigl[\, \sigma^{\mathrm{rev}}_D(x, y) \,\bigr] \le C \log n.
\]""",
'Pr_{z} [ pK^t( z | f(z) ) ≤ log |f^{−1}(f(z))| + c log n ] < 1/q(n).':
r"""\[
\Pr_{z} \bigl[\, \mathrm{pK}^t( z \mid f(z) ) \le \log |f^{-1}(f(z))| + c \log n \,\bigr] < 1/q(n).
\]""",
'E_D [ σ^rev_D ] ≤ log p_0(n) + c_D log n + (2n + 2d) / n^2 ≤ C log n':
r"""\[
\mathrm{E}_D \bigl[\, \sigma^{\mathrm{rev}}_D \,\bigr] \le \log p_0(n) + c_D \log n + (2n + 2d) / n^2 \le C \log n
\]""",
'E_D [ σ^rev_D ] ≥ c log n · (1 − 1/n) − 2 (L + 2) ≥ (c − 3) log n − 2 log 3 − 4 − c log n / n.':
r"""\[
\mathrm{E}_D \bigl[\, \sigma^{\mathrm{rev}}_D \,\bigr] \ge c \log n \cdot (1 - 1/n) - 2 (L + 2) \ge (c - 3) \log n - 2 \log 3 - 4 - c \log n / n.
\]""",
# --- section 5 ---
'σ_t(x, y) := log m_F(x, y) − log m_R(x, y) = [ pK^t(y) + pK^t(x | y) ] − [ pK^t(x) + pK^t(y | x) ].':
r"""\[
\sigma_t(x, y) := \log m_F(x, y) - \log m_R(x, y) = \bigl[\, \mathrm{pK}^t(y) + \mathrm{pK}^t(x \mid y) \,\bigr] - \bigl[\, \mathrm{pK}^t(x) + \mathrm{pK}^t(y \mid x) \,\bigr].
\]""",
'σ_t(x, y) = [ pK^t(y) − pK^t(y | x) ] − [ pK^t(x) − pK^t(x | y) ]\n= [ pK^t(x | y) − pK^t(y | x) ] − [ pK^t(x) − pK^t(y) ].':
r"""\[
\begin{aligned}
\sigma_t(x, y) &= \bigl[\, \mathrm{pK}^t(y) - \mathrm{pK}^t(y \mid x) \,\bigr] - \bigl[\, \mathrm{pK}^t(x) - \mathrm{pK}^t(x \mid y) \,\bigr] \\
&= \bigl[\, \mathrm{pK}^t(x \mid y) - \mathrm{pK}^t(y \mid x) \,\bigr] - \bigl[\, \mathrm{pK}^t(x) - \mathrm{pK}^t(y) \,\bigr].
\end{aligned}
\]""",
'pK^{ct}(x, y) ≤ pK^t(x) + pK^t(y | x) + O(log t), pK^{ct}(x, y) ≤ pK^t(y) + pK^t(x | y) + O(log t).':
r"""\[
\mathrm{pK}^{ct}(x, y) \le \mathrm{pK}^t(x) + \mathrm{pK}^t(y \mid x) + O(\log t), \qquad \mathrm{pK}^{ct}(x, y) \le \mathrm{pK}^t(y) + \mathrm{pK}^t(x \mid y) + O(\log t).
\]""",
'σ_t(x, y) = e_R(x, y) − e_F(x, y), e_R(x, y) ≥ −O(log t), e_F(x, y) ≥ −O(log t).':
r"""\[
\sigma_t(x, y) = e_R(x, y) - e_F(x, y), \qquad e_R(x, y) \ge -O(\log t), \qquad e_F(x, y) \ge -O(\log t).
\]""",
'E_{(x,y) ~ D} [ 2^{ −σ_t(x,y) } ] ≤ n^C and E_{(x,y) ~ D} [ 2^{ +σ_t(x,y) } ] ≤ n^C.':
r"""\[
\mathrm{E}_{(x,y) \sim D} \bigl[\, 2^{-\sigma_t(x,y)} \,\bigr] \le n^C \qquad \text{and} \qquad \mathrm{E}_{(x,y) \sim D} \bigl[\, 2^{+\sigma_t(x,y)} \,\bigr] \le n^C.
\]""",
'E_{D} [ 2^{ +σ_t } ] ≥ n^a and E_{D′} [ 2^{ −σ_t } ] ≥ n^a.':
r"""\[
\mathrm{E}_{D} \bigl[\, 2^{+\sigma_t} \,\bigr] \ge n^a \qquad \text{and} \qquad \mathrm{E}_{D'} \bigl[\, 2^{-\sigma_t} \,\bigr] \ge n^a.
\]""",
'NP ⊆ BPP ⇒ BEM ⇒ no io-OWF.':
r"""\[
\mathrm{NP} \subseteq \mathrm{BPP} \;\;\Rightarrow\;\; \mathrm{BEM} \;\;\Rightarrow\;\; \text{no io-OWF}.
\]""",
'σ^fwd_D(z, f(z)) = pK^t(f(z) | z) + pK^t(z) − n ≤ c_f log n + d,':
r"""\[
\sigma^{\mathrm{fwd}}_D(z, f(z)) = \mathrm{pK}^t(f(z) \mid z) + \mathrm{pK}^t(z) - n \le c_f \log n + d,
\]""",
'σ_t(z, f(z)) ≥ c log n − (log n + 4) − (c_f log n + d) = (a + 1) log n − d − 4.':
r"""\[
\sigma_t(z, f(z)) \ge c \log n - (\log n + 4) - (c_f \log n + d) = (a + 1) \log n - d - 4.
\]""",
'm_F(x, y) ≥ D(x, y) / ( p_D(n) n^{c_D} ) and m_R(x, y) ≥ D(x, y) / ( p_D(n) n^{c_D} ) on supp D.':
r"""\[
m_F(x, y) \ge D(x, y) / \bigl( p_D(n)\, n^{c_D} \bigr) \qquad \text{and} \qquad m_R(x, y) \ge D(x, y) / \bigl( p_D(n)\, n^{c_D} \bigr) \qquad \text{on } \operatorname{supp} D.
\]""",
'E_D [ 2^{−σ_t} ] = Σ_{supp D} D · m_R / m_F ≤ p_D(n) n^{c_D} Σ_{supp D} m_R ≤ p_D(n) n^{c_D} (3/2)^2 (n + d)^2,':
r"""\[
\mathrm{E}_D \bigl[\, 2^{-\sigma_t} \,\bigr] = \sum_{\operatorname{supp} D} D \cdot m_R / m_F \le p_D(n)\, n^{c_D} \sum_{\operatorname{supp} D} m_R \le p_D(n)\, n^{c_D}\, (3/2)^2 (n + d)^2,
\]""",
# --- section 7 ---
'no io-OWF ⇒ BEM':
r"""\[
\text{no io-OWF} \;\;\Rightarrow\;\; \mathrm{BEM}
\]""",
'Σ⁺_{s,P}(x, y) := [ pK^{P(s)}(y) + pK^{P(s)}(x | y) ] − [ pK^s(x) + pK^s(y | x) ],\nΣ⁻_{s,P}(x, y) := [ pK^{P(s)}(x) + pK^{P(s)}(y | x) ] − [ pK^s(y) + pK^s(x | y) ].':
r"""\[
\begin{gathered}
\Sigma^{+}_{s,P}(x, y) := \bigl[\, \mathrm{pK}^{P(s)}(y) + \mathrm{pK}^{P(s)}(x \mid y) \,\bigr] - \bigl[\, \mathrm{pK}^s(x) + \mathrm{pK}^s(y \mid x) \,\bigr], \\
\Sigma^{-}_{s,P}(x, y) := \bigl[\, \mathrm{pK}^{P(s)}(x) + \mathrm{pK}^{P(s)}(y \mid x) \,\bigr] - \bigl[\, \mathrm{pK}^s(y) + \mathrm{pK}^s(x \mid y) \,\bigr].
\end{gathered}
\]""",
'NP ⊆ BPP ⇒ DistNP ⊆ AvgBPP ⇒ BEM_skew ⇒ no io-OWF, NP ⊆ BPP ⇒ BEM ⇒ BEM_skew':
r"""\[
\begin{gathered}
\mathrm{NP} \subseteq \mathrm{BPP} \;\;\Rightarrow\;\; \mathrm{DistNP} \subseteq \mathrm{AvgBPP} \;\;\Rightarrow\;\; \mathrm{BEM}_{\mathrm{skew}} \;\;\Rightarrow\;\; \text{no io-OWF}, \\
\mathrm{NP} \subseteq \mathrm{BPP} \;\;\Rightarrow\;\; \mathrm{BEM} \;\;\Rightarrow\;\; \mathrm{BEM}_{\mathrm{skew}}
\end{gathered}
\]""",
'pK^t(x, y) ≥ pK^{p(t)}(x) + pK^{p(t)}(y | x) − log p(t). (H1)':
r"""\[
\mathrm{pK}^t(x, y) \ge \mathrm{pK}^{p(t)}(x) + \mathrm{pK}^{p(t)}(y \mid x) - \log p(t). \qquad \text{(H1)}
\]""",
'pK^{cs}(x, y) ≤ pK^s(x) + pK^s(y | x) + O(log s) (E1), pK^{cs}(x, y) ≤ pK^s(y) + pK^s(x | y) + O(log s) (E2).':
r"""\[
\begin{gathered}
\mathrm{pK}^{cs}(x, y) \le \mathrm{pK}^s(x) + \mathrm{pK}^s(y \mid x) + O(\log s) \quad \text{(E1)}, \\
\mathrm{pK}^{cs}(x, y) \le \mathrm{pK}^s(y) + \mathrm{pK}^s(x \mid y) + O(\log s) \quad \text{(E2)}.
\end{gathered}
\]""",
'Σ⁺_{s,P}(z, f(z)) ≥ [ n + c log n − log n − 4 ] − [ n + d + c_f log n ] = (c − c_f − 1) log n − d − 4,':
r"""\[
\Sigma^{+}_{s,P}(z, f(z)) \ge \bigl[\, n + c \log n - \log n - 4 \,\bigr] - \bigl[\, n + d + c_f \log n \,\bigr] = (c - c_f - 1) \log n - d - 4,
\]""",
'L = { (u, v, w, w\', 1^s) : ∃ M ∈ {0,1}^s such that M(w, w\') prints uv in |w| steps, and s = |u| + |v| − 10 }.':
r"""\[
\begin{gathered}
L = \bigl\{\, (u, v, w, w', 1^s) : \exists\, M \in \{0,1\}^s \text{ such that } M(w, w') \text{ prints } uv \text{ in } |w| \text{ steps,} \\
\text{and } s = |u| + |v| - 10 \,\bigr\}.
\end{gathered}
\]""",
'DistPH^O ⊆ AvgP^O and UP^O ∩ coUP^O ⊄ BPTIME^O[ 2^{ n / ω(log n) } ];':
r"""\[
\mathrm{DistPH}^O \subseteq \mathrm{AvgP}^O \qquad \text{and} \qquad \mathrm{UP}^O \cap \mathrm{coUP}^O \not\subseteq \mathrm{BPTIME}^O\bigl[\, 2^{n / \omega(\log n)} \,\bigr];
\]""",
'DistNP^O ⊆ HeurP^O and DistNP^O ⊄ AvgSIZE^O[ 2^{ a n / log n } ];':
r"""\[
\mathrm{DistNP}^O \subseteq \mathrm{HeurP}^O \qquad \text{and} \qquad \mathrm{DistNP}^O \not\subseteq \mathrm{AvgSIZE}^O\bigl[\, 2^{a n / \log n} \,\bigr];
\]""",
'log(1/μ) = 6 a n i(t) / log n ≤ (6/7) · n · (log log m + log k) / log n = o(n).':
r"""\[
\log(1/\mu) = 6\, a\, n\, i(t) / \log n \le (6/7) \cdot n \cdot (\log \log m + \log k) / \log n = o(n).
\]""",
'E_{D_m} [ 2^{ +σ_t } ] ≥ μ² · 2^n / ( 2^{O(1)} · t ) = 2^{ n − o(n) }.':
r"""\[
\mathrm{E}_{D_m} \bigl[\, 2^{+\sigma_t} \,\bigr] \ge \mu^2 \cdot 2^n / \bigl( 2^{O(1)} \cdot t \bigr) = 2^{n - o(n)}.
\]""",
'σ_t(x, y) ≥ (n − 6) + (log N − log t − 6) − (2n + O(1)) = log |M_t| − log t − O(1),':
r"""\[
\sigma_t(x, y) \ge (n - 6) + (\log N - \log t - 6) - (2n + O(1)) = \log |M_t| - \log t - O(1),
\]""",
'E_D [ 2^{ +σ_t } · 1_S ] = D(S) · E_D [ 2^{ σ_t } | S ] ≤ D(S) · 2^{ log(1/D(S)) + O(log n) } = n^{O(1)}.':
r"""\[
\mathrm{E}_D \bigl[\, 2^{+\sigma_t} \cdot \mathbf{1}_S \,\bigr] = D(S) \cdot \mathrm{E}_D \bigl[\, 2^{\sigma_t} \bigm| S \,\bigr] \le D(S) \cdot 2^{\log(1/D(S)) + O(\log n)} = n^{O(1)}.
\]""",
'E_D [ 2^{ −σ_t } · 1_G ] ≤ n^{O(1)} and E_D [ 2^{ +σ_t } · 1_G ] ≤ n^{O(1)}.':
r"""\[
\mathrm{E}_D \bigl[\, 2^{-\sigma_t} \cdot \mathbf{1}_G \,\bigr] \le n^{O(1)} \qquad \text{and} \qquad \mathrm{E}_D \bigl[\, 2^{+\sigma_t} \cdot \mathbf{1}_G \,\bigr] \le n^{O(1)}.
\]""",
'E_D [ 2^{−σ_t} · 1_G ] = Σ_G D · m_R / m_F ≤ p n^{c_D} Σ_G m_R ≤ p n^{c_D} (3/2)^2 (n + d)^2,':
r"""\[
\mathrm{E}_D \bigl[\, 2^{-\sigma_t} \cdot \mathbf{1}_G \,\bigr] = \sum_G D \cdot m_R / m_F \le p\, n^{c_D} \sum_G m_R \le p\, n^{c_D}\, (3/2)^2 (n + d)^2,
\]""",
'DistNP ⊆ AvgBPP ⇒ BEM_skew ⇒ no io-OWF, DistNP ⊆ HeurP ⇒ no io-OWF, DistNP ⊆ HeurP ⇏_rel BEM.':
r"""\[
\begin{gathered}
\mathrm{DistNP} \subseteq \mathrm{AvgBPP} \;\;\Rightarrow\;\; \mathrm{BEM}_{\mathrm{skew}} \;\;\Rightarrow\;\; \text{no io-OWF}, \qquad \mathrm{DistNP} \subseteq \mathrm{HeurP} \;\;\Rightarrow\;\; \text{no io-OWF}, \\
\mathrm{DistNP} \subseteq \mathrm{HeurP} \;\;\nRightarrow_{\mathrm{rel}}\;\; \mathrm{BEM}.
\end{gathered}
\]""",
'H_pK ⇒? BEM (the same-time question)':
r"""\[
\mathrm{H}_{\mathrm{pK}} \;\;\Rightarrow ?\;\; \mathrm{BEM} \qquad \text{(the same-time question)}
\]""",
'BEM_skew ⇒? (i) (the characterization question)':         # E68: was H_pK on the right until B38
r"""\[
\mathrm{BEM}_{\mathrm{skew}} \;\;\Rightarrow ?\;\; \text{(i)} \qquad \text{(the characterization question)}
\]""",
'DistNP ⊆ AvgBPP ⇒ H_pK ⇒ BEM_skew ⇒ no io-OWF ⇔ average-case symmetry of information for pK^t at level 1 − 1/poly ⇒ error-prone average-case computation of K on samplable D':
r"""\[
\begin{gathered}
\mathrm{DistNP} \subseteq \mathrm{AvgBPP} \;\;\Rightarrow\;\; \mathrm{H}_{\mathrm{pK}} \;\;\Rightarrow\;\; \mathrm{BEM}_{\mathrm{skew}} \;\;\Rightarrow\;\; \text{no io-OWF} \\
\Leftrightarrow\;\; \text{average-case symmetry of information for } \mathrm{pK}^t \text{ at level } 1 - 1/\mathrm{poly} \\
\Rightarrow\;\; \text{error-prone average-case computation of } K \text{ on samplable } D
\end{gathered}
\]""",
# --- added 15 Sep 2026 for Proposition 8, the second top (E68, thread B36 / B38) ---
'pK^t(x, y) ≥ pK^{t^{c_1}}(x) + pK^{t^{c_1}}(y | x) − O(log n).':
r"""\[
\mathrm{pK}^t(x, y) \ge \mathrm{pK}^{t^{c_1}}(x) + \mathrm{pK}^{t^{c_1}}(y \mid x) - O(\log n).
\]""",
'pK^t(x_1, …, x_ℓ | y) ≥ Σ_i pK^{t^{c_1}}(x_i | y, x_1, …, x_{i−1}) − ℓ · O(log N) − δ(2N, 2t).':
r"""\[
\mathrm{pK}^t(x_1, \ldots, x_\ell \mid y) \ge \sum_i \mathrm{pK}^{t^{c_1}}(x_i \mid y, x_1, \ldots, x_{i-1}) - \ell \cdot O(\log N) - \delta(2N, 2t).
\]""",
'DistNP ⊆ AvgBPP ⇒ H_pK ⇒ BEM_skew ⇒ no io-OWF, (i) ⇒ BEM_skew [Proposition 13]':
r"""\[
\begin{gathered}
\mathrm{DistNP} \subseteq \mathrm{AvgBPP} \;\;\Rightarrow\;\; \mathrm{H}_{\mathrm{pK}} \;\;\Rightarrow\;\; \mathrm{BEM}_{\mathrm{skew}} \;\;\Rightarrow\;\; \text{no io-OWF}, \\
\text{(i)} \;\;\Rightarrow\;\; \mathrm{BEM}_{\mathrm{skew}} \qquad \text{[Proposition 13]}
\end{gathered}
\]""",
# --- section 8 ---
'σ^rev_D(x, y) ≤ O(log n),':
r"""\[
\sigma^{\mathrm{rev}}_D(x, y) \le O(\log n),
\]""",
'σ^rev_D(x, y) = [ pK^t(y) + pK^t(x | y) ] − log 1/D(x, y).':
r"""\[
\sigma^{\mathrm{rev}}_D(x, y) = \bigl[\, \mathrm{pK}^t(y) + \mathrm{pK}^t(x \mid y) \,\bigr] - \log 1/D(x, y).
\]""",
# --- added 15 Sep 2026 for Definition 10, Theorem 4 and Corollary 2 in Section 8.2 (E70, thread B40) ---
'S(x | y) ≥ D(x | y) / n^c for every y ∈ Y and every x with (x, y) ∈ supp D.':
r"""\[
S(x \mid y) \ge D(x \mid y) / n^c \qquad \text{for every } y \in Y \text{ and every } x \text{ with } (x, y) \in \operatorname{supp} D.
\]""",
'pK^t(x | y) ≤ k implies Pr[ USamp_t(y) = x ] ≥ 1 / (a · n · 2^k)':
r"""\[
\mathrm{pK}^t(x \mid y) \le k \qquad \text{implies} \qquad \Pr\bigl[\, \mathrm{USamp}_t(y) = x \,\bigr] \ge 1 / (a \cdot n \cdot 2^k)
\]""",
'USamp_t(x | y) ≥ D(x | y) / (b n^{c+3}),':
r"""\[
\mathrm{USamp}_t(x \mid y) \ge D(x \mid y) / (b\, n^{c+3}),
\]""",
'σ^rev_D(x, y) ≤ c′ log n.':
r"""\[
\sigma^{\mathrm{rev}}_D(x, y) \le c' \log n.
\]""",
'pK^t(x | y) ≤ c log n + log 1/D(x, y) − log 1/D_2(y) + log n + log(3(n + d)/2) = log 1/D(x | y) + (c + 1) log n + log(3(n + d)/2).':
r"""\[
\begin{aligned}
\mathrm{pK}^t(x \mid y) &\le c \log n + \log 1/D(x, y) - \log 1/D_2(y) + \log n + \log(3(n + d)/2) \\
&= \log 1/D(x \mid y) + (c + 1) \log n + \log(3(n + d)/2).
\end{aligned}
\]""",
# --- added 19 Sep 2026 for B43 (E73-E76): Proposition 10, Lemma 12, Proposition 11 (a), (c) and its proof,
#     Propositions 12 and 13, Remarks 5 and 6, all in Section 8.2 ---
'σ^rev_D(x, y) ≤ O(log n) for every (x, y) ∈ supp D,':
r"""\[
\sigma^{\mathrm{rev}}_D(x, y) \le O(\log n) \qquad \text{for every } (x, y) \in \operatorname{supp} D,
\]""",
'pK^{ct}(x | z) ≤ pK^t(y | z) + pK^t(x | y) + O(log t).':
r"""\[
\mathrm{pK}^{ct}(x \mid z) \le \mathrm{pK}^t(y \mid z) + \mathrm{pK}^t(x \mid y) + O(\log t).
\]""",
'E[ σ^rev_{D_{G∘F}}(x, z) at time ct ] ≤ E[ σ^rev_{D_F}(x, y) at time t ] + E[ σ^rev_{D_G}(y, z) at time t ] + H(Y | X, Z) + O(log t),':
r"""\[
\begin{aligned}
\mathrm{E}\bigl[\, \sigma^{\mathrm{rev}}_{D_{G \circ F}}(x, z) \text{ at time } ct \,\bigr]
\;\le\; &\mathrm{E}\bigl[\, \sigma^{\mathrm{rev}}_{D_F}(x, y) \text{ at time } t \,\bigr]
+ \mathrm{E}\bigl[\, \sigma^{\mathrm{rev}}_{D_G}(y, z) \text{ at time } t \,\bigr] \\
&+ H(Y \mid X, Z) + O(\log t),
\end{aligned}
\]""",
'σ^rev_{D×D′}(⟨x, x′⟩, ⟨y, y′⟩) at time ct ≤ σ^rev_D(x, y) at time t + σ^rev_{D′}(x′, y′) at time t + O(log t).':
r"""\[
\begin{aligned}
\sigma^{\mathrm{rev}}_{D \times D'}(\langle x, x' \rangle, \langle y, y' \rangle) \text{ at time } ct
\;\le\; &\sigma^{\mathrm{rev}}_D(x, y) \text{ at time } t + \sigma^{\mathrm{rev}}_{D'}(x', y') \text{ at time } t \\
&+ O(\log t).
\end{aligned}
\]""",
'Δ = [ log D_{G∘F}(x, z) − log D_F(x, y) − log D_G(y, z) ] + [ pK^{ct}(x | z) − pK^t(x | y) − pK^t(y | z) ] + [ pK^{ct}(z) − pK^t(z) ] − pK^t(y).':
r"""\[
\begin{aligned}
\Delta = {} &\bigl[\, \log D_{G \circ F}(x, z) - \log D_F(x, y) - \log D_G(y, z) \,\bigr]
+ \bigl[\, \mathrm{pK}^{ct}(x \mid z) - \mathrm{pK}^t(x \mid y) - \mathrm{pK}^t(y \mid z) \,\bigr] \\
&+ \bigl[\, \mathrm{pK}^{ct}(z) - \mathrm{pK}^t(z) \,\bigr] - \mathrm{pK}^t(y).
\end{aligned}
\]""",
'E_D[ σ^rev_D ] = ( E_D[ pK^t(x | y) ] − H(X | Y) ) ± O(log n),':
r"""\[
\mathrm{E}_D\bigl[\, \sigma^{\mathrm{rev}}_D \,\bigr] \;=\; \bigl(\, \mathrm{E}_D\bigl[\, \mathrm{pK}^t(x \mid y) \,\bigr] - H(X \mid Y) \,\bigr) \;\pm\; O(\log n),
\]""",
'E_D[ σ^rev_D at time t ] ≥ log 1/ε(n) − H(X | f(X)) − O(log n);':
r"""\[
\mathrm{E}_D\bigl[\, \sigma^{\mathrm{rev}}_D \text{ at time } t \,\bigr] \;\ge\; \log 1/\varepsilon(n) \;-\; H(X \mid f(X)) \;-\; O(\log n);
\]""",
'σ^rev_{D^{φ,ψ}}(φ(x), ψ(y)) at time ct + 2T(n) + O(n) ≤ σ^rev_D(x, y) at time t + O(1),':
r"""\[
\sigma^{\mathrm{rev}}_{D^{\varphi,\psi}}(\varphi(x), \psi(y)) \text{ at time } ct + 2T(n) + O(n) \;\le\; \sigma^{\mathrm{rev}}_D(x, y) \text{ at time } t + O(1),
\]""",
'USamp_{p(t_S)}(x | y) ≥ S(x | y) / n^{e}.':
r"""\[
\mathrm{USamp}_{p(t_S)}(x \mid y) \;\ge\; S(x \mid y) / n^{e}.
\]""",
}

# --------------------------------------------------------------------------------------------
# 2. Character-level conversion of prose (outside the fragments).
# --------------------------------------------------------------------------------------------

CHARS = {
    '§': r'\S{}',         # section sign
    '—': '---',           # em dash
    '–': '--',            # en dash
    '…': r'\dots{}',      # ellipsis
    '∎': r'$\blacksquare$',   # end of proof
    '†': r'\dag{}',          # citation from memory (B42, 18 Sep 2026)
    'á': r"\'a", 'é': r"\'e", 'í': r"\'{\i}",
    'ü': r'\"u', 'ö': r'\"o', 'ä': r'\"a',
    'Ü': r'\"U', 'è': r"\`e",     # B46: the Loschmidt/Zermelo and Poincare titles in the reference list
}

ESCAPE = {'\\': r'\textbackslash{}', '{': r'\{', '}': r'\}', '$': r'\$', '&': r'\&',
          '#': r'\#', '_': r'\_', '%': r'\%', '~': r'\textasciitilde{}', '^': r'\^{}',
          '<': r'\textless{}', '>': r'\textgreater{}'}

GREEK = set('σΣρλωμνταβδεΩΦΠΔℓφψπ')
STRONG = set('^_{}|~<>') | GREEK | set(
    '≤≥≠≈∈⊆⊄⊇⊕⇒⇔⇏→↦←'
    '−±×·⋯∖∩⟨⟩⌈⌉⊥∞′'
    '²⁺⁻₁¹'
    '∘∫\u0303')          # B43: composition, integral, the combining tilde of P̃

PLACE = '\x00%d\x00'

CLASSWORD = re.compile(r'\b(NP|BPP|DistNP|AvgP|AvgBPP|HeurP|HeurBPP|UP|coUP|BEM|USamp|BPTIME|AvgSIZE|DistPH|GF|supp|poly)\b')


def tt(text):
    """Typewriter for the reference-list file names: breakpoints after / and _, no -- ligature."""
    out = []
    for ch in text:
        if ch in ESCAPE:
            out.append(ESCAPE[ch])
        else:
            out.append(ch)
        if ch == '-':
            out.append('{}')
        elif ch in '/_':
            out.append(r'\allowbreak{}')
    return r'\texttt{' + ''.join(out) + '}'


_KEYS = sorted(set(MATH) | set(RAW) | set(PROSE), key=len, reverse=True)
_PAT = re.compile("(?<![\\w'])(?:" + '|'.join(re.escape(k) for k in _KEYS) + ')(?!\\w)')

LEFTOVERS = []          # (context, offending text), collected across the whole document
USED = set()


def prose_escape(text):
    out = []
    for ch in text:
        if ch in ESCAPE:
            out.append(ESCAPE[ch])
        elif ch in CHARS:
            out.append(CHARS[ch])
        else:
            out.append(ch)
    return ''.join(out)


def leftover_check(text, ctx, refs):
    """text is prose with fragments already replaced by placeholders.  Anything mathematical
    left in it is an error: we collect it (with context) so a run reports every miss at once."""
    probe = re.sub('\x00\\d+\x00', '\x01', text)
    probe = re.sub(r'`[^`]*`', ' ', probe)
    probe = re.sub(r'(?<=\d)\([a-z0-9]+\)', ' ', probe)                # Theorem 1(a), Lemma 26(1)
    probe = re.sub(r'\bpp?\.(?= ?\d)', ' ', probe)                      # p. 391, pp. 17-18
    if refs:
        probe = re.sub(r'\b[A-Z]\.', ' ', probe)                         # initials
    hits = []
    for m in re.finditer('[' + re.escape(''.join(sorted(STRONG))) + ']', probe):
        hits.append(m.start())
    for pat in (r"(?<![\w'\-])[b-zB-HJ-Z](?!\w)", r'[A-Za-z]\(', r'\d[A-Za-z]|[A-Za-z]\d',
                r'\d/\d', CLASSWORD.pattern):
        for m in re.finditer(pat, probe):
            hits.append(m.start())
    if hits:
        windows = []
        last = -100
        for h in sorted(hits):
            if h - last < 25 and windows:
                continue
            windows.append(probe[max(0, h - 30):h + 30].replace('\x01', '#'))
            last = h
        LEFTOVERS.append((ctx, windows))


def inline(text, refs=False, ctx=''):
    """Convert one joined markdown paragraph / cell / heading to LaTeX."""
    text = re.sub(r'\s+', ' ', text).strip().replace('\\|', '|')
    spans = []

    def grab_tt(m):
        body = m.group(1)
        if body not in TT:
            raise KeyError('code span not in TT: %r' % body)
        USED.add(('tt', body))
        spans.append(tt(body))
        return PLACE % (len(spans) - 1)
    text = re.sub(r'`([^`]+)`', grab_tt, text)

    def grab_page(m):                      # p. 391, pp. 381-383: prose, never a variable p
        spans.append(prose_escape(m.group(0)))
        return PLACE % (len(spans) - 1)
    text = re.sub(r'\bpp?\. ?\d+(?:–\d+)?', grab_page, text)

    def grab_frag(m):
        key = m.group(0)
        if key in MATH:
            USED.add(('math', key))
            spans.append('$' + MATH[key] + '$')
        elif key in RAW:
            USED.add(('raw', key))
            spans.append(RAW[key])
        else:
            USED.add(('prose', key))
            spans.append(prose_escape(key))
        return PLACE % (len(spans) - 1)
    if refs:                               # an author's initial is never a variable
        text = re.sub(r'\b[A-Z]\.', grab_page, text)
    text = _PAT.sub(grab_frag, text)

    leftover_check(text, ctx, refs)

    if text.count('"') % 2:
        raise ValueError('odd number of double quotes in: %r' % text[:120])
    out, open_q = [], True
    for ch in text:
        if ch == '"':
            out.append('``' if open_q else "''")
            open_q = not open_q
        else:
            out.append(ch)
    text = ''.join(out)
    text = prose_escape(text)

    text = re.sub(r'\*\*(.+?)\*\*', lambda m: r'\textbf{%s}' % m.group(1), text, flags=re.S)
    text = re.sub(r'\*(.+?)\*', lambda m: r'\emph{%s}' % m.group(1), text, flags=re.S)
    if '*' in text:
        raise ValueError('unpaired emphasis marker in: %r' % text[:120])

    text = re.sub('\x00(\\d+)\x00', lambda m: spans[int(m.group(1))], text)
    if text.startswith('['):
        text = '{}' + text
    # an end-of-proof mark that closes the paragraph is set flush right on its last line, as
    # amsthm's \qed does (B42, 18 Sep 2026; 24 marks then, 31 after B43, all closing their
    # paragraph except Remark 6's, which the markdown follows with a sentence: that one stays inline)
    if text.endswith(CHARS['∎']):
        text = text[:-len(CHARS['∎'])].rstrip() + r'\qed'
    return text


# --------------------------------------------------------------------------------------------
# 3. Tables.  Five, in source order; column specs by hand.  xltabular = tabularx that breaks
#    across pages, which the two appendix tables need; every table is exactly \textwidth wide.
# --------------------------------------------------------------------------------------------

L = r'>{\hsize=%s\hsize\raggedright\arraybackslash}X'

TABLES = [
    # 0: the objects in the order they appear (4 cols), How to read this paper (added 18 Sep 2026, B42)
    dict(size=r'\small', cols=r'@{}' + L % '0.72' + L % '0.90' + L % '0.62' + L % '1.76' + r'@{}'),
    # 1: Crooks's setup against this paper's (3 cols), section 2.6
    dict(size=r'\small', cols=r'@{}' + L % '1.05' + L % '1.05' + L % '0.90' + r'@{}'),
    # 2: one statement, two instances (3 cols), section 8.4
    dict(size=r'\small', cols=r'@{}' + L % '0.50' + L % '1.15' + L % '1.35' + r'@{}'),
    # 3: the Crooks-HILNO correspondence, seventeen rows (5 cols), appendix A.1
    dict(size=r'\footnotesize', sep='3pt',
         cols=r'@{}' + L % '0.22' + L % '1.22' + L % '1.78' + L % '1.38' + L % '0.40' + r'@{}'),
    # 4: one statement, two instances, thirteen rows (5 cols), appendix A.2
    dict(size=r'\footnotesize', sep='3pt',
         cols=r'@{}' + L % '0.24' + L % '0.66' + L % '1.30' + L % '1.90' + L % '0.90' + r'@{}'),
]


def table(rows, index):
    spec = TABLES[index]
    head, body = rows[0], rows[2:]
    n = len(head)
    out = [r'\par\medskip\noindent']
    open_grp = '{' + spec['size']
    if spec.get('sep'):
        open_grp += r'\setlength{\tabcolsep}{%s}' % spec['sep']
    out.append(open_grp)
    out.append(r'\begin{xltabular}{\textwidth}{%s}' % spec['cols'])
    out.append(r'\toprule')
    out.append(' & '.join(inline(c, ctx='table %d head' % index) for c in head) + r' \\')
    out.append(r'\midrule')
    out.append(r'\endhead')
    for j, row in enumerate(body):
        if len(row) != n:
            raise ValueError('table %d: row has %d cells, header has %d: %r' % (index, len(row), n, row))
        if j:
            out.append(r'\addlinespace[3pt]')
        out.append(' & '.join(inline(c, ctx='table %d row %r' % (index, row[0])) for c in row) + r' \\')
    out.append(r'\bottomrule')
    out.append(r'\end{xltabular}}')
    out.append(r'\par\medskip')
    return '\n'.join(out)


# --------------------------------------------------------------------------------------------
# 4. Block structure.
# --------------------------------------------------------------------------------------------

PREAMBLE = r"""%% Generated by md_to_tex_paper.py from ENTROPY_PRODUCTION.md -- do not edit by hand.
\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[margin=2.5cm]{geometry}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\renewcommand{\qedsymbol}{$\blacksquare$}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{xltabular}
\usepackage{array}
\usepackage{enumitem}
\usepackage{microtype}
\usepackage[hidelinks,pdfusetitle]{hyperref}

\setlength{\parskip}{0.45em}
\setlength{\parindent}{0pt}
\emergencystretch=4em
\hyphenpenalty=200
\renewcommand{\arraystretch}{1.12}
\allowdisplaybreaks

%% Theorem-like environments with the note's own numbers.  amsthm numbers automatically; the
%% inner/outer pair below lets each instance carry its number by hand, so Theorem 0 stays 0 and
%% nothing is renumbered.  Bodies are upright (definition style) so that the italic plain
%% readings inside them stay italic and stand out.
\theoremstyle{definition}
\newtheorem{innertheorem}{Theorem}
\newenvironment{theoremx}[1]{\renewcommand\theinnertheorem{#1}\innertheorem}{\endinnertheorem}
\newtheorem{innerlemma}{Lemma}
\newenvironment{lemmax}[1]{\renewcommand\theinnerlemma{#1}\innerlemma}{\endinnerlemma}
\newtheorem{innerproposition}{Proposition}
\newenvironment{propositionx}[1]{\renewcommand\theinnerproposition{#1}\innerproposition}{\endinnerproposition}
\newtheorem{innerdefinition}{Definition}
\newenvironment{definitionx}[1]{\renewcommand\theinnerdefinition{#1}\innerdefinition}{\endinnerdefinition}
\newtheorem{innerremark}{Remark}
\newenvironment{remarkx}[1]{\renewcommand\theinnerremark{#1}\innerremark}{\endinnerremark}
\newtheorem{innercorollary}{Corollary}
\newenvironment{corollaryx}[1]{\renewcommand\theinnercorollary{#1}\innercorollary}{\endinnercorollary}

\title{%(title)s}
\author{%(author)s}
\date{%(date)s}
\hypersetup{pdfauthor={Casey Thornton}}

\begin{document}
\maketitle
\thispagestyle{plain}
"""

ENV = {'Theorem': 'theoremx', 'Lemma': 'lemmax', 'Proposition': 'propositionx',
       'Definition': 'definitionx', 'Remark': 'remarkx', 'Corollary': 'corollaryx'}
HEAD = re.compile(r'^\*\*(Theorem|Lemma|Proposition|Definition|Remark|Corollary) (\d+) \((.*?)\)\.\*\*\s*(.*)$', re.S)
CONT = re.compile(r'^(\((?:a|b|c|i|ii|iii|1|2)\)|\*Plain reading|where c_0|and the same for|and likewise|'
                  r'and consequently|Equivalently:|and \(ii\)|\(⇒\)|\(⇐\)|\(Universal witness\.\)|where b :=|'
                  # B43 (19 Sep 2026): the statement continuations of Propositions 10, 11, 12, 13 and Remark 5
                  r'whether or not the chain|the expectations over the joint draw|more precisely the difference|'
                  r'for a permutation H|and the same with the two processes)')

ENVLOG = []


def section(text, level):
    body = inline(text, ctx='heading')
    cmd = r'\section*' if level == 2 else r'\subsection*'
    return '%s{%s}\n\\phantomsection\\addcontentsline{toc}{%s}{%s}' % (
        cmd, body, 'section' if level == 2 else 'subsection', body)


def display(buf):
    key = '\n'.join(l.strip() for l in buf)
    key = re.sub(r'[ \t]+', ' ', key)
    if key not in DISPLAY:
        raise KeyError('display not in DISPLAY:\n' + key)
    USED.add(('display', key))
    return DISPLAY[key]


def blocks(lines):
    """Split the markdown into typed blocks: ('h', level, text) ('d', [lines]) ('t', rows)
    ('ul', items) ('ol', items) ('p', text)."""
    i, out = 0, []
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.strip() == '---':
            i += 1
            continue
        if line.startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            out.append(('h', level, line[level:].strip()))
            i += 1
            continue
        if line.startswith('    '):
            buf = []
            while i < len(lines) and lines[i].startswith('    '):
                buf.append(lines[i])
                i += 1
            out.append(('d', buf))
            continue
        if line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                rows.append([c.strip() for c in re.split(r'(?<!\\)\|', lines[i].strip().strip('|'))])
                i += 1
            out.append(('t', rows))
            continue
        if line.startswith('- ') or re.match(r'^\d+\. ', line):
            kind = 'ul' if line.startswith('- ') else 'ol'
            items = []
            while i < len(lines) and (lines[i].startswith('- ') or re.match(r'^\d+\. ', lines[i])
                                      or (lines[i][:1] in (' ', '\t') and lines[i].strip())):
                m = re.match(r'^(- |\d+\. )', lines[i])
                if m:
                    items.append([m.group(1).strip(), lines[i][m.end():].strip()])
                else:
                    items[-1][1] += ' ' + lines[i].strip()
                i += 1
            out.append((kind, items))
            continue
        para = [line]
        i += 1
        while i < len(lines):
            nxt = lines[i]
            if (not nxt.strip() or nxt.startswith('#') or nxt.startswith('|') or nxt.startswith('    ')
                    or nxt.startswith('- ') or re.match(r'^\d+\. ', nxt) or nxt.strip() == '---'):
                break
            para.append(nxt)
            i += 1
        out.append(('p', ' '.join(x.strip() for x in para)))
    return out


def main():
    src = open(SRC, encoding='utf-8').read()
    bl = blocks(src.split('\n'))
    out = []
    title = None
    author = date = None
    n_tables = 0
    in_refs = False
    env_open = None          # name of the open theorem-like environment, or None
    k = 0

    def close_env():
        nonlocal env_open
        if env_open:
            out.append(r'\end{%s}' % env_open)
            ENVLOG[-1].append(out[-2][:70])
            env_open = None

    while k < len(bl):
        b = bl[k]
        kind = b[0]

        if kind == 'h':
            close_env()
            if b[1] == 1:
                title = inline(b[2], ctx='title')
            else:
                out.append(section(b[2], b[1]))
                in_refs = (b[2] == 'References')
            k += 1
            continue

        if kind == 'd':
            # a display is attached to the paragraph before it (no blank line: one paragraph)
            if out[-1].endswith(r'\qed'):
                raise ValueError('end-of-proof mark followed by a display: ' + out[-1][-80:])
            out[-1] = out[-1] + '\n' + display(b[1])
            k += 1
            continue

        if kind == 't':
            close_env()
            out.append(table(b[1], n_tables))
            n_tables += 1
            k += 1
            continue

        if kind in ('ul', 'ol'):
            close_env()
            if kind == 'ul':
                out.append(r'\begin{itemize}[leftmargin=1.2em,itemsep=3pt,topsep=3pt,parsep=0pt]')
                for lab, it in b[1]:
                    out.append(r'\item ' + inline(it, refs=in_refs, ctx='item ' + it[:30]))
                out.append(r'\end{itemize}')
            else:
                out.append(r'\begin{enumerate}[leftmargin=1.6em,itemsep=3pt,topsep=3pt,parsep=0pt]')
                for lab, it in b[1]:
                    out.append(r'\item[%s] ' % lab + inline(it, ctx='item ' + it[:30]))
                out.append(r'\end{enumerate}')
            k += 1
            continue

        # a paragraph
        text = b[1]
        m = HEAD.match(text)
        if m:
            close_env()
            name, num, note, rest = m.groups()
            env_open = ENV[name]
            ENVLOG.append(['%s %s' % (name, num)])
            head = r'\begin{%s}{%s}[{%s}]' % (env_open, num, inline(note, ctx='note ' + name + num))
            body = inline(rest, ctx=name + ' ' + num) if rest.strip() else ''
            out.append(head + (' ' + body if body else ''))
            k += 1
            continue
        if env_open and not CONT.match(text):
            close_env()
        if title is not None and author is None:
            # the header line under the title ("<author>. Version of <date>.") becomes the title
            # block's author and date (B43, 19 Sep 2026; the DRAFT line it replaced is gone)
            hm = re.match(r'^(.+?)\. (Version of .+?)\.$', text)
            if not hm:
                raise ValueError('header line under the title not understood: %r' % text[:80])
            author, date = inline(hm.group(1), ctx='author'), inline(hm.group(2), ctx='date')
            # title block: name / affiliation / email on three lines (owner, 20 Sep 2026)
            author = ' \\\\ '.join(part.strip() for part in author.split(', '))
            k += 1
            continue
        out.append(inline(text, refs=in_refs, ctx=text[:40]))
        k += 1
    close_env()

    if LEFTOVERS:
        print('LEFTOVERS: %d paragraphs with unclassified mathematics' % len(LEFTOVERS))
        for ctx, windows in LEFTOVERS:
            print('  [%s]' % ctx)
            for w in windows:
                print('        ...%s...' % w)
        raise SystemExit(1)

    allkeys = ({('math', k) for k in MATH} | {('raw', k) for k in RAW} | {('prose', k) for k in PROSE}
               | {('tt', k) for k in TT} | {('display', k) for k in DISPLAY})
    unused = allkeys - USED
    if unused:
        raise SystemExit('dictionary entries never used: %s' % sorted(unused))
    if len(ENVLOG) != 48:
        raise SystemExit('expected 48 theorem-like environments, found %d: %s' % (len(ENVLOG), ENVLOG))

    tex = PREAMBLE % {'title': title, 'author': author, 'date': date} + '\n\n' + '\n\n'.join(out) + '\n\n\\end{document}\n'
    bad = sorted({c for c in tex if ord(c) > 127})
    if bad:
        raise SystemExit('non-ASCII characters survived: %s' % [hex(ord(c)) for c in bad])
    open(OUT, 'w', encoding='utf-8').write(tex)
    nfrag = len({k for c, k in USED if c in ('math', 'raw', 'prose')})
    print('wrote %s  (%d bytes, %d tables, %d displays, %d fragment keys used, %d code spans, '
          '%d theorem-like environments, pure ASCII)'
          % (os.path.basename(OUT), len(tex), n_tables, len([1 for c, k in USED if c == 'display']),
             nfrag, len({k for c, k in USED if c == 'tt'}), len(ENVLOG)))
    if '--envs' in sys.argv:
        for e in ENVLOG:
            print('   ', e)


if __name__ == '__main__':
    main()
