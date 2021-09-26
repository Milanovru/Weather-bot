from rest_framework import routers
from .views import UsersViewSet, RegistrationViewSet


router = routers.DefaultRouter()
router.register('subscribers', UsersViewSet, basename='subscribers')
router.register('accounts/users', RegistrationViewSet, basename='users')

urlpatterns = router.urls
