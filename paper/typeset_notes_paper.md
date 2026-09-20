# Typesetting the draft paper in LaTeX — decisions and verification

15 September 2026. Typesetting only. `ENTROPY_PRODUCTION.md` (871 lines, sha256 `dae17113…`) was
**not edited**: no wording, number, label, tag or citation was changed. The recipe is the one that
produced `pass17/Thornton_ERCA_note.pdf`; where this paper differs from the note, the difference and
the decision are recorded below.

New files:

| file | what it is |
|---|---|
| `md_to_tex_paper.py` | markdown → LaTeX; the three fragment dictionaries and the display dictionary live here |
| `ENTROPY_PRODUCTION.tex` | generated, pure ASCII, do not hand-edit |
| `ENTROPY_PRODUCTION.pdf` | **40 pages**, the deliverable |
| `ENTROPY_PRODUCTION.log` | tectonic build log (the evidence for zero overfull boxes and zero missing characters) |
| `verify_tex_paper.py` | checks the PDF against the markdown; 28 checks, all pass |
| `typeset_notes_paper.md` | this file |

Build: `.venv/bin/python md_to_tex_paper.py && tectonic --keep-logs ENTROPY_PRODUCTION.tex`
(tectonic 0.17.0; a few seconds once the packages are cached).
Check: `.venv/bin/python verify_tex_paper.py` — exit 0 iff every check passes.

## 1. What the brief expected and what the file contains

The brief was written from the ERCA recipe and three of its estimates do not describe this file.

- **"Classify every code span … expect several hundred."** The file has **33 backtick spans, 32
  distinct, all of them file names in the reference list** (`sources/…pdf`, `HANDOFF.md`,
  `passes/…md`). The paper writes its mathematics as Unicode text in the prose — `pK^t(x | y)`,
  `σ^rev_D`, `2^{−pK^t(y)}`, `E_D[2^{−σ}] = Σ_{supp D} m_R` — with no delimiters at all. So the
  object classified by hand is the *fragment*, not the span: every run of mathematics in the prose is
  an entry of an explicit dictionary, and the "several hundred" is **524 fragment keys** (462
  mathematics, 27 mixed prose-and-mathematics, 35 prose that only looks mathematical), plus the 32
  code spans and the 52 displays. Section 2 says how the dictionary is made safe.
- **"The two tables in §8.4 and the appendix."** There are **four** tables: the Crooks-setup table in
  §2.6 (3 columns), the five-slot table in §8.4 (3 columns), and the two appendix tables A.1
  (5 columns, 17 rows) and A.2 (5 columns, 13 rows). All four get the same treatment.
- **"Section numbers 1–9."** The file has eight numbered sections, 1 to 8, then the Appendix and the
  References. Nothing was renumbered; `verify_tex_paper.py` check F3 asserts the numbered sections
  are exactly 1–8.

One more thing outside the file: `MANIFEST.md` still lists `ENTROPY_PRODUCTION.md` at 136,767 B; the
file has been 138,217 B since the E51 edit. Corrected in this pass's MANIFEST update.

## 2. The fragment dictionaries

Without delimiters a dictionary alone is a lookup with silent misses, so the safety comes from two
checks that run on every build:

1. **Longest-first matching at word boundaries.** The 524 keys are matched against each paragraph,
   table cell, heading and list item, longest key first, and only where the character before and
   after is not a letter, digit or apostrophe (so `s` is not taken out of "sampler's", and `E` is
   not taken out of "E27"). Author initials in the reference list and page references ("p. 391",
   "pp. 17–18") are set aside as prose before matching.
2. **The leftover check.** After matching, whatever is left in the prose is scanned for anything
   mathematical: any of the 58 non-ASCII mathematical characters (`^ _ { } | ~ < >`, every Greek
   letter, `≤ ≥ ≠ ∈ ⊆ ⊄ ⇒ ⇔ ⇏ − · ± × ⟨ ⟩ ⌈ ⌉ ∖ ⊥ ∞ ′ ² ⁺ ⁻ ₁`), any lone variable letter (every
   single letter except a, A, I), any function application `f(`, any digit–letter join (`2q`,
   `n2`), any bare fraction `2/3`, and any complexity-class or operator word (`NP`, `BPP`, `supp`,
   `poly`, …). Every hit is collected with thirty characters of context on each side and the build
   fails, listing all of them at once. **Nothing is guessed: a fragment the dictionary does not
   know cannot reach the PDF as prose.**

A third check, as in the ERCA script, fails the build on any dictionary entry that is never used, so
the dictionary cannot silently drift away from the file. A fourth asserts that exactly 32
theorem-like environments were opened (4 theorems, 10 lemmas, 6 propositions, 8 definitions, 4
remarks) — a misplaced environment boundary is invisible to every text-based check, because the words
are all still there.

