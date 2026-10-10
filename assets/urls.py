from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard'),
    path('resolve/<int:event_id>/', views.resolve_event, name='resolve_event'),
    path('inventory/', views.asset_inventory, name='asset_inventory'),
    path('threats/', views.threat_logs, name='threat_logs'),

]