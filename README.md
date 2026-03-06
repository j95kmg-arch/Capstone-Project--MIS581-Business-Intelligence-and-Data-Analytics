# Capstone-Project--MIS581-Business-Intelligence-and-Data-Analytics
Consumer Price Inflation and Homeowners Insurance Claim Frequency: A California Study
Project Overview
This repository contains the complete analysis code and documentation for a capstone research project examining the relationship between consumer price inflation and homeowners insurance claim frequency in California during 2021-2024. The study employs behavioral economics theory and synthetic data methodology to test whether macroeconomic conditions influence consumer insurance behavior.
Research Question
Primary Question: Does consumer price inflation significantly influence non-catastrophe homeowners insurance claim frequency in California?
Key Findings: Statistical analysis found no significant correlation between Consumer Price Index values and claim frequency across current and lagged time periods (r-values ranging from 0.000 to 0.216, all p > 0.05).
Methodology

Data Approach: Synthetic homeowners insurance claims data (10,000 policies, 2,134 claims)
Time Period: 48 months (January 2021 - December 2024)
Statistical Methods: Pearson correlation analysis with temporal lag testing (3, 6-month delays)
Software: R/RStudio for statistical analysis, Python for data generation

Repository Structure
├── code/
│   ├── synthetic_data_generation.py    # Python script for creating synthetic claims data
│   └── correlation_analysis.R          # R script for statistical testing and visualization
├── visualizations/
│   ├── cpi_claims_correlation.png      # Primary scatter plot results
│   └── lag_analysis_summary.png        # Summary table of lag tests
└── README.md                           # This file
Key Results
Test PeriodCorrelation (r)P-ValueStatistical SignificanceCurrent Month0.0000.935No3-Month Lag0.0970.525No6-Month Lag0.2160.169No

How to Reproduce This Analysis
Prerequisites

R/RStudio with packages: tidyverse, corrr, broom
Python 3.x with packages: pandas, numpy, datetime

Running the Analysis

Clone this repository
Run synthetic_data_generation.py to create the dataset
Execute correlation_analysis.R to perform statistical testing
View generated visualizations in /visualizations/ folder

Data Sources

Consumer Price Index: U.S. Bureau of Labor Statistics (CPI-U, 2021-2024)
Industry Baselines: Insurance Information Institute frequency standards
Template Structure: Kaggle Insurance Claims Dataset (Litvinenko, 2024)

Academic Context
This research addresses a significant gap in behavioral economics and insurance literature by providing the first systematic examination of inflation's impact on claim frequency patterns. The null findings contribute valuable evidence for insurance industry operational planning and actuarial model development.

Date: February 2026

## License
Academic research project - code available for educational and research purposes.
