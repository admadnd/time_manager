from django.conf.urls.defaults import *
from time_manager.views import UserCreationView,TaskCreationView,CategoryCreationView
from time_manager.views import StatsView
urlpatterns = patterns(
    'time_manager.views',
    (r'^register/$', UserCreationView.as_view()),
    (r'^add_task/$', 'task_creation_view'),
    (r'^add_category/$', 'category_creation_view'),
    (r'^view/$', 'task_list_view'),
    (r'^stats/$', StatsView.as_view()),
    (r'^pie/$', 'pie_gen_view'),
    (r'^weeklyline/$', 'lgraph_gen_view'),
    (r'^timeline/$', 'timeline_view'),
    (r'^sorted/$', 'sorted_view'),
    (r'^sorted2/$', 'sorted2_view'),
    (r'^sorted3/$', 'sorted3_view'),
    (r'^sorted4/$', 'sorted4_view'),
)

urlpatterns += patterns(
    'django.contrib.auth.views',
    url(r'^login/$','login',  {'template_name': 'login.html'}),
    url(r'^login/?next=(?P<next>.*)/$','login',  {'template_name': 'login.html'}),
    
    url(r'^logout/$','logout', {'template_name': 'logout.html','next_page': '/login/'}),
)    
