from re import I
from flask import Flask

app = Flask(__name__)

from app import views
from app import add_items
from app import edit_items
from app import history
from app import report
from app.database import Database


@app.before_first_request
def initialize_database():
    Database.initialize()
