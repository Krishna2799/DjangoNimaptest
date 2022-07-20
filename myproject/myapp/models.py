from django.db import models

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=150)

    def __str__(self):
        return self.project_name


class Client(models.Model):
    client_name = models.CharField(max_length=150)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='assign_to', null=True)

    def __str__(self):
        return self.client_name


class User(models.Model):
    user_name = models.CharField(max_length=150)

    def __str__(self):
        return self.user_name
