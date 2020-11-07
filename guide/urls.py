from django.urls import path,include
from django.conf.urls import url
from . import views

app_name="guide"

urlpatterns = [
    url(r'^$', views.NumaraListele.as_view(), name='numara_liste'),
    url(r'^(?P<pk>\d+)$', views.numara_detay, name='numara_detay'),
    url(r'^(?P<pk>[0-9]+)/guncelle/$', views.NumaraGuncelle.as_view(), name='numara_guncelle'),
    url(r'^sil/(?P<pk>[0-9]+)/$', views.NumaraSil.as_view(), name='numara_sil'),
    url(r'^olustur/$', views.NumaraOlutur.as_view(), name='numara_olustur'),
]