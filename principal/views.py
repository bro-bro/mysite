from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseBadRequest
from django.template.loader import get_template
from django.template import Context
from social.pipeline.social_auth import load_extra_data
from django.contrib.auth import logout
import facebook

class IndexView (TemplateView):
    template_name = 'index.html'

def done(request):
    t = get_template('done.html')
    social_user = request.user.social_auth.filter(provider='facebook',).first()

    html = t.render(Context({'name':social_user.extra_data['access_token']}))
    return HttpResponse(html)


def list(request):
    social_user = request.user.social_auth.get(provider='facebook',)
    token = social_user.extra_data['access_token']
    graph = facebook.GraphAPI(access_token=token)
    graph.put_object(parent_object='me', connection_name='feed', message='Hello, world')
    t = get_template('list.html')
    html = t.render(Context({'var':'Hello world'}))
    return HttpResponse(html)

def get(request):
    social_user = request.user.social_auth.filter(provider='facebook',).first()
    token = social_user.extra_data['access_token']
    graph = facebook.GraphAPI(access_token=token)
    #graph.put_object(parent_object='me', connection_name='feed', message='Hello, world')
    groups = graph.get_connections(id='me', connection_name='groups')
    mass = ''
    #for i in groups['data']:
     #   mass += groups[i]['name']
    #graph.put_object("page id", "feed", message='My message goes here')
    for i in range (0, len(groups)):
        mass += str(i)
        mass += ')   Name: '
        mass += str(groups['data'][i]['name'])
        mass += ';   Administrator: '
        mass += str(groups['data'][i]['administrator'])
        mass += '   '
    
    graph.put_object(parent_object=groups['data'][0]['id'], connection_name='feed', message='I write from site')
    graph.put_object(parent_object=groups['data'][1]['id'], connection_name='feed', message='I write from site')
    t = get_template('list.html')
    html = t.render(Context({'var': mass}))
    return HttpResponse(html)


def LogOut(request):
    logout(request)
    return redirect('/')