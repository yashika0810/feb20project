from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=30)


    def __str__(self):
        return self.username




class Python(models.Model):
    session=models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.session


class student(models.Model):
    name=models.CharField(max_length=30,unique=False)
    session=models.ForeignKey("Python",on_delete=models.PROTECT)

