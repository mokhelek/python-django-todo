from django.db import models

# Create your models here.


"""
A database table for a Todo Entry

"""

class Entry(models.Model):
    title = models.CharField(max_length=100)       
    body = models.TextField(null=True,blank=True)
    date_added = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

