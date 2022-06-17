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
1. **Data Loading:** Collecting data from different sources (csv file and API) and joining them into a single table;
2. **Data Description:** Know the characteristics of each variable, in order to plan data cleaning;
3. **Data Cleaning:**
4. **Feature Selection:**
5. **Exploratory Data Analysis:**

## 4. Top 3 Data Insights

## 5. Business Results

## 6. Conclusions

## 7. Lessons Learned
1. ETL script creation;
2. Data visualization tools: Matplotlib, Seaborn and Folium;
3. Data manipulation tools: Pandas;
4. Creating a Data Visualization App with Streamlit;
5. Hosting the app on a free cloud: Heroku.

## 8. Next Steps to Improve
1. Collect data about the location of properties using another source, such as the Google Maps API;
2. Collect data on points of interest close to properties, such as: hospitals, schools, parks, businesses, etc.
