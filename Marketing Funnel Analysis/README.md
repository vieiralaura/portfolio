# 📊 Conversion Funnel Analysis with Data-Driven Insights

## 📝 Project Overview
This project focuses on analyzing the conversion funnel of a user investment journey, with data extracted from website navigation logs.
The goal is to identify areas of drop-off, assess user qualifications, and propose improvements to increase the overall conversion rates.
It involves a thorough examination of the funnel’s performance, alongside recommendations for optimization.

The funnel comprises four stages where users interact with the platform: 
1 - Homepage: The landing page for all users entering the funnel
2 - Questionnaire: A page where users answer questions about their investment profile and simulate the amount they intend to invest
3 - Investment Plan: After the questionnaire responses are processed, the user is directed to a screen that displays the investment allocations identified for their profile. This is an important step, as it serves as a decision point where the user evaluates whether they like the proposed plan.
4 - Registration: If the user is satisfied with the investment plan, they proceed to start the registration process. This is the final step of conversion.

## 🗂️ Dataset
The dataset (user_navigation.csv) contains user navigation data, that tracks user progression through various stages of a conversion funnel. Key components include:
- User data: Information about users as they move through each stage of the conversion funnel
  • User ID(id): Unique identifier for each user.
  • Traffic Source(source): Channel through which the user accessed the website (e.g., Paid Search, Social).
  • Device(device): Device used by the user (e.g., mobile, desktop).
  • Page(page): Pages visited by the user (Homepage, Questionnaire, Investment Plan, Registration).
  • Simulated Investment Amount(amount): The amount the user intends to invest, simulated during the Questionnaire stage (in BRL).
  
- Example Data:
  • User ID 1: Accessed through Paid Search on a desktop, visited only the Homepage.
  • User ID 2: Accessed through Social on a mobile device, visited only the Homepage.
  • User ID 3: Accessed through Paid Search on mobile, completed Registration with a simulated investment of BRL 2000.
  • User ID 4 and 5: Accessed through Paid Search on desktop, reached the Questionnaire. The average simulated investment amount was BRL 12,500.

## 🛠️ Tools and Technologies
- Excel/Google Sheets for graph
- Jupyter Notebook

## 🔍 Methodology
1. **Data Exploration**: Load and explore the data to understand its structure, content, and quality. Handle any missing values or data inconsistencies.
2. **Descriptive Analysis**: Calculate metrics like conversion rates, drop-off rates, and user segmentation.
3. **Visualization**: Create charts and graphs to illustrate user flow, identify major drop-off points, and overall funnel performance.
4. **Insights Generation**: Interpret the analysis results to identify the stages that need improvement and suggest strategies to optimize conversion rates.

## 📊 Analysis Steps
- Conversion Funnel Analysis: Calculate the number of users at each stage of the funnel and the drop-off rates between stages
- Simulated Investment Analysis: Analyze the distribution of simulated investment amounts
- Traffic Source and Device Analysis: Cross-reference user progression through the funnel with their traffic source and device
- Performance Metrics: Identify key metrics like conversion rates at each stage, user qualification rates, and drop-off points
- Present the findings: Use text, tables, and charts to explain each point of your analysis
- Highlight potential areas for improvement based on the previous findings

## 📈 Results and Key Findings
Overall Funnel Conversion:
• The overall conversion rate of the funnel is 15,7%.
• The lowest conversion stage is from Homepage to Questionnaire, with a conversion rate of 41,6%.

Funnel Performance by Channel:
• The “Direct” channel achieved the highest conversion rate, which aligns with expectations as users likely arrive with a defined goal.
• “Paid search” generated the most visits but had the lowest conversion rate

Device Performance:
• Desktop users exhibited a higher conversion rate than mobile users

Acquisition Channel Effectiveness:
• “Direct” and “Organic search” channels are significant contributors to user registrations, collectively representing 70% of registrations.
• The average simulated value is substantially higher for the “Direct” channel, with a total average of R$ 120.520,54.
• Although Organic Search generates more registrations, the average simulated value is lower compared to Direct. 


## 💡 Recommendations
• To enhance conversion rates, efforts should focus on increasing engagement and interest on the homepage through A/B testing of content, images, and CTAs. It’s crucial to review past tests to avoid rework.
• Reevaluating channel segmentations and conducting analyses on specific channels can aid in improving performance.
• For paid search, directing users to a tailored Landing Page instead of the homepage may improve conversions by aligning content with user expectations
• Investigating the site’s optimization for mobile devices may provide insights for improvement.

Future Analysis Proposals:
• Investigate monthly performance trends to determine if observed behaviors are consistent or isolated.
• Employ multiple linear regression models to identify variables that contribute significantly to returns.
• Assess the sales cycle for each channel to pinpoint those yielding quicker returns.
• Analyze channels for client acquisition effectiveness to determine which yield the highest lead conversion rates.
• Evaluate the cost per lead (CPL) for paid channels and consider if increased spending could boost conversions.

## 📝 Conclusion
The analysis reveals key insights into user behavior throughout the conversion funnel and identifies opportunities for improvement in user retention and conversion rates. By focusing on optimizing the Questionnaire experience and enhancing the mobile interface, the platform can achieve better user engagement and higher conversion rates.

## 💬 Note
This study was conducted while I was searching for my first job as a data analyst, in 2018, and I successfully secured a position!
While I recognize that this analysis is quite basic, reflecting the level of a junior analyst, I plan to revisit it in the future to develop a more advanced approach.


