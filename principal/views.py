# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, FormView
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from form import Group_List
from utils import Group
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

def LogOut(request):
    logout(request)
    return redirect('/')

def form_list(me, group, page):
    return [[("Моя страница"), [['me', me],]], [("Группы"), group], [("Публичные страницы"), page]]

class DoneView(TemplateView):
    template_name = 'list.html'

class CreatePost(FormView):
    template_name = "create_post.html"
    success_url = 'list/'
    form_class = Group_List

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        self.social_user = request.user.social_auth.get(provider='facebook',)
        self.group = Group(self.social_user.extra_data['access_token'])
        return super(CreatePost, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreatePost, self).get_form_kwargs()
        kwargs['mylist'] = form_list(self.social_user, self.group.getgroups(), self.group.getpages())
        return kwargs

    def get_context_data(self, form, **kwargs):
        context = super(CreatePost, self).get_context_data(**kwargs)
        context['token'] = self.social_user.extra_data['access_token']
        context['username'] = self.social_user
        context['form'] = form
        return context

    def form_valid(self, form):
        text = form.cleaned_data['Text']
        listofchosen = form.cleaned_data['POST']
        self.group.create_posts(text,listofchosen)
        return super(CreatePost, self).form_valid(form)
