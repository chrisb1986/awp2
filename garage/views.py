from django.http import HttpResponse
from .models import Car_model


def index(request):
    all_cars  = Car_model.objects.all()
    html = ''
    for cars in all_cars:
        url = '/garage/' + str(cars.id) + '/'
        html += '<a href="' + url + '">' + cars.model_name + '</a><br>'
    return HttpResponse(html)
    # return HttpResponse("<h1>This is 'Garage' page!</h1>")

def detail(request, car_id):
    return HttpResponse("<h2>Details for Car id: " + str(car_id) + "</h2>" )
