from django.db import models

# Create your models here.

# class CustomerProfile(models.Model):
#     customer_first_name = models.CharField(max_length=50)
#     customer_last_name = models.

class TestClass(models.Model):
    name = models.CharField(max_length=100)
    field_one = models.CharField(max_length=50)
    field_two = models.CharField(max_length=50)

    def __str__(self):
        return self.name