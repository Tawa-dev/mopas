from app import app          
from app.database import Database      

from flask import render_template, request, url_for, redirect, session
import datetime
import itertools
from bson.objectid import ObjectId


@app.route('/login/reports',methods=['POST','GET'])
def reports():
    msg = ''
    report=''
    if request.method == 'POST':
        # Get form data
        office = request.form['office']
        # Search items with provided info
        # Check if report is for all offices
        if office == "all":
            report = Database.find_report("Items",{})
        else:
            report = Database.find_report("Items",{'Office':office})
        # Check if reports were found 
        if report:
            report = report
        else:
            # items doesnt exist in specified office
            msg = 'No Items Were Found In Specified Office!'
        
    return render_template('report.html', msg=msg,report=report)

