from .models import Service
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ServiceSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework import viewsets
from .pagination import StandardResultsSetPagination


class ServiceViewSetAdmin(viewsets.ModelViewSet):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAdminUser]

# Mostrar la lista de servicios


class GetAllServiceView(APIView):

    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        servicios = Service.objects.all()
        serializer = ServiceSerializer(servicios, many=True)
        return Response(serializer.data)
