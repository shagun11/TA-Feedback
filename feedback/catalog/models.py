# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
     name = models.CharField(max_length=128)
     term = models.CharField(max_length=128)
     year = models.IntegerField(default=2018)
     user = models.ManyToManyField(User)

     def __str__(self):
         return self.name


class TAssistant(models.Model):
    name = models.CharField(max_length=128)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    ta = models.ForeignKey(TAssistant, null=True, blank=True)
    course = models.ForeignKey(Course, null=True, blank=True)
    text = models.CharField(max_length=128)
    add_details = models.TextField(null=True, blank=True)
    st_details = models.CharField(max_length=128, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)




