import os
from datetime import timedelta

class Config(object):
	MONGODB_SETTINGS = {
		'db': 'posts',
		'host': 'mongodb+srv://{}:{}@blogdb.8xcwj.mongodb.net/Blogdb?retryWrites=true&w=majority'.format(os.getenv('USERNAME'), os.getenv('PASSWORD')),
		'port': 27017,
	}
	SECRET_KEY = os.urandom(24)
	PERMANENT_SESSION_LIFETIME = timedelta(days=31)

class ProdConfig(Config):
	pass

class DevConfig(Config):
	DEBUG = True
