from rest_framework import viewsets, status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import mixins
from rest_framework.pagination import LimitOffsetPagination
from .models import Author, Book, Article, Biography
from .serializers import AuthorModelSerializer, BookModelSerializer, ArticleModelSerializer, BiographyModelSerializer, \
    SimpleAuthorModelSerializer


class BookLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ArticleLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class AuthorModelViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    filterset_fields = ['first_name', 'last_name', 'birthday_year']


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    pagination_class = BookLimitOffsetPagination
    filterset_fields = ['name']


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
    pagination_class = ArticleLimitOffsetPagination
    filterset_fields = ['name', 'author']


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer
