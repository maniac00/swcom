from django.db import models

class Shop(models.model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    postcode = models.PositiveIntegerField()
    road_address = models.CharField(max_length=100)
    detail_address = models.CharField(max_length=100)
    # main_image = 
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)