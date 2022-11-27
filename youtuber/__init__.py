from flask import Flask
from flask_sqlalchemy import SQLAlchemy






app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///youtube.db'
app.config['UPLOAD_FILE'] = '' #put full path of videos folder (inside static directory) example in app-guide.txt
db = SQLAlchemy(app)

from youtuber import routes