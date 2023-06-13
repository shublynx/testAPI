from django.shortcuts import render
from .models import Product
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import ProductSerializer

@api_view(['GET','PUT','POST'])
def index(request):
    if request.method == 'GET':

        quesryset = Product.objects.all()
        serializer = ProductSerializer(quesryset,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        posted_data = request.data    # data posted
        serializer = ProductSerializer(data=posted_data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)