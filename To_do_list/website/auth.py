from flask import Blueprint, render_template, request, redirect, flash, url_for
from .models import User_Name
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, current_user, logout_user, login_required

auth = Blueprint('auth',__name__)


@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method== 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User_Name.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Please type correct password')
        else:
            flash('Please type correct credentials')

    return render_template("login.html",user=current_user)



@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if len(name)<2:
            flash('Name must be greater than 1 character',category='error')
        elif len(email)<4:
            flash('Email must be greater than 3 characters',category='error')
        elif len(password)<7:
            flash('Password must be greater than 6 characters',category='error')
        else:
            new_user = User_Name(name=name, email=email, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))
    
    return render_template("signup.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))