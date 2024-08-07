from django.urls import path
from .views import lista_tasksView, create_tasksView, delete_tasksView

urlpatterns = [
    path('', lista_tasksView),
    path('new/', create_tasksView, name='create_tasksView'),
    path('delete/<int:tasks_id>/', delete_tasksView, name='delete_tasksView'),
]