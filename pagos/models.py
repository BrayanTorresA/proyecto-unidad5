from django.db import models
from users.models import User
from servicios.models import Service

# Create your models here.


class PaymnentUser(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cliente")
    servicio = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="servicio")
    monto = models.FloatField(default=0.0)
    fecha_pago = models.DateField(auto_now_add=True)
    fecha_expiracion = models.DateField()

    class Meta:
        db_table = "pagos"

class ExpiredPayments(models.Model):
    pago_usuario=models.ForeignKey(PaymnentUser,on_delete=models.CASCADE,related_name="pago_usuario")
    penalty_fee_amount=models.FloatField(default=0.0)

    class Meta:
        db_table="pagos_vencidos"