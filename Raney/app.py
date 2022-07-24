from xml.dom.minidom import Document
from flask import Flask, render_template, request
import predictions


app = Flask(__name__)

errorMessage = {}  
featureMessage = {}

def validateForm():
    valid = True
    squarefeet = 0
    schoolrat = 0
    numberofbath = 0
    featureMessage = {}
    errorMessage = {}
    try:
        squarefeet = int(request.form['sqft']) 
        if squarefeet > 0:
            featureMessage["sqftMessage"] = f"Square Footage = {squarefeet}"
        else:
            errorMessage["sqftMessage"] = "Square Feet should be greater than 0"       
            valid = False
    except:
        errorMessage["sqftMessage"] = "Square Feet should be greater than 0"       
        valid = False
    try:
        schoolrat = int(request.form['isd']) 
        if schoolrat > 0:
            featureMessage["isdMessage"] = f"School Rating = {schoolrat}"
        else:
            errorMessage["isdMessage"] = "School Rating should be greater than 0"
            valid = False
    except:
        errorMessage["isdMessage"] = "School Rating should be greater than 0"     
        valid = False
    try:
        numberofbath = int(request.form['bath'])
        if numberofbath > 0:
            featureMessage["bathMessage"] = f"Number of Baths = {numberofbath}"
        else:
            errorMessage["bathMessage"] = "Number of Baths should be greater than 0"
            valid = False
    except:
        errorMessage["bathMessage"] = "Number of Baths should be greater than 0"     
        valid = False
    return valid,squarefeet, schoolrat, numberofbath, featureMessage, errorMessage

@app.route('/')  
def index_page():
    errorMessage = {}  
    return render_template('index.html',errorMessage = errorMessage)

@app.route('/results',methods=['GET','POST'])  
def submit():
    filterCond = {}
    if request.method == 'POST':        
        valid,squarefeet, schoolrat, numberofbath, featureMessage, errorMessage = validateForm()
        print(errorMessage)
        if valid:
            filterCond["livingAreaSqFt"] = squarefeet
            filterCond["avgSchoolRating"] = schoolrat
            filterCond["numOfBathrooms"] = numberofbath
            
            price = predictions.predict_houseprice(filterCond)
            
            featureMessage["priceMessage"] = "Predicted Price = " + '${:,.2f}'.format(price)

            filterCond["latestPrice"] = price


            predictions.jsonify_data(filterCond)

            return render_template('results.html', featureMessage = featureMessage)
        else:
            return render_template('index.html', errorMessage = errorMessage)

if __name__ == "__main__":
   app.run()