# Exploring and Predicting 2018-2021 House Prices in Austin, TX. 

# Background
Austin has among the most overpriced and competitive housing markets in the nation. As of July 2022, research suggests it is the second second most overpriced housing market, with a 69.20% premium relative to its long-term pricing trend. Paralleling nationwide trends in urban areas, migration to the city, low mortgage rates, and low housing supplies are fueling a booming housing market, though there are signs suggesting cooling in the latter half of 2022. Subjectively, buying a house is reportedly extremely difficult, with seller's receiving multiple offers over asking price immediately after listing a property.

# Purpose
The purpose of this project was to do an in-depth exploratory analysis of Austin house sales data to 1) identify which home characteristics determine price 2) discover meaningful insights about relationships between the variables in a sale 4) apply a machine learning model to predict the price of a typical house in Austin, TX. 

## Objective:
1) identify which home characteristics determine price 
2) discover meaningful insights about relationships between the variables in a sale 
3) apply a machine learning model to predict the price of a typical house in Austin, TX. 

### Topic Motivation
As discussed in the background section, Austin, TX has an incredibly competitive housing market, fueled by low inventory and increasing demand from migration. Buyers faced additional challenges as mortgage rates began to increase in the latter half of 2021. For aspiring homeowners, the experience of trying purchase a house is harrowing, with listings receiving multiple offers over asking price almost immediately. Austin is also the home of three of our group members, two of whom are hoping to buy a home in the next five years. These exciting changes in the marekt make it an attractive target for exploratory data analysis and to practice our skills by applying a machine learning model to predict house price. 

### Data Source
The "Austin Housing Data" dataset we are using is sourced from Kaggle, and was originaly scraped from Zillow using a third party API by Eric Pierce. We chose this dataset because it is extensive (over 15,000 data points), covers several years of interest (2018 - 2021), and has a broad set of house characteristics concerning location, size, rooms, school information, and more. House sales are not public record in Texas, so extensive datasets are difficult to access. In addition, other analyses of this dataset are publicly available, which provides some context for our project. Link to the dataset is below: https://www.kaggle.com/code/threnjen/austin-housing-eda-nlp-models-visualizations/data?select=austinHousingData.csv

### Focus Questions
1) Can we predict the price of a house in Austin under December 2019 market conditions using a machine learning model?
2) Which features drive the price of houses in Austin?
3) What other meaningful relationships between variables can be discovered in this dataset?

### Machine Learning Model
-   Scikit-learn is the python library we'll be using to create our models. Our training and testing setup is using .7 percent of our data to train and .3 to test. 
![Random Forest Regressor](Images/random_forest_regressor.png)

-   Takes in static data from the database.
![Database Connection](Images/database_connection.png)

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

## Resources
- Kaggle Data set for Data https://www.kaggle.com/code/threnjen/austin-housing-eda-nlp-models-visualizations/data?select=austinHousingData.csv

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
