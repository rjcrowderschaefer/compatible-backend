from django.db import models

# class CustomerProfile(models.Model):
#     customer_first_name = models.CharField(max_length=50)
#     customer_last_name = models.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=500)
    category_img1 = models.CharField(max_length=200)
    category_img2 = models.CharField(max_length=200)
    category_img3 = models.CharField(max_length=200)
    active_offer_total = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        ordering = ['category_name']


class Feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField
    feedback = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta: 
        ordering = ['created_at']
