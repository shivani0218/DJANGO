from rest_framework import status
from .serializers import  ItemsSerializer
from rest_framework.views import  APIView
from  rest_framework.response import Response
from .models import Items
# Create your views here.

class ItemView(APIView):
    def post(self,request):
        serializer = ItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success","data": serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
       items = Items.objects.all()
       serializer = ItemsSerializer(items,many=True)
       return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def get(self,request, product=None):
        if product:
            item = Items.objects.get()
            serializer = ItemsSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        items = Items.objects.all()
        serializer = ItemsSerializer(items, many = True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)