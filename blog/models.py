from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Author(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Post(models.Model):
    headline = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    # content = models.TextField()
    # adding ckeditor rich text field instead of built in text field
    content = RichTextField()

    def __str__(self):
        return self.headline
