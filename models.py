from django.db import models 
from django.contrib.auth import models as auth_model


class Task(models.Model):
    name = models.CharField(max_length=15)
    start = models.DateTimeField()
    end = models.DateTimeField()
    categories = models.ManyToManyField("Category",blank=True)
    description = models.TextField(blank=True)
    user = models.ForeignKey(auth_model.User,editable=False)
    
    class Meta:
        ordering = ['start']

class Category(models.Model):
    name = models.CharField(max_length=15,unique=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return "%s" % self.name
