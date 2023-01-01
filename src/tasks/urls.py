from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (
    UserRegisterView,
    UserLoginView,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskReorderView
)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),

    path('', TaskListView.as_view(), name='task_list'),
    path('task-create/', TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorderView.as_view(), name='task-reorder'),
]
