# Register the admin site for the application
from django.contrib import admin
from .models import Task, Goal, Quote, Book

admin.site.register(Task)
admin.site.register(Goal)
admin.site.register(Quote)
admin.site.register(Book)
