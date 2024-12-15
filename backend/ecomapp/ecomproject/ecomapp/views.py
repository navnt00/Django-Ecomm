from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Products
from .seralizers import ProductSeralizers
from django.db.models import Q
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def getProduct(request, pk):
    try:
        product = Products.objects.get(_id=pk) 
        serializer = ProductSeralizers(product, many=False)
        return Response(serializer.data)
    except Products.DoesNotExist:
        return Response({'detail': 'Product not found'}, status=404)

@api_view(['GET'])
def getAllProducts(request):
    try:
        products = Products.objects.all()
        serializer = ProductSeralizers(products, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'detail': str(e)}, status=500)


@api_view(['GET'])
def searchProduct(request, keyword):
    try:
        query = Q(productname__icontains=keyword) | \
                Q(productbrand__icontains=keyword) | \
                Q(productcategory__icontains=keyword) | \
                Q(product_Info__icontains=keyword)
        products = Products.objects.filter(query)
        serializer = ProductSeralizers(products, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'detail': str(e)}, status=500)

@api_view(['POST'])
def addProduct(request):
    try:
        data = request.data
        serializer = ProductSeralizers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
    except Exception as e:
        logger.error(f"Error in addProduct: {str(e)}")
        return Response({'detail': str(e)}, status=500)