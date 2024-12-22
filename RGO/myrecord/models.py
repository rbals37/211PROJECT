from django.db import models
from django.conf import settings


# Create your models here.

#그 뭐냐 
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title