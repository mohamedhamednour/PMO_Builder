

from  django.urls import path , include
from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("projects", views.ProjectViewSet, basename="project")
urlpatterns = [
    path("", include(router.urls)),
    path("inital-webhook-project/", views.inital_webhook_project, name="inital-webhook-project"),
    path('genrate-domain', views.genrate_domain, name="genrate-domain"),
]