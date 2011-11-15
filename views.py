# Create your views here. 
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import ModelFormMixin
from django.views.generic import FormView,ListView
from midtermproj.forms import TaskForm,CategoryForm
from midtermproj.models import Task,Category
import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect 

# Handles creation of users
class UserCreationView(FormView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = '/login/'

@login_required(login_url='/midtermproj/login/')
def task_creation_view(request):
    # create dummy Task object to handle displaying on subset of ModelForm
    # fields issue
    task = Task(name= '',start=datetime.datetime.now(),end=datetime.datetime.now(),user = request.user)

    # create form instance
    form = TaskForm(request.POST,instance=task)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/midtermproj/view/')
    else:
        form = TaskForm(instance=task)
    
    return render_to_response('add_form.html', { 'form': form, }, context_instance=RequestContext(request))


@login_required(login_url='/midtermproj/login/')
def category_creation_view(request):
    form = CategoryForm(request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/midtermproj/view/')
    else:
        form = CategoryForm()

    # Request Context needed for csrf token to be given to the web page
    return render_to_response('add_form.html', { 'form': form, }, context_instance=RequestContext(request))

@login_required(login_url='/midtermproj/login/')
def  task_list_view(request):
    task_list = Task.objects.filter(user=request.user)
    
    # generate statistics
    avg = list()
    categories = Category.objects.all()
    
    for category in categories:
        # get total amount of time
        total_time_dt = datetime.timedelta()
        dates = dict()
        if category.task_set.all():
            for task in category.task_set.all():
                total_time_dt = total_time_dt + (task.end-task.start)
                date = (task.start.year,task.start.month,task.start.day)
                if date not in dates:
                    dates[date] = 1
            days = len(dates)
            avg_tuple = ( category.name, (total_time_dt/days) )
            avg.append(avg_tuple)
            
    return render_to_response('task_list.html',{'task_list':task_list, 'day_avgs': avg }, context_instance=RequestContext(request))
    
class CategoryCreationView(ModelFormMixin):
    form_class = CategoryForm
    model = Category
    template_name = 'add_form.html'
    success_url = '/midtermproj/view/'

class TaskCreationView(ModelFormMixin):
    model=Task
    template_name = 'add_form.html'
    success_url = '/view/'

    def get_object(queryset=None):
        task = Task(start=datetime.now(),end=datetime.now(),user = request.user)
        return task

    
