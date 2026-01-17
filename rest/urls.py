from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


app_name = "rest"

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = router.urls
