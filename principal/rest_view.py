
# -*- coding: utf-8 -*-
from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from form import Group_List
from views import CreatePost, form_list
from utils import Group
import jwt
from datetime import datetime

class PostResource(DjangoResource):

    def list(self):
        social_user = self.request.user.social_auth.get(provider='facebook',)
        token = social_user.extra_data['access_token']
        group = Group(token)
        authtoken = jwt.encode({'user': str(social_user)}, 'secret')
        fake_db = [
        {
            "facebook token": str(token),
            "authtoken": str(authtoken),
            "username": str(social_user),
            "Groups": group.getgroups(),
            "Pages": group.getpages(),
        }
        ]
        return fake_db

    def create(self):
        social_user = self.request.user.social_auth.get(provider='facebook',)
        group = Group(social_user.extra_data['access_token'])
        group.create_posts(self.data['text'],[self.data['send']])
        return "Post created"


    def is_authenticated(self):
        if self.request.META.get('HTTP_AUTHORIZATION') == "hello":
            #login facebook
            return True
        else: 
            token = self.request.META.get('HTTP_AUTHORIZATION')
            try:
                detoken = jwt.decode(token, 'secret')
            except AttributeError:
                return False
            self.social_user = self.request.user.social_auth.get(provider='facebook',)
            if detoken == {"user": str(self.social_user)}:
                return True
            else:
                return False
       
