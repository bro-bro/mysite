from django.conf.urls import patterns, include, url
from django.contrib import admin


from principal.views import IndexView

urlpatterns = patterns('',
	url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', IndexView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url (r'^hello/$', 'principal.views.LogOut'),
    url(r'^create_post/$', 'principal.views.create_post', name='create_post'),
    url(r'^create_post/list/$', 'principal.views.list', name='list'),
)
