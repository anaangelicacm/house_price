# House Rocket
![breno-assis-r3WAWU5Fi5Q-unsplash.jpg](https://github.com/anaangelicacm/house_price/blob/main/images/breno-assis-r3WAWU5Fi5Q-unsplash.jpg?raw=true)


## 1. Business Problem
House Rocket is a Washington state-based real estate company whose objective is to expand its activities to other regions of the state. For this, a survey of available real estate in King County was carried out.

Not all properties would result in good deals, so the company has the need to identify which houses are in good condition, what is the best selling price and what is the best quarter of the year that it could be sold.

## 2. Business Assumptions
The assumptions about the business problem are as follows:
- Selection of properties:
     - Only those whose condition is greater than or equal to three will be considered;
     - The properties must have been built with good quality materials (grade greater than or equal to 5);
     - It will be suggested the purchase of properties whose price is lower than the median value of the neighborhood in which it is located. 
     
- Pricing of selected properties:
     - If the purchase value is greater than the median value of the region (zipcode) + quarter influence: sale price + 10%;
     - If the purchase value is less than the median value for the region (zipcode) + quarter influence: sale price + 30%.

## 3. Solution Strategy
- **Step 1. Data Loading:** Collecting data from different sources (csv file and API) and joining them into a single table;
- **Step 2. Data Description:** Know the characteristics of each variable, in order to plan data cleaning;
- **Step 3. Data Cleaning:** This step consisted of deleting duplicate lines, dealing with missing data, dealing with inconsistent data and filtering the lines according to the business rules established at the beginning of the project.;
- **Step 4. Feature Selection:** Selection of columns according to business rules;
- **Step 5. Exploratory Data Analysis:** Visualization of data and raising of hypotheses;
- **Step 6. Business Results**: Calculation of business results obtained;
- **Step 7. Dashboard**: Creating a dashboard and hosting it in the cloud. The result can be seen through this [link](https://kc-house-analysis.herokuapp.com).

## 4. Top 3 Data Insights
- Houses waterfront have the average price approximately the same as houses that are not near the water;
- Taking into account seasonality, the average price of houses is the same in both semesters of the year;
- Considering the index that quantifies the condition of the properties, the average house price is the average independent of the index (taking into account only houses with an index equal to or greater than 3).

## 5. Business Results
- Of the 21613 homes available in King County, 10306 were selected according to business rules;
- The sale value of the homes is US$468388.82;
- The average home profit is US$79163.84;
- If all houses are sold by House Rocket, the real estate company can earn up to US$815862515.80.

## 6. Conclusions
The project achieved initial expectations, creating a cloud-hosted application that can be consulted by people in the company when offering homes according to what the customer wants. In addition, possible gains were calculated if the project were put into practice.

## 7. Lessons Learned
- ETL script creation;
- Data visualization tools: Matplotlib, Seaborn and Folium;
- Data manipulation tools: Pandas;
- Creating a Data Visualization App with Streamlit;
- Hosting the app on a free cloud: Heroku.

## 8. Next Steps to Improve
- Collect data about the location of properties using another source, such as the Google Maps API;
- Collect data on points of interest close to properties, such as: hospitals, schools, parks, businesses, etc.
