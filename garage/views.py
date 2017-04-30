from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car_model

class IndexView(generic.ListView):
    template_name = 'garage/index.html'
    context_object_name = 'all_cars'

    def get_queryset(self):
        return Car_model.objects.all()

class DetailView(generic.DetailView):
    model = Car_model
    template_name = 'garage/detail.html'

class CarCreate(CreateView):
    model = Car_model
    fields = ['engine', 'model_name', 'colour', 'car_image']