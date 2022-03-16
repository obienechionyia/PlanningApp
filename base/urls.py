# Create the url patterns for the application. Each view will have a different url path that leads to the page with said view
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage, \
    GoalList, GoalDetail, GoalCreate, GoalUpdate, GoalDelete, QuoteList, QuoteCreate, QuoteUpdate, QuoteDelete, \
    BookList, BookCreate, BookUpdate, BookDelete
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='base/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='base/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='base/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='base/password_reset_complete.html'), name='password_reset_complete'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task_create/', TaskCreate.as_view(), name='task_create'),
    path('task/<int:pk>/update/', TaskUpdate.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDelete.as_view(), name='task_delete'),
    path('goals/', GoalList.as_view(), name='goals'),
    path('goal/<int:pk>/', GoalDetail.as_view(), name='goal'),
    path('goal_create/', GoalCreate.as_view(), name='goal_create'),
    path('goal/<int:pk>/update/', GoalUpdate.as_view(), name='goal_update'),
    path('goal/<int:pk>/delete/', GoalDelete.as_view(), name='goal_delete'),
    path('quotes/', QuoteList.as_view(), name='quotes'),
    path('quote_create/', QuoteCreate.as_view(), name='quote_create'),
    path('quote/<int:pk>/update/', QuoteUpdate.as_view(), name='quote_update'),
    path('quote/<int:pk>/delete/', QuoteDelete.as_view(), name='quote_delete'),
    path('books/', BookList.as_view(), name='books'),
    path('book_create/', BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', BookDelete.as_view(), name='book_delete'),

]
