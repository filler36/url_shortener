from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'LKdhs23H43Gdj122H50Jfd8HlQl30Kfh24h9d'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app