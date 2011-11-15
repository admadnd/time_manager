from django.conf.urls.defaults import *
from midtermproj.views import UserCreationView,TaskCreationView,CategoryCreationView
urlpatterns = patterns(
    'midtermproj.views',
    (r'^register/$', UserCreationView.as_view()),
    (r'^add_task/$', 'task_creation_view'),
    (r'^add_category/$', 'category_creation_view'),
    (r'^view/$', 'task_list_view'),
    
)

urlpatterns += patterns(
    'django.contrib.auth.views',
    url(r'^login/$','login',  {'template_name': 'login.html'}),
    url(r'^login/?next=(?P<next>.*)/$','login',  {'template_name': 'login.html'}),
    
    url(r'^logout/$','logout', {'template_name': 'logout.html','next_page': '/midtermproj/login/'}),
)    
