
from rest_framework.routers import SimpleRouter
from .views import EmpViewSet

routerInstance = SimpleRouter()
routerInstance.register('employee',EmpViewSet)

urlpatterns = routerInstance.urls