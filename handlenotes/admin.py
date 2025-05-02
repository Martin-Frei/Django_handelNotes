from django.contrib import admin
from .models import HandleNotes , NewsArticle, News, Ticker
# Register your models here.


admin.site.register(HandleNotes)
admin.site.register(NewsArticle)
admin.site.register(News)
admin.site.register(Ticker)