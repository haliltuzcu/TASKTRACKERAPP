from django.urls import path, include

from .views import (
    # FBV:
    todo_list,
    todo_add,
)

# after '/':
urlpatterns = [
    path('list/', todo_list),
    path('add/', todo_add),
]
