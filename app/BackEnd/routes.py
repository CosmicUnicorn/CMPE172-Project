from flask import render_template, redirect, flash, request
from app import flaskApp, login
from .forms import LoginForm, RegisterForm
from flask_login import current_user, login_required, logout_user, login_user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect("/home")
    form = LoginForm()
    if form.validate_on_submit():
        
        #check if username and password are correct

        #if they are correct:
        login_user(user, remember=form.remember_me.data)
        return redirect("/home")
    return render_template('login.html', title='Login', form=form)