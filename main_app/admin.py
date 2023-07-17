from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Category, Listing, FeaturedListing, Feedback, CustomUser

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__all__')

class ListingAdmin(admin.ModelAdmin):
    list_display = '__all__'

class FeaturedListingAdmin(admin.ModelAdmin):
    list_display = '__all__'

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('__all__')

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email']

admin.site.register(Category)
admin.site.register(Feedback)
admin.site.register(Listing)
admin.site.register(FeaturedListing)
admin.site.register(CustomUser, CustomUserAdmin)