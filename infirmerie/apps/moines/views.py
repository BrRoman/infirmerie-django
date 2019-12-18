""" apps/moines/views.py """

from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .models import Moine
from .forms import MoineForm


class MoineListView(ListView):  # pylint: disable=too-many-ancestors
    """ List of Moines. """
    template_name = 'moines/list.html'

    def get_queryset(self):
        return Moine.objects.order_by('-nom_religieux')[:5]


class MoineCreateView(CreateView):
    """ Create Moine. """
    model = Moine
    form_class = MoineForm
    template_name = 'moines/form.html'
    success_url = reverse_lazy('moines:list')


class MoineDetailView(DetailView):
    """ Detail of Moine. """
    fields = ('__all__')
    model = Moine
    template_name = 'moines/detail.html'


class MoineUpdateView(UpdateView):
    """ Update Moine. """
    model = Moine
    form_class = MoineForm
    template_name = 'moines/form.html'
    success_url = reverse_lazy('moines:list')
