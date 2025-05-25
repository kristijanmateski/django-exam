from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Umetnik(models.Model):
    UMETNICKI_CHOICES = [
        ('im', 'Impressionism'),
        ('pa', 'Pop art'),
        ('gr', 'Graffiti')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    umetnichki_stil = models.CharField(max_length=2, choices=UMETNICKI_CHOICES)

    def __str__(self):
        return self.name


class Izlozhba(models.Model):
    naslov = models.CharField(max_length=255)
    date_pochetok = models.DateTimeField()
    date_kraj = models.DateTimeField()
    opis = models.TextField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.naslov


class UmetnichkoDelo(models.Model):
    naslov = models.CharField(max_length=255)
    date = models.DateField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    umetnik = models.ForeignKey(Umetnik, on_delete=models.CASCADE)
    izlozhba = models.ForeignKey(Izlozhba, on_delete=models.CASCADE)

    def __str__(self):
        return self.naslov
