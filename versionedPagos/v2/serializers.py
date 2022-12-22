from rest_framework import serializers
from servicios.models import Service
from pagos.models import PaymnentUser
from pagos.models import ExpiredPayments
from users.models import User

class PaymentUserSerializerV2(serializers.ModelSerializer):
    usuario=serializers.SlugRelatedField(queryset=User.objects.all(),slug_field="email")

    class Meta:
        model = PaymnentUser
        fields = ['id','usuario','servicio','monto','fecha_pago','fecha_expiracion']
        read_only_fields =['fecha_pago',]

class ExpiredPaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpiredPayments
        fields = "__all__"