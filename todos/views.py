from django.shortcuts import redirect, render
from .models import *
from .forms import EntryForm
# Create your views here.

def index(request):
    entries = Entry.objects.all()

    if request.method != 'POST':
        todoForm = EntryForm()

    else:
        todoForm = EntryForm(request.POST, request.FILES )
        if todoForm.is_valid():
            todoForm.save()
            return redirect("todos:index")

    context = {"entries":entries, "todoForm":todoForm }

    return render(request,'todos/index.html',context )

