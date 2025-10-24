from flask import Flask
from flask_cors import CORS
#from routes.auth_route import auth_bp

from routes.student_route import student_bp
from routes.admin_route import admin_bp
from routes.config import sql_db

from routes.chatbot_route import chatbot_bp

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
#CORS(app)  # enable CORS for React frontend
CORS(app, origins=["http://localhost:3000"], supports_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("POSTGRES_URI")  # PostgreSQL connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

sql_db.init_app(app)

#app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(student_bp, url_prefix="/api/student")
app.register_blueprint(admin_bp, url_prefix="/api/admin")

app.register_blueprint(chatbot_bp, url_prefix="/api/chatbot")


if __name__ == "__main__":
    app.run(debug=True)
