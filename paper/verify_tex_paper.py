"""Check that the typeset ENTROPY_PRODUCTION.pdf lost nothing from ENTROPY_PRODUCTION.md.

Extracts the PDF text with `pdftotext -raw` (content-stream order, which keeps every table
cell in one piece; the -layout mode interleaves neighbouring cells line by line) and checks,
mechanically:
  A  every distinct numeric token of the markdown appears in the PDF;
  B  every cell of the seven markdown tables appears in the PDF (the results box and the five dictionary
     rows of section 1 added in B50 Revision 1, 20 Sep 2026);
  F  every heading appears verbatim, numbers included, and in the markdown's order (the numbered
     sections are 1 to 9 since B48, 20 Sep 2026: Abstract first, then 1 with 1.1-1.3, Theorem 4 as
     section 6, the old 6-8 as 7-9, Appendix A, Appendix B with the oracle proofs);
  T  the first sentence of every theorem-like statement (Theorems 0-4, Lemmas 1-12,
     Propositions 1-13, Definitions 1-10, Remarks 1-6, Corollaries 1-2) appears, with its own number;
  P  all N_PLAIN italic "In words" sentences (the plain readings, renamed in B50 Phase 3) appear, and in the .tex each one is an emph group that is
     not nested inside another italic group (a nested emph would flip upright);
  L  the counts of the proof label and the two read-status brackets agree (Proof; [read; [via.
     B50 Revision 1, 20 Sep 2026: the Proved / Proved-conditional / Proved; known labels became
     Proof or moved into statement heads, and the reference list's Read / cited via / not opened
     notes became one bracket per entry; [Unverified] dropped 20 Sep 2026; the 'not read' status
     and the body dagger dropped in B46, 20 Sep 2026, when the last nine unread works were read;
     [Inference] and [Speculation] dropped in B47, 20 Sep 2026, when the bracket tags were
     replaced by hedges in words);
  D  every displayed formula survives, word by word;
  G  every code-span file name appears (one since Revision 1: notes/READ_STATUS.md);
  X  the one ```tex-figure block (B50 Phase 2) is typeset as one figure environment with a
     tikzpicture, its node labels and its caption with the plain reading appear in the PDF; the
     block is stripped from the markdown before every other check, since its TikZ source is not
     text of the paper;
  H  the header line under the title is name, e-mail, date; all three on page 1 (the e-mail as a footnote,
     B50 Phase 3, 20 Sep 2026);
  I  every other markdown paragraph appears in the PDF, whole and in one piece;
  Z  the build log has no overfull box wider than 10pt and no missing character.

Usage:  ../../../../.venv/bin/python verify_tex_paper.py
Exit status 0 iff every check passes.
"""

