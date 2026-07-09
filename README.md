# Retained History and Leakage in Nonequilibrium Systems

This repository contains the manuscript source, generated figure, and minimal reproduction script for:

**Retained History and Leakage in Nonequilibrium Systems:  
A Four-Channel Audit Framework for Phase-Amplitude Correspondence**

Author: Yoshida  
Date: July 9, 2026

## Overview

This manuscript proposes a four-channel audit framework for systems in which observable structure may depend on:

- phase `phi`
- coherent amplitude `A`
- retained history `Gamma`
- leakage or exported history `J_out`

The paper is a correspondence and audit framework, not a replacement for established physical, chemical, thermodynamic, quantum, or biological theories.  Its main purpose is to clarify when a candidate retained-history coordinate should be treated as a testable variable rather than as a metaphor.

## Repository Contents

```text
.
├── README.md
├── retained_history_leakage_four_channel_audit_framework.tex
├── retained_history_leakage_four_channel_audit_framework.pdf
├── outputs/
│   ├── retained_history_leakage_audit_demo.png
│   └── retained_history_leakage_audit_demo.json
└── scripts/
    └── retained_history_leakage_audit_demo.py
```

## Build Requirements

The manuscript was compiled with `pdflatex` via `latexmk`.

Required LaTeX packages:

- `geometry`
- `amsmath`
- `amssymb`
- `amsthm`
- `bm`
- `graphicx`
- `array`
- `booktabs`
- `caption`
- `hyperref`

The figure-generation script requires Python with:

- `numpy`
- `matplotlib`

## Reproducing the Figure

From this directory, run:

```bash
python3 scripts/retained_history_leakage_audit_demo.py
```

This regenerates:

```text
outputs/retained_history_leakage_audit_demo.png
outputs/retained_history_leakage_audit_demo.json
```

The numerical model is dimensionless and methodological.  It illustrates the sign reversal between target-side leakage and observer-side data gain; it is not proposed as a universal microscopic measurement theory.

## Compiling the Manuscript

From this directory, run:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error retained_history_leakage_four_channel_audit_framework.tex
```

The expected output is:

```text
retained_history_leakage_four_channel_audit_framework.pdf
```

The current source has no external `\input{...}` dependency.  The only required figure file is:

```text
outputs/retained_history_leakage_audit_demo.png
```

## Recommended GitHub and Zenodo Workflow

Use GitHub for the live source and Zenodo for DOI-backed archival releases.

Recommended workflow:

1. Create a GitHub repository.
2. Add the manuscript source, PDF, figure, script, and this README.
3. Create a GitHub release, for example `v1.0.0`.
4. Enable Zenodo integration for the GitHub repository.
5. Let Zenodo archive the release and mint a DOI.
6. If desired, add the Zenodo DOI badge/link to this README and future manuscript versions.

Avoid uploading unrelated working files, editor previews, or temporary LaTeX build products as part of the archived release.

## Suggested Release Files

For a clean first release, include:

```text
README.md
retained_history_leakage_four_channel_audit_framework.tex
retained_history_leakage_four_channel_audit_framework.pdf
outputs/retained_history_leakage_audit_demo.png
outputs/retained_history_leakage_audit_demo.json
scripts/retained_history_leakage_audit_demo.py
```

Do not include temporary build files such as:

```text
*.aux
*.fdb_latexmk
*.fls
*.log
*.out
*.synctex
```

## Citation

A formal DOI citation should be added after the Zenodo release is created.

Temporary citation format:

```text
Yoshida. Retained History and Leakage in Nonequilibrium Systems:
A Four-Channel Audit Framework for Phase-Amplitude Correspondence.
Version 1.0.0, 2026.
```

## License

No license has been specified yet.  Before public release, choose a license appropriate for the manuscript and code.  Common choices are:

- CC BY 4.0 for manuscript text and figures
- MIT, BSD-3-Clause, or Apache-2.0 for code

If no license is added, reuse rights may be ambiguous even if the repository is public.