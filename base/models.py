from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create the database models that the application will pull from
class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    # return the title of the Task when Task is called
    def __str__(self):
        return self.title or ''

    # Meta class to order the Tasks by completion
    class Meta:
        ordering = ['complete']


class Goal(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or ''
    
    class Meta:
        ordering = ['complete']


class Quote(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    author = models.CharField(max_length=30, null=True, blank=True)
    quote = models.TextField(null=True, blank=True)
    category = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quote


class Book(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    author = models.CharField(max_length=30, null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    genre = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    complete = complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
