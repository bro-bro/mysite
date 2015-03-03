# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseBadRequest
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth import logout
import facebook
from django.shortcuts import render

def index(request):
    return render('done.html')

class IndexView (TemplateView):
    template_name = 'index.html'

def done(request):
    
    social_user = request.user.social_auth.get(provider='facebook',)
    token = social_user.extra_data['access_token']
    graph = facebook.GraphAPI(access_token=token)
    groups = graph.get_object("me/groups")
    

    l_group = []
    for i in range(0, len(groups['data'])):
        l_group.append(groups['data'][i]['name'])

    user = request.user
    public_page = graph.get_object("me/accounts")

    l_page = []

    for i in range(0, len(public_page['data'])):
        l_page.append(public_page['data'][i]['name'])

    t = get_template('done.html')
    html = t.render(Context({'name':social_user.extra_data['access_token'], 'username':social_user, 'list_group': l_group, 'list_pubpage':l_page }))
    return HttpResponse(html)


def LogOut(request):
    logout(request)
    return redirect('/')


def contact(request):
    text = request.POST['fname'].encode('utf-8')
    group_post = request.POST.getlist('Cbox')
    page_post = request.POST.getlist('Pbox')
    social_user = request.user.social_auth.get(provider='facebook',)
    token = social_user.extra_data['access_token']
    graph = facebook.GraphAPI(access_token=token)
    if request.POST.getlist('checks'):
        graph.put_object(parent_object='me', connection_name='feed', message=text)
    #if group_post:
     #   for i in range(0, len(group_post)) :
      #     graph.put_object(parent_object=group_post[i].encode('utf-8'), connection_name='feed', message=text)
    #if page_post:
     #   for i in page_post:
      #      graph.put_object(parent_object=i, connection_name='feed', message=text)
                    
    t = get_template('list.html')
    html = t.render(Context({'message': group_post}))
    return HttpResponse(html)

    

