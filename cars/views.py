from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect

from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  UpdateView,
  DeleteView,
)

from django.urls import reverse_lazy
from .models import Car, CarMaintenance

class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'

class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'

class CarCreateView(CreateView):
    model = Car
    fields = '__all__'
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('car_list')

class CarUpdateView(UpdateView):
    model = Car
    fields = '__all__'
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('car_list')

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'cars/car_delete.html'
    success_url = reverse_lazy('car_list')

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'cars/car_delete.html'
    success_url = reverse_lazy('car_list') # Or use reverse_lazy('car_list')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.error(
                self.request,
                "Cannot delete this car because one or more employees (like James Behling) are still assigned to it."
            )
            return redirect(self.success_url)

class MaintenanceCreateView(CreateView):
    model = CarMaintenance
    fields = '__all__'
    template_name = 'cars/maintenance_form.html'

    def form_valid(self, form):
        # Automatically tie the maintenance record to the car being viewed
        form.instance.car_id = self.kwargs['car_pk']
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch the specific car and add it to the template context
        context['car'] = Car.objects.get(pk=self.kwargs['car_pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.kwargs['car_pk']})
