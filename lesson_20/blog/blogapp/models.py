from django.db import models

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
    skills = models.ManyToManyField(Skills) #, through="Enrollment")

    def __str__(self):
        return self.name

# class Enrollment(models.Model):
#     vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
#     skills = models.ForeignKey(Skills, on_delete=models.CASCADE)


