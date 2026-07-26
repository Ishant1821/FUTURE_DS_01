# Business Sales Performance Analytics (Task 1)

## Overview
This repository contains the official submission for **Task 1** of the Data Science & Analytics Internship at Future Interns. The project focuses on analyzing an e-commerce sales dataset to extract actionable business insights, evaluate revenue trends, and identify top-performing products.

## Dataset
* **Source:** Kaggle (`ulrikthygepedersen/online-retail-dataset`)
* **Description:** A transnational dataset containing transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.

## Tools & Libraries Used
* **Python** (Data manipulation and analysis)
* **Pandas** (Data cleaning, aggregation, and metric calculation)
* **Matplotlib** (Data visualization)

## Key Business Insights

1. **Total Sales Revenue:**
   * The business generated a total revenue of **$8,911,407.90** during the recorded period after data cleaning (removing cancellations and zero/negative quantities).

2. **Top 5 Products by Revenue:**
   * PAPER CRAFT, LITTLE BIRDIE ($168,469.60)
   * REGENCY CAKESTAND 3 TIER ($142,592.95)
   * WHITE HANGING HEART T-LIGHT HOLDER ($100,448.15)
   * JUMBO BAG RED RETROSPOT ($85,220.78)
   * MEDIUM CERAMIC TOP STORAGE JAR ($81,416.73)

3. **Monthly Revenue Trend:**
   * Sales show significant variance throughout the year, with a massive spike in revenue leading into the final quarter (Q4), peaking in November. 
   * *See `monthly_revenue_trend.png` for the detailed visual breakdown.*

## Files in this Repository
* `sales_performance_analysis.py`: The complete Python script used to download, clean, and analyze the dataset.
* `monthly_revenue_trend.png`: A generated line chart visualizing the revenue growth over time.
* `README.md`: Project documentation and findings summary.

## How to Run the Code
1. Install the required dependencies:
   ```bash
   pip install pandas matplotlib kagglehub