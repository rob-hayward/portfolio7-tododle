import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'H@142088925r'

    LOCAL_USERNAME = 'rob_hayward'
    LOCAL_PASSWORD = 'new_password'
    LOCAL_DBNAME = 'tododledb'
    DATABASE_URL = os.environ.get('DATABASE_URL') or \
                   f'postgresql://{LOCAL_USERNAME}:{LOCAL_PASSWORD}@localhost:5432/{LOCAL_DBNAME}'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
