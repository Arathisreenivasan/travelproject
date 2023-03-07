from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name=models.CharField(max_length=2500)
    image=models.ImageField(upload_to='picz')
    desc=models.TextField()

    def __str__(self):
        return self.name