import os
import re
import subprocess
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(HERE, 'ENTROPY_PRODUCTION.md')
PDF = os.path.join(HERE, 'ENTROPY_PRODUCTION.pdf')
TEX = os.path.join(HERE, 'ENTROPY_PRODUCTION.tex')
LOG = os.path.join(HERE, 'ENTROPY_PRODUCTION.log')
N_PLAIN = 99          # italic 'In words' sentences after formulas, tables or the figure (the abstract's among them); the label was
                      # 'Plain reading' until B50 Phase 3 (20 Sep 2026), when the count also stopped including the mention in the
                      # Conventions (1.3): the pattern now requires the colon, so it counts the sentences and not the label's name.
                      # History (as 'Plain reading', with the Conventions mention counted, so one more than the sentences):
                      # plus the mention in the Conventions (section 1.3 since B48, 20 Sep 2026; the section numbers in the
                      # history below are those before B48, when the Conventions and the abstract preceded section 1)
                      # (62 at E52; 64 after the B20 edit of 15 Sep 2026 added the section now numbered 1.1 (1.4 at E55) and the
                      # proof-structure paragraph of Section 7.1, one plain reading each; 68 after the B21
                      # edit of the same day, E57: Definition 9 and Proposition 3 one each, the second
                      # open question of Section 7.5 one, the placement chain of Section 7.6 one; 73 after
                      # the B23 edit of the same day, E60: Proposition 8 two (statement and proof),
                      # Corollary 1 one, the observer paragraph of Section 8.2 one, the Fox, Karamchedu
                      # and Mygdalas paragraph of Section 8.5 one; 74 after the B24 paste of the same day,
                      # E63: the new Lemma 6, the coding theorem with an auxiliary input, one; 80 after the
                      # B38 edit of the same day, E68: the error-prone-world paragraph of Section 7.3 one,
                      # the obstructions paragraph of Section 7.5 one, the new Proposition 8 two (statement
                      # and proof), the two-top placement of Section 7.6 one, and the closing sentence of
                      # Section 1.1 replaced in place, no change in count; 87 after the Theorem 4 insertion
                      # of the same day, E70: Definition 10 one, the universal reverse sampler one, Theorem 4
                      # three (one per part), its proof one, Corollary 2 one; unchanged by the pass-22
                      # referee corrections of 18 Sep 2026, E72: 93 wording edits, plain readings rewritten
                      # in place, none added or removed; 88 after the How-to-read section of the same day,
                      # B42: the sandwich display one; 99 after B43 of 19 Sep 2026, E73-E76: Proposition 10
                      # one, Lemma 12 one, Proposition 11 four (parts (a), (b), (c) and its proof),
                      # Propositions 12 and 13 one each, Remarks 5 and 6 one each, the axiom paragraph of
                      # Section 8.4 one, with no display; 100 after B50 Phase 2 of 20 Sep 2026: the figure's caption
                      # carries its own plain reading; the 33 readings shortened by B50 item 5 were rewritten in place)
N_STMT = 48           # theorem-like statements: 5 theorems, 12 lemmas, 13 propositions, 10 definitions,
                      # 6 remarks, 2 corollaries (32 at E52: 6 propositions, 8 definitions; +1 each at E57;
                      # E60 added Proposition 8 and Corollary 1, the paper's first corollary; E63 added
                      # Lemma 6, the coding theorem with an auxiliary input, and renumbered Lemmas 6-10
                      # to 7-11; E68 added Proposition 8, the second top of the skewed sandwich, and
                      # renumbered the reversible-process proposition 8 to 9; E70 added Definition 10,
                      # Theorem 4 and Corollary 2 in Section 8.2; E72 retitled Definition 4 and
                      # Propositions 4 and 6 and relabelled Proposition 2 Proved, no change in count;
                      # B42 of the same day, the How-to-read section and the read-status detagging, added none;
                      # B43 of 19 Sep 2026, E73-E76, added Proposition 10, Lemma 12, Propositions 11-13 and
                      # Remarks 5-6 in Section 8.2)
N_DISP = 75           # displayed formulas (52 at E52; E57 added the language L of Definition 9 and the
                      # placement chain of Section 7.6, and replaced the one display of Section 7.5 by two;
                      # E60 added the bound of Proposition 8 and changed the last arrow of the chain, which
                      # stays one display; E63 added the bound of Lemma 6; E68 replaced the characterization
                      # question of Section 7.5 in place and added the chain rule of Proposition 8, the
                      # Kabanets-Kolokolova chain rule in its proof, and the two-top placement; E70 added
                      # the domination condition of Definition 10, the Proposition 22 bound of the universal
                      # reverse sampler, the two bounds of Theorem 4 and the one display of its proof;
                      # E72 changed no display; B42 of the same day added the sandwich of the How-to-read
                      # section, drawn as one display; B43 of 19 Sep 2026 added nine: Proposition 10's bound,
                      # Lemma 12, Proposition 11 (a) and (c) and the split of Delta in its proof,
                      # Propositions 12 and 13, Remarks 5 and 6)

NUM = re.compile(r'\d[\d,]*(?:\.\d+)?')
LIG = {'ﬀ': 'ff', 'ﬁ': 'fi', 'ﬂ': 'fl', 'ﬃ': 'ffi', 'ﬄ': 'ffl',
       '−': '-', '–': '-', '—': '-', '’': "'", '‘': "'",
       '“': '"', '”': '"', ' ': ' ', '­': '',
       '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4',
       '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9',
       '⁺': '+', '⁻': '-', '₀': '0', '₁': '1', '₂': '2', '₃': '3',
       '₄': '4', '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9'}


