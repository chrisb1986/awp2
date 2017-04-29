# from django.http import Http404
# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Car_model

def index(request):
    all_cars  = Car_model.objects.all()
    # html = ''
    # for cars in all_cars:
    #     url = '/garage/' + str(cars.id) + '/'
    #     html += '<a href="' + url + '">' + cars.model_name + '</a><br>'
    # template = loader.get_template('garage/index.html')
    context = {'all_cars': all_cars}
    return render(request, 'garage/index.html', {'all_cars': all_cars})
    # return HttpResponse(template.render(context, request))
    # return HttpResponse("<h1>This is 'Garage' page!</h1>")

def detail(request, car_id):
    # return HttpResponse("<h2>Details for Car id: " + str(car_id) + "</h2>" )
    # try:
    #     cars = Car_model.objects.get(pk=car_id)
    # except Car_model.DoesNotExist:
    #     raise Http404("Car does not exist")
    cars = get_object_or_404(Car_model, pk=car_id)
    return render(request, 'garage/detail.html', {'cars': cars})
