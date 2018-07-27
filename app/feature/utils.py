"""
Utility functions used for view functions involving featured stories
"""
from flask_login import current_user

from app.constants.event import ADD_FEATURED_STORY, HIDE_FEATURED_STORY, EDIT_FEATURED_STORY
from app.db_utils import update_object, create_object
from app.models import Events, FeaturedStories


def create_featured_story(story, left_right, title, description, rank):
    """
    A utility function to create a featured story.
    :param story: the story object you would like to create in Featured Story
    :param left_right: left or right side where the image will go
    :param description: description of the activist
    :param rank: the order of the featured story

    :return: None
    """

    #current_featured_story = FeaturedStories.query.filter_by(is_visible=True)
    #if current_featured_story is not None:
    #    update_object({"is_visible": False}, FeaturedStories, current_featured_story.id)

    featured_story = FeaturedStories(
        story_id=story.id,
        left_right=True if left_right == 'left' else False,
        is_visible=True,
        title=title,
        description=description,
        rank=rank
    )

    create_object(featured_story)

    create_object(Events(
        story_id=story.id,
        user_guid=story.user_guid,
        _type=ADD_FEATURED_STORY,
        new_value=featured_story.val_for_events
    ))


def update_featured_story(featured_story, left_right, title, is_visible, description, rank):
    """
    A utility function to update a featured story.
    Updating attributes such as the following:
    :param featured_story:
    :param left_right: left or right side where the image will go
    :param is_visible: the visibility of the featured story
    :param description: description of the activist
    :param rank: the order of the featured story

    :return: None
    """
    featured_story_fields = {
        "left_right",
        "is_visible",
        "title",
        "description",
        "rank"
    }

    featured_story_field_vals = {
        "left_right": left_right,
        "is_visible": is_visible,
        "title": title,
        "description": description,
        "rank": rank
    }

    old = {}
    new = {}

    for field in featured_story_fields:
        val = featured_story_field_vals[field]
        if val is not None:
            if val == '':
                featured_story_field_vals[field] = None  # null in db, not empty string
            cur_val = getattr(featured_story, field)
            new_val = featured_story_field_vals[field]
            if cur_val != new_val:
                old[field] = cur_val
                new[field] = new_val
                print(new_val)

    if new:
        cur_rank = getattr(featured_story, "rank")

        update_object(new, FeaturedStories, featured_story.id)

        if new.get('is_visible') is not True or new.get('rank'):
            update_rank(featured_story.story_id, cur_rank, rank)

        create_object(Events(
            _type=EDIT_FEATURED_STORY,
            story_id=featured_story.story_id,
            user_guid=current_user.guid,
            previous_value=old,
            new_value=new
        ))


def hide_current_featured_story(story_id):
    """
    A utility function to hide a visible featured story (main page).
    Hiding does not *delete* the record from the table, but rather makes it invisible.
    :param: story_id: story id of the featured story that will be hidden

    :return: None
    """
    featured_story = FeaturedStories.query.filter_by(story_id=story_id, is_visible=True).one_or_none()
    
    # current_featured_story = FeaturedStories.query.filter_by(is_visible=True).one_or_none()
    
    if featured_story is not None:
        update_object({"is_visible": False}, FeaturedStories, featured_story.id)

        create_object(Events(
            _type=HIDE_FEATURED_STORY,
            story_id=featured_story.story_id,
            user_guid=current_user.guid,
            previous_value={"is_visible": True},
            new_value={"is_visible": False}
        ))


def update_rank(story_id, old_rank, new_rank):
    """
    A utility function to update the ranks of the featured stories when a change is made.
    :param story_id: story id of the featured story that is modified
    :param old_rank:
    :param new_rank:

    :return: None
    """

    featured_story = FeaturedStories.query.filter_by(story_id=story_id).one_or_none()
    featured_stories = FeaturedStories.query.filter_by(is_visible=True).all()

    if featured_story.is_visible:
        if old_rank is not None:
            if old_rank < new_rank:
                for story in featured_stories:
                    if story.story_id is not featured_story.story_id and old_rank < story.rank <= new_rank:
                        update_object({"rank": story.rank-1}, FeaturedStories, story.id)
            else:
                for story in featured_stories:
                    if story.story_id is not featured_story.story_id and old_rank > story.rank >= new_rank:
                        update_object({"rank": story.rank+1}, FeaturedStories, story.id)
        else:
            for story in featured_stories:
                if story.story_id is not featured_story.story_id and story.rank >= new_rank:
                    update_object({"rank": story.rank+1}, FeaturedStories, story.id)

    else:
        update_object({"rank": None}, FeaturedStories, featured_story.id)
        if old_rank is not None:
            for story in featured_stories:
                if story.id != featured_story.id and story.rank >= old_rank:
                    update_object({"rank": story.rank-1}, FeaturedStories, story.id)
