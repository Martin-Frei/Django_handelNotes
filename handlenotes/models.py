from django.db import models
from django.utils import timezone

# Create your models here.

class HandleNotes(models.Model):
    id = models.AutoField(primary_key= True)
    notes = models.CharField(max_length=500)
    timestamp = models.DateTimeField(default = timezone.now)


class NewsArticle(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    url = models.URLField()
    image_url = models.URLField(null=True, blank=True)
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title

class News(models.Model):
    id = models.AutoField(primary_key=True)
    news = models.CharField(max_length=500)
    snippet = models.CharField(max_length=500)
    newsurl = models.URLField(max_length=300)
    thumbnail = models.URLField(max_length=300)
    timestamp = models.IntegerField()
    

# class Ticker(models.Model) :
#     id = models.AutoField(primary_key = True)
#     ticker = models.CharField(max_length=10)

class Ticker(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.CharField(max_length=10, unique=True)
    domain = models.CharField(max_length=100, blank=True)
    active = models.BooleanField(default=True)  

    def __str__(self):
        return f"{self.ticker} ({'Aktiv' if self.active else 'Inaktiv'})"