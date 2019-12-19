import os


class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') 
	SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') 
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

# export SECRET_KEY='cf239ddb3d442f57d148c74ca64100a5dfaabee0e388cea7cb4eab0ab7f6be33'
# export SQLALCHEMY_DATABASE_URI='sqlite:///site.db'