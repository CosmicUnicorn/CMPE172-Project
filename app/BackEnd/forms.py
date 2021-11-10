from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError, StringField, TimeField, IntegerField, SelectField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email, NumberRange
from wtforms.fields.html5 import EmailField, DateField
from .model import User, DBConnector

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    enrollDate = DateField('Enrollment Date', validators=[DataRequired()],format="%Y-%m-%d")
    submit = SubmitField('Create Student')

class AssignmentForm(FlaskForm):
    worksheet = SelectField('Worksheet', validators=[DataRequired()])
    dueDate = DateField('Due Date', validators=[DataRequired()],format="%Y-%m-%d")
    deliveredDate = DateField('Delivered Date',format="%Y-%m-%d")
    score = IntegerField('Score')
    submit = SubmitField('Confirm')

class EmployeeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    jobTitle = StringField('Job Title', validators=[DataRequired()])
    submit = SubmitField('Add Employee')

#class WorksheetForm(FlaskForm):

#class AttendanceForm(FlaskForm):

#class SubjectForm(FlaskForm):

#class ParentForm(FlaskForm):

class RegisterForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('confirmPassword', message = "Passwords Don't Match!")])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired()])
    centerID = IntegerField("Center ID",validators=[DataRequired()])
    submit = SubmitField('Register Account')

    def validate_username(self, username):
        connector = DBConnector()
        user = connector.queryUser(username.data)
        if user is not None:
            flash("Username is taken.")
            raise ValidationError('Username is taken.')

