"""from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # load .env file

MONGO_URI = os.getenv("MONGO_URI")  # Your Atlas connection string
client = MongoClient(MONGO_URI)
db = client['placementcord']

# Collections
students_col = db['Student']
admins_col = db['Admin']
jobs_col = db['jobs']"""
#applications_col = db['applications']






from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

#app = Flask(__name__)
# ----------------------------
# Gemini API key
# # ----------------------------


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ----------------------------
# PostgreSQL Configuration
# ----------------------------
"""app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("POSTGRES_URI")  # PostgreSQL connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False"""
sql_db = SQLAlchemy()  # SQLAlchemy instance NOT linked to app yet

# ----------------------------
# MongoDB Configuration
# ----------------------------
MONGO_URI = os.getenv("MONGO_URI")  # MongoDB Atlas connection string
mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client['placementcord']

# Collections
students_col = mongo_db['Student']
admins_col = mongo_db['Admin']
jobs_col = mongo_db['jobs']
#applications_col = mongo_db['applications']

# Optional: print to confirm connections
#print("PostgreSQL and MongoDB configured successfully!")
