from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Apartment
from .forms import ApartmentForm
# Create your views here.


class HomeView(TemplateView):
    template_name = 'apartments/home.html'


class ApartmentListView(ListView):
    model = Apartment


class ApartmentDetailView(DetailView):
    model = Apartment
    # PK -->{{apartment}}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def create_apartment(request):
    form = ApartmentForm()
    if request.method == "POST":
        form = ApartmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/apartments/list")
    context = {
        "form": form
    }
    return render(request, "apartments/create_apartment.html", context)


def apartment_update(request, pk):
    apartment = Apartment.objects.get(id=pk)
    form = ApartmentForm(instance=apartment)

    if request.method == "POST":
        form = ApartmentForm(
            request.POST, instance=apartment, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/apartments/list")
    context = {
        "form": form
    }
    return render(request, "apartments/apartment_update.html", context)


class ApartmentDeleteView(DeleteView):
    # form -->confirm delete button
    # default template: model_confirm_delete.html
    model = Apartment
    success_url = reverse_lazy('apartments:apartment_list')
