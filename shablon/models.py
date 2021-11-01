from django.db import models
class Gullar(models.Model):
    nomi = models.CharField(null=False, blank=False, max_length=300)
    narxi = models.IntegerField()
    rasmi = models.CharField(max_length=400)
    kategoriya = models.ForeignKey('Kategoriya',on_delete = models.PROTECT)

    class Meta():
        ordering = ['pk']

class Kategoriya(models.Model):
    nomi = models.CharField(null=False, blank=False, max_length=300)

    class Meta():
        ordering = ['nomi']

  


# Create your models here.
