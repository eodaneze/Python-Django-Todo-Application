from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Todo
# Create your views here.
def list_todo_items(request):
    context = {'index' : Todo.objects.all()}
    return render(request,'index.html', context)

    # return HttpResponse('from list_todo_items')
def insert_todo_item(request:HttpRequest):
    # content = request.POST['content']
    # pushing the data to postgrsql
    todo = Todo(content = request.POST['content'])
    todo.save()
    return redirect('/')
    #  return render(request,'insert_todo.html')



# function for delete operation

def delete_todo_item(request,todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/')