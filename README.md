
# Solar Challenge – Week 0
Welcome to the solar-challenge-week0 repository! 
This project is part of the 10Academy Week 0 challenge, focused on setting up a robust data science environment and performing exploratory data analysis (EDA) on solar datasets from three countries. The ultimate goal is to support MoonLight Energy Solutions in identifying high-potential regions for solar installation aligned with their sustainability goals.
---
##  Repository Setup & Environment Configuration
- Initialized GitHub repository: `solar-challenge-week0`
- Cloned locally and set up Python virtual environment using `venv`
- Created `.gitignore` to exclude:
  - `data/`
  - `.csv` files
- Added `requirements.txt` for dependency management
- Configured GitHub Actions CI workflow (`.github/workflows/ci.yml`) to:
  - Run `pip install -r requirements.txt`
  - Verify Python version
###  Folder Structure
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/
│   ├── init.py
│   └── README.md
├── tests/
│   ├── init.py
└── scripts/
├── init.py
└── README.md
## Exploratory Data Analysis (EDA)
Performed EDA on solar datasets from **Benin**, **Sierra Leone**, and **Togo**:
-  Summary statistics (`df.describe()`)
-  Missing value report (`df.isna().sum()`)
-  Outlier detection using Z-scores for GHI, DNI, DHI, ModA, ModB, WS, WSgust
-  Imputation of missing values using median
-  Time series plots for solar irradiance and temperature
-  Correlation heatmaps and scatter plots
-  Wind rose plots and histograms
-  Bubble charts for GHI vs. Tamb with RH/BP as bubble size
Cleaned datasets exported to `data/<country>_clean.csv` (excluded from Git).
## Cross-Country Comparison
Notebook: `compare_countries.ipynb`
-  Loaded cleaned data for all three countries
-  Boxplots for GHI, DNI, DHI across countries
-  Summary table of mean, median, and standard deviation
-  One-way ANOVA test on GHI values (p-value reported)
-  Bar chart ranking countries by average GHI
-  Key observations documented in markdown cells
## Contributions
- Set up Git & CI workflows
- Created and documented environment setup
- Performed EDA and data cleaning for three countries
- Conducted cross-country comparison and statistical testing
- Developed strategic insights for solar investment
---

## How to Reproduce the Environment
```bash
# Clone the repository
git clone https://github.com/gashawbekele06/solar-challenge-week0.git
cd solar-challenge-week0
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\\Scripts\\activate
# Install dependencies
pip install -r requirements.txt