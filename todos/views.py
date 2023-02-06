from django.shortcuts import redirect, render
from .models import *
from .forms import EntryForm
# Create your views here.

def index(request):
    entries = Entry.objects.all().order_by("-date_added")

    if request.method != 'POST':
        todoForm = EntryForm()

    else:
        todoForm = EntryForm(request.POST, request.FILES )
        if todoForm.is_valid():
            todoForm.save()
            return redirect("todos:index")

    context = {"entries":entries, "todoForm":todoForm }

    return render(request,'todos/index.html',context )


def todoDetail(request,todo_id):
    entry = Entry.objects.get(id = todo_id)

    context = {"entry":entry }

    return render(request,'todos/todoDetail.html',context )

def deleteTodo(request,todo_id):
    entry = Entry.objects.get(id = todo_id)
    entry.delete()
    return redirect("todos:index")

def editTodo(request,todo_id):
    entry = Entry.objects.get(id = todo_id)
    if request.method != 'POST':
        todoForm = EntryForm(instance=entry)

    else:
        todoForm = EntryForm(instance=entry,data=request.POST)
        if todoForm.is_valid():
            todoForm.save()
            return redirect("todos:index")

    context = {"todoForm":todoForm ,"entry":entry}
    return render(request,'todos/editTodo.html',context )

def markComplete(request, todo_id):
    entry = Entry.objects.get(id = todo_id)
    entry.completed = True
    entry.save()
    return redirect("todos:todoDetail",todo_id)

def searchTodos(request):
    search_text = request.POST.get("search")
    print(search_text)
    entries = Entry.objects.filter(title__contains = search_text).order_by("-date_added")

    if request.method != 'POST':
        todoForm = EntryForm()

    else:
        todoForm = EntryForm(request.POST, request.FILES )
        if todoForm.is_valid():
            todoForm.save()
            return redirect("todos:index")

    context = {"entries":entries, "todoForm":todoForm }

    return render(request,'todos/index.html',context )