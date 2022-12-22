from .api import PaymentUserViewSetV2, ExpiredPaymentViewSet, ServiceViewSet
from rest_framework import routers

router_pagos = routers.DefaultRouter()
router_pagos.register(r'pagos', PaymentUserViewSetV2, basename='pagosV2')

pagos_urlpatterns = router_pagos.urls

router_servicios = routers.DefaultRouter()
router_servicios.register(
    r'servicios', ServiceViewSet, basename='serviciosV2')

servicios_urlpatterns = router_servicios.urls

router_servicios_vencidos = routers.DefaultRouter()
router_servicios_vencidos.register(
    r'pagos-vencidos', ExpiredPaymentViewSet, basename='pagos-vencidos')

servicios_vencidos_urlpatterns = router_servicios_vencidos.urls

urlpatterns = pagos_urlpatterns+servicios_urlpatterns+servicios_vencidos_urlpatterns


