from flask import redirect, url_for, request, flash
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from movierating import admin, db
from movierating.models import User, Movie

models = [User, Movie]


class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        flash('You must login first', 'info')
        return redirect(url_for('login', next=request.url))


def add_to_admin():
    for model in models:
        admin.add_view(AdminModelView(model, db.session))
