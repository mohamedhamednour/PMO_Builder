

from  django.urls import path , include
from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("subscribe", views.SubscribeViewset, basename="subscribe")
urlpatterns = [
    path("", include(router.urls)),
]