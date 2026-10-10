from django.shortcuts import render, redirect, get_object_or_404
from .models import NetworkAsset, SecurityEvent
import psutil
from .forms import NetworkAssetForm


def dashboard_home(request):
    assets = NetworkAsset.objects.all()
    recent_events = SecurityEvent.objects.all().order_by('-timestamp')[:5]
    live_cpu = psutil.cpu_percent(interval=0.1)

    critical_count = SecurityEvent.objects.filter(severity='CRITICAL').count()
    high_count = SecurityEvent.objects.filter(severity='HIGH').count()
    medium_count = SecurityEvent.objects.filter(severity='MEDIUM').count()
    low_count = SecurityEvent.objects.filter(severity='LOW').count()
    unresolved_count = SecurityEvent.objects.filter(is_resolved=False).count()
    context = {
        'total_assets': assets.count(),
        'online_assets': assets.filter(status='ONLINE').count(),
        'recent_events': recent_events,
        'cpu_usage': live_cpu,
        'critical_count': critical_count,
        'high_count': high_count,
        'medium_count': medium_count,
        'low_count': low_count,
        'unresolved_count': unresolved_count,
    }
    return render(request, 'dashboard.html', context)


def resolve_event(request, event_id):
    event = get_object_or_404(SecurityEvent, id=event_id)
    event.is_resolved = True
    event.save()
    return redirect('dashboard')
def asset_inventory(request):
    all_assets = NetworkAsset.objects.all()
    if request.method == 'POST':
        form = NetworkAssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_inventory')
    else:
        form = NetworkAssetForm()

    context = {
        'form': form,
        'all_assets': all_assets,
    }
    return render(request, 'inventory.html', context)

def threat_logs(request):
    all_events = SecurityEvent.objects.all().order_by('is_resolved', '-timestamp')

    context = {
        'all_events': all_events
    }
    return render(request, 'threats.html', context)