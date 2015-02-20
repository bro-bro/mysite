from django.shortcuts import render
from django.views.generic import TemplateView
from social.apps.django_app.utils import psa
from django.http import HttpResponse, HttpResponseBadRequest
from django.template.loader import get_template
from django.template import Context

#import requests

class IndexView (TemplateView):

	template_name = 'index.html'

@psa('social:complete')
def auth(request, backend):
    if isinstance(request.backend, BaseOAuth2):
        token = request.REQUEST.get('access_token')
    else:
        raise HttpResponseBadRequest('Wrong backend type')
    user = request.backend.do_auth(request.GET.get('access_token'))
    if user:
        login(request, user)
        data = {'id': user.id, 'username': user.username}
        return 'OK'
    else:
        return 'ERROR'

def done(request):
    view = "facebook"
    t = get_template('done.html')
    html = t.render(Context({'name':view}))
    return HttpResponse(html)
