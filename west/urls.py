from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'west.views.first_page'),
    url(r'^staff/', 'west.views.staff'),
    url(r'^templay/', 'west.views.templay'),
    url(r'^form/', 'west.views.form'),
    url(r'^investigate/', 'west.views.investigate'),
)
