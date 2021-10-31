from flask import render_template, redirect, flash, request
from __init__ import flaskApp, login
from .forms import LoginForm, RegisterForm, StudentForm
from .model import User, DBConnector
from flask_login import current_user, login_required, logout_user, login_user
from .student import Student

@login_required
@flaskApp.route("/",methods=['GET', 'POST'])
def default():
    logout_user()
    return redirect("/login")
    #if not current_user.is_authenticated:
        #return redirect("/home")
    #user = current_user
    #events = Event.query.filter_by(username=user.username).all()
    #return render_template('index.html', title='Home',user = user, events = events)

@flaskApp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect("/students")
    form = LoginForm()
    if form.validate_on_submit():
        
        connector = DBConnector()
        user = connector.queryUser(username=form.username.data)
        
        if(user is None or not user.check_password(form.password.data)):
            flash('Invalid Username or Password')
            return redirect("login")
        login_user(user, remember=form.remember_me.data)
        return redirect("/students")

    return render_template('login.html', title='Login', form=form)

@flaskApp.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect("/login")

@flaskApp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect("/students")
    form = RegisterForm()
    if form.validate_on_submit():
        connector = DBConnector()
        user = connector.registerUser(form.username.data, form.password.data, form.centerID.data)
        if(user is not None):
            flash('Account created')
            return redirect('login')
        else:
            flash('Failed to create account.')
            return redirect('register')
    return render_template('register.html', title='Register', form=form)

@login_required
@flaskApp.route('/students', methods=['GET', 'POST'])
def studentsPage():
    if not current_user.is_authenticated:
        return redirect("/login")
    form = StudentForm()
    connector = DBConnector()
    studentsList = connector.queryStudents()
    if form.validate_on_submit():
        student = Student(name=form.name.data, enrollDate=form.enrollDate.data, centerID=current_user.centerID)
        connector.insertStudent(student)
        return redirect("/students")
    return render_template('students.html', title='Students', students=studentsList, form=form)

@login_required
@flaskApp.route('/student/<id>', methods=['GET', 'POST'])
def studentPage(id):
    pass