# -*- coding: utf-8 -*-
import facebook
from utils import Group
import mock
from mock import Mock,MagicMock
import unittest
from django.test import TestCase
import random
import string
import jwt
from mock import patch


class PostResourceTest(TestCase):

    def setUp(self):
        self.social_user = "Name"
        self.AUTH = False
        self.token = "fakeOAuth"
        self.authtoken = jwt.encode({'user': str(self.social_user)}, 'secret')
        self.groups = Group(self.token)
        self.groups.graph = Mock()


    def test_list(self):
        
        self.groups.getgroups = Mock(return_value=[['1', 'a'], ['4', 'd'], ['3','c'], ['2', 'b']])
        self.groups.getpages = Mock(return_value=[['1', 'a'], ['4', 'd'], ['3','c'], ['2', 'b']])
        fake_db = [
        {
            "facebook token": str(self.token),
            "authtoken": str(self.authtoken),
            "username": str(self.social_user),
            "Groups": self.groups.getgroups(),
            "Pages": self.groups.getpages(),
        }
        ]
        self.assertEqual(fake_db, [{ "facebook token": str("fakeOAuth"),
                                      "authtoken" : str(self.authtoken),
                                      "username": str(self.social_user),
                                      "Groups": [['1', 'a'], ['4', 'd'], ['3','c'], ['2', 'b']],
                                      "Pages": [['1', 'a'], ['4', 'd'], ['3','c'], ['2', 'b']],}])

    
    def test_is_authenticated_login_true(self):

        request = Mock()
        request.META = {'HTTP_AUTHORIZATION': 'hello'}
        if request.META.get('HTTP_AUTHORIZATION') == 'hello':
            self.AUTH = True
        self.assertEqual(self.AUTH,True)

    def test_is_authenticated_login_false(self):
        self.AUTH = True
        request = Mock()
        request.META = {'HTTP_AUTHORIZATION': 'hellko'}
        if request.META.get('HTTP_AUTHORIZATION') != 'hello':
            self.AUTH = False
        self.assertEqual(self.AUTH,False)

    def test_is_authenticated_true(self):
        request = Mock()
        request.META = {'HTTP_AUTHORIZATION': self.authtoken}
        token = request.META.get('HTTP_AUTHORIZATION')
        detoken = jwt.decode(token, 'secret')
        if detoken == {'user': self.social_user}:
            self.AUTH = True
        self.assertEqual(self.AUTH,True)


    def test_is_authenticated_true(self):
        self.AUTH = True
        request = Mock()
        request.META = {'HTTP_AUTHORIZATION': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiVGF0eWFuYUNoZXJlZCJ9.rMc1wahlF5enk8A4Vd-FRyzkxvnUJTduA8pdbNfBfcw"}
        token = request.META.get('HTTP_AUTHORIZATION')
        detoken = jwt.decode(token, 'secret')
        if detoken != {'user': self.social_user}:
            self.AUTH = False
        self.assertEqual(self.AUTH,False)


    def test_create(self):
        self.groups.create = Mock()
        self.groups.create_posts("text","me")
        test_create_post.assert_called_with("post created")





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


def random_digits(n):
    a = string.digits
    return ''.join([random.choice(a) for i in range(n)])

def random_text(n):
    a = string.ascii_letters + string.digits
    return ''.join([random.choice(a) for i in range(n)])

