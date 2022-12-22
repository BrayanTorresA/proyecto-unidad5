from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from pagos.models import PaymnentUser,ExpiredPayments
from servicios.models import Service
from servicios.serializers import ServiceSerializer
from rest_framework import viewsets
from .serializers import PaymentUserSerializerV2,ExpiredPaymentSerializer
from rest_framework.permissions import IsAuthenticated
from .pagination import StandardResultsSetPaginationV2
from rest_framework import viewsets, filters
from .throttle import v2RateThrottle


class PaymentUserViewSetV2(viewsets.ModelViewSet):
    queryset = PaymnentUser.objects.all()
    serializer_class = PaymentUserSerializerV2
    pagination_class = StandardResultsSetPaginationV2
    filter_backends = [filters.SearchFilter]
    search_fields = ['fecha_pago', 'fecha_expiracion']
    # throttle_classes = v2RateThrottle

    def get_permissions(self):
        if self.action in ['partial_update', 'update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        pago = super().create(request, *args, **kwargs)
        ultimo_pago = PaymnentUser.objects.order_by('-id').first()
        pago_db = PaymnentUser.objects.get(id=ultimo_pago.id)
        if pago_db.fecha_expiracion < pago_db.fecha_pago:
            penalty = pago_db.monto*0.15
            expired_payment = ExpiredPayments(
                pago_usuario=pago_db, penalty_fee_amount=penalty)
            expired_payment.save()
        return pago

class ExpiredPaymentViewSet(viewsets.ModelViewSet):

    queryset = ExpiredPayments.objects.all()
    serializer_class = ExpiredPaymentSerializer

    def get_permissions(self):

        if self.action in ['destroy','partial_update','update']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes=[IsAuthenticated]
        return [permission() for permission in permission_classes]


class ServiceViewSet(viewsets.ModelViewSet):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_permissions(self):

        if self.action in ['destroy','partial_update','update','create']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes=[IsAuthenticated]
        
        return [permission() for permission in permission_classes]
