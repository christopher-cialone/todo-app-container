from django.shortcuts import redirect, render

from django.views import View

from todo_app.forms import TaskForm
from todo_app.models import Task


# Create your views here.

class HomeView(View):
    '''
    HomeView function as the site's homepage, listing out all Task objects in the database and linking out 
    to each one's detail view
    '''
    def get(self, request):
        '''The content required to render the homepage'''
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
        '''
        This method saves new Tasks to the databse before redirecting to 
        the 'get' method of the homepage
        '''
        task_form = TaskForm(request.POST)
        task_form.save()
        #tasks = Task.objects.all()
        return redirect('home')


class TaskDetailView(View):
    '''
    TaskDetailView provides the ability to update and delete individual
    Task objects from the database
    '''
    def get(self, request, task_id):
        '''The content required to render the Task object's detail page'''
        task = Task.objects.get(id=task_id)

        task_form = TaskForm(instance=task)

        html_data = {
            'task_object': task,
            'form': task_form,
        }
        return render(
            request=request,
            template_name='detail.html',
            context=html_data,
        )

        '''when user clicks Update save our changes to the db and bring us back home'''
    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)

        '''This is the logic behind clicking either Update or Delete'''
        if 'update' in request.POST:
            task_form = TaskForm(request.POST, instance=task)
            task_form.save()
        elif 'delete' in request.POST:
            task.delete()

        return redirect('home')

     
