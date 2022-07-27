from xml.dom.minidom import Document
from flask import Flask, render_template, request
import predictions


app = Flask(__name__)


def validateForm():
    valid = True
    zipcode = ""
    yearBuilt = 0
    lotSizeSqFt = 0
    livingAreaSqFt = 0
    avgSchoolRating = 0
    featureMessage = {}
    errorMessage = {}
    featureValues ={}
    selectionMessage = {}
    try:
        zipcode = request.form['zipcode']
        if zipcode != "":
            featureMessage["zipcode"] = f"Zipcode = {zipcode}"
            featureValues["zipcode"] = zipcode
            selectionMessage["zipcode"] = f"Zipcode selected is {zipcode}"       
        else:
            errorMessage["zipcode"] = "Zipcode should be selected"       
            valid = False
    except:
        errorMessage["zipcode"] = "Zipcode should be selected" 
        valid = False
    try:
        yearBuilt = int(request.form['yearBuilt']) 
        if yearBuilt > 0:
            featureMessage["yearBuilt"] = f"Year Built = {yearBuilt}"
            featureValues["yearBuilt"] = yearBuilt
            selectionMessage["yearBuilt"] = f"Year Built between  {yearBuilt - 5} and {yearBuilt + 5} "
        else:
            errorMessage["yearBuilt"] = "Year Built should be greater than 0"       
            valid = False
    except:
        errorMessage["yearBuilt"] = "Year Built should be greater than 0"     
        valid = False
    try:
        lotSizeSqFt = int(request.form['lotSizeSqFt']) 
        if lotSizeSqFt > 0:
            featureMessage["lotSizeSqFt"] = f"Lot Size Square Feet = {lotSizeSqFt}"
            featureValues["lotSizeSqFt"] = lotSizeSqFt
            selectionMessage["lotSizeSqFt"] = f"Lot Size Square Feet between  {lotSizeSqFt - 2000} and {lotSizeSqFt + 2000}"
        else:
            errorMessage["lotSizeSqFt"] = "Lot Size Square Feet should be greater than 0"       
            valid = False
    except:
        errorMessage["lotSizeSqFt"] = "Lot Size Square Feet should be greater than 0"  
        valid = False
    try:
        livingAreaSqFt = int(request.form['livingAreaSqFt']) 
        if livingAreaSqFt > 0:
            featureMessage["livingAreaSqFt"] = f"Living Area Square Feet = {livingAreaSqFt}"
            featureValues["livingAreaSqFt"] = livingAreaSqFt
            selectionMessage["livingAreaSqFt"] = f"Living Area Square Feet between  {livingAreaSqFt - 200} and {livingAreaSqFt + 200} "
        else:
            errorMessage["livingAreaSqFt"] = "Living Area Square Feet should be greater than 0"       
            valid = False
    except:
        errorMessage["livingAreaSqFt"] = "Living Area Square Feet should be greater than 0"     
        valid = False
    try:
        avgSchoolRating = int(request.form['avgSchoolRating']) 
        if avgSchoolRating > 0:
            featureMessage["avgSchoolRating"] = f"Average School Rating = {avgSchoolRating}"
            featureValues["avgSchoolRating"] = avgSchoolRating
            selectionMessage["avgSchoolRating"] = f"Average School Rating between  {avgSchoolRating - 1} and {avgSchoolRating + 1} "
        else:
            errorMessage["avgSchoolRating"] = "Average School Rating should be greater than 0"
            valid = False
    except:
        errorMessage["avgSchoolRating"] = "Average School Rating should be greater than 0"     
        valid = False
    return valid,featureValues,featureMessage, selectionMessage, errorMessage

@app.route('/')  
def index_page():
    errorMessage = {}  
    return render_template('index.html',errorMessage = errorMessage)

@app.route('/results',methods=['GET','POST'])  
def submit():

    featureValues = {}
    selectionMessage = {}
    featureMessage = {}
    errorMessage = {}    

    if request.method == 'POST':        
        valid,featureValues,featureMessage, selectionMessage, errorMessage = validateForm()
        print(errorMessage)
        if valid:                    
            price = predictions.predict_houseprice(featureValues)
            
            featureMessage["priceMessage"] = "Predicted Price = " + '${:,.2f}'.format(price)
            print(featureMessage["priceMessage"])

            #featureValues["latestprice"] = price


            predictions.jsonify_data(featureValues)

            return render_template('results.html', featureMessage = featureMessage,selectionMessage = selectionMessage)
        else:
            return render_template('index.html', errorMessage = errorMessage)

if __name__ == "__main__":
   app.run()