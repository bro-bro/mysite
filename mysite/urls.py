from django.conf.urls import patterns, include, url
from django.contrib import admin


from principal.views import IndexView, create_post

urlpatterns = patterns('',
	url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', IndexView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url (r'^hello/$', 'principal.views.LogOut'),
    url(r'^create_post/$', create_post.as_view()),
    url(r'^create_post/list$', 'principal.views.create_post', name='list'),
    url(r'^api-auth/', include('principal.rest_urls', namespace='rest_framework'))
)
