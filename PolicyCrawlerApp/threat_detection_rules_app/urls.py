from django.urls import path, include
from .views import Index, SearchEngine, export_threat_detection_rules_xls
urlpatterns = [
    path('threat-detection/', Index, name='threat-detection'),
    # path('policy/search/', SearchEngine.as_view(), name='search'),
    path('search-threat-detection-rule/', SearchEngine, name='search-data-threat-detection-rule'),
    path(r'^export-threat-detection-rules/xls/$', export_threat_detection_rules_xls, name='export_threat_detection_rules_xls')
]
