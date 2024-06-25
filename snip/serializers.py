from rest_framework import serializers
from .models import Book
from .models import Item




# class ItemSerializer(serializers.ModelSerializer):
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)

#     class Meta:
#         model = Item
#         fields = '__all__'

#     def validate_price(self, value):
#         try:
#             return float(value)
#         except ValueError:
#             raise serializers.ValidationError('Price must be a decimal number')








# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         fields = '__all__'





class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id','category', 'subcategory', 'name', 'amount')
        
        
        

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']








