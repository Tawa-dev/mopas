from app import app          
from app.database import Database      

from flask import render_template, request, url_for, redirect, session
import datetime
import itertools
from bson.objectid import ObjectId


@app.route('/login/find-history',methods=['POST','GET'])
def find_history():
    msg = ''
    history=''
    if request.method == 'POST':
        # Get form data
        office = request.form['office']
        Name = request.form['Name']
        # Search item with provided info
        history = Database.find("history",{'Office':office,'Name':Name})
        # Check if history was found 
        if history:
            history = history
        else:
            # item doesnt exist in specified office
            msg = 'No Item Was Found In Specified Office!'

    return render_template('history.html', msg=msg,history=history)

