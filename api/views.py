from django.contrib.auth import authenticate, login as DjangoLogin
from django.db.models import Count, Avg
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book, Review
from .serializers import LoginSerializer, BookSerializer, ReviewSerializer

class AuthViewSet(ViewSet):
    @action(['POST'], False)
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                DjangoLogin(request, user)
                return Response({'message': 'You have successfully logged in.'})
            else:
                return Response({'message': 'username or password is wrong.'}, 401)
        else:
            return Response(serializer.errors, 400)

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        kwargs = self.request.query_params.dict()
        return queryset.filter(**kwargs)
    
    @action(['GET'], False)
    def suggest(self, request):
        favorite_genre = (
            Review.objects
            .filter(user=request.user)
            .values('book__genre')
            .annotate(genre_count=Count('book__genre'))
            .order_by('-genre_count')
            .first()
        )
        if favorite_genre:
            genre = favorite_genre['book__genre']
            top_books = (
                Book.objects
                .filter(genre=genre)
                .annotate(average_rating=Avg('review__rating'))
                .order_by('-average_rating')[:10]
            )
            serializer = self.get_serializer(top_books, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "There is not enough data about you."}, status=404)

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
