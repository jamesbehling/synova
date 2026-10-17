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
from .models import Title

class TitleListView(ListView):
    model = Title
    template_name = 'titles/list.html'

class TitleCreateView(CreateView):
    model = Title
    fields = [
        'name'
    ]
    template_name = 'titles/form.html'
    success_url = reverse_lazy('title_list')

class TitleUpdateView(UpdateView):
    model = Title
    fields = [
        'name'
    ]
    template_name = 'titles/form.html'
    success_url = reverse_lazy('title_list')

class TitleDeleteView(DeleteView):
    model = Title
    template_name = 'titles/delete.html'
    success_url = reverse_lazy('title_list')

class TitleDeleteView(DeleteView):
    model = Title
    template_name = 'titles/delete.html'
    success_url = reverse_lazy('title_list') # Or use reverse_lazy('title_list')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.error(
                self.request,
                "Cannot delete this title because one or more employees (like James Behling) are still assigned to it."
            )
            return redirect(self.success_url)
