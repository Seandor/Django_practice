from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'users.views.first_page'),
    url(r'^login/', 'users.views.user_login'),
    url(r'^logout/', 'users.views.user_logout'),                       
	url(r'^register/', 'users.views.register'),
)
