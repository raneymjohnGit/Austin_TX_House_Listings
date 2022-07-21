from flask import Flask, render_template
import predictions
import jyserver.Flask as js

app = Flask(__name__)

@js.use(app)
class App:
    def __init__(self):
        self.sqft = 2000
        self.schrat = 7
        self.bathcount = 3
        self.houseprice = 1400
    
    def call_preditcion(self):
        self.sqft = self.js.dom.getElementById("sqft").value        
        self.schrat = self.js.document.getElementById("isd").value        
        self.bathcount = self.js.document.getElementById("bath").value      
        print("before call")
        print(self.sqft)
        self.houseprice = predict_houseprice(self.sqft, self.schrat, self.bathcount)
        self.js.document.getElementById("price").innerHTML = 1400
        print("after call")

       

@app.route("/")
def index():
    return App.render(render_template("index.html"))


if __name__ == "__main__":
   app.run()