from django.contrib import admin
from workouts import models

# Register your models here.
admin.site.register(models.Client)
admin.site.register(models.Workout)