from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.views.generic import UpdateView, DeleteView, CreateView

from .models import Guide
from .forms import GuideForm


# Create your views here.

class NumaraListele(generic.ListView):
    model = Guide
    template_name = 'kisi_liste.html'
    success_url = '/'
    
    def get_queryset(self):
        return Guide.objects.all()

class NumaraOlutur(CreateView):
    model = Guide
    form_class = GuideForm
    template_name = 'kisi_duzenle.html'
    success_url = '/'

    def form_valid(self, form):
        self.objects = form.save(commit=False)
        self.objects.user = self.request.user
        self.objects.save()
        return super().form_valid(form)

class NumaraGuncelle(UpdateView):
    model = Guide
    form_class = GuideForm
    template_name = 'kisi_duzenle.html'
    success_url = '/'

    def get_object(self):
        return Guide.objects.get(pk=self.kwargs['pk'])

    def form_valid(self, form):
        self.objects = form.save(commit=False)
        self.objects.user = self.request.user
        self.objects.save()
        return super().form_valid(form)

class NumaraSil(DeleteView):
    model = Guide
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

def numara_detay(request, pk):
    numaralar = get_object_or_404(Guide, pk=pk)
    return render(request, 'kisi_detay.html', {'numaralar': numaralar})
