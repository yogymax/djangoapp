from rest_framework.routers import SimpleRouter
from .views import StudentViewSet

routerInstance = SimpleRouter()
routerInstance.register('student',StudentViewSet)

urlpatterns = routerInstance.urls