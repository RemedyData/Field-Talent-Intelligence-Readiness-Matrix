# Field-Talent Intelligence & Readiness Matrix

[![Data Pipeline Status](https://img.shields.io/badge/Data%20Pipeline-Active-success)](https://github.com/RemedyData/Field-Talent-Intelligence)
[![Dashboard](https://img.shields.io/badge/Dashboard-Google%20Sheets-blue)](https://docs.google.com/spreadsheets/d/1dIy3P4KT0GkA1xi1TS58vA7nSJWTJvIB06Zg4f_ysJc/edit?usp=sharing)
[![Python](https://img.shields.io/badge/Python-3.9+-yellow)](https://www.python.org/)


> *"Your data is either an asset or a risk; there is no in-between."*

## Project Overview

This project is a strategic data analytics pipeline designed to map regional technical talent (Field Data Engineers, Site Surveyors, Community Leads) against specific subnational energy and mining markets. It was conceptualized to support the operations of organizations like **Prime Frontier Group** and the **AREIS platform**, ensuring that HR and People Operations can proactively forecast time-to-hire and talent pool availability across targeted African regions.

While the foundation of this project utilizes software engineering (Python scripting, data scraping), its primary objective is **analytical**: transforming fragmented, unstructured talent data into clean, actionable intelligence for executive HR decision-making.

## Strategic Value Add

*   **Predictive HR Intelligence:** Shifts recruitment from a reactive process to a proactive strategy by forecasting regional talent availability before project deployment.
*   **Subnational Focus:** Aligns with platforms requiring ground-truth measurements by scoring talent density in specific zones (e.g., Kano, Accra, Copperbelt) rather than relying on skewed national averages.
*   **Seamless Workflow Integration:** The data output is strictly formatted to integrate seamlessly into existing People Operations tech stacks, including Google Sheets, Airtable, and Notion, reducing manual HR workload.

## Architecture & Data Flow

The architecture prioritizes analytical structuring to ensure the data is instantly usable for visualization and reporting.

1.  **Data Extraction (Python):** Simulates the extraction of technical talent profiles from professional networks and regional job boards.
2.  **Data Cleaning & Aggregation (Pandas):** Processes raw candidate records, normalizing skill matrices (e.g., QField, KoboToolbox, Solar PV Sizing) and aggregating key metrics like `Avg_Days_to_Available` and `Talent_Pool_Size`.
3.  **Visualization (Spreadsheet Dashboard):** Outputs structured CSVs that power an automated, color-coded readiness matrix, instantly highlighting talent surpluses and shortages.

## Getting Started

### Prerequisites
*   Python 3.9+
*   `pandas`

### Installation & Execution

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/RemedyData/Field-Talent-Intelligence.git](https://github.com/RemedyData/Field-Talent-Intelligence.git)
    cd field-talent-intelligence
    ```

2.  **Install dependencies:**
    ```bash
    pip install pandas
    ```

3.  **Run the data pipeline:**
    ```bash
    python scraper.py
    ```
    *This will generate two structured datasets: `PFG_Raw_Talent_Pool.csv` (granular data) and `PFG_Strategic_Readiness.csv` (aggregated metrics).*

## Dashboard Integration

The output CSV files are pre-formatted for direct upload into the accompanying Google Sheets Dashboard template. 
*   **Raw Data** feeds a hidden backend sheet.
*   **Pivot Logic** automatically visualizes regional talent gaps.
*   **Dynamic Dropdowns** allow cross-referencing of technical experience by specific subnational markets.

## Core Competencies Demonstrated

*   **Data Analytics & Structuring:** Designing relational data models that answer specific business questions.
*   **Process Automation:** Reducing manual data entry and HR administrative overhead.
*   **Python Programming:** Building scalable scripts for data generation and cleaning.
*   **Business Acumen:** Translating operational bottlenecks (staffing field projects) into automated data solutions.
