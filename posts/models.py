from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

#this is used for rich text editor
from tinymce import HTMLField

User = get_user_model()
# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    profile_pic = models.ImageField()
    def __str__(self):
        return self.user.username
class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Post(models.Model):
    title=models.CharField(max_length=150)
    overview = models.TextField()
    content = HTMLField('Content') #this is used for rich text editor
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categorys= models.ManyToManyField(Category)
    featured = models.BooleanField()

    def summry(self):
        return self.overview[:200]
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post',kwargs={
            'id':self.id
        })

        