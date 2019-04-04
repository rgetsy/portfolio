from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField (max_length=100)
    pubdte = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField (upload_to='images/')
#def get_now():
#    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
