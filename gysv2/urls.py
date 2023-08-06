from django.contrib import admin
from django.urls import include, path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Get Your Slots api",
      default_version='v1',
      description="Booking API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kamleshgupta594@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path("locations/", include("locations.urls")),
    path("bookings/", schema_view.with_ui('redoc', cache_timeout=0)),
    path('api-auth/', include('rest_framework.urls')),
    path("auth/", include("accounts.urls")),

]
