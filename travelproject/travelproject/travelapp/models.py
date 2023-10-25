from django.db import models

# Create your models here.
class Place(models.Model):
    Name=models.CharField(max_length=250)
    Image=models.ImageField(upload_to='photos')
    Discription=models.TextField()


class Plc(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='photos')
    description=models.TextField()


# def __str__(self):
#     return self.Name