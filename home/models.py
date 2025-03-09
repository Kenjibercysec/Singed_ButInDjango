from django.db import models

# Create your models here.
class Dispositivos(models.Model):
    id_tombamento = models.CharField(max_length=30)
    tipo_de_disp = models.EmailField()
    qnt_armaz = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    funcionando = models.CharField(max_length=6)
    data_de_an = models.CharField(max_length=11)
    locat_do_disp = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    
    def __str__(self):
        return self.id_tombamento