from django.conf.urls import url 
from todoApp import views

urlpatterns=[
    url(r'^signup',views.signUp),
    url(r'^todo/$',views.todoApi),
    url(r'^todo/([0-9]+)$',views.todoApi)
]