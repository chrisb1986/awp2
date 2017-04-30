from django.conf.urls import url
from . import views

app_name = 'garage'

urlpatterns = [
    # /garage/ = garage index page.
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /garage/<car_id>/ = car id after /garage/ page.
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
