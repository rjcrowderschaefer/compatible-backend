from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main_app import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryView, 'category')
router.register(r'feedbacks', views.FeedbackView, 'feedback')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
