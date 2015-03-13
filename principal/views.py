# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from form import Group_List
from utils import Group

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


def LogOut(request):
    logout(request)
    return redirect('/')

def create_post(request):
    social_user = request.user.social_auth.get(provider='facebook',)
    group = Group(social_user.extra_data['access_token'])
    if request.method == 'GET':
        my_form1 = Group_List(form_list(social_user, group.getgroups(), group.getpages()))
        t = get_template('create_post.html')
        html = t.render(Context({'token':social_user.extra_data['access_token'], 'username':social_user, 'form1':my_form1 }))

    elif request.method == 'POST':
        t = get_template('list.html')
        if len(request.POST.get('textname')) == 0:
            html = t.render(Context({'message': "Пожалуйста, ведите текст.", 'message1': "Ошибка!", 'username':social_user}))
        elif not request.POST.get('POST'):
            html = t.render(Context({'message': "Пожалуйста, выберите страницу или группу.", 'message1': "Ошибка!", 'username':social_user}))
        else:
            group.create_posts(request.POST)
            html = t.render(Context({'message': "Сообщение успешно отправлено!", 'username':social_user}))

    return HttpResponse(html)

def form_list(me, group, page):
    return [[("Моя страница"), [['me', me],]], [("Группы"), group], [("Публичные страницы"), page]]