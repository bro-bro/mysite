# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.template.loader import get_template
from django.template import Context
from form import Group_List, User_g
from utils import Group
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


def LogOut(request):
    logout(request)
    return redirect('/')

def create_post(request):
    social_user = request.user.social_auth.get(provider='facebook',)
    token = social_user.extra_data['access_token']
    group = Group(token)
    if request.method == 'GET':
        listofme = (("me", social_user),)
        listofgroup = group.getgroups()
        listofpages = group.getpages()
        lists = ( (("Моя страница"), listofme), (("Группы"), listofgroup), (("Публичные страницы"), listofpages))

        my_form1 = Group_List()
        my_form1.fields['POST'].choices = lists
        t = get_template('create_post.html')
        html = t.render(Context({'token':social_user.extra_data['access_token'], 'username':social_user, 'form1':my_form1 }))

    elif request.method == 'POST':
        if request.POST['textname'] :
            text = request.POST['textname']

            listsget = request.POST['POST']

            t = get_template('create_post.html')
            html = t.render(Context({'message': text, }))


    return HttpResponse(html)
