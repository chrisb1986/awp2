from django.conf.urls import url
from . import views

app_name = 'garage'

urlpatterns = [
    # /garage/ = garage index page.
    url(r'^$', views.index, name='index'),

    # /garage/<car_id>/ = car id after /garage/ page.
    url(r'^(?P<car_id>[0-9]+)/$', views.detail, name='detail'),

    # /garage/<car_id>/favorite/
    # url(r'^(?P<car_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]
