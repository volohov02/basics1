from django.db import models
from usersapp.models import BlogUser

# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=32, unique = True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    name = models.CharField(max_length=32)
    areal = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    skills = models.ManyToManyField(Skills)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


