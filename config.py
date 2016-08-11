import os


class Config:


    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'localhost'
    # MAIL_PORT = os.environ.get('MAIL_PORT') or 2500
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or False
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or None
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or None
    # MAIL_SUBJECT_PREFIX = os.environ.get('MAIL_SUBJECT_PREFIX') or '[Women\'s Activism NYC]'
    # MAIL_SENDER = os.environ.get('MAIL_SENDER') or 'Women\'s Activism NYC Admin <womensactivismnyc@gmail.com>'
    # WOMENS_ADMIN = 'womensactivismnyc@gmail.com'
    # RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
    # RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')
    # POSTS_PER_PAGE = 10
    # COMMENTS_PER_PAGE = 10
    # RECAPTCHA_ENABLED = True
    # RECAPTCHA_SITE_KEY = os.environ.get('RECAPTCHA_SITE_KEY')
    # RECAPTCHA_SECRET_KEY = os.environ.get('RECAPTCHA_SECRET_KEY')

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'womensactivismnyc@gmail.com'
    MAIL_PASSWORD = 'doris1234'
    MAIL_SUBJECT_PREFIX = '[Womens Activism NYC]'
    MAIL_SENDER = 'Womens Activism NYC Admin <flasky@example.com>'
    WOMENS_ADMIN = 'womensactivismnyc@gmail.com'
    POSTS_PER_PAGE = 10
    COMMENTS_PER_PAGE = 10

    RECAPTCHA_PUBLIC_KEY = '6LetUSYTAAAAALgTT8Rt2nLZ2OTBNph6Qa1TbrAH'
    RECAPTCHA_PRIVATE_KEY = '6LetUSYTAAAAAN1pLPLyyIFUh6rEemXczfMFT4um'

    RECAPTCHA_ENABLED = True
    RECAPTCHA_SITE_KEY = "6LetUSYTAAAAALgTT8Rt2nLZ2OTBNph6Qa1TbrAH"
    RECAPTCHA_SECRET_KEY = "6LetUSYTAAAAAN1pLPLyyIFUh6rEemXczfMFT4um"



    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'postgresql://localhost:5432/womens_activism_nyc_dev'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'postgresql://localhost:5432/womens_activism_nyc_test'


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or None
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or None
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or False
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
