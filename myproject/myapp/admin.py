from django.contrib import admin
from .models import Project, Client, User

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_name', 'project']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name']
