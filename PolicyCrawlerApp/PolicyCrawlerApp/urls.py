
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('policies_app.urls')),
    path('', include('overview.urls')),
    path('', include('apis_app.urls')),
    path('', include('threat_detection_rules_app.urls')),
]
