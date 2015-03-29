# -*- coding: utf-8 -*-
import facebook
from utils import Group
import mock
from mock import Mock
import unittest
from django.test import TestCase
import random
import string
class SimpleFacebookTestCase(TestCase):

    def setUp(self):
        self.groups = Group("fakeOAuth")
        self.groups.graph = Mock()
        
    def test_getgroups_empty(self):
        self.groups.graph.get_object = Mock(return_value=dict())
        self.assertEqual(self.groups.getgroups(), [])

    def test_getgroups_with_data(self):
        self.groups.graph.get_object = Mock(return_value={'data':[{'id':'1', 'name':'a'},
                                                                  {'id':'4', 'name':'d'},
                                                                  {'id':'3', 'name':'c'},
                                                                  {'id':'2', 'name':'b'}]})
        self.assertEqual(self.groups.getgroups(), [['1', 'a'], ['4', 'd'], ['3','c'], ['2', 'b']])


    def test_getpages_empty(self):
        self.groups.graph.get_connections = Mock(return_value=dict())
        self.assertEqual(self.groups.getpages(), [])

    def test_getpages_with_data(self):
        self.groups.graph.get_connections = Mock(return_value={'data':[{'id':'1', 'name':'a'},
                                                                  {'id':'4', 'name':'d'},
                                                                  {'id':'3', 'name':'c'},
                                                                  {'id':'2', 'name':'b'}]})
        self.assertEqual(self.groups.getpages(), [['1', 'a'], ['4', 'd'], ['3','c'], ['2', 'b']])
      
    def test_create_posts(self):
        self.text = random_text(40)
        for cntr in range(1,15):
            self.form = [[random_digits(10), random_text(10)],
                         [random_digits(10), random_text(10)],
                         [random_digits(10),random_text(10)],
                         [random_digits(10), random_text(10)]]
            for i in self.form:
              self.groups.graph.put_object = Mock()
              self.groups.create_post(i,self.text)
              self.groups.graph.put_object.assert_called_with(parent_object = i, connection_name="feed", message=self.text)
import random
import string

def random_digits(n):
    a = string.digits
    return ''.join([random.choice(a) for i in range(n)])

def random_text(n):
    a = string.ascii_letters + string.digits
    return ''.join([random.choice(a) for i in range(n)])