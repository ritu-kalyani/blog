from django.db import models

# Create your models here.
class Post(models.Model):
    sno =models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=15)
    content=models.TextField()
    slug=models.CharField(max_length=100)
    views =models.IntegerField(default=0)
    timeStamp=models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' by '+ self.author