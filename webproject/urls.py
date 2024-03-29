"""
URL configuration for webproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from webproject import settings


schema_view = get_schema_view(
   openapi.Info(
      title="TG-Tire API",
      default_version='v1',
      description="Welcome to the TG-Tire API – your gateway to comprehensive vehicle data sourced from the Astra Federal Office of Switzerland. Our meticulously processed and standardized dataset allows you to seamlessly access information about tire and wheel dimensions for various vehicle models.",
      contact=openapi.Contact(email="ricardo.landolt1@gmail.com"),
   ),
   public=True, # Set to False restrict access to protected endpoints
   permission_classes=(permissions.AllowAny,), # Permissions for docs access
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tgcodes/', include('tgcode.urls')),
    path('rims/', include('rim.urls')),
    path('tires/', include('tire.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)