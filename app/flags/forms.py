"""
Modules needed for flags/forms.py
flask_wtf:
    used class Form from which FlagsForm inherits from
wtforms:
    used SelectField for drop down list of options
    used TextAreaField for area for user's explanation
    used SubmitField for submit button
wtforms.validators:
    used Length to verify the length maximum of 500 characters
flask_wtf.recaptcha:
    used RecaptchaField for Recaptcha verification of form submission
app.utils:
    used flag_choices list to populate the drop down menu
"""
from flask_wtf import Form
from wtforms import SelectField, SubmitField, TextAreaField
from wtforms.validators import Length
from flask_wtf.recaptcha import RecaptchaField
from app.utils import flag_choices


class FlagsForm(Form):
    """
    FlagsForm used for user to create a flag ticket that identifies something wrong with post/comment
    flag_reason is a drop down menu that includes all possible reasons to flag something
    flag_description is a box where a user can type their explanation for flagging something
    """
    flag_reason = SelectField('Please choose a reason for flagging:', choices=flag_choices)
    flag_description = TextAreaField('Please provide a brief description:', validators=[Length(0, 500)])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')
