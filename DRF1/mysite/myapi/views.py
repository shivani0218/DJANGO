from rest_framework import viewsets

from .serializers import ProductSerializer, OrderSerializer
from .models import Product,Order
from  rest_framework.decorators import api_view
from  rest_framework.response import  Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

@api_view(['GET'])
def OrderList(request):
    orders = Order.objects.all()
    serializers = OrderSerializer(orders,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def OrderDetail(request,pk):
    orders = Order.objects.all(id = pk)
    serializers = OrderSerializer(orders,many=True)
    return Response(serializers.data)

@api_view(['POST'])
def OrderCreate(request):
    serializers = OrderSerializer(data = request.data)

    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def OrderUpdate(request,pk):
    order = Order.objects.get(id=pk)
    serializers = OrderSerializer(instance = order ,data = request.data)

    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def OrderDelete(request,pk):
    order = Order.objects.get(id=pk)
    order.save()
    return Response('Deleted')