from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to="media/image/")

class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


class Output(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, null=True)

