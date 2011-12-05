# Create your views here. 
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import ModelFormMixin
from django.views.generic import FormView,ListView
from time_manager.forms import TaskForm,CategoryForm
from time_manager.models import Task,Category
import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import TemplateView
from django.db.models import Q,Sum
from json import JSONEncoder

class StatsView(TemplateView):
    template_name = "stats.html"

@login_required(login_url='/login/')
# create a view to generate html snippet within view
def sorted_view(request):
    #obtain a queryset of task objects filtered by user and ordered by name
    QO = Task.objects.filter(user = request.user).order_by('name')
    #put QuerySet in contect for template that will generate html snippit and return HTTP response
    return render_to_response('table_creation.html', { 'task_list': QO, }, context_instance=RequestContext(request))

@login_required(login_url='/login/')
# create a view to generate html snippet within view
def sorted2_view(request):
    #obtain a queryset of task objects filtered by user and ordered by name
    QO2 = Task.objects.filter(user = request.user).order_by('start')
    #put QuerySet in contect for template that will generate html snippit and return HTTP response
    return render_to_response('table_creation.html', { 'task_list': QO2, }, context_instance=RequestContext(request))

@login_required(login_url='/login/')
# create a view to generate html snippet within view
def sorted3_view(request):
    #obtain a queryset of task objects filtered by user and ordered by name
    QO3 = Task.objects.filter(user = request.user).order_by('-name')
    #put QuerySet in contect for template that will generate html snippit and return HTTP response
    return render_to_response('table_creation.html', { 'task_list': QO3, }, context_instance=RequestContext(request))

@login_required(login_url='/login/')
# create a view to generate html snippet within view
def sorted4_view(request):
    #obtain a queryset of task objects filtered by user and ordered by name
    QO4 = Task.objects.filter(user = request.user).order_by('-start')
    #put QuerySet in contect for template that will generate html snippit and return HTTP response
    return render_to_response('table_creation.html', { 'task_list': QO4, }, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def lgraph_gen_view(request):
    
    categories = Category.objects.all()

    series = list() 

    for category in categories:
        # iterating through all twelve months (exclusive)
        
        # initializing options for data series
        data = dict();
        data['lines'] = dict([('show',True)])
        data['data'] = list()
        data['label'] = category.name
        for i in range(1,13):
            sum = datetime.timedelta() 
            # summing all the time deltas
            for task in category.task_set.filter(start__month=i):
                sum = sum + (task.end - task.start)
            # add month,total # of hours 
            data['data'].append(list((i,sum.total_seconds()/3600)))

        # add series object to list of series
        series.append(data);            

    
    dat = JSONEncoder().encode(series)

    return HttpResponse(dat,'application/json')

@login_required(login_url='/login/')
def pie_gen_view(request):
    categories = Category.objects.all()

    data = []
    for category in categories:
        
        # look at tasks for a given category in the last 7 days
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=7)
        print start_date
        print end_date
        query = Q(user=request.user,
                  start__gte=start_date,
                  start__lt=end_date,
                  end__gt=start_date,
                  end__lte=end_date,
                 )
                  
        total_time_dt = datetime.timedelta()
        for task in category.task_set.filter(query):
            # calculate the amount of time spent for every time under a category
            total_time_dt = total_time_dt + (task.end-task.start)
            print total_time_dt

        # Only add category if there are tasks w non-zero time associated 
        # with it
        if total_time_dt != datetime.timedelta():
            data.append(dict([("label",category.name),("data",total_time_dt.total_seconds()/3600)]))

    # create JSON object from python 
    dat = JSONEncoder().encode(data)

    return HttpResponse(dat,'application/json')

# Handles creation of users
class UserCreationView(FormView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = '/login/'

@login_required(login_url='/login/')
def task_creation_view(request):
    # create dummy Task object to handle displaying on subset of ModelForm
    # fields issue
    task = Task(name= '',start=datetime.datetime.now(),end=datetime.datetime.now(),user = request.user)

    # create form instance
    form = TaskForm(request.POST,instance=task)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/view/')
    else:
        form = TaskForm(instance=task)
    
    return render_to_response('add_form.html', { 'form': form, }, context_instance=RequestContext(request))


@login_required(login_url='/login/')
def category_creation_view(request):
    form = CategoryForm(request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/view/')
    else:
        form = CategoryForm()

    # Request Context needed for csrf token to be given to the web page
    return render_to_response('add_form.html', { 'form': form, }, context_instance=RequestContext(request))

@login_required(login_url='/login/')
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
    success_url = '/view/'

class TaskCreationView(ModelFormMixin):
    model=Task
    template_name = 'add_form.html'
    success_url = '/view/'

    def get_object(queryset=None):
        task = Task(start=datetime.now(),end=datetime.now(),user = request.user)
        return task

    
