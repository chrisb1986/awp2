from django.views import generic
from .models import Car_model

class IndexView(generic.ListView):
    template_name = 'garage/index.html'
    context_object_name = 'all_cars'

    def get_queryset(self):
        return Car_model.objects.all()

class DetailView(generic.DetailView):
    model = Car_model
    template_name = 'garage/detail.html'
