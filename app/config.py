import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://newuser:password@localhost/flasktest'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
