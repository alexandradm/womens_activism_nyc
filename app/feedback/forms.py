# TODO: Module level docstring
from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf.recaptcha import RecaptchaField


class FeedbackForm(Form):
    # TODO: Description of form with form fields
    subject = StringField('Subject', validators=[DataRequired("Please enter the subject."), Length(1, 64)])
    email = StringField('Email', validators=[DataRequired("Please enter your email."), Email(), Length(1, 64)])
    reason = TextAreaField('Comments', validators=[DataRequired("Please enter your report."), Length(1, 500)])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')