#forms.py under sdwan folder

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddTest(FlaskForm):

    test_name = StringField('Name of new test: ')
    submit = SubmitField('Create Test')

class DelTest(FlaskForm):

    id = IntegerField('ID of test being removed: ')
    submit = SubmitField('Delete Test')

