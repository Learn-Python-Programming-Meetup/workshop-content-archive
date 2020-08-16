from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.secret_key = "My secret"

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"

    from home import home_bp
    from auth import auth_bp
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from model import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    db.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=7000, debug=True)

