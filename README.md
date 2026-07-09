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




## License

This repository is licensed under the following terms:

- **Code:** [MIT License](https://opensource.org/licenses/MIT)
- **Manuscript and Figures:** [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
