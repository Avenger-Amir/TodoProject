from rest_framework import serializers
from .models import Todo, NewUserForm

class TodoSerealizers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')

class NewUserFormSerealizers(serializers.ModelSerializer):
    class Meta:
        model = NewUserForm
        fields = ('id', 'userName', 'email', 'password')
