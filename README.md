# One-way functions are computational entropy production

One-way functions exist if and only if some efficiently samplable process produces more than logarithmic computational entropy on average, for infinitely many input lengths. We make this precise. For a polynomial-time samplable distribution D on pairs (x, y), the computational entropy production of a pair is σ = log D(x, y) + pK^t(y) + pK^t(x | y), where pK^t is the probabilistic time-bounded Kolmogorov complexity as defined by Hirahara, Ilango, Lu, Nanashima and Oliveira (2023, HILNO below) following Goldberg, Kabanets, Lu and Oliveira (2022): the log-probability the process assigns to the pair, against the length of a bounded observer's shortest fast description of it, output first, then input given output. We prove unconditionally that E_D[2^{−σ}] lies between an inverse polynomial and a polynomial in n and that E_D[σ] ≥ −O(log n): a time-bounded fluctuation inequality and a computational second law. We show that, up to a polynomial and outside a 1/n slice of outputs, σ is small on a pair exactly when an efficient sampler, given the output, recovers the input with about the right odds, HILNO's universal sampler serving as the witness: dissipation, in this sense, is the hardness of running the process backward. The equivalence in the first sentence is HILNO's duality restated in these terms, for infinitely-often one-way functions. For the antisymmetric Zurek defect, one-way functions force superpolynomial exponential moments, and bounded moments sit between NP ⊆ BPP and the non-existence of one-way functions; whether the lower arrow reverses is left open, with a conditional relativization barrier on that arrow and oracle evidence on the other. Physics is the frame, not the subject.

**Status:** prepared for submission to ECCC; the submission date and the report number
(TR26-xxx) will be filled in here when known.

**Author:** Casey Thornton, independent researcher — caseythornton@utexas.edu

## What is here

- `paper/` — the paper: `ENTROPY_PRODUCTION.md` (the source of record), the generated
  `ENTROPY_PRODUCTION.tex`, the built `ENTROPY_PRODUCTION.pdf`, the converter
  `md_to_tex_paper.py`, the verifier `verify_tex_paper.py`, the span dictionary
  `typeset_notes_paper.md`, and `COVER_ABSTRACT.md` (the short abstract).
- `referees/` — four blind referee reports on disjoint parts of the paper, run before submission;
  see `referees/README.md`.
- `notes/` — `READ_STATUS.md`, the full reading record for every work the paper cites (the paper's
  reference list carries one short bracket per entry and points here), and the eleven reading notes
  that record cites by file name.
- `checks/` — three small exhaustive computations from the paper's research phase; none of them
  feeds a number in the paper. See `checks/README.md`.

## Rebuilding the PDF

Needs Python 3.11+ (standard library only), [tectonic](https://tectonic-typesetting.github.io)
and poppler's `pdftotext`.

    python paper/md_to_tex_paper.py            # ENTROPY_PRODUCTION.md -> ENTROPY_PRODUCTION.tex
    tectonic --keep-logs paper/ENTROPY_PRODUCTION.tex
    python paper/verify_tex_paper.py           # checks the PDF lost nothing from the markdown

The verifier reads the build log that `--keep-logs` leaves next to the .tex, and exits 0 only
if every check passes.

## Sources

The papers consulted are not included, for copyright reasons. The paper's reference list names,
for every entry, the part of it that was read.

## How the paper was written

The paper was written with an AI system (Claude, Anthropic) as a research collaborator, as its
acknowledgement says. The judgement, the claims and the mistakes are the author's.

## Licences

- The paper (`paper/ENTROPY_PRODUCTION.md`, `.tex`, `.pdf`, `COVER_ABSTRACT.md`), the referee
  reports and the reading notes: [CC BY 4.0](LICENSE-PAPER).
- The scripts (`paper/*.py`, `checks/*.py`) and their JSON outputs: [MIT](LICENSE-CODE).
