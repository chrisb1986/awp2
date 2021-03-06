from django.db import models
from django.core.urlresolvers import reverse

class Car_model(models.Model):
    engine = models.CharField(max_length=4)
    model_name = models.CharField(max_length=15)
    colour = models.CharField(max_length=10)
    # car_image = models.CharField(max_length=1000)
    car_image = models.FileField()

    def get_absolute_url(self):
        return reverse('garage:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.model_name + ' - ' + self.engine

class Variation (models.Model):
    car_model = models.ForeignKey(Car_model, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    variation_type = models.CharField(max_length=15)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.variation_type