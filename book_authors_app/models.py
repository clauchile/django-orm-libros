from enum import auto
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length= 250)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"{self.title}"


class Author(models.Model):
    first_name= models.CharField(max_length= 250)
    last_name= models.CharField(max_length= 250)
    books = models.ManyToManyField(Book, related_name="authors")
    notas = models.CharField(max_length= 250)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
