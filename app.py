# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 17:24:08 2022

@author: shrey
"""

from flask import  render_template ,request, flash ,Flask, redirect, url_for

import pandas as pd

import pickle
# importing model

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is the secret key'



@app.route('/')  
def home():  
    return render_template("home.html")

@app.route('/')
def back():
    return redirect(url_for('app.home'))

@app.route('/contact')
def contact():
    return render_template('info.html')

@app.route('/success', methods = ['POST'])  
def success():  
    #if request.method == 'POST':  
     
    
    l = []
    brand = request.form.get('brand')
    car_model = request.form.get('model')
    fuel = request.form.get('fuel')
    gear_type = request.form.get('gear_type')
    offer_type = request.form.get('offer_type')
    hp = float(request.form.get('hp'))
    km = int(request.form.get('KMs_driven'))
    year = int(request.form.get('year'))
    age = 2022 - year
        
    #flash('File uploaded!', category='success')
    
    l.append(brand) 
    l.append(car_model)
    l.append(fuel)
    l.append(gear_type)
    l.append(offer_type)
    l.append(hp)
    l.append(km)
    l.append(age)
    
    
    if (len(l)):
        flash('File uploaded!', category='success')
       
        df = pd.DataFrame([[brand, car_model, fuel , gear_type , offer_type , hp , km , age]] ,
        columns=["Brand", "Model","fuel",'Gear_type','offerType' ,'Hp','KMs_driven',"Age"])
        
        pred = model.predict(df)
        your_list = pred
        return render_template('process.html', your_list = your_list)
    else:
        flash("File upload unsuccessful",category = 'error')
            
    return render_template("home.html")  

# =============================================================================
#     return render_template('login.html' , text= "Testing",user = "SGA")
# =============================================================================

   # return render_template("login.html", user=current_user)



if __name__ == '__main__':
    app.run(debug=True)