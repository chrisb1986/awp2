from django.db import models

class Car_model(models.Model):
    engine = models.CharField(max_length=4)
    model_name = models.CharField(max_length=15)
    colour = models.CharField(max_length=10)
    car_image = models.CharField(max_length=1000)

class Variation (models.Model):
    car_model = models.ForeignKey(Car_model, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    variation_type = models.CharField(max_length=15)