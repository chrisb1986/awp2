from django.conf.urls import url
from . import views

urlpatterns = [
    # /garage/ = garage index page.
    url(r'^$', views.index, name='index'),

    # /garage/xx/ = garage id after /garage/ page.
    url(r'^(?P<car_id>[0-9]+)/$', views.detail, name='detail'),
]