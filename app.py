from flask import Flask
import numpy as np
from flask import render_template,request
import pickle
model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def input():
    return render_template("index.html")
@app.route('/home',methods=["POST"])
def predict():
    company = request.form["company"]
    type = request.form["TypeName"]
    ram = request.form["Ram"]
    weight = request.form["Weight"]
    touchscreen = 1 if request.form["TouchScreen"]=='Yes' else 0 
    ips = 1 if request.form["ips"]=='Yes' else 0
    screen_size = request.form["Inches"]
    resolution = request.form["ScreenResolution"]
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((float(X_res)**2) + (float(Y_res)**2))**0.5/float(screen_size)
    cpu = request.form["Cpu"]
    hdd= request.form["HDD"]
    ssd= request.form["SSD"]
    gpu = request.form["Gpu"]
    os = request.form["OpSys"] 



    data = [
        company,
        type,
        ram,
        weight,
        touchscreen,
        ips,
        ppi,
        cpu,
        hdd,
        ssd,
        gpu,
        os
    ]


    prediction =np.exp(model.predict([data])) 
    array = prediction
    string = str(array)
    string = string.replace("[", "")
    string = string.replace("]", "")
    return render_template("home.html",prediction=string)
if __name__ == "__main__":
    app.run(debug=True)
    