from rest_framework import serializers
from .models import Category, Listing, Feedback, FeaturedListing, CustomUser

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    listings = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=False,
        queryset=Listing.objects.all()
        )
    
    class Meta:
        model = Category
        fields = '__all__'

class FeaturedListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedListing
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'last_login', 'date_joined', 'is_staff')