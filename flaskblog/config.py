import os #for env var


class Config:
    SECRET_KEY = '3090657a7c7bbbfebf02f365802085fe'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'silenme3@gmail.com' #os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = 'SilenAa7@'#os.environ.get('EMAIL_PASS')
