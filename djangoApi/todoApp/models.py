from pickle import FALSE
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default = False)

    def _str_(self):
        return self.title


class NewUserForm(models.Model):
    userName = models.CharField(max_length = 120)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    def _str_(self):
        return self.userName