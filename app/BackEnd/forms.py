from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError, StringField, TimeField, IntegerField, SelectField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email, NumberRange
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

#class StudentForm(FlaskForm):

#class EmployeeForm(FlaskForm):

#class AssignmentForm(FlaskForm):

#class WorksheetForm(FlaskForm):

#class AttendanceForm(FlaskForm):

#class SubjectForm(FlaskForm):

#class ParentForm(FlaskForm):

class RegisterForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('confirmPassword', message = "Passwords Don't Match!")])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register Account')

    #def validate_username(self, username):
        #check if user already exists
        #if user is not None:
            #flash("Username is taken.")
            #raise ValidationError('Username is taken.')

