from rest_framework import serializers
from pagos.models import PaymnentUser

class PaymentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymnentUser
        fields = '__all__'
        read_only_fields = '__all__',