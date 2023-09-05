from rest_framework import generics
from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(APIView):
    
    def get(self, request):
        data = {
            "message": "Welcome to the menu project!",
        }
        return Response(data)

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemList(generics.ListCreateAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        category_name = self.request.query_params.get('category')
        if category_name:
            return MenuItem.objects.filter(category__name=category_name)
        return MenuItem.objects.all()