from rest_framework import serializers
from .models import Book
from .models import Item



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id','category', 'subcategory', 'name', 'amount')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']








