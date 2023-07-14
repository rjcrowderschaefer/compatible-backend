from django.contrib import admin
from .models import Category
from .models import Feedback

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_description', 'category_img1', 'category_img2', 'category_img3', 'active_offer_total', 'created_at')

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'feedback', 'created_at')

admin.site.register(Category)
admin.site.register(Feedback)