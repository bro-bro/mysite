from django.conf.urls import patterns, include, url
from django.contrib import admin

from principal.views import IndexView

urlpatterns = patterns('',
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view()),
    url(r'^done_auth/$', 'principal.views.done',  name='done'),
    url(r'^done_auth/list/$', 'principal.views.my_post', name='list'),
    url(r'^done_auth/get/$', 'principal.views.get', name='get'),
    url (r'^hello/$', 'principal.views.LogOut'),
)

