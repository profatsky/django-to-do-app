from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import CustomUserCreationForm
from .models import Task


class UserLoginView(LoginView):
    template_name = 'tasks/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task_list')


class UserRegisterView(CreateView):
    template_name = 'tasks/register.html'
    success_url = reverse_lazy('login')
    form_class = CustomUserCreationForm

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super().form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task_list')
        return super().get(*args, **kwargs)


class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'tasks/task_form.html'
    model = Task
    fields = ['title', 'description', 'is_complete']
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'tasks/task_form.html'
    model = Task
    fields = ['title', 'description', 'is_complete']
    success_url = reverse_lazy('task_list')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'tasks/task_delete.html'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user.pk)
