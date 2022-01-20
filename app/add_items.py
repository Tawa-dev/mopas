from app import app          
from app.database import Database   

from flask import render_template, request, url_for, redirect, session
import datetime
import itertools
from bson.objectid import ObjectId


@app.route('/login/add-items/',methods=['POST','GET'])
def add_items():
    msg = ''
    
    if request.method == 'POST':
        username = session['username']
        # Get form data
        office = request.form['office']
        Name = request.form['Name']
        quantity = int(request.form['quantity'])
        aDate = datetime.datetime.strptime(request.form['aDate'], '%Y-%m-%d')
        supplier = request.form['supplier']
        invoice = request.form['invoice']
        
        # Insert items
        items = {"Office": office,"Name": Name,"Quantity":quantity,"Date":aDate,"Supplier":supplier,"Invoice_Num":invoice}
        Database.insert("Items",items)
    
        msg = 'Successfully Added Items'

    return render_template('add_items.html', msg=msg)



