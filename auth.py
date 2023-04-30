from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app, Flask
from flask_login import login_required, logout_user
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_user
import time
from flask_mail import Mail, Message

auth = Blueprint('auth', __name__)

mail_app = Flask(__name__)
#Email app config
mail_app.config['MAIL_SERVER']='smtp.gmail.com'
mail_app.config['MAIL_PORT'] = 587
mail_app.config['MAIL_USERNAME'] = 'georgsinventory@gmail.com'
mail_app.config['MAIL_PASSWORD'] = 'udqkmynqxdduvvci'
mail_app.config['MAIL_USE_TLS'] = True
mail_app.config['MAIL_USE_SSL'] = False
mail = Mail(mail_app)


@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    print(user)

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
    
    if not user.is_active:
        flash('Your account is not active')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    time.sleep(3)
    return redirect(url_for('main.index'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@login_required
@auth.route('/logout')
def logout():    
    logout_user()
    time.sleep(3)
    return redirect(url_for('main.index'))

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    confirm = request.form.get('confirm_password')
    surname = request.form.get('surname')
    api_key = request.form.get('api_key')
    user_name = request.form.get('user')
    is_admin = False
    is_active = False

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
    username = User.query.filter_by(username=user_name).first()

    if password != confirm:
        flash('Passwords are different.. Typo?')
        return redirect(url_for('auth.signup'))
    elif user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address: ' + email + ' already exists')
        return redirect(url_for('auth.signup'))
    elif username: # if a username is found, we want to redirect back to signup page so user can try again
        flash('Username: ' + str(username) + ' already exists')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(username=user_name, surname=surname, name=name, email=email, password=generate_password_hash(password, method='sha256'), api_key=api_key, is_admin=is_admin, is_active=is_active)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    
    #send email to user
    msg = Message('Hey your account was succesfully created!', sender =   'georgsinventory@gmail.com', recipients = [email])
    msg.body = "An email has been sent to the Admin for granting you access to your own Inventory. You'll receive an email notification once your account is active."
    mail.send(msg)
    
    #send email to admin
    msg2 = Message('New Access Request!', sender =   'georgsinventory@gmail.com', recipients = ['lofflerg@hotmail.com'])
    msg2.body = "New User " + str(email) + " has requested access for the inventory."
    mail.send(msg2)

    time.sleep(3)
    flash("Account Created! You can now Log In.")
    return redirect(url_for('auth.login'))