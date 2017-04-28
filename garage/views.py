from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is 'Garage' page!</h1>")

def detail(request, car_id):
    return HttpResponse("<h2>Details for Car id: " + str(car_id) + "</h2>" )
