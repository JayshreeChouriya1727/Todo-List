from django.shortcuts import render,redirect
from django.contrib import messages

# import todo Tapp form and models
from .forms import TodoForm
from .models import Todo

# Create your views here.

def index(request):
    item_list = Todo.objects.order_by("-date") # get all data as per current date wise
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = TodoForm()
    page={
        "forms" : form,
        "list" : item_list,
        "title" : "TODO LIST",
        }
    return render(request,'index.html',page)

def remove(request,id):
    item = Todo.objects.get(id=id)
    item.delete()
    messages.info(request,"item removed !!!") # when your request successfully deleted it will show you remove item in frontend through message.
    return redirect('index')
