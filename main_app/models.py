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
    active_listing_total = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        ordering = ['category_name']

LISTING_TYPE = (
    ('Skill', 'Skill'),
    ('Need', 'Need'),
)

LISTING_COMP_CHOICES = (
    ('Skill Swap/Trade', 'Skill Swap/Trade'),
    ('Paid/Fee-based', 'Paid/Fee-based'),
    ('Free/No charge', 'Free/No charge'),
)

LISTING_STATUS_CHOICES = (
    ('Active', 'Active'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
    ('Withdrawn', 'Withdrawn'),
    ('Inactive', 'Inactive'),
)

class Listing(models.Model):
    listing_name = models.CharField(max_length=200)
    listing_description = models.TextField(max_length=500)
    listing_type = models.CharField(max_length=10, choices=LISTING_TYPE, default='Skill Swap/Trade')
    listing_comp_type = models.CharField(max_length=20, choices=LISTING_COMP_CHOICES)
    listing_status = models.CharField(max_length=20, choices=LISTING_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="listings")

    def __str__(self):
        return self.listing_name

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField
    feedback = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta: 
        ordering = ['created_at']
