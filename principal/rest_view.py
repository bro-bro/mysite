
# -*- coding: utf-8 -*-
from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from form import Group_List
from views import CreatePost, form_list
from utils import Group

from models import ApiKey



class PostResource(DjangoResource):

    def list(self):
        social_user = self.request.user.social_auth.get(provider='facebook',)
        group = Group(social_user.extra_data['access_token'])
        token = social_user.extra_data['access_token']
        username = social_user
        fake_db = [
        {
            "token": token,
            "username": str(username),
            "Groups": group.getgroups(),
            "Pages": group.getpages(),
        }
        ]
        return fake_db

    def create(self):
        social_user = self.request.user.social_auth.get(provider='facebook',)
        group = Group(social_user.extra_data['access_token'])
        group.create_posts(self.data['text'],['me'])
        return "ok"


    def is_authenticated(self):
        return True



