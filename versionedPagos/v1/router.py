from .api import PaymentUserViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'pagos',PaymentUserViewSet,basename='pagos')

urlpatterns=router.urls