from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('',views.index , name = "index"),          # home page and a list of my To-Do's
    path('todo/<int:todo_id>/',views.todoDetail, name = "todoDetail"),          # URL to a selected to-do
    path('delete-todo/<int:todo_id>/',views.deleteTodo, name = "deleteTodo"),       # URL to delete a to-do
    path('edit-todo/<int:todo_id>/',views.editTodo, name = "editTodo"),         # URL to modify the to-do
    path('mark-complete/<int:todo_id>/',views.markComplete, name = "markComplete"),  
]