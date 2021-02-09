from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSetMixin

from titles.models import Category, Genre, Review, Title, User

from .filters import TitleFilter
from .permissions import IsAdminOrReadOnly, IsSuperUserPermission
from .serializers import (CategorySerializer, CommentsSerializer,
                          GenreSerializer, ReviewSerializer,
                          TitleProvideSerializer, TitleTakeSerializer,
                          UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (IsSuperUserPermission, )
    serializer_class = UserSerializer
    search_fields = ['username']
    lookup_field = 'username'

    @action(methods=['GET', 'PATCH'], detail=False,
            name='me', permission_classes=(IsAuthenticated, ))
    def me(self, request):
        user = get_object_or_404(
            User,
            username=request.user.username
        )
        serializer = UserSerializer(user)
        if request.method == 'PATCH':
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
        return Response(serializer.data)


class CategoriesList(
    ViewSetMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'


class GenresList(
    ViewSetMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'


class TitlesViewSet(ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg("reviews__score"))
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, )
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method in ["POST", "PATCH"]:
            return TitleTakeSerializer
        return TitleProvideSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsSuperUserPermission]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs["title_id"])
        queryset = title.reviews.all()

        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentsViewSet(ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = [IsSuperUserPermission]
    pagination_class = PageNumberPagination

    @property
    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs["review_id"])
        queryset = review.comments.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
