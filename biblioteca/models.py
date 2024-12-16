from django.db import models

# Create your models here.

class Persona(models.Model):
    nom= models.CharField(max_length=30)
    ape= models.CharField(max_length=30)
    idn= models.CharField(max_length=30)
    sx = models.CharField(max_length=20)
    fec = models.CharField(max_length=20)
    dirc = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    cor = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s %s %s %s %s %s %s' %(self.nom, self.ape, self.idn, self.sx, self.fec, self.dirc, self.tel, self.cor)