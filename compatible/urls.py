from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main_app import views
from main_app import urls

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryView, 'category')
router.register(r'listings', views.ListingView, 'listing')
router.register(r'featuredlists', views.FeaturedListingView, 'featurelist')
router.register(r'feedbacks', views.FeedbackView, 'feedback')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/v1/users/', include('main_app.urls')),
]
