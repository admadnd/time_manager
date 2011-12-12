from django import forms
from time_manager.models import Task,Category
from django.db.models import Q
import datetime
from django.core.exceptions import ValidationError

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # adjust format of start and end time to remove seconds in show
        # in 12-hour time
        widgets = { 
            'start': forms.DateTimeInput(format= '%m/%d/%Y %I:%M %p'),
            'end': forms.DateTimeInput(format= '%m/%d/%Y %I:%M %p'),
        } 
            

    def clean(self):
        # call original clean function to get cleaned_data
        super(TaskForm,self).clean()

        start = self.cleaned_data.get('start')
        end = self.cleaned_data.get('end')
    
        
        if  start is None or end is None:
            raise ValidationError(u'start or end is not defined')

        # Make sure that end does not come before start in time 
        if end < start:
            raise ValidationError(u'End Time occurs before Start Time')
        
        print end 
        print start

        
        list = Task.objects.filter(
            Q(start__lt=start,end__gt=end) |  # superset
            Q(start=start,end=end) | #equal 
            Q(start__gt=start,end__lt=end) | # subset
            Q(start__lt=start,end__gt=start,end__lte=end) | # left overlap
            Q(start__gte=start,start__lt=end,end__gt=end)  # right overlap
            )
        if list:
            print "Fail"
            raise ValidationError(u'Date overlapp with Task in db')
        
        print "Success"
        return self.cleaned_data
    
        

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
