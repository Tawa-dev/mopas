from app import app          
from app.database import Database      

from flask import render_template, request, url_for, redirect, session
import datetime
import itertools
from bson.objectid import ObjectId


@app.route('/login/edit/find-item',methods=['POST','GET'])
def find_item():
    msg = ''
    item=''
    if request.method == 'POST':
        # Get form data
        office = request.form['office']
        Name = request.form['Name']
        # Search items with provided info
        item = Database.find_one("Items",{'Office':office,'Name':Name})
        # Check if a item was found with specified office and name
        if item:
            item = item
        else:
            # item doesnt exist in specified office
            msg = 'No Item Was Found In Specified Office!'

    return render_template('edit_items.html', msg=msg,item=item)

@app.route('/login/edit/edit-items',methods=['POST'])
def edit_items():

    # Fetch for item before its updated
    item_id = request.form['_id']
    query = {"_id": ObjectId(item_id)}

    old_item = Database.find_one("Items",query)

    # Today's Date
    todayDate = datetime.datetime.today()
    # Insert old item in history database
    items = {"Office": old_item['Office'],"Name":old_item['Name'],"Quantity":old_item['Quantity'],"Date":todayDate,"Supplier":old_item['Supplier'],"Invoice_Num":old_item['Invoice_Num'],"User":session["username"]}
    Database.insert("history",items)
    # Update office items
    
    # Get updated form data
    username = session['username']
    office = request.form['office']
    Name = request.form['Name']
    quantity = int(request.form['quantity'])
    # Convert Date back to Date
    aDate = datetime.datetime.strptime(request.form['aDate'], '%Y-%m-%d')
    supplier = request.form['supplier']
    invoice = request.form['invoice']

    # Set new values
    
    updated_items = {"$set":{"Office": office,"Name": Name,"Quantity":quantity,"Date":aDate,"Supplier":supplier,"Invoive_Num":invoice}}
    Database.update_one("Items",query,updated_items)
    msg = 'Office Item/s Updated'
    return render_template('edit_items.html',msg=msg)

@app.route('/login/edit/remove-items',methods=['POST'])
def remove_items():
    # Get form data
    item_id = request.form['_id']
    query = {"_id": ObjectId(item_id)}
    
    # Remove items with specified id
    Database.delete("Items",query)

    msg = 'Office Item/s Removed'
    return render_template('edit_items.html',msg=msg)