from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (
    UserRegisterView,
    UserLoginView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView
)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),

    path('task-create/', TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
]
