from django.db import models

# Create your models here.
class person(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=15)
    dob=models.DateField(max_length=8)
    phone=models.IntegerField()
    address=models.CharField(max_length=30)
    def __str__(self):
        return  self.firstname

class info(models.Model):
    moviename = models.CharField(max_length=30, unique=True)
    genre = models.CharField(max_length=10)
    language = models.CharField(max_length=10)
    year = models.CharField(max_length=6)
    price = models.FloatField()
    rentby = models.ForeignKey(person,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.moviename

