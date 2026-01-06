# Geographic Efficiency Analysis and unlocking Hidden Revenue in UK Markets

![Status](https://img.shields.io/badge/Status-Completed-success)
![Python](https://img.shields.io/badge/Python-Data%20Analysis-blue)
![Strategy](https://img.shields.io/badge/Strategy-Market%20Optimization-green)

##  Executive Summary
**Objective**
To evaluate the geographic performance of the company's UK market, identifying revenue concentration risks and efficiency gaps between major cities and satellite towns.

**Key Achievement**
Through advanced data augmentation (integrating `uk-towns.csv`), this project reduced "Unknown" location data from **46% to <8%**, uncovering a **£264 Million** "Hidden Market" in commuter towns previously invisible to stakeholders.

**Top Strategic Insight**
The analysis challenges the "London-Centric" growth strategy. Data reveals that **Commuter Towns (e.g., Reading)** and **Northern Hubs (e.g., Manchester)** offer significantly higher Revenue Per Capita (ROI) than London.



##  Technical Methodology
The project followed a rigorous data engineering pipeline:
1.  **Data Augmentation,** Merged transactional data with an external database of 43,000+ UK towns to resolve unmapped locations.
2.  **Hierarchical Matching,** Implemented a custom Python string-matching algorithm to identify towns missed by standard city-level filters.
3.  **Feature Engineering,** Created the **"Spend Per Capita"** metric to normalize revenue against population, allowing for fair comparison between large cities and smaller towns.



## Critical Business Insights 

### A. The "Northern Efficiency" Gap (Manchester vs. Leeds)
While Manchester stands out as the company's most efficient market (**£19.01 per capita**), Leeds significantly underperforms (**£6.58 per capita**) despite sharing similar demographic and economic profiles.
* **Diagnosis.** This discrepancy suggests a specific operational or sales execution issue in the Yorkshire region (Leeds), rather than a lack of market demand.
* **Implication.** Leeds represents a "Low-Hanging Fruit" for growth. Replicating the Manchester sales strategy here could triple the regional revenue.

### B. The "Commuter Wealth" Effect (London vs. Reading)
A comparative analysis reveals that **Reading** (a commuter town) generates higher revenue per person (**£13.97**) than **London** (**£9.73**).
* **Diagnosis.** High disposable income is concentrated in the "Commuter Belt" rather than the capital city center. The cost of customer acquisition in London is likely higher, making Reading a more profitable target.
* **Implication.** Marketing budgets should be reallocated from saturated London channels to targeted campaigns in high-value satellite towns.

### C. Market Penetration Variance (Reading vs. Luton)
Despite both being major satellite towns with airports and direct rail links to London, **Luton** generates less than 50% of the revenue seen in **Reading** (£1.0M vs £2.2M).
* **Diagnosis.** This indicates a lack of product-market fit or brand awareness specifically within the Luton demographic.
* **Implication.** Requires a localized investigation to understand why the brand resonates in Berkshire (Reading) but not in Bedfordshire (Luton).



##  Visualizations

### 1. The "Hidden Market" Discovery
*Visualizing the £264M revenue shift from "Unknown" to identified Commuter Towns.*
![Top 15 Towns](output/ibcs_top15_towns.png)

### 2. Market Efficiency (Spend Per Capita)
*Highligting the superior efficiency of Manchester and Reading compared to the capital.*
![Efficiency Chart](output/ibcs_efficiency.png)



## Strategic Recommendations
Based on the data, the following strategic pivots are recommended:

1.  **Diversify to Tier-2 Towns.**
    Formally recognize "Commuter Towns" (Reading, Northampton, Milton Keynes) as a distinct market tier. They currently drive massive organic revenue and should be prioritized over costly London expansion.
2.  **Operational Audit in Leeds.**
    Launch a review of the Leeds sales channel, logistics, and stock availability to address the efficiency gap relative to Manchester.
3.  **Optimization over Expansion.**
    Instead of entering new territories, focus resources on lifting the performance of underperforming assets like **Luton** and **Sheffield** to meet the benchmarks set by their peer cities.



##  Repository Structure
* `data/`: Contains raw customer data (anonymized) and the augmented `uk-towns.csv` reference file.
* `scripts/`: Python scripts for data cleaning, geocoding logic, and visualization.
* `output/`: Generated IBCS-standard charts used in this report.
