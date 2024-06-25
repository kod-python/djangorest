from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from .models import Book, Item
from .serializers import BookSerializer
from .serializers import ItemSerializer
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.permissions import DjangoModelPermissions
# from rest_framework.decorators import permission_classes


# from snip.models import Snippet
# from snip.serializers import SnippetSerializer




@csrf_exempt   
@api_view(['GET'])
# @permission_classes((DjangoModelPermissions,))
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
 
    return Response(api_urls)   
    


@csrf_exempt
@api_view(['GET'])
def book_list(request):
    
     if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books,  many=True)
        return Response(serializer.data)
    

# TRIAL OPTIONS 

@csrf_exempt
@api_view(['POST'])
def add_items(request):
    serializer = ItemSerializer(data=request.data)
    
    if Item.objects.filter(**request.data).exists():
        return Response({'error': 'This data already exists'}, status=status.HTTP_400_BAD_REQUEST)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['GET'])
def view_items(request):
    if request.query_params:
        items = Item.objects.filter(**request.query_params.dict())
    else:
        items = Item.objects.all()

    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['PATCH'])
def update_items(request, pk):
    item = get_object_or_404(Item, pk=pk)
    serializer = ItemSerializer(instance=item, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)







# ENDS HERE












    



# @api_view(['GET'])
# def book_list(request):
    
#      if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookSerializer(books,  many=True)
#         return Response(serializer.data)
    
    
   
# @api_view(['POST'])
# def add_items(request):
#     item = ItemSerializer(data=request.data)
 
   
#     if Item.objects.filter(**request.data).exists():
#         raise serializers.ValidationError('This data already exists')
 
#     if item.is_valid():
#         item.save()
#         return Response(item.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)



# @api_view(['GET'])
# def view_items(request):
            
#     if request.query_params:
#         items = Item.objects.filter(**request.query_params.dict())
#     else:
#         items = Item.objects.all()
 
#     if items:
#         serializer = ItemSerializer(items, many=True)
#         return Response(serializer.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)





# @api_view(['PATCH'])
# def update_items(request, pk):
#     item = Item.objects.get(pk=pk)
#     data = ItemSerializer(instance=item, data=request.data)
 
#     if data.is_valid():
#         data.save()
#         return Response(data.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)





# @api_view(['DELETE'])
# def delete_items(request, pk):
# 	item = get_object_or_404(Item, pk=pk)
# 	item.delete()
# 	return Response(status=status.HTTP_202_ACCEPTED)
















