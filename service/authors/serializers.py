from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, StringRelatedField
from .models import Author, Article, Book, Biography


class SimpleAuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'url']


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BiographyModelSerializer(HyperlinkedModelSerializer):
    author = SimpleAuthorModelSerializer()

    class Meta:
        model = Biography
        fields = '__all__'


class ArticleModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class BookModelSerializer(HyperlinkedModelSerializer):
    authors = SimpleAuthorModelSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
