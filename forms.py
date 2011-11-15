from django import forms
from midtermproj.models import Task,Category
from django.db.models import Q
import datetime
from django.core.exceptions import ValidationError

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task

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
            Q(start__lte=start,end__gte=end) |  # O subset of N
            Q(start__gte=start,end__lte=end) |  # N subset of O
            Q(end__gt=start,end__lt=end)     |  # O intersect N from left
            Q(start__gt=start,start__lt=end)    # O intersect N from right
            )
        if list:
            print "Fail"
            raise ValidationError(u'Date overlapp with Task in db')
        
        print "Success"
        return self.cleaned_data
    
        

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
