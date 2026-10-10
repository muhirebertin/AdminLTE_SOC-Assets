from django import forms
from .models import NetworkAsset


class NetworkAssetForm(forms.ModelForm):
    class Meta:
        model = NetworkAsset
        fields = ['name', 'ip_address', 'asset_type', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Core-Router-01'}),
            'ip_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '192.168.1.1'}),
            'asset_type': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }