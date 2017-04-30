from django.conf.urls import url
from . import views

app_name = 'garage'

urlpatterns = [
    # /garage/ = garage index page.
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /garage/<car_id>/ = car id after /garage/ page.
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /garage/car/add/ = add new car page.
    url(r'car/add/$', views.CarCreate.as_view(), name='car-add'),

    # /garage/car/<car_id>/ = update car page.
    url(r'car/(?P<pk>[0-9]+)/$', views.CarUpdate.as_view(), name='car-update'),

    # /garage/car/<car_id>/delete/ = delete car page.
    url(r'car/(?P<pk>[0-9]+)/delete/$', views.CarDelete.as_view(), name='car-delete'),
]
