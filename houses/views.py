from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect

from django.views.generic import (
  ListView,
  CreateView,
  UpdateView,
  DeleteView,
)

from django.urls import reverse_lazy
from .models import House

class HouseListView(ListView):
    model = House
    template_name = 'houses/house_list.html'

class HouseCreateView(CreateView):
    model = House
    fields = '__all__'
    template_name = 'houses/house_form.html'
    success_url = reverse_lazy('house_list')

class HouseUpdateView(UpdateView):
    model = House
    fields = '__all__'
    template_name = 'houses/house_form.html'
    success_url = reverse_lazy('house_list')

class HouseDeleteView(DeleteView):
    model = House
    template_name = 'houses/house_delete.html'
    success_url = reverse_lazy('house_list')

class HouseDeleteView(DeleteView):
    model = House
    template_name = 'houses/house_delete.html'
    success_url = reverse_lazy('house_list') # Or use reverse_lazy('house_list')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.error(
                self.request,
                "Cannot delete this house because one or more employees (like James Behling) are still assigned to it."
            )
            return redirect(self.success_url)
