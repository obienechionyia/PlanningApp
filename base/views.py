# Create a view for each page of the application
from re import search
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserCreationFormWithEmail
from django.contrib.auth import login
from .models import Quote, Task, Goal, Book

# This view will be the login page, which will also function as the home page
class CustomLoginView(LoginView):
    # Point to the login html template
    template_name = 'base/login.html'
    # This view includes all of the fields in the 'Task' database model
    fields = '__all__'
    # Redirect the users if they are already logged in
    redirect_authenticated_user = True
    # If the user successfully logs in, they will be redirected to the 'tasks' url
    def get_success_url(self):
        return reverse_lazy('tasks')

# This view will be the page where users can register for an account on the application
class RegisterPage(CreateView):
    # Point to the register html page
    template_name = 'base/register.html'
    # State the form class - this is a User Creation Form that comes with the Django framework
    form_class = UserCreationFormWithEmail
    # Redirect the user to the homepage if they are already logged in
    redirect_authenticated_user = True
    # If the user successfully registers, they will be redirected to the 'tasks' url
    success_url = reverse_lazy('tasks')

    # This method is called if valid form info is POSTed
    def form_valid(self, form):
        user = form.save()
        # Log the user in after they have registered
        if user is not None:
            login(self.request, user)
        # return super(RegisterPage, self).form_valid(form)
        return redirect(self.success_url)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


# Create the Task List subclass that inherits from the Django-provided LoginRequiredMixin and ListView classes. This is the logged in home page
class TaskList(LoginRequiredMixin, ListView):
    # tell Django the database model that the class will pull from
    model = Task
    context_object_name = 'tasks'
    # Create function to create task search and task count functionalities
    def get_context_data(self, **kwargs):
        # Create context dictionary that we'll later pull from for searches and incomplete task counts
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        # Gets the input from the search box, assigns it to the 'search_input' variable and returns any matching tasks
        search_input = self.request.GET.get("search_area") or ""
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_input)

        context['search_input'] = search_input

        return context

# Create detail view that will give a closer look at each individual task
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

# Create a create view - this view will be the page that allows the user to create a new task
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # Unlike the login view, this view will only incorporate three of the database fields
    fields = ['title', 'description', 'complete']
    # After successfully creating a task, the user will be redirected back to the tasks page, where they will see the updated task list
    success_url = reverse_lazy('tasks')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

# Create an update view that will allow the user to update views they have already created
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

# Create a view that will allow the users to delete their tasks individually
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

class GoalList(LoginRequiredMixin, ListView):
    model = Goal
    context_object_name = 'goals'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goals'] = context['goals'].filter(user=self.request.user)
        context['count'] = context['goals'].filter(complete=False).count()
        search_input = self.request.GET.get("search_area") or ""
        if search_input:
            context['goals'] = context['goals'].filter(title__icontains=search_input)
        
        context['search_input'] = search_input

        return context

class GoalCreate(LoginRequiredMixin, CreateView):
    model = Goal
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('goals')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(GoalCreate, self).form_valid(form)

class GoalDetail(LoginRequiredMixin, DetailView):
    model = Goal
    context_object_name = 'goal'
    template_name = 'base/goal.html'
    
class GoalUpdate(LoginRequiredMixin, UpdateView):
    model = Goal
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('goals')

class GoalDelete(LoginRequiredMixin, DeleteView):
    model = Goal
    context_object_name = 'goal'
    success_url = reverse_lazy('goals')

class QuoteList(LoginRequiredMixin, ListView):
    model = Quote
    context_object_name = 'quotes'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quotes'] = context['quotes'].filter(user=self.request.user)
        search_input = self.request.GET.get("search_area") or ""
        if search_input:
            context['quotes'] = context['quotes'].filter(category__icontains=search_input)
        
        context['search_input'] = search_input

        return context

class QuoteCreate(LoginRequiredMixin, CreateView):
    model = Quote
    fields = ['author', 'quote', 'category']
    success_url = reverse_lazy('quotes')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(QuoteCreate, self).form_valid(form)

class QuoteUpdate(LoginRequiredMixin, UpdateView):
    model = Quote
    fields = ['author', 'quote', 'category']
    success_url = reverse_lazy('quotes')

class QuoteDelete(LoginRequiredMixin, DeleteView):
    model = Quote
    context_object_name = 'quote'
    success_url = reverse_lazy('quotes')

class BookList(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = context['books'].filter(user=self.request.user)
        context['count'] = context['books'].filter(complete=False).count()
        search_input = self.request.GET.get("search_area") or ""
        if search_input:
            context['books'] = context['books'].filter(title__icontains=search_input)
        
        context['search_input'] = search_input

        return context

class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['author', 'title', 'genre']
    success_url = reverse_lazy('books')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BookCreate, self).form_valid(form)

class BookDetail(LoginRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'base/book.html'
    
class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['author', 'title', 'genre', 'complete']
    success_url = reverse_lazy('books')

class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    context_object_name = 'book'
    success_url = reverse_lazy('books')

