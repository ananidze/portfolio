from django.contrib import admin
from .models import Social, Project


# Register your models here.
@admin.register(Project, Social)
class Admin(admin.ModelAdmin):
    pass
