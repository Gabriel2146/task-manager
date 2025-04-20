from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Project(models.Model):
    name = models.CharField(max_length=200)

class Task(models.Model):
    id_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    date_start = models.DateField()
    estimate_time = models.IntegerField()
    status = models.CharField(max_length=50)
