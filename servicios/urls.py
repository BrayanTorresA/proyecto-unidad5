from rest_framework import routers
from .api import GetAllServiceView,ServiceViewSetAdmin
from django.urls import path

router_service=routers.DefaultRouter()
router_service.register(r'api/v2/servicios/admin',ServiceViewSetAdmin,'servicios-admin')

urlpatterns=[
    path(r'api/v2/servicios',GetAllServiceView.as_view(),name="servicios")
]

urlpatterns += router_service.urls