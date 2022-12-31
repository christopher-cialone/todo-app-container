from django.forms import ModelForm

from todo_app.models import Task
'''We can use this form to update a Task, or create a new one'''
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['description']