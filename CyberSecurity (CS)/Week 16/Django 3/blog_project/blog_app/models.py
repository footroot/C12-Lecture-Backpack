from django.db import models

# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=60)
    body = models.TextField()

    def __str__(self):
        return f"{self.author} - {self.title}"