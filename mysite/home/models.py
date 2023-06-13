from django.db import models

class Book(models.Model):

    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    issued_date=models.DateField()
    pages=models.IntegerField()
    template=models.ImageField()
