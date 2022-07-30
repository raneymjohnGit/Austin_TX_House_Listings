import joblib
import pandas as pd
from sqlalchemy.engine.create import create_engine
import sklearn

def predict_houseprice (featureValues):
    #load the model
    model = joblib.load("rf_front_end_final-model_jlib")
    print('The scikit-learn version is {}.'.format(sklearn.__version__))
    
    zipcode = featureValues["zipcode"]
    yearBuilt = featureValues["yearBuilt"]
    lotsizeSqFt = featureValues["lotSizeSqFt"]
    livingAreaSqFt = featureValues["livingAreaSqFt"]
    avgSchoolRating = featureValues["avgSchoolRating"]
    
    #get the predictions from the model
    predictions = model.predict([[zipcode, yearBuilt, lotsizeSqFt,livingAreaSqFt,avgSchoolRating]])
    return int(predictions[0])

def jsonify_data(featureValues):
    raw_db_url='dpaclsxjrpfluk:4fa14e6fdb846bd14d1a9eda261d554fab9688f2f4dd5483bc38d94cdee010ad@ec2-3-219-52-220.compute-1.amazonaws.com:5432/d7s0s0hs0a5lar'
    # Convert binary string to a regular string & remove the newline character
    db_url = raw_db_url

    # Convert "postgres://<db_address>"  --> "postgresql+psycopg2://<db_address>" needed for SQLAlchemy
    final_db_url = "postgresql+psycopg2://" + db_url.lstrip("postgres://")  # lstrip() is more suitable here than replace() function since we only want to replace postgres at the start!


    # Create SQLAlchemy engine
    # ------------------------
    engine = create_engine(final_db_url)

    # dataframe to sql
    df = pd.read_sql_table('cleaned_data_1', engine)

    
    zipcode = int(featureValues["zipcode"])
    yearBuilt = int(featureValues["yearBuilt"])
    lotsizeSqFt = int(featureValues["lotSizeSqFt"])
    livingAreaSqFt = int(featureValues["livingAreaSqFt"])
    avgSchoolRating = int(featureValues["avgSchoolRating"])


    # Filter the dat frame based on zipcode.
    filtered_df = df[df["zipcode"] == zipcode]

    # Filter the dat frame based on Year built range.
    filtered_df = filtered_df.loc[(df["yearBuilt"] >= (yearBuilt - 5)) & (df["yearBuilt"] <= (yearBuilt + 5))]
    
    # Filter the dat frame based on Lot Size Square Feet range.
    filtered_df =filtered_df.loc[(filtered_df["lotSizeSqFt"] >= (lotsizeSqFt - 2000)) & (filtered_df["lotSizeSqFt"] <= (lotsizeSqFt + 2000))]
    
    # Filter the dat frame based on Living Area Square Feet range.
    filtered_df =filtered_df.loc[(filtered_df["livingAreaSqFt"] >= (livingAreaSqFt - 200)) & (filtered_df["livingAreaSqFt"] <= (livingAreaSqFt + 200))]
    
    # Filter the dat frame based on School Rating range.
    filtered_df =filtered_df.loc[(filtered_df["avgSchoolRating"] >= (avgSchoolRating - 1)) & (filtered_df["avgSchoolRating"] <= (avgSchoolRating + 1))]
    
    #Combine the Lattitudes and longitudes in one single column for geomapping
    filtered_df["location"] = filtered_df[["latitude","longitude"]].values.tolist()
    
    #Selected columns
    columns = ["city","zipcode","lotSizeSqFt","livingAreaSqFt","avgSchoolRating","numOfBedrooms","numOfBathrooms","streetAddress", "latestprice","location"]
    
    filtered_df = filtered_df[columns]    
    
    #Create the JSON file for JS to use
    filtered_df.to_json('C:/Users/raney/OneDrive/Desktop/Analysis_Projects/Austin_TX_House_Listings/Raney/static/js/dataset.js', orient = 'records')