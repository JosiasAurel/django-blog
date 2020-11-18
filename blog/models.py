from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField()
    date_published = models.DateField(auto_now=True)
    date_edited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.CharField(max_length=600)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on {self.post}"
