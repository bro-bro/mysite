# -*- coding: utf-8 -*-
import facebook

class Group(object):
    def __init__(self, token):
        self.graph = facebook.GraphAPI(access_token=token)
        
    def getgroups(self):
        self.groups = self.graph.get_object("me/groups")
        if self.groups.get('data'):
            return [[group['id'],group['name']] for group in self.groups['data']]
        else:
            return []
        
    def getpages(self):
        self.pages = self.graph.get_connections(id='me', connection_name='accounts')
        if self.pages.get('data'):
            return [[page['id'],page['name']] for page in self.pages['data']]
        else:
            return []

    def create_posts(self, text):
        for i in text.getlist('POST'):
            self.create_post(i, text['textname'])
            
    def create_post(self, i, text):
        self.graph.put_object(parent_object=i, connection_name='feed', message=text.encode('utf-8'))