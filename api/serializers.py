from rest_framework.serializers import Serializer, ModelSerializer, SerializerMethodField, CharField
from django.contrib.auth.models import User
from .models import User, Book, Review

class LoginSerializer(Serializer):
    username = CharField()
    password = CharField()

class BookSerializer(ModelSerializer):
    reviews = SerializerMethodField()

    def get_reviews(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            reviews = Review.objects.filter(user=request.user, book=obj)
            return ReviewSerializer(reviews, many=True).data
        else:
            return []

    class Meta:
        model = Book
        fields = "__all__"

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
