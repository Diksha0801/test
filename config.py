import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dbmappper import DbEngine

"""This script prompts a to create configuration"""

# Get the underlying Flask app instance
APP = Flask(__name__)
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Create the SqlAlchemy db instance
DB = SQLAlchemy(APP)
DbSession = DbEngine
