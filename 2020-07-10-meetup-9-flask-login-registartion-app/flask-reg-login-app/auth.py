from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from form import RegistrationForm, LoginForm
from model import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user is None:
            flash('user does not exist')
            return redirect(url_for('auth.login'))

        if not check_password_hash(user.password, password):
            flash('password wrong')
            return redirect(url_for('auth.login'))

        login_user(user)
        return redirect(url_for('home.index'))
    return render_template('login.html', form=login_form)


@auth_bp.route("/registration", methods=['GET', 'POST'])
def registration():
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exist')
            return redirect(url_for('auth.registration'))
        new_user = User(email=email, name=name, password=generate_password_hash(password=password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        flash('Thanks for registartion')
        return redirect(url_for('auth.login'))
    return render_template('registration.html', form=registration_form)


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
