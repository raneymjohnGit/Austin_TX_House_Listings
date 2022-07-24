import joblib
import pandas as pd
from sqlalchemy.engine.create import create_engine

def predict_houseprice (filterCond):
    model = joblib.load("model.joblib")
    
    livingAreaSqFt = filterCond["livingAreaSqFt"]
    avgSchoolRating = filterCond["avgSchoolRating"]
    numOfBathrooms = filterCond["numOfBathrooms"]
    
    predictions = model.predict([[livingAreaSqFt,avgSchoolRating,numOfBathrooms]])
    print("inside predict_house")
    return int(predictions[0])

def jsonify_data(filterCond):
    raw_db_url='dpaclsxjrpfluk:4fa14e6fdb846bd14d1a9eda261d554fab9688f2f4dd5483bc38d94cdee010ad@ec2-3-219-52-220.compute-1.amazonaws.com:5432/d7s0s0hs0a5lar'
    # Convert binary string to a regular string & remove the newline character
    db_url = raw_db_url

    # Convert "postgres://<db_address>"  --> "postgresql+psycopg2://<db_address>" needed for SQLAlchemy
    final_db_url = "postgresql+psycopg2://" + db_url.lstrip("postgres://")  # lstrip() is more suitable here than replace() function since we only want to replace postgres at the start!


    # Create SQLAlchemy engine
    # ------------------------
    engine = create_engine(final_db_url)

    # dataframe to sql
    df = pd.read_sql_table('raw_housing_data_2', engine)

    
    livingAreaSqFt = filterCond["livingAreaSqFt"]
    avgSchoolRating = filterCond["avgSchoolRating"]
    numOfBathrooms = filterCond["numOfBathrooms"]
    latestPrice = filterCond["latestPrice"]


    filtered_df =df.loc[(df["numOfBathrooms"] >= (numOfBathrooms - 1)) & (df["numOfBathrooms"] <= (numOfBathrooms + 1))]
    filtered_df =filtered_df.loc[(filtered_df["livingAreaSqFt"] >= (livingAreaSqFt - 200)) & (filtered_df["livingAreaSqFt"] <= (livingAreaSqFt + 200))]
    filtered_df =filtered_df.loc[(filtered_df["latestPrice"] >= (latestPrice - 50000)) & (filtered_df["latestPrice"] <= (latestPrice + 50000))]
    filtered_df =filtered_df.loc[(filtered_df["avgSchoolRating"] >= (avgSchoolRating - 0.5)) & (filtered_df["avgSchoolRating"] <= (avgSchoolRating + .5))]
    filtered_df["location"] = filtered_df[["latitude","longitude"]].values.tolist()
    columns = ["zpid","city","zipcode", "location","latestPrice", "numOfBathrooms", "livingAreaSqFt","streetAddress"]
    filtered_df = filtered_df[columns]
    filtered_df.to_json('C:/Users/raney/OneDrive/Desktop/Analysis_Projects/Austin_TX_House_Listings/Raney/static/js/dataset.js', orient = 'records')