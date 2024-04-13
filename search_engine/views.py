from rest_framework import generics, permissions
from shop.models import Product
from shop.serializers import ProductSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

category_param = openapi.Parameter(
    'categories', openapi.IN_QUERY, required=False, type=openapi.TYPE_ARRAY,
    items=openapi.Items(type=openapi.TYPE_STRING), description='Filter products by comma-separated category names'
)

query_param = openapi.Parameter(
    'query', openapi.IN_QUERY, required=False, type=openapi.TYPE_STRING,
    description='Search products by name, description, or other relevant fields'
)

class SearchEngineView(generics.ListAPIView):
    
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


    @swagger_auto_schema(manual_parameters=[category_param, query_param])
    def get_queryset(self):
        # Get the search query from the request's query parameters
        search_query = self.request.query_params.get('query', '')
        categories = self.request.query_params.getlist('categories')
        
        if search_query:
            # Use the custom search method from the ProductManager
            return Product.objects.search_products(search_query, categories)
        else:
            # If no search query is provided, return all products
            return Product.objects.all()
