from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)

# two decorators, same function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = "name" in HTML form
       vin = request.form.get("vin")
       tire_pressure = request.form.get("tire_pressure")
       first_name = request.form.get("first_name")
       last_name = request.form.get("last_name")
       email = request.form.get("email")
       phone_number = request.form.get("phone_number")

       url = f'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/{vin}?format=json'
       r = requests.get(url)
       parsed = json.loads(r.text);		
       pretty_json = json.dumps(parsed, indent =4)
       return "Your vehicle info:  "+ pretty_json 
    return render_template("start.html")

# def start():
#     return render_template('start.html', the_title='Mechanic-Auto-Invoice')
    
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Tiger Home Page')

@app.route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='Tiger As Symbol')

@app.route('/myth.html')
def myth():
    return render_template('myth.html', the_title='Tiger in Myth and Legend')

if __name__ == '__main__':
    app.run(debug=True)
