# Markeging Campaign Analysis

## 📝 Project Overview
This project aims to assist the marketing team in optimizing customer acquisition strategies and investment in marketing channels. The primary objective is to identify which channels yield the highest returns and improve the allocation of financial resources through data analysis.

## 🗂️ Dataset
The project utilizes two datasets:
- **Trials**: A list of all trial stores created over the last 20 months.
- **Costs**: The marketing costs associated with acquiring these trials.

### Definitions
- **Source**: The channel through which trials are acquired, including:
 - Facebook Campaigns
 - Google Adwords Brand Campaigns
 - Google Adwords Non-Brand Campaigns
 - Partners (Marketing agencies compensated per payment)
- **Device**: The device used to create the store (Mobile or Desktop).
- **Payment Probability**: The likelihood that a trial converts to a payment. A value of 0.75 or higher indicates a high likelihood of payment.

## 🛠️ Tools and Technologies
- SQL (MySQL Workbench) for data manipulation
- Python (Jupyter Notebook) for analysis
- Microsoft Excel for data visualization

## 🔍 Methodology
The analysis begins by understanding the business context and requirements. Data from trials and payments are examined, focusing on conversion rates from trials to payments. Key performance indicators (KPIs) are established to evaluate the marketing team's performance across various acquisition channels.

## 📊 Analysis Steps
1. **Data Exploration**: Analyze the trials-to-payments conversion funnel and calculate the conversion rate and cost per acquisition (CPA).
2. **KPI Development**: Establish KPIs to assess overall performance and by acquisition channel.
3. **Channel Performance Evaluation**: Identify which channels yield the highest returns and assess their effectiveness based on conversion rates.

## 📈 Results and Key Findings
- The overall conversion rate from trials to payments was found to be 11.5%, stable over the analyzed period.
- Channels such as Facebook Campaigns and Google Adwords Brand Campaigns contributed significantly to trials, but conversion rates varied.
- Partners yielded the highest conversion rates, indicating effective collaboration with marketing agencies.
- Desktop devices showed a significantly higher conversion rate compared to mobile devices.

## 💡 Recommendations
- Improve engagement on the website through A/B testing of content and design.
- Reassess and optimize Facebook Campaigns to enhance conversion rates.
- Investigate the user experience on mobile devices to increase mobile conversion rates.
- Consider calculating Customer Acquisition Cost (CAC) to get a complete picture of channel performance.

## 📝 Conclusion
While some channels demonstrate strong performance, others like Facebook Campaigns require improvements due to low conversion rates and high CPA. The next steps include assessing the complete marketing funnel and potentially implementing retargeting strategies to convert trials into payments. Regular monitoring and visualization of key metrics will empower the marketing team to make data-driven decisions and improve overall performance.