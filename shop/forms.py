from django import forms
from .models import Package


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ('location', 'pack_number', 'description', 'price', 'start_date', 'end_date', 'rating', 'weather',
                  'lat', 'lng',)
