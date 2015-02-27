from django.conf.urls import patterns, include, url
from django.contrib import admin

from principal.views import IndexView

urlpatterns = patterns('',
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view()),
    url(r'^done/$', 'principal.views.done', name='done'),
    url(r'^done/list/$', 'principal.views.list', name='list'),
    url(r'^done/get/$', 'principal.views.get', name='get'),
)

