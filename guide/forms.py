from django import forms
from .models import Guide
from django.db import models


class GuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = ('isim', 'soyisim', 'numara')