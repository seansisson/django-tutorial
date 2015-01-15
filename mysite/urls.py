from django.conf.urls import patterns, include, url
from django.contrib import admin

from mysite.polls import views as polls

urlpatterns = patterns('',
	    # Examples:
	    # url(r'^$', 'mysite.views.home', name='home'),
	    # url(r'^blog/', include('blog.urls')),

		#url(r'^polls/', include('polls.urls', namespace="polls")),
	    url(r'^admin/', include(admin.site.urls)),

		# ex: /polls/
		url(r'^polls/$', polls.IndexView.as_view(), name='index'),
		# ex: /polls/5/
		url(r'^polls/(?P<pk>\d+)/$', polls.DetailView.as_view(), name='detail'),
		# ex: /polls/5/results/
		url(r'^polls/(?P<pk>\d+)/results/$', polls.ResultsView.as_view(), name='results'),
		# ex: /polls/5/vote/
		url(r'^polls/(?P<question_id>\d+)/vote/$', polls.vote, name='vote'),
)
