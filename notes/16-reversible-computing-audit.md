# Research 16: audit of the three reversible-computing citations for the interpretation section

Ticket: `.scratch/owf-entropy-paper/issues/16-interpretation-section.md`, owner addendum (billiard-ball chain). Written 2026-09-13.
Purpose: the owner's addendum cites Fredkin–Toffoli 1982, Bennett 1973 and Landauer 1961 from memory and says "audit before drafting". All three were obtained and read (text extracted with pdftotext; PDFs and text in `pass16/sources/`). Verdict: all three claims in the addendum are supported by the papers as read, with one wording correction (Landauer's number) and two useful extras.

## Sources

| paper | file | read-status |
|---|---|---|
| Bennett, C. H. (1973). Logical reversibility of computation. IBM J. Res. Dev. 17(6):525–532. | `sources/bennett1973_logical_reversibility.pdf/.txt` (8 pp.) | **Read**: abstract, Introduction (p. 525), opening of "Logically reversible Turing machines" (p. 526); construction section skimmed |
| Fredkin, E., Toffoli, T. (1982). Conservative logic. Int. J. Theor. Phys. 21(3/4):219–253. | `sources/fredkin_toffoli1982_conservative_logic.pdf/.txt` (Princeton course copy) | **Read**: abstract, §4, §6 opening and §6.1, §7 opening, §8, §10; §§2–3, 5, 6.2–6.4, 9 text-searched. Volume and page range from the Semantic Scholar record, not from the copy's page headers |
| Landauer, R. (1961). Irreversibility and heat generation in the computing process. IBM J. Res. Dev. 5(3):183–191. | `sources/landauer1961_irreversibility.pdf/.txt` (9 pp.) | **Read**: abstract, §1 (p. 183), §3 end and §4 (pp. 186–187); §5 (bistable well) skimmed |

## What each paper says, checked against the addendum

**Addendum item 1: "A reversible physical system can compute anything: Fredkin–Toffoli 1982 (billiard-ball model)."** Supported. Abstract: the second model "is based on elastic collisions of identical 'balls'" and "Quite literally, the functional behavior of a general-purpose digital computer can be reproduced by a perfect gas placed in a suitably shaped container and given appropriate initial conditions." §6 opening: the model is "based on stylized but quite recognizable physical effects, namely, elastic collisions involving balls and fixed reflectors", and its rules "are identical to those that underlie the classical kinetic theory of perfect gases"; then "by giving the container a suitable shape ... and the balls suitable initial conditions ... one can carry out any specified computation." §4 gives universality of conservative logic via one-to-one replacement of AND/OR/NOT/FAN-OUT, and cites Bennett 1973 for universal reversible Turing machines.

**Addendum item 2: "Run the film backward and the balls undo the multiplication for free ... Reversible computing costs nothing in principle (Bennett 1973)."** Supported, with the exact mechanism. Bennett p. 525: "An irreversible computer can always be made reversible by having it save all the information it would otherwise throw away" on an extra history tape; the history tape "is not random" and can be erased reversibly by "carrying out the entire computation backward, eventually returning the history tape to its original blank condition", after first copying the output. Abstract: such machines dissipate "considerably less than kT of energy per logical step". Cost: "about twice as many steps" and possibly "a large amount of temporary storage" (p. 525).

**Addendum item 3: "erasing a bit costs at least kT ln 2 of heat: Landauer 1961."** Supported. §4, pp. 186–187: resetting an ensemble of bits to ONE cuts the number of states in half; "The entropy therefore has been reduced by k log_e 2 = 0.6931 k per bit"; this "must appear elsewhere as a heating effect, supplying 0.6931 kT per restored bit to the surroundings. This is, of course, a minimum heating effect". Bennett p. 525 restates it as "at least kT ln 2 of energy ... for each bit of information it erases or otherwise throws away", attributing it to Landauer.

**Addendum item 5: "Landauer's cost is per erased bit and is a lower bound on heat, not on time."** Supported in Landauer's own words. §1, p. 183: the arguments "show that there is a minimum heat generation, independent of the rate of the process". Fredkin–Toffoli §8 adds: "there is no necessary connection between the energy involved in a computation and its length or complexity."

## Two extras worth one sentence each in the paper

1. **Bennett on many-to-one maps (p. 525):** the reversible machine "must be allowed to save its input — otherwise it could not be reversible and still carry out computations in which the input was not uniquely determined by the output." This is the lost/hidden distinction in 1973 words: when the map is many-to-one the input must be kept (else it is lost); when it is one-to-one only the history need be kept (else it is hidden).
2. **Fredkin–Toffoli on hidden information as dissipation (§7):** energy may be dissipated "by our losing knowledge (and thus control) of a mechanical mode's current state, which in the course of a computation may end up depending on the initial conditions through such a complex relationship that we may not be willing or able to unravel it." That is a bounded-observer remark inside a physics paper; the paper may quote it as a parallel, never as a premise.

## Not audited here

Loschmidt 1876 and Zermelo 1896 remain cited from memory (handoff §8 audit list already carries them). Baker–Gill–Solovay 1975, Razborov–Rudich 1994, Aaronson–Wigderson 2008 remain cited from memory (handoff thread N4). Bennett 1982 ("The thermodynamics of computation — a review") was not obtained; the paper cites Bennett 1973 only.
