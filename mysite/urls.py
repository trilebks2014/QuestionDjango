from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples#:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('polls.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^',include(admin.site.urls)),
    url(r'^admin/',include(admin.site.urls)),
    #url(r'^admin/polls/question/{{ question.id }}/vote/$', views.vote, name='vote'),
)