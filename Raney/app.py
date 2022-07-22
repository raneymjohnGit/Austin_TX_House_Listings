from xml.dom.minidom import Document
from flask import Flask, render_template, request
import predictions

app = Flask(__name__)

@app.route('/')  
def index_page():
    return render_template('index.html')

@app.route('/results',methods=['GET','POST'])  
def submit():
    print('before')
    errorMessage = ""    
    sqftMessage = ""
    isdMessage = ""
    bathMessage = ""
    priceMessage = ""
    bedMessage = ""
    if request.method == 'POST':                
        try:
            squarefeet = int(request.form['sqft'])
            sqftMessage = f"Square Footage = {squarefeet}"
        except:
            if errorMessage == "":
                errorMessage = "Square Feet needs to greater than 0"                                
        try :
            schoolrat = int(request.form['isd'])
            isdMessage = f"School Rating = {schoolrat}"
        except :
            if errorMessage == "":
                errorMessage = "School Rating needs to greater than 0"
            else:    
                errorMessage += " \n School Rating needs to greater than 0"
        try:
            numbeofbath = int(request.form['bath'])
            bathMessage = f"Number of Baths = {numbeofbath}"
        except:
            if errorMessage == "":
                errorMessage = "School Rating needs to greater than 0"
            else:
                errorMessage +=  "\n School Rating needs to greater than 0"
        if errorMessage == "":
            price = predictions.predict_houseprice(squarefeet, schoolrat, numbeofbath)
            priceMessage = "Predicted Price = " + '${:,.2f}'.format(price)

            


            return render_template('results.html', sqftMessage = sqftMessage, isdMessage= isdMessage, bathMessage= bathMessage,bedMessage = bedMessage,priceMessage = priceMessage)
        else:
            return render_template('index.html', errorMessage = errorMessage)

if __name__ == "__main__":
   app.run()