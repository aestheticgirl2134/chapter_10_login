import os
basedir = os.path.abspath (os.path.dirname(__file__))

class Config(object):
    """define app configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY')or 'hard-to-guess'


    #Database configurations
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False