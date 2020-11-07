from django.contrib import admin
from .models import Guide


# Register your models here.

class GuideAdmin(admin.ModelAdmin):
    list_display = ('isim', 'soyisim', 'numara')
    list_filter = ('isim',)
    list_select_related = ('isim',)
    class Meta:
        model = Guide

admin.site.register(Guide)