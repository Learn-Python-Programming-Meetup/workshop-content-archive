from flask import Flask
from app.db import db


def create_app(db_name=None):
    app = Flask(__name__)
    app.secret_key = "My secret"

    if db_name is None:
        db_name = 'db'
    else:
        db_name = db_name

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{db}.sqlite".format(db=db_name)

    from app.api.person import person_bp
    app.register_blueprint(person_bp)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=7000, debug=True)
