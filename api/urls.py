from rest_framework.routers import SimpleRouter
from .views import CustomersViewSet

routers = SimpleRouter()
routers.register('customers', CustomersViewSet)