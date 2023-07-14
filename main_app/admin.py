from django.contrib import admin
from .models import Category, Listing, Feedback

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__all__')

class ListingAdmin(admin.ModelAdmin):
    list_display = '__all__'

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('__all__')

admin.site.register(Category)
admin.site.register(Feedback)