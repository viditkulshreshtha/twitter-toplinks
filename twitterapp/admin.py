from django.contrib import admin
from .models import model_tweet

admin.register(model_tweet)(admin.ModelAdmin)
# Register your models here.
