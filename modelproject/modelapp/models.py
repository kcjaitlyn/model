from django.db import models

# Create your models here.
class Article(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField('date')
    
    # admon 글 제목 표시하기 위한 함수
    def __str__(self):
        return self.title

class Blog(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField('date')
    
    # admon 글 제목 표시하기 위한 함수
    def __str__(self):
        return self.title
