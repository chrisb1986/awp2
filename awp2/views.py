from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>iGarage website created by Chris Brierley - U1374769</h1>"
                        "<h2>Created using Django for Advance Web Programming Assignment #2</h2>"
                        "<h3>Click <a href='/garage/'>HERE</a> to enter iGarage!</h3>")