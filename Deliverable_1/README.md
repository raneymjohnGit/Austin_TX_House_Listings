# Austin_TX_House_Listings

![image_name](https://github.com/raneymjohnGit/Austin_TX_House_Listings/blob/raneybranch/Deliverable_1/Resources/AustinTXZillowImage.png)

![image_name](https://github.com/raneymjohnGit/Austin_TX_House_Listings/blob/raneybranch/Deliverable_1/Resources/AusitinHosueImage.png)

With mortgage rates rising and housing prices continuing to climb, a new study finds Austin has the second most overpriced housing market.It found that based on historical trends, the average price of a home in Travis County in February 2022 should have been $347,775. Instead, the study found that the actual average price is $573,123. That’s 65% higher than where historical data shows they should be.The idea of this project is to do an in-depth analysis the Austin Housing Dataset through apprropriate Machine Learning models and predict the Austin house price for the year 2023.

![image_name](https://github.com/raneymjohnGit/Austin_TX_House_Listings/blob/raneybranch/Deliverable_1/Resources/Austin_Historical_Trends.png)

## Resources
- Google search, https://www.kxan.com/news/local/study-austin-2nd-most-overpriced-housing-market-in-us/
- Kaggle Data set for Data https://www.kaggle.com/code/threnjen/austin-housing-eda-nlp-models-visualizations/data austinHousingData.csv

## Objective:
-   Build a Machine Learning Model to predict house prices in Austin and see what features drive the price of the houses in Austin.

## Deliverbale 1: Final Project Segment 1

### Reason why we selected the topic
Low inventory, fiery competition and massive price gains have battered buyers since covid pandemic, but now rapidly rising mortgage rates are making it even harder to purchase an affordable home. For many buyers, higher mortgage rates mean they can no longer afford homes in specific price ranges. The problem is that even modest single-family homes cost as much as lavish pads did a few years ago, so buyers are stuck either waiting for more inventory to come online or moving to a more affordable area. And there are many more who are hoping prices will drop—but that might not happen anytime soon.  

And we chose Austin,Texas house listings as our topic, since we are interested to see if we could apply a machine learning model to such a robust market.

The database we are using is an Austin Housing Data csv from Kaggle. We chose this dataset because it was clean and has the features, we were looking for such as zip code, square footage, number of rooms, number of bathrooms and several others. Link to the dataset is below. https://www.kaggle.com/code/threnjen/austin-housing-eda-nlp-models-visualizations/data

The question we are trying to answer is can we determine the price of a house in Austin, Texas based on certain features of the property. We are also interested to see what features drive the price of the houses in Austin as well

### Machine Learning Model

-   SciKitLearn is the ML library we'll be using to create a LinearRegression model. Our training and testing setup is using .7 percent of our data to train and .3 
    to test. 

![image_name](https://github.com/raneymjohnGit/Austin_TX_House_Listings/blob/raneybranch/Deliverable_1/Resources/MachineLearning_Model_Image1.png)

-   Takes in data in from the provisional database 
![image_name](https://github.com/raneymjohnGit/Austin_TX_House_Listings/blob/raneybranch/Deliverable_1/Resources/MachineLearning_Model_Image2.png)

-  Heat Map for different features to see features that correlate
![image_name](https://github.com/raneymjohnGit/Austin_TX_House_Listings/blob/raneybranch/Deliverable_1/Resources/MachineLearning_Model_Image3_Heatmap.png)

### Data Cleaning and Analysis
-   Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using Python.

### Database 
-   pgAdmin is the database we intend to use, and we will integrate Flask to display the data.

### Dashboard:
-   In addition to using a Flask template, we will also integrate D3.js for a fully functioning and interactive dashboard. It will be hosted on github. We will also 
    use google slides to create a slide deck for our presentation.


## Communication Protocols
    - Join Weekly class hours
    - Join Office class hours
    - Connecting via Slack  

## Branches
    -   main        - main branch
    -   Lucy        - Branch for Lucy
    -   jayanbranch - Branch for Jayan  
    -   stephenbranch - Branch for Stephen
    -   raneybranch - Branch for Raney 
