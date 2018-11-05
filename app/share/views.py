from flask import render_template, redirect, url_for, flash, request, Markup, current_app

from app.constants import RECAPTCHA_STRING
from app.models import Tags, Events
from app.share import share
from app.share.forms import StoryForm
from app.lib.utils import create_story, create_user, create_subscriber
from app.lib.emails_utils import send_email
from app.db_utils import create_object
from app.constants.event_type import EMAIL_SENT


@share.route('/', methods=['GET', 'POST'])
def new():
    """
    View function for creating a story
    :return: If the story form was fully validated, create a Story and Poster object to store in the database
    """
    form = StoryForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            first_name = form.user_first.data
            last_name = form.user_last.data
            email = form.user_email.data
            phone = form.user_phone.data

            if first_name or last_name or email:
                user_guid = create_user(user_first=first_name,
                                        user_last=last_name,
                                        user_email=email,
                                        user_phone=phone)
                # Email to admin
                if form.subscription.data:
                    create_subscriber(first_name=first_name,
                                      last_name=last_name,
                                      email=email,
                                      phone=phone)

                    email_body = render_template('emails/new_subscriber_agency.html',
                                                 first_name=form.user_first.data,
                                                 last_name=form.user_last.data,
                                                 email=form.user_email.data,
                                                 phone=form.user_phone.data)
                    send_email(subject="WomensActivism - New Subscriber",
                               sender=current_app.config['MAIL_SENDER'],
                               recipients=[current_app.config['MAIL_RECIPIENTS']],
                               html_body=email_body)
                    create_object(Events(
                        _type=EMAIL_SENT,
                        user_guid=user_guid,
                        new_value={"email_body": email_body}
                    ))
                # Email to user
                if form.user_email.data:
                    unsubscribe_link = url_for('unsubscribe.unsubscribe', _external=True)
                    email_user_body = render_template('emails/new_subscriber_user.html',
                                                      first_name=form.user_first.data,
                                                      last_name=form.user_last.data,
                                                      unsubscribe_link=unsubscribe_link)
                    send_email(subject="Confirmation Email",
                               sender=current_app.config['MAIL_SENDER'],
                               recipients=[form.user_email.data],
                               html_body=email_user_body)
                    create_object(Events(
                        _type=EMAIL_SENT,
                        user_guid=user_guid,
                        new_value={"email_body": email_body}
                    ))
            else:
                user_guid = None

            tag_string = form.tags.data
            tags = []
            for t in tag_string.split(','):
                tags.append(Tags.query.filter_by(id=t).one().name)

            story_id = create_story(activist_first=form.activist_first.data,
                                    activist_last=form.activist_last.data,
                                    activist_start=form.activist_start.data,
                                    activist_end=form.activist_end.data,
                                    tags=tags,
                                    content=form.content.data,
                                    activist_url=form.activist_url.data,
                                    image_url=form.image_url.data,
                                    video_url=form.video_url.data,
                                    user_guid=user_guid)
            flash(Markup('Story submitted!'), category='success')
            return redirect(url_for('stories.view', story_id=story_id))
        else:
            for field, error in form.errors.items():
                if field == RECAPTCHA_STRING:
                    flash('Please complete the RECAPTCHA to submit your story.', category="danger")
                else:
                    flash(form.errors[field][0], category="danger")
            return render_template('share/share.html', form=form, tags=Tags.query.order_by(Tags.name).all())
    return render_template('share/share.html', form=form, tags=Tags.query.order_by(Tags.name).all())
