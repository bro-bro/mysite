# -*- coding: utf-8 -*-
import facebook
from utils import Group
import mock
from mock import Mock
import unittest

class SimpleFacebookTestCase(unittest.TestCase):
    
#    def test_create_post(self):
 #       groups = Group("fakeOAuth")
  #      groups.graph.put_object = mock.create_autospec(groups.graph.put_object)
   #     groups.create_post("me","gooz")
    #    groups.graph.put_object.assert_called_with(parent_object = "me", connection_name="feed", message="gooz")

    def test_getgroups(self):
        self.groups = Group("fakeOAuth")
        self.groups.graph = Mock()
        self.groups.graph.get_object = Mock(return_value=dict())
        self.groups.getgroups()
        self.groups.graph.get_object.assert_called_with('me/groups')

    def test_getpages(self):
        self.groups = Group("fakeOAuth")
        self.groups.graph = Mock()
        self.groups.graph.get_connections = Mock(return_value=dict())
        self.groups.getpages()
        self.groups.graph.get_connections.assert_called_with(id='me', connection_name='accounts')


    def test_create_post(self):
        self.groups = Group("fakeOAuth")
        self.groups.graph = Mock()
        self.groups.graph.put_object = Mock()
        self.groups.create_post("me","gooz")
        self.groups.graph.put_object.assert_called_with(parent_object = "me", connection_name="feed", message="gooz")

