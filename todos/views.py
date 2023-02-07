from django.shortcuts import redirect, render
from .models import *
from .forms import EntryForm
# Create your views here.

def index(request):
    entries = Entry.objects.all().order_by("-date_added")       # retrieving all the entries from the database

    if request.method != 'POST':
        todoForm = EntryForm()                                  # empty form

    else:
        todoForm = EntryForm(request.POST)
        if todoForm.is_valid():                                 # if form is validated, then save
            todoForm.save()
            return redirect("todos:index")

    context = {"entries":entries, "todoForm":todoForm }

    return render(request,'todos/index.html',context )


def todoDetail(request,todo_id):
    entry = Entry.objects.get(id = todo_id)                     # getting the entry of a specific Todo

    context = {"entry":entry }

    return render(request,'todos/todoDetail.html',context )

def deleteTodo(request,todo_id):
    entry = Entry.objects.get(id = todo_id)
    entry.delete()                                              # delete the selected entry
    return redirect("todos:index")                              #   redirect to the index page after deleting

def editTodo(request,todo_id):
    entry = Entry.objects.get(id = todo_id)
    if request.method != 'POST':
        todoForm = EntryForm(instance=entry)                    # populate the EntryForm with the data

    else:
        todoForm = EntryForm(instance=entry,data=request.POST)
        if todoForm.is_valid():
            todoForm.save()
            return redirect("todos:index")

    context = {"todoForm":todoForm ,"entry":entry}
    return render(request,'todos/editTodo.html',context )

def markComplete(request, todo_id):
    entry = Entry.objects.get(id = todo_id)
    entry.completed = True                                          # mark the selected entry as completed and save
    entry.save()
    return redirect("todos:todoDetail",todo_id)

def searchTodos(request):
    search_text = request.POST.get("search")                            # get the search text from the form

    entries = Entry.objects.filter(title__contains = search_text).order_by("-date_added")   # filter entries based on the search text

    if request.method != 'POST':
        todoForm = EntryForm()

    else:
        todoForm = EntryForm(request.POST, request.FILES )
        if todoForm.is_valid():
            todoForm.save()
            return redirect("todos:index")

    context = {"entries":entries, "todoForm":todoForm }

    return render(request,'todos/index.html',context )

def filterTodos(request):
    entries = Entry.objects.all().order_by("-date_added")
    filter_action = request.GET

    """  
        Filter the entries based on whether option 'all', 'completed' or 'uncompleted' 
    """

    if "all" in filter_action:
        entries = Entry.objects.all().order_by("-date_added")

    if "completed" in filter_action:
        entries = Entry.objects.filter(completed = True).order_by("-date_added")

    if "uncompleted" in filter_action:
        entries = Entry.objects.filter(completed= False).order_by("-date_added")

    if request.method != 'POST':
        todoForm = EntryForm()

    else:
        todoForm = EntryForm(request.POST, request.FILES )
        if todoForm.is_valid():
            todoForm.save()
            return redirect("todos:index")

    context = {"entries":entries, "todoForm":todoForm }

    return render(request,'todos/index.html',context )