def pdftext(path):
    out = subprocess.run(['pdftotext', '-raw', path, '-'],
                         capture_output=True, text=True, check=True).stdout
    for a, b in LIG.items():
        out = out.replace(a, b)
    # -raw ends each page with its footer number on a line of its own, immediately before the
    # form feed ("cited\n44\fvia"); strip exactly the expected number so that a tag split across
    # a page break still counts (E60: "cited" / "via" broke across pages 44-45 in the references)
    pages = out.split('\f')
    for i in range(len(pages) - 1):
        tail = '\n' + str(i + 1)
        if pages[i].endswith(tail):
            pages[i] = pages[i][:-len(str(i + 1))]
    out = '\f'.join(pages)
    # an explicit hyphen broken at a line end ("Proved-" / "conditional") is rejoined; this runs
    # after the page numbers are stripped, so that a hyphen at a page end ("non-\n46\flinear",
    # B47, 20 Sep 2026, page 46) does not glue the page number into the word
    out = re.sub(r'-\n\s*', '-', out)
    return out


def flat(text):
    """Whitespace-collapsed; the space pdftotext leaves before closing punctuation after a
    raised digit is dropped on both sides."""
    return re.sub(r' +([,;.)])', r'\1', re.sub(r'\s+', ' ', text))


def squash(text):
    """Alphanumerics only, lowercased: survives hyphenation, line breaks, ligatures and the
    difference between ASCII mathematics and its typeset form."""
    return re.sub(r'[^a-z0-9]', '', text.lower())


def words(text):
    return [w for w in (squash(w) for w in re.split(r'[\s^_{}|()\[\]]+', text)) if w]