The dictionary was built by iterating on the leftover report until it was empty (about a dozen rounds),
then reading every one of the 524 entries once. That reading caught the things the mechanical checks
cannot: a key that had swallowed the first word of the next sentence (`i_max(n) = … . F`), item labels
inside mathematics (`(b) BEM ⇒ BEM_skew` is `(b)` in prose and `BEM ⇒ BEM_skew` in mathematics),
bare `log`, `ln`, `good`, `bad` matched where the note uses them as English words ("a few log bits",
"a bad pair"), and `Σ` set as the letter where the note means a sum.

**Conventions inside the mathematics.** Notation is preserved, not modernised, as for the note:

- `pK^t` → `\mathrm{pK}^t` (HILNO's own typography); `E` → `\mathrm{E}` and `Pr` → `\Pr`, both
  upright (`\mathbb{E}` was avoided because `pdftotext` mangles blackboard bold, which would have
  blinded the verification);
- complexity classes upright: `NP`, `BPP`, `DistNP`, `AvgBPP`, `HeurP`, `HeurBPP`, `AvgP`, `UP`,
  `coUP`, `BPTIME`, `AvgSIZE`, `DistPH`, `BEM`, `BEM_skew`, `USamp`, `PA`, `SAT`; the class `P` in
  `P ≠ NP`, `P = NP`, `BPP ⊇ P`, "the P of HeurP", "P vs NP", "P versus NP" is upright, while the
  polynomial `P` of Definition 8 and Proposition 2 and the set `P` of Proposition 4 stay italic — a
  hand decision for every occurrence, since the file uses one letter for three things;
- `σ^rev_D` → `\sigma^{\mathrm{rev}}_D`, `σ^fwd_D` likewise; `Σ⁺_{s,P}` is the letter
  `\Sigma^{+}_{s,P}` (an object), every other `Σ` is `\sum` (an operator);
- the conditional bar `x | y` → `x \mid y`; `|x|`, `|M_t|`, `|f^{−1}(y)|` stay absolute values;
- slash fractions stay slashes (`3(n + d)/2`, `μ² 2^n / (2^{O(1)} t)`), bracket indexing stays
  bracket indexing, and no summation index or `\frac` is invented anywhere;
- `1_S`, `1_G` → `\mathbf{1}_S`, `\mathbf{1}_G`; `#{…}` → `\#\{…\}`; `⇏_rel` → `\nRightarrow_{\mathrm{rel}}`;
  `⇒?` in the sharpened question stays the two characters `\Rightarrow ?`;
- words inside mathematics (`no io-OWF`, `Q prints y`, `touch (z, w)`, `some program of length ≤ k`)
  are `\text{}`; bare `io-OWF` in prose is left as prose;
- `∎` → `$\blacksquare$` (the filled square the file uses), not amsthm's open box.

**Code spans** → `\texttt{}` with a breakpoint after every `/` and `_` and an empty group after every
hyphen (the `--` ligature defect found in the ERCA build cannot recur, though this file has no
command-line flags).

## 3. Displays, environments, tables, sections

**Displays.** The 56 four-space-indented lines form **52 displays**, each a hand-written entry of the
`DISPLAY` dictionary keyed by its exact source text; an unknown display is a hard error. Two-line
displays (Definition 5, Lemma 7, Lemma 9(iii), Definition 8) are `aligned`/`gathered`; the three long
chains (§1's route, §7.1's refined sandwich, §7.5's divide) are `gathered` and break at the source's
comma; the tags `(H1)`, `(E1)`, `(E2)` stay inline text where the source puts them, not `\tag`.

**Theorem-like environments.** amsthm, with the file's own numbers: `\newtheorem{innertheorem}` plus
an outer environment that sets the number by hand, so Theorem 0 stays 0 and nothing is renumbered.
All five kinds use `\theoremstyle{definition}` (bold head, **upright body**): with the plain style's
italic body the plain readings inside a theorem would have flipped to upright under `\emph`, and the
brief asks that every plain reading stay in italics. The `proof` environment is **not** used — it
prints "Proof." and an automatic box, which would change the verbatim labels — so **Proved**,
**Proved-conditional**, **Proved; known**, **Proof of Theorem 2, (1) ⇒ (2)** are bold paragraphs
exactly as in the file, with the file's own `∎`. Statement extent: an environment runs from its bold
head to the first block that is bold-led, a heading, a table or a non-continuation paragraph;
continuations are displays, plain readings, the (a)/(b)/(c)/(i)/(ii)/(iii)/(1)/(2) items, and the
six sentences that complete a statement after its plain reading ("and the same for D_2", "and
likewise, with Lemma 2 …", "where c_0 is …", "and consequently", "Equivalently: …", "and (ii)
GKLO22's remark …"). All 32 extents were printed and read once. The **Open Problem** and the
**Sharpened question** are not in the brief's list and stay bold paragraphs.

**Tables.** Four, all `xltabular` (tabularx that breaks across pages — A.1 runs to three pages and
A.2 to two; `tabularx` alone cannot break) with `booktabs`, hand-written `\hsize` weights, exactly
`\textwidth` wide; the two appendix tables in `\footnotesize` with 3pt column separation, the other
two in `\small`; `\addlinespace` between rows; the header row repeats on every page a table runs
to. A cell that begins with `[` is guarded with `{}` so `\\[` is never read as a vertical skip.
Nothing is rotated or landscaped.

**Sections.** Hand-written numbers (`\section*{2.1 …}`), as for the note, so nothing shifts;
Conventions, Abstract and References are `\section*` too (not the `abstract` environment), so every
heading is verbatim. The `---` rules between sections are dropped (the section headings carry the
separation). The H1 is the title; author Casey Thornton; date 15 September 2026; the "DRAFT. Not for
circulation." line and "Written 2026-09-12 to 2026-09-14, pass 16." — one markdown paragraph — are
the unnumbered opening block, `\small`, under the title. §8.3's numbered list keeps its labels
`1.`–`5.` explicitly.

## 4. Characters

As for the note, every non-ASCII character is mapped to a macro and the emitted `.tex` is asserted
pure ASCII (XeTeX drops an unmapped glyph in text mode silently). The 58 distinct non-ASCII
characters of the file are all either inside a fragment key (and hence converted by that key's
hand-written value) or one of the prose characters `§ – — … ∎ á é í ü ö`. Straight `"` pairs become
TeX quotes with a loud failure on an odd count; `%`, `&`, `#`, `_`, `{`, `}`, `<`, `>` in prose are
escaped. `\emergencystretch` is 4em (2em left one inline formula 10.3pt overfull; at 4em the line
breaks inside it).

## 5. Verification

`verify_tex_paper.py` extracts the PDF with `pdftotext -raw` — content-stream order, which keeps
every table cell in one piece; `-layout`, which the ERCA script used, interleaves neighbouring cells
line by line and split two "cited from memory" tags across a column boundary — folds ligatures,
superscript digits, dashes and quotes on both sides, and runs 28 checks. **All 28 pass; exit 0.**

| check | result |
|---|---|
| A: every distinct numeric token of the markdown (221) appears | pass |
| B/B2: every non-empty cell of the 4 tables (193) appears | pass (8 wrapped cells matched word by word) |
| F/F2/F3: all 38 headings verbatim, in order; numbered sections are 1–8 | pass |
| T1–T3: 32 statements parsed (4/10/6/8/4), theorems numbered 0–3, every head (kind, number, title) and the first clause of its statement present | pass (the clause is cut at the first `. : , ;`, so for a head that stands alone, such as Theorem 3, it is the opening of item (a)) |
| P1–P3: 62 italic plain readings in the markdown (61 after formulas or tables + the Conventions mention), all present in the PDF, and all 62 are `\emph` groups in the `.tex` with none nested inside another italic group | pass |
| L: Proved 24, Proved-conditional 4, Proved; known 1, Proof 5, [Inference] 11, [Speculation] 1, [Unverified] 1, Read 131, cited via 33, cited from memory 22, not opened 14 — markdown = PDF | pass (Read is 133 in the PDF: 2 in the repeated A.1 header row, counted) |
| D: all 52 displays survive word by word | pass |
| G: all 32 code-span file names appear | pass |
| I: all 329 markdown paragraphs and list items appear whole and in one piece | pass (23 matched word by word past a stacked sub/superscript) |
| Z1/Z2: build log has no overfull box over 10pt (0 in all), no missing character | pass |

Check I is the strongest, as for the note: an alphanumerics-only collapse makes the ASCII source and
the typeset mathematics the same string (`pK^t(x | y)` and `pK^t(x \mid y)` both become `pktxy`), so a
paragraph that survives it survived typesetting word for word, mathematics included.

Build log: **0 overfull boxes, 0 "Missing character" warnings**, four underfull `\hbox`es of badness
1033–3009 (one at the inline formula above, three in the reference list where a long typewriter file
name leaves loose interword space). All 34 fonts embedded and subsetted (`pdffonts`: `emb yes` on
every row); the PDF metadata carries the title and "Casey Thornton" (`pdfusetitle`).

## 6. Things that looked wrong while typesetting — reported, not fixed

Nothing in the mathematics or the text looked wrong. Two small things a reader may stumble on, both the
author's call:

- **The Ebtekar–Hutter citation.** §1 cites "[Ebtekar and Hutter 2024, Lemma 5, Theorem 7 and
  eq. (44), Read]"; the reference entry lists the parts read as "§IV C–D, Appendix B Lemma 5,
  Theorems 6–7" and does not name eq. (44). Consistent, but the entry does not say where eq. (44)
  was read.
- **Two labels defined and never used.** The Conventions define five labels; **[Speculation]** and
  **[Unverified]** occur nowhere else in the paper (the counts above are 1 each, both in the
  Conventions). That is a fact about the paper's claims, not an error, and it is recorded so nobody
  reads the two labels as missing.

The three mis-estimates in the brief (spans, tables, section count) and the stale MANIFEST size are in
Section 1.
