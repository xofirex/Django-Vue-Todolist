from rest_framework import routers
from .api import TaskViewSet

app_name = 'tasks'
router = routers.DefaultRouter()
router.register('api/tasks', TaskViewSet, 'tasks')

urlpatterns = router.urls