# Fraud Detection and Risk Analysis for a Digital Bank

## 📝 Project Overview
This project focuses on analyzing transaction data from a digital bank mobile app to identify potential fraud and develop risk classification rules. The analysis aims to evaluate transaction events, classify risk levels, and provide actionable insights to enhance fraud detection mechanisms.


## 🗂️ Dataset
The dataset contains information on transaction events, including:
• Transaction IDs
• Transaction values
• Client decisions (approved or denied)
• Device characteristics (e.g., emulator status, root permissions, app integrity)

## 🛠️ Tools and Technologies
- **Programming Language**: Python (Jupyter notebook)
- **Libraries**: `pandas`, `numpy`, `matplotlib`, `seaborn`
- **Techniques**: ETL, Data Cleaning, Exploratory Data Analysis (EDA), Data Visualization.

## 🔍 Methodology
1. Data Quality Process: Conducted a thorough review of the dataset to identify data quality issues, such as non-unique transaction IDs and missing values. This step included deciding how to handle duplicates and null entries to ensure data integrity.
2. Descriptive Analysis: Analyzed key statistics for all relevant variables, including transaction values and client decisions. This analysis provided insights into the overall distribution of transactions and highlighted any anomalies.
3. Device and Account Distribution: Investigated the distribution of devices per account and accounts per device, revealing potential patterns in user behavior and device usage that could influence fraud detection.
4. Impact Evaluation of New Decision Flow: Compared the performance of the new decision flow against previous methods, focusing on approval rates, chargeback rates, and net revenue. This evaluation involved assessing the effectiveness of the new decision rules in minimizing fraud while maximizing user experience.

## 📊 Analysis Steps
• Verified the uniqueness of transaction IDs and addressed duplicates
• Assessed the distribution of devices per account and accounts per device
• Explored null values in critical columns and made decisions on their handling
• Compared the effectiveness of the new decision flow against previous methods

## 📈 Results and Key Findings
• Data Quality Issues: Identified 136 transactions with transaction ID = 0 and 4 repeating transaction IDs. Excluded these from further analysis.
• Missing Values: Found 68 transactions with null values in key device-related columns. The overall null percentage was low, so no further investigation was deemed necessary.
• Transaction Dynamics:
• The approval rate increased significantly with the new decision flow, reaching 86.16%.
• The chargeback rate decreased to 11.81%, suggesting improved fraud detection.
• Net revenue increased by 29% due to better transaction approvals, despite an increase in false positive costs.
• The new decision rule allowed for a higher percentage of transactions to be approved, enhancing user experience while still effectively reducing fraud
In summary, the new decision flow shows promising results with improved fraud detection and increased revenue, indicating a 20% increase in net revenue

## 💡 Recommendations
• Adjust Decision Thresholds: Experiment with different decision thresholds to optimize the balance between fraud detection and user experience.
• Enhance Feature Engineering: Explore additional data sources or variables to further improve model performance.
• Implement Monitoring Systems: Regularly assess decision performance and update rules based on new data.
• Foster Collaboration: Ensure collaboration among fraud prevention teams, data scientists, and business stakeholders for effective decision-making.
• Adopt Real-Time Detection Methods: Enhance system responsiveness and reduce losses by identifying fraudulent transactions as they occur

## 📝 Conclusion
The analysis of the Digital Bank Mobile App’s fraud detection system revealed significant insights into its performance and financial implications. The new decision system shows potential for enhancing user experience and increasing revenue while improving fraud detection rates. By carefully considering the recommendations outlined, the Digital Bank Mobile App can establish a robust fraud detection system that aligns with its business objectives.
