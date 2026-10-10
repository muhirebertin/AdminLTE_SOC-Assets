from django.db import models

class NetworkAsset(models.Model):
    ASSET_TYPES = (
        ('SERVER', 'Server'),
        ('ROUTER', 'Router'),
        ('FIREWALL', 'Firewall'),
        ('ENDPOINT', 'Workstation'),
    )
    STATUS_CHOICES = (
        ('ONLINE', 'Online'),
        ('OFFLINE', 'Offline'),
        ('MAINTENANCE', 'In Maintenance'),
    )

    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(unique=True)
    asset_type = models.CharField(max_length=20, choices=ASSET_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ONLINE')
    last_checked = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.ip_address})"


class SecurityEvent(models.Model):
    SEVERITY_LEVELS = (
        ('CRITICAL', 'Critical'),
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )

    asset = models.ForeignKey(NetworkAsset, on_delete=models.CASCADE, related_name='events')
    event_title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(max_length=20, choices=SEVERITY_LEVELS)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"[{self.severity}] {self.event_title} on {self.asset.name}"