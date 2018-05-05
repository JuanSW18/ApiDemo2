from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=50)
    apellido_cliente = models.CharField(max_length=50)
    telefono_cliente = models.CharField(max_length=9)

    def __str__(self):
        return "%s %s" % (self.nombre_cliente, self.apellido_cliente)

class TipoPropiedad(models.Model):
    id_tipoPropiedad = models.AutoField(primary_key=True)
    tipoPropiedad = models.CharField(max_length=20)

    def __str__(self):
        return self.tipoPropiedad

class Propiedad(models.Model):
    id_propiedad = models.AutoField(primary_key=True)
    id_tipoPropiedad = models.ForeignKey(TipoPropiedad, on_delete=models.CASCADE, default=2)
    num_habitacion = models.IntegerField()

    def __str__(self):
        return str(self.id_tipoPropiedad)

class ContratoEstado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return self.estado

class Contrato(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=1)
    id_propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, default=1)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    id_estadoContrato = models.ForeignKey(ContratoEstado, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return "%s %s" % (str(self.fecha_inicio), str(self.fecha_fin))


