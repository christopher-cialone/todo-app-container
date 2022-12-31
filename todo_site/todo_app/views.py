from django.shortcuts import redirect, render
from django.views import View

from todo_app.forms import TaskForm
from todo_app.models import Task


# Create your views here.

class HomeView(View):
    def get(self, request):
        task_form = TaskForm()
        tasks = Task.objects.all()

        html_data = {
            'task_list': tasks,
            'form': task_form,
        }
        return render(
            request=request,
            template_name='index.html',
            context=html_data,
        )
    
    
    def post(self, request):
       
        task_form = TaskForm(request.POST)
        task_form.save()
        #tasks = Task.objects.all()
        return redirect('home')


class TaskDetailView(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)

        html_data = {
            'task_object': task,
           # 'form': task_form,
        }
        return render(
            request=request,
            template_name='detail.html',
            context=html_data,
        )

     
