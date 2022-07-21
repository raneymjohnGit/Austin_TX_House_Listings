from flask import Flask, render_template
import predictions
import jyserver.Flask as js
from jyserver.Server import Client, Server

app = Flask(__name__)

@js.use(app)
class App:
    def __init__(self):
        self.sqft = 2000
        self.schrat = 7
        self.bathcount = 3
        self.houseprice = 0
        self.count = 0
    
    def call_prediction(self):
        #self.sqft = self.js.document.getElementById("sqft").value        
        #self.schrat = self.js.document.getElementById("isd").value        
        #self.bathcount = self.js.document.getElementById("bath").value      
        #print("before call")
        #print(str(self.sqft))
        #self.houseprice = predictions.predict_houseprice(self.sqft, self.schrat, self.bathcount)
        self.count += 1
        self.js.dom.price.innerHTML = self.count
        print('after call')

       

@app.route("/")
def index():
    return App.render(render_template("index.html"))


if __name__ == "__main__":
   app.run()