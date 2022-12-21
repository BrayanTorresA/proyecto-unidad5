from pagos.models import PaymnentUser
from rest_framework import viewsets
from .serializers import PaymentUserSerializer
from rest_framework.permissions import IsAuthenticated
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters


class PaymentUserViewSet(viewsets.ModelViewSet):
    queryset = PaymnentUser.objects.all()
    serializer_class = PaymentUserSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user_id','fecha_pago','servicio']
