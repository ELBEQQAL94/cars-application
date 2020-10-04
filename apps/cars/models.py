from django.db import models
#from django.contrib.auth.models import User

# Car Model
class Car(models.Model):
    # def charFieldType(models):
    #     return models.CharField(max_length=number)
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=4)
    image = models.CharField(max_length=2000)
    company = models.CharField(max_length=30)
    logo = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.PositiveIntegerField()
    color = models.CharField(max_length=30)
    car_type = models.CharField('car type',max_length=30)
    description = models.TextField()
    is_store =  models.BooleanField('is store',default=True)
    #seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
