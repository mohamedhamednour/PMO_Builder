
from django.contrib import admin
from django.urls import path , include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userapp.urls')),
    path('', include('subscribeapp.urls')),
    path('', include('uploadprojectapp.urls')),
    # OpenAPI schema endpoint
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Redoc UI
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)