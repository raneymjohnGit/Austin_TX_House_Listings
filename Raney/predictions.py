import joblib

def predict_houseprice (sqft = 2000, schrat = 7, bathcount = 3):
    model = joblib.load("model.joblib")
    predictions = model.predict([[sqft,schrat,bathcount]])
    print("inside predict_house")
    return predictions[0]
