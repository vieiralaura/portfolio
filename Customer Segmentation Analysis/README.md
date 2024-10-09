# Customer Segmentation Analysis: Understanding Your Customers

## 📋 Project Overview
This project focuses on analyzing customer segmentation and performance data from a marketing campaign and departmental sales over time. The analysis covers two main topics: campaign effectiveness and year-over-year department sales performance. 


## 🎯 Objectives
The goal is to understand customer behavior and provide insights for future marketing strategies and sales growth.

## 🗂️ Dataset
The project utilizes multiple datasets:
- Marketing Campaign Data
	- Customers: Contains customer identifiers (ID), their assigned profiles (ProfileID), and segments(SegmentID).
	- Sales: Records sales data for customers who made purchases following the campaign(Spend).
	- Versions: Details the promotional material each customer received(Version), including control group indicators(MailInd).

- Departmental Sales Data
	- Dept Data: Aggregated sales data(Sales and Customers) by department(DepartmentID), year(Year), customer segment(SegmentID), and profile(ProfileID).

- Supplemental Info
	- Segments: Customer behavior classifications based on transactional history
	- Profiles: General demographic and lifestyle groupings
	- Departments: Categories of retail products and non-merchandise transactions
	- Versions: Different combinations of offers and creative materials used in the campaign

## 🛠️ Tools and Technologies
- **Programming Language**: Python (Jupyter notebook), SQL (MySQL)
- **Libraries**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `sklearn`
- **Techniques**: ETL, Data Cleaning, Exploratory Data Analysis (EDA), Data Visualization.

## 🔍 Methodology
1. ETL process: Read and processed datasets to remove duplicates and inconsistencies, create MySQL database and Analytical Base Table (ABT)
2. Data Exploration: Conducted exploratory data analysis (EDA) to understand trends, distributions, and relationships between variables.
3. Campaign Effectiveness Analysis: Evaluated the impact of different versions of marketing communications on sales performance.
4. Year-over-Year Analysis: Compared departmental sales performance by customer segment and profile over two years.

## 📊 Analysis Steps
-  ETL Process:
	- Read and preprocess the datasets to ensure data quality and consistency
	- Create a MySQL database and upload the processed datasets
	- Establish an ABT and a departmental analysis table within the MySQL database

- Marketing Campaign Analysis
1. Conversion Rate Calculation: Assessed the percentage of users who made a purchase after receiving promotional materials, using this as the primary Success Metric
2. Total Spend Calculation: Evaluated the total spending of users who participated in the campaigns to understand the financial impact
3. A/B Test:
	- Create the hyopteses:
• Hypothesis 1: Users receiving promotional material A are more likely to purchase compared to those who did not
• Hypothesis 2: Users receiving promotional material B are more likely to purchase compared to those who did not
• Hypothesis 3: Users receiving promotional material A are more likely to purchase compared to users receiving material B
	- Statistical Significance Testing: Analyzed the differences in conversion rates between groups to determine if variations were meaningful or merely coincidental.
	
- Department Analysis
• Sales and Customers Analysis: Calculate the number of customers and total revenue by year, analyzing trends and behaviors
• Department Growth Analysis: Evaluate the performance of each department, identifying which grew or declined over time
• Average Ticket Calculation: Calculate the average ticket value by department and analyze variations
• Segment Performance Analysis: Examine the performance of different customer segments, identifying revenue declines and variations in customer numbers.
• Profile Contribution Analysis: Analyze the contribution of different customer profiles to sales, observing variations over time.

- Present Recommendations
Based on the analysis, suggest improvements for marketing strategies and departmental focus areas.

## 📈 Results and Key Findings
- Campaign Performance:
	- Conversion Rate Analysis:
		- Both Version A and its control group had similar conversion rates, with Version A showing a slight edge. However, statistical testing revealed that this difference was not significant
		- Version B displayed a slightly higher conversion rate than its control group, but again, the difference was not statistically significant
		- When comparing Version A to Version B directly, Version B had a marginally higher conversion rate. However, this difference also failed to achieve statistical significance
	- Total Spend Analysis:
		- Users in Group A showed better incremental results in terms of total spend compared to Group B, though this cannot be definitively attributed to the campaign
		- While Version A had a higher average ticket value, the revenue increase observed may be influenced by factors outside the scope of the marketing materials
	- Segment-Specific Performance:
		- Version B demonstrated improved conversion rates within specific customer segments (e.g., new customers)
		- This suggests that the impact of the promotional materials may vary depending on customer profiles and segments

- Department Performance
	- Overall Performance:
		• The analysis revealed a decrease of $4,750k in revenue compared to 1999, with a 7% reduction in the customer base.
		• The average ticket value dropped from $15.35 to $6.01, indicating changes in customer behavior.
	- Department Growth:
		• Only three departments showed growth, with the “Boots” department contributing 8% of total revenue.
		• The cessation of operations for “Knick Knacks,” which represented 64% of revenue, was a significant factor in the overall decline.
	- Average Ticket Trends:
		• Most departments maintained stable average ticket values, with “Boots” exceeding “Formalwear” and “Store Use.”
	- Segment Performance:
		• All segments experienced revenue declines, particularly “Core Customers” and “Power Shoppers.”
		• The “New Customers” segment was an exception, maintaining its number of customers, suggesting effective acquisition strategies.
	- Profile Contribution:
		• The “Pinched Pockets” and “Rich & Richer” profiles showed declines in contributions, while “Mr. & Mrs. Smiths” had a slight increase.
		• The loss of the “Knick Knacks” department resulted in a 60% decrease in average ticket values across all profiles, but spending patterns remained consistent.

## 💡 Recommendations
- Marketing Campaign:
1. Refinement of A/B Testing Approach:
• Conduct tests on individual elements such as background colors, text fonts, call-to-action (CTA) wording, and other design elements that better align with brand identity.
• The initial tests combined all elements, making it difficult to identify which changes were effective. Future tests should isolate variables to pinpoint drivers of success.
2. Collaborate with User Researchers:
• Engage with user researchers who specialize in qualitative analysis to gain insights that could guide future tests and adjustments.
3. Explore Granular Metrics:
• Beyond conversion rates, analyze metrics like click-through rate (CTR), bounce rate, and other micro-conversion rates for a deeper understanding of user engagement.
4. Utilize Pre-Test Data:
• Having access to data from before the campaign could provide valuable context for understanding shifts in user behavior and help identify trends related to the marketing interventions.

- Marketing and Sales teams:
• Focus on the “New Customers” segment, which accounts for 28% of revenue, while continuing to engage the existing customer base for cost-effectiveness.
• Actively promote the new “Boots” department to the current audience and explore retargeting options for abandoned carts and previous customers, particularly targeting segments like “Core Customers” and “Power Shoppers.”
• Consider implementing a customer loyalty program to reward and retain existing customers.
• Engage users and employee advocates to create user-generated content (UGC) for improved brand visibility and potential virality.
• Prioritize listening to customer feedback to enhance offerings and satisfaction.
• Explore and promote other departments to offset revenue losses from the closure of “Knick Knacks.”

- Data & Analytics team:
• Evaluate the availability of full-funnel data to identify focal points for optimization, ensuring comprehensive measurement of the customer journey.
• Reassess customer profiles and segments for accuracy, considering cluster analysis to group them meaningfully.
• Analyze the sales cycle for each channel to identify those with quicker returns, using metrics like Lifetime Value (LTV) and Monthly Recurring Revenue (MRR).
• Assess key financial metrics by channel, including Customer Acquisition Cost (CAC), Return on Investment (ROI), Cost Per Click (CPC), Cost Per Lead (CPL), and Cost Per Sale (CPS), ensuring alignment with stakeholder expectations.
• Determine opportunities for increased spending to enhance conversion rates based on these evaluations.


## 📝 Conclusion
The analysis of our marketing campaign’s A/B tests revealed that while Version A demonstrated slightly better financial returns and Version B showed potential in specific segments, none of the differences were statistically significant.
This highlights the importance of refining our testing strategies to focus on more granular elements and better understanding customer preferences.
By leveraging insights from user researchers and experimenting with individual design elements, we can enhance future campaigns’ effectiveness.
Though the results were not conclusive, they provide a foundation for deeper learning and more targeted efforts in understanding customer behavior.

The analysis indicates concerning trends in overall customer engagement and revenue generation, necessitating immediate attention to specific segments and departments.
While some areas show promise, particularly with the “Boots” department and the acquisition of new customers, significant efforts are required to address the declines in existing customer segments and average ticket values.
Proactive strategies targeting declining segments and leveraging growth opportunities will be critical to reversing these trends and enhancing overall business performance

## 📧 Contact
For any questions or suggestions, please contact [laurafbvieira@gmail.com](mailto:laurafbvieira@gmail).

