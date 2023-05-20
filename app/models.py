from django.db import models
from django.urls import reverse
# Create your models here.


class School(models.Model):
    id=models.IntegerField(primary_key=True,default=10)
    name=models.CharField(max_length=50)
    principal=models.CharField(max_length=30)
    location=models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('school_details',kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

    


class Student(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
    sname=models.CharField(max_length=30)
    sage=models.IntegerField()

    def __str__(self):
        return self.sname