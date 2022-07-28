# Austin_TX_House_Listings

![image_name](https://github.com/raneymjohnGit/Austin_TX_House_Listings/blob/main/Deliverable_1/Resources/AustinTXZillowImage.png)

![image_name](https://github.com/raneymjohnGit/Austin_TX_House_Listings/blob/main/Deliverable_1/Resources/AusitinHosueImage.png)

A new study found Austin, Texas has the second most overpriced housing market due to mortgage rates rising and housing prices continuing to climb. The study found that based on historical trends, the average price of a home in Travis County in February 2022 should have been $347,775. Instead, the study found that the actual average price is $573,123. That’s 65% higher than what historical data predicts them to be. The purpose of this project was to do an in-depth analysis of Austin house sales data and to determine if there are any interesting relationships within the data. We applied a machine learning model to predict the price of a typical house in Austin, TX based on available information up to December 2019. 

![image_name](https://github.com/raneymjohnGit/Austin_TX_House_Listings/blob/main/Deliverable_1/Resources/Austin_Historical_Trends.png)

## Resources
- Google search, https://www.kxan.com/news/local/study-austin-2nd-most-overpriced-housing-market-in-us/
- Kaggle Data set for Data https://www.kaggle.com/code/threnjen/austin-housing-eda-nlp-models-visualizations/data?select=austinHousingData.csv

## Objective:
-   To build a Machine Learning Model that predicts house prices in Austin based on features currently driving the housing market.

### Topic Motivation
Low inventory, fiery competition and massive price gains have battered buyers since the COVID pandemic, but now rapidly rising mortgage rates are making it even harder to purchase an affordable home. For many buyers, higher mortgage rates mean they can no longer afford homes in specific price ranges. Even modest single-family homes cost as much as lavish pads did a few years ago, so buyers are stuck either waiting for more inventory to become available or are moving to a more affordable area. Many potential homebuyers are hoping prices will drop — but that might not happen anytime soon.  

We chose Austin, TX as our location because most of our group lives here and we are interested in seeing if we could apply a machine learning model to such a robust market.

### Data Source
The dataset we are using is an Austin Housing Data csv from Kaggle. We chose this dataset because it is extensive and has the features we were looking for such as zip code, square footage, number of rooms, and number of bathrooms, among others. House sales are not public record in Texas, so extensive datasets are difficult to access. This dataset was originally scraped from Zillow using a third party API. Link to the dataset is below:
https://www.kaggle.com/code/threnjen/austin-housing-eda-nlp-models-visualizations/data?select=austinHousingData.csv

### Focus Questions
The question we are trying to answer is can we predict the price of a typical house in Austin, Texas by inputing certain criteria into our predictor. We are also curious what features of a house drive the price and what other interesting relationships between features and price there are that we might not have realized.

### Machine Learning Model
-   Scikit-learn is the python library we'll be using to create our Random Forest Regressor model. Our training and testing setup is using .7 percent of our data to train and .3 to test. 
![Random Forest Regressor](Images/random_forest_regressor.png)

-   Takes in data from the provisional database 
![image_name](https://github.com/raneymjohnGit/Austin_TX_House_Listings/blob/main/Deliverable_1/Resources/MachineLearning_Model_Image2.png)

-  Heat Map for different features to see features that correlate
![image_name](https://github.com/raneymjohnGit/Austin_TX_House_Listings/blob/main/Deliverable_1/Resources/MachineLearning_Model_Image3_Heatmap.png)

### Explanation of Model

We chose the Random Forest Regressor based on empirical experimentation with the accuracy of different models. Random forest is a supervised learning algorithm that uses an ensemble learning method for classification and regression.

We used the built-in feature selection function to determine feature importances and reduce the amount of input for the ideal model. We further reduced the number of features to only 5 for the purposes of creating a model for interactive prediction on our front end ('zipcode' - hot encoded, 'yearBuilt', 'lotSizeSqFt', 'livingAreaSqFt', 'avgSchoolRating').

We continued to improve the model by performing a grid search for hyperparameters, thereby reaching a coefficient of determination of about 73%. 

### Data Cleaning and Analysis
-   Python and pandas were used to clean and analyze the data in google colab notebooks. See the Cleaning Data for Machine Learning Model google colab notebook for a detailed, and commented analysis. 

### Data Exploration
-   Data was explored with pandas, seaborn visualiations, tableau visualizations, and other python libraries. See the Cleaning Data for Machine Learning Model google colab notebook for a detailed, and commented analysis.  

### Database 
-   The database we are using is PostgreSQL. Currently, our database contains seven tables. We will integrate Flask and JavaScript to display the data on the front end. 

![Database Structure](Images/database_ERD.png)


### Dashboard:
-   In addition to using a Flask template, we will also integrate D3.js for a fully functioning and interactive dashboard. It will allow a user to input features and receive a predicted price based on our machine learning model.
-   Our front end will also incorporate a Tableau story with visualizations. 
-   We will use google slides to create a slide deck for our class presentation. 

![Front End](Images/front_end_show_houses.png)

## Google Slides Presentation 

[Google Slides Presentation](https://docs.google.com/presentation/d/1qW7ySGBoWv22oxZI2QIVgwt6B0VDeACSnAcm5nQMxZI/edit?usp=sharing)

![Google Slides Screenshot](Images/google_slides_presentation.png)

-------------------------------------------------------------------------
## Branches
-   main           - Main Branch
-   Lucy           - Branch for Lucy
-   jayanbranch    - Branch for Jayan  
-   stephenbranch  - Branch for Stephen
-   raneybranch    - Branch for Raney 
-   Visualizations - Branch for Visuals

## Segment 1 Role
-   Raney       - Square
-   Jayan       - Triangle
-   Lucy        - Circle
-   Stephen     - X


## Segment 2 Role
-   Raney       - X
-   Jayan       - Square
-   Lucy        - Circle
-   Stephen     - Triangle

## Segment 3 Role
-   Raney
-   Jayan
-   Lucy
-   Stephen

## Segment 4 Role
-   Raney
-   Jayan
-   Lucy
-   Stephen
