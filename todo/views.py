from django.shortcuts import render

from .forms import (
    Todo, TodoForm
)

# ------------------------------------
# Function Based Views
# ------------------------------------

# List:
def todo_list(request):
    return render(request, 'list.html', {
        "todos": Todo.objects.all()
    })

# Add:
def todo_add(request):
    form = TodoForm()
    context = {
        "form": form
    }
    return render(request, 'add.html', context)
