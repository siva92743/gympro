from django.db import models

# Create your models here.


class Task(models.Model):
    subject = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.subject
