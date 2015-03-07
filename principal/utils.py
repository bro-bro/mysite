import facebook
import sys


class Group(object):
    def __init__(self, token):
        self.graph = facebook.GraphAPI(access_token=token)
        self.groups = self.graph.get_object("me/groups")['data']
        self.pages = self.graph.get_connections(id='me', connection_name='accounts')['data']

    def getgroups(self):
        return tuple([tuple([group['id'],group['name']]) for group in self.groups])

    def getpages(self):
        return tuple([tuple([page['id'],page['name']]) for page in self.pages])



