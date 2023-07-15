from rest_framework import serializers
from .models import Category, Listing, Feedback

# Song
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'

# Artist

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    listings = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=False,
        queryset=Listing.objects.all()
        )
    
    class Meta:
        model = Category
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'