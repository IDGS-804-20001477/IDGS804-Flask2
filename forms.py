from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField, PasswordField
from wtforms import validators
from wtforms.fields import EmailField

def My_Validation(form, field):
    if len(field.data) == 0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula = StringField('Matricula', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=5, max=10, message='Ingresa min 5 max 10')
    ])
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El campo nombre es requerido')
    ])
    apaterno = StringField('Apaterno', [
        My_Validation
    ])
    amaterno = StringField('Amaterno')
    email = EmailField('Correo')

class WordsForm(Form):
    spanish = StringField('Spanish')
    english = StringField('English')

class LoginForm(Form):
    username = StringField('usuario', [
        validators.DataRequired(message='El campo Usuario es requerido'),
        validators.length(min = 5, max = 20, message = 'Ingresa min 5 max 10')
    ])
    password = PasswordField('Contrasenia', [
        validators.DataRequired(message = 'El campo Contrasenia es requerido'),
        validators.length(min = 5, max = 10, message = 'El campo Contrasenia es requerido')
    ])