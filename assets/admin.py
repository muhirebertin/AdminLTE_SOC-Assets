from django.contrib import admin
from .models import NetworkAsset, SecurityEvent

@admin.register(NetworkAsset)
class NetworkAssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'asset_type', 'status', 'last_checked')
    list_filter = ('asset_type', 'status')
    search_fields = ('name', 'ip_address')

@admin.register(SecurityEvent)
class SecurityEventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'asset', 'severity', 'timestamp', 'is_resolved')
    list_filter = ('severity', 'is_resolved')
    search_fields = ('event_title', 'description')