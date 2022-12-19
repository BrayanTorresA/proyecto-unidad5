from django.db import models

# Create your models here.


class Service(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    logo = models.URLField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table="servicios"
