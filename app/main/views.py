"""
Modules needed for main/views.py
flask:
    used render_template to load templates
    used redirect to redirect to specific url
    used url_for to designate the specific url
    used current_app for config data variables
    used flash to send messages to the user
    used request to get information from the ckeditor html form in index.html
app.db_helpers:
    used to add and commit sessions for Post with the put_obj() function
app.models:
    used Post table to add of data every time user successfully submitted a post
    used Tag table to provide a list of tags to decide from when creating a post
app.main:
    used to import the main blueprint where routes are identified from
app:
    used recaptcha for verification purposes - prevent bot spam
"""
from flask import render_template, redirect, url_for, flash, request, current_app
from app.db_helpers import put_obj
from app.models import User, Post, Tag, PostTag
from app.main import main
from app import recaptcha


@main.route('/', methods=['GET', 'POST'])
# TODO: Delete this route, we don't need it anymore - any changes made by simon needs to be implemented into index.html
def index():
    visible_posts = len(Post.query.filter_by(is_visible=True).all())

    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.creation_time.desc()).paginate(
        page, per_page=current_app.config['POSTS_PER_PAGE'],
        error_out=True)
    posts = pagination.items

    page_posts = []

    for post in posts:
        post_tags = PostTag.query.filter_by(post_id=post.id).all()
        tags = []
        for post_tag in post_tags:
            name = Tag.query.filter_by(id=post_tag.tag_id).first().name
            tags.append(name)
        story = {
            'id': post.id,
            'activist_first': post.activist_first,
            'activist_last': post.activist_last,
            'activist_start': post.activist_start,
            'activist_end': post.activist_end,
            'creation_time': post.creation_time,
            'edit_time': post.edit_time,
            'content': post.content,
            'is_visible': post.is_visible,
            'is_edited': post.is_edited,
            'tags': tags
        }
        page_posts.append(story)

    return render_template('new_index.html', posts=page_posts, pagination=pagination, visible_posts=visible_posts)


@main.route('/about', methods=['GET', 'POST'])
def about():
    # TODO: rename this route
    return render_template('about.html')


@main.route('/catalog', methods=['GET', 'POST'])
def catalog():
    # TODO: rename this route and put it into posts/views.py
    # TODO: edit catalog.html to have the contents of postTab.html and then delete postTab.html
    tags = Tag.query.all()
    return render_template('catalog.html', tags=tags)