def main():
    md = open(MD, encoding='utf-8').read()
    # the tex-figure block is LaTeX source, not text of the paper: cut it out before every check
    # (B50 Phase 2, 20 Sep 2026); its own check is X below
    figs = re.findall(r'^```tex-figure\n(.*?)^```\n', md, re.S | re.M)
    md = re.sub(r'^```tex-figure\n.*?^```\n', '', md, flags=re.S | re.M)
    for a, b in LIG.items():
        md = md.replace(a, b)
    pdf = pdftext(PDF)
    md_flat, pdf_flat = flat(md), flat(pdf)
    md_sq, pdf_sq = squash(md), squash(pdf)

    fails, notes = [], []

    def check(ok, label, detail=''):
        (notes if ok else fails).append(('PASS' if ok else 'FAIL') + '  ' + label +
                                        (('  --  ' + detail) if detail else ''))

    # ---- A. every numeric token ------------------------------------------------------------
    md_nums = sorted(set(NUM.findall(md)))
    missing = [t for t in md_nums if t not in pdf_flat]
    check(not missing, 'A  all %d distinct numeric tokens of the markdown appear in the PDF'
          % len(md_nums), 'missing: %s' % missing[:20])

    # ---- B. every table cell ---------------------------------------------------------------
    cells, ntab, intab = [], 0, False
    for line in md.split('\n'):
        if line.startswith('|'):
            if not intab:
                ntab += 1
                intab = True
            if set(line.replace('|', '').strip()) <= set('- '):
                continue
            cells += [c.strip() for c in re.split(r'(?<!\\)\|', line.strip().strip('|'))]
        else:
            intab = False
    bad, wrapped = [], 0
    for c in cells:
        c = re.sub(r'[*`]', '', c).replace('\\|', '|').strip()
        if not c or squash(c) == '':
            continue
        if squash(c) in pdf_sq:
            continue
        ws = words(c)
        if all(w in pdf_sq for w in ws):
            wrapped += 1
        else:
            bad.append(c[:60])
    check(not bad, 'B  all %d non-empty cells of the %d markdown tables appear in the PDF '
                   '(%d of them wrapped, matched word by word)' % (len(cells), ntab, wrapped),
          'missing: %s' % bad[:12])
    check(ntab == 7, 'B2 seven tables in the markdown (results box and five dictionary rows, B50; symbol table, B42; '
                     'Crooks setup 2.6; two instances 8.4; A.1; A.2)', str(ntab))

    # ---- F. headings -----------------------------------------------------------------------
    heads = [h.strip() for h in re.findall(r'^#{2,3} (.+)$', md, re.M)]
    badh = [h for h in heads if squash(h) not in pdf_sq]
    check(not badh, 'F  all %d section headings appear verbatim, numbers included' % len(heads),
          str(badh))
    # each heading is searched for after the previous one (since B48, 20 Sep 2026, the How-to-read
    # section is 1.2 and follows the 1.1 heading it names, so no heading is named before it appears)
    order, pos = [], 0
    for h in heads:
        nxt = pdf_sq.find(squash(h), pos)
        order.append(nxt)
        if nxt >= 0:
            pos = nxt
    check(all(o >= 0 for o in order), 'F2 the headings appear in the order the markdown has them '
                                      '(each found after the one before it)', str(order))
    numbered = [h for h in heads if re.match(r'\d+\. ', h)]
    check([h.split()[0] for h in numbered] == ['1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.'],
          'F3 the numbered sections are 1 to 9 (the file has nine, plus Appendices A and B)')

    # ---- T. theorem-like statements --------------------------------------------------------
    paras_raw = [p for p in re.split(r'\n\s*\n', md)]
    HEAD = re.compile(r'^\*\*(Theorem|Lemma|Proposition|Definition|Remark|Corollary) (\d+) \((.*?)\)\.\*\*\s*(.*)$', re.S)
    heads_t, badt = [], []
    for i, p in enumerate(paras_raw):
        m = HEAD.match(p.strip())
        if not m:
            continue
        kind, num, note, rest = m.groups()
        rest = re.sub(r'\s+', ' ', rest).strip()
        if not rest:                                # head alone on its line: next paragraph
            rest = re.sub(r'\s+', ' ', paras_raw[i + 1]).strip()
            if rest.startswith('    ') or paras_raw[i + 1].startswith('    '):
                rest = re.sub(r'\s+', ' ', paras_raw[i + 1]).strip()
        first = re.split(r'(?<=[.:,;])\s', rest, maxsplit=1)[0]
        first = re.sub(r'[*`]', '', first)
        heads_t.append((kind, num, note, first))
        if squash('%s %s (%s)' % (kind, num, note)) not in pdf_sq:
            badt.append('%s %s head' % (kind, num))
        elif squash(first) not in pdf_sq and not all(w in pdf_sq for w in words(first)):
            badt.append('%s %s: %s' % (kind, num, first[:50]))
    kinds = Counter(k for k, n, _, _ in heads_t)
    check(len(heads_t) == N_STMT and kinds == Counter({'Theorem': 5, 'Lemma': 12, 'Proposition': 13,
                                                       'Definition': 10, 'Remark': 6, 'Corollary': 2}),
          'T1 %d theorem-like statements parsed: 5 theorems, 12 lemmas, 13 propositions, '
          '10 definitions, 6 remarks, 2 corollaries' % N_STMT, str(kinds))
    nums = sorted(int(n) for k, n, _, _ in heads_t if k == 'Theorem')
    check(nums == [0, 1, 2, 3, 4], 'T2 the theorems are numbered 0, 1, 2, 3, 4', str(nums))
    check(not badt, 'T3 every statement head (kind, number, title) and its first sentence appear',
          str(badt))
    q = 'Question 1 (the open problem).'
    check(md.count('**' + q + '**') == 1 and squash(q) in pdf_sq and 'Open Problem (status' not in md,
          'T4 the open problem is stated once as Question 1 (B50 item 3) and its head appears in the PDF')

    # ---- P. plain readings -----------------------------------------------------------------
    prs = re.findall(r'(?<!\*)\*In words:[^*]*\*', md)
    badp = [p[:50] for p in prs if squash(p) not in pdf_sq and not all(w in pdf_sq for w in words(p))]
    check(len(prs) == N_PLAIN, 'P1 %d italic "In words" sentences in the markdown (after formulas, tables or '
                               'the figure, the abstract\'s among them; the label\'s mention in the Conventions, 1.3, not counted)' % N_PLAIN, str(len(prs)))
    check(not badp, 'P2 all %d "In words" sentences appear in the PDF' % len(prs), str(badp))
    tex = open(TEX, encoding='utf-8').read()
    emph = [m.start() for m in re.finditer(r'\\emph\{In words:', tex)]
    nested = 0
    for pos in emph:                       # an unclosed \emph{ or \textit{ before it would nest it
        depth = 0
        for m in re.finditer(r'\\(?:emph|textit)\{|\{|\}', tex[max(0, pos - 4000):pos]):
            tok = m.group(0)
            if tok.endswith('{') and tok != '{':
                depth += 1
            elif tok == '}' and depth:
                depth -= 1
        nested += bool(depth)
    check(len(emph) == N_PLAIN and nested == 0, 'P3 all %d "In words" sentences are set italic (\\emph) in the '
          '.tex, none nested inside another italic group' % N_PLAIN, '%d emph, %d nested' % (len(emph), nested))

    # ---- L. labels and tags ----------------------------------------------------------------
    md_plain = re.sub(r'\*', '', md_flat)
    def count(pat, text):
        return len(re.findall(pat, text))
    LABELS = [('Proof', r'\bProof\b'),
              ('[read (read-status)', r'\[read'),
              ('[via (read-status)', r'\[via')]        # B42 added a dagger row and a 'not read' row; both dropped in B46 (20 Sep 2026): no unread work remains;
                                                       # the [Inference] and [Speculation] rows dropped in B47 (20 Sep 2026): the tags became ordinary hedges;
                                                       # the three Proved rows and the Read / cited via / not opened rows dropped in B50 Revision 1 (20 Sep 2026)
    check('Proved' not in md_plain, 'L0 no Proved label remains (B50 item 1: every statement has Proof or a hypothesis in its head)')
    # a table that breaks across pages repeats its header row on every page (xltabular);
    # a tag inside a header row is therefore counted once more per extra page
    header_rows = []
    intab = False
    for line in md.split('\n'):
        if line.startswith('|') and not intab:
            header_rows.append(re.sub(r'[*`]', '', line).replace('\\|', '|'))
        intab = line.startswith('|')
    repeats = [(h, pdf_sq.count(squash(h)) - 1) for h in header_rows]
    for name, pat in LABELS:
        a, b = count(pat, md_plain), count(pat, pdf_flat)
        extra = sum(r * count(pat, h) for h, r in repeats)
        check(a + extra == b and a > 0, 'L  %-22s %3d in the markdown, %3d in the PDF%s'
              % (name, a, b, (' (%d in repeated table headers)' % extra) if extra else ''))

    # ---- D. displays -----------------------------------------------------------------------
    disp, buf = [], []
    for line in md.split('\n'):
        if line.startswith('    '):
            buf.append(line.strip())
        elif buf:
            disp.append(' '.join(buf))
            buf = []
    badd = [d[:50] for d in disp if not all(w in pdf_sq for w in words(d))]
    check(len(disp) == N_DISP and not badd, 'D  all %d displayed formulas survive word by word'
          % len(disp), 'missing: %s' % badd)

    # ---- G. code spans ---------------------------------------------------------------------
    spans = sorted(set(re.findall(r'`([^`]+)`', md)))
    badg = [s for s in spans if squash(s) not in pdf_sq]
    check(not badg, 'G  all %d distinct code-span file names appear' % len(spans), str(badg))

    # ---- X. the figure ---------------------------------------------------------------------
    nfig_tex = tex.count('\\begin{figure}')
    ok_env = (len(figs) == 1 and nfig_tex == 1 and tex.count('\\begin{tikzpicture}') == 1
              and figs[0].strip() in tex and re.search(r'\\begin\{figure\}\[t\]\n\\centering\n.*?\\caption\{.*?\}\n\\end\{figure\}', tex, re.S) is not None)
    check(ok_env, 'X1 one tex-figure block in the markdown, typeset verbatim as one figure environment with one tikzpicture and a caption',
          '%d blocks, %d figure envs' % (len(figs), nfig_tex))
    labels = ['NP', 'BPP', 'BEM', 'no io-OWF', 'Thm 3(b)', 'Thm 3(c), by (a)', 'Question 1', 'no relativizing proof (Prop. 10, conditional)']   # second arrow relabelled by Referee E (b1), B50 Phase 3
    badx = [l for l in labels if squash(l) not in pdf_sq]
    capm = re.search(r'^\*Figure 1\. (.+?)\* (\*In words: .+\*)$', md, re.M)
    cap_ok = capm is not None and squash('Figure 1: ' + capm.group(1)) in pdf_sq and squash(capm.group(2)) in pdf_sq
    check(not badx and cap_ok, 'X2 the figure\'s node labels, its caption ("Figure 1: ...") and its "In words" sentence appear in the PDF',
          'missing labels %s; caption %s' % (badx, cap_ok))

    # ---- I. every paragraph, whole ---------------------------------------------------------
    pagenumless = []
    for page in pdf.split('\f'):
        plines = page.rstrip().split('\n')
        while plines and not plines[-1].strip():
            plines.pop()
        if plines and plines[-1].strip().isdigit():
            plines.pop()
        pagenumless.append('\n'.join(plines))
    body_sq = squash('\n'.join(pagenumless))
    paras, buf = [], []
    for line in md.split('\n'):
        if not line.strip() or line.startswith(('#', '|', '    ')) or line.strip() == '---':
            if buf:
                paras.append(' '.join(buf))
                buf = []
            continue
        if line.startswith('- ') or re.match(r'^\d+\. ', line):
            if buf:
                paras.append(' '.join(buf))
            buf = [re.sub(r'^(- |\d+\. )', '', line).strip()]
            continue
        buf.append(line.strip())
    if buf:
        paras.append(' '.join(buf))
    # the header line under the title ("<name>, <e-mail>. Version of <date>.") is typeset as the title block
    # with the e-mail as a first-page footnote and the date without "Version of" (owner, 20 Sep 2026, B50 Phase 3),
    # so it is checked as three parts on page 1 and not as one paragraph
    hm = re.match(r'^(.+?), (\S+@\S+)\. Version of (.+?)\.$', paras[0])
    check(hm is not None, 'H  the header line has the form "<name>, <e-mail>. Version of <date>."', paras[0][:60])
    page1 = squash(pagenumless[0])
    hok = hm is not None and all(squash(x) in page1 for x in hm.groups())
    check(hok, 'H2 the name, the e-mail (as the first-page footnote) and the plain date of the header line are on page 1 of the PDF',
          'page 1 lacks: %s' % ([x for x in (hm.groups() if hm else ()) if squash(x) not in page1]))
    paras = paras[1:]
    badi, split_p = [], 0
    for para in paras:
        p = re.sub(r'[*`]', '', para).replace('\\|', '|')
        if squash(p) in body_sq:
            continue
        if all(w in body_sq for w in words(p)):
            split_p += 1
        else:
            badi.append(para[:70])
    check(not badi, 'I  all %d markdown paragraphs and list items appear in the PDF, whole and in '
                    'one piece (%d matched word by word past a stacked sub/superscript)'
          % (len(paras), split_p), 'missing: %s' % badi[:8])

    # ---- Z. the build log ------------------------------------------------------------------
    log = open(LOG, encoding='utf-8', errors='replace').read()
    over = [float(x) for x in re.findall(r'Overfull \\hbox \(([\d.]+)pt too wide', log)]
    check(not [x for x in over if x > 10], 'Z1 no overfull box wider than 10pt in the build log '
          '(%d overfull boxes in all)' % len(over), str(over))
    check('Missing character' not in log, 'Z2 no "Missing character" warning (no glyph dropped)')
    m = re.search(r'Output written on .*? \((\d+) pages', log)
    notes.append('INFO  pages: %s' % (m.group(1) if m else '?'))

    for line in notes:
        print(line)
    for line in fails:
        print(line)
    print('\n%d checks passed, %d failed.' % (len([n for n in notes if n.startswith('PASS')]),
                                              len(fails)))
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
