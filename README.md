# AIPArchEval
Automates modular product compatibility using AutoML for real-time insights, reducing manual effort and speeding decisions. It streamlines manufacturing and enables agile, future-proof solutions.


## Table of Contents
1. [Overview](#overview)
2. [Repository Structure](#repository-structure)
3. [Compilation Instructions](#compilation-instructions)
4. [Figures](#figures)
5. [Key Packages Used](#key-packages-used)
6. [How to Cite](#how-to-cite)
7. [License](#license)

---

## Overview
This project aims to:
- **Automate** compatibility assessments for modular products using **AI** and **AutoML**.
- Provide a **user-friendly interface** so that non-technical stakeholders can easily predict and interpret compatibility scores.
- Highlight how **modular product architectures** can streamline manufacturing, reduce complexity, and adapt to evolving stakeholder requirements.

### Main Contributions
1. **Modular Product Architecture**: Demonstrates step-by-step modular decomposition, design-for-variety, and component grouping.
2. **AI / Machine Learning Integration**: 
   - Uses **AutoML** (through PyCaret) to select optimal regression models for predicting compatibility scores.
   - Illustrates how a user-friendly **Streamlit** interface can be deployed for real-time predictions.
3. **Framework & Evaluation**: 
   - Includes data preprocessing, model training, evaluation (using metrics like \( R^2 \) and RMSE), and result visualization.

---

## Repository Structure

```
.
├── figures/               # Folder containing all images/figures used in the thesis
│   ├── 1_product.jpeg
│   ├── 2_product.png
│   ├── 3_product.png
│   ├── 4_product.jpg
│   ├── 5_product.png
│   ├── flow.png
│   ├── matrix.png
│   ├── distribution.png
│   ├── error.png
│   ├── rvcef.png
│   ├── feature.png
│   ├── preprocessing.png
│   ├── morphological_box.png
│   ├── swot.png
│   ├── page_1.png
│   ├── page_2.png
│   ├── last.png
│   ...
├── references.bib         # BibTeX file containing all citations
├── main.tex               # Main LaTeX file (entry point)
├── README.md              # You are here!
└── ...
```

- **`main.tex`**: The main LaTeX file that compiles the entire document.
- **`figures/`**: A directory containing all image assets referenced in the LaTeX source.
- **`references.bib`**: A BibTeX file listing all references/citations used in the thesis.
- (Optional) **`autoML_script.py`** or **`inference_script.py`** if you plan to include code for PyCaret or Streamlit (not shown above, but you can add them for reference).

---

## Compilation Instructions

1. **Clone or Download** this repository.
2. **Install LaTeX** distribution (e.g., [TeX Live](https://www.tug.org/texlive/), [MikTeX](https://miktex.org/), etc.), ensuring you have the packages listed in [`main.tex`](#key-packages-used).
3. **Navigate** to the repository folder via terminal/command prompt.
4. **Compile** using your preferred method:
   ```bash
   pdflatex main.tex
   bibtex main
   pdflatex main.tex
   pdflatex main.tex
   ```
   - Alternatively, you can use an IDE like [TeXStudio](https://www.texstudio.org/) or [Overleaf](https://www.overleaf.com/).

After successful compilation, you should get a **`main.pdf`** containing the complete thesis (Title page, abstract, chapters, references, etc.).

---

## Figures

All figures referenced in the thesis are stored in the `figures/` folder. Below is a brief overview of their purpose:

1. **`1_product.jpeg`**  
   Illustrates the first step in modular product architecture (decomposing an existing product structure).

2. **`2_product.png`**  
   Shows the second step, analyzing components for modularization.

3. **`3_product.png`**  
   Depicts how modular product structures help reduce internal complexity and costs.

4. **`4_product.jpg`**  
   Example of a robotic arm’s technical specifications (actuators, sensors, etc.).

5. **`5_product.png`**  
   Illustrates the grouping of components into new modules as part of the modularization process.

6. **`flow.png`**  
   A flowchart of the AI pipeline for compatibility prediction using AutoML.

7. **`matrix.png`**  
   The feature correlation matrix visualizing how features in the dataset correlate with each other.

8. **`distribution.png`**  
   Distribution of the target variable (Compatibility Score).

9. **`error.png`**  
   Prediction error plot for linear regression, comparing actual vs. predicted values.

10. **`rvcef.png`**  
    The Recursive Feature Elimination with Cross-Validation (RFECV) plot for linear regression.

11. **`feature.png`**  
    Feature importance bar chart, showing which features have the highest impact on the model.

12. **`preprocessing.png`**  
    Summarizes the data preprocessing steps (normalization, cleaning, etc.).

13. **`morphological_box.png`**  
    Morphological box example for parameterizing modular components.

14. **`swot.png`**  
    SWOT analysis diagram, outlining Strengths, Weaknesses, Opportunities, and Threats.

15. **`page_1.png`** / **`page_2.png`**  
    Screenshots of the user-friendly Streamlit interface.

16. **`last.png`**  
    Shows the final modular product structure after implementing the steps of modularization.

If you add new figures, place them in `figures/` and reference them in the LaTeX code similarly:
```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=1\textwidth]{figures/new_figure.png}
  \caption{Brief description of the new figure.}
  \label{fig:new_figure}
\end{figure}
```

---

## Key Packages Used

- **`babel`** and **`inputenc`**: For language support and encoding (UTF-8).
- **`T1` and `lmodern`**: For improved font encoding.
- **`graphicx`**: For handling images (`\includegraphics`).
- **`amsmath`**: Mathematical typesetting.
- **`hyperref`**: Clickable links for references.
- **`natbib`**: Bibliography and citation handling.
- **`glossaries`**: Abbreviation and glossary management.
- **`booktabs`**: Enhanced table formatting.
- **`abstract`**: Customizable abstract environment.
- **`tabularx`, `array`, `multirow`**: Improved table layouts.
- **`scrbook`**: KOMA-Script book class with flexible formatting.

Ensure these packages are installed in your LaTeX environment before compiling.

---

## How to Cite

If you use or reference this work in any way, please cite it as follows (example in BibTeX format):

```bibtex
@misc{saad2023ai,
  title        = {AI-Enhanced Evaluation of Products Architecture: A Study in Industrial Engineering at TRUMPF},
  author       = {Saad, Nada},
  howpublished = {Bachelor Thesis, German Jordanian University, 2023},
  note         = {Available at your repository or link here if public.}
}
```

---

## License

This work is provided for educational and research purposes. Please see [LICENSE](LICENSE) (if included in your repository) for details on permissions and restrictions.

**Enjoy using this thesis repository, and feel free to contribute or raise issues for improvements!**
```
