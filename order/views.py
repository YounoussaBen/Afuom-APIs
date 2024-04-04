from rest_framework import generics, status
from rest_framework.response import Response
from cart.models import Cart
from .models import ShippingAddress, Order, OrderItem
from .serializers import ShippingAddressSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated

class CheckoutView(generics.CreateAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get authenticated user
        user = request.user

        # Create shipping address
        shipping_address = serializer.save()

        # Get user's cart items
        cart_items = Cart.objects.filter(created_by=user)

        # Calculate total price of the order
        total_price = sum(item.product.price * item.quantity for item in cart_items)

        # Create order with the associated shipping address and user
        order = Order.objects.create(created_by=user, shipping_address=shipping_address, total_price=total_price)

        # Create order items
        for cart_item in cart_items:
            OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity, price=cart_item.product.price)

        # Clear user's cart
        cart_items.delete()

        return Response(status=status.HTTP_201_CREATED)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Order.objects.filter(created_by=user)
        else:
            # Return an empty queryset or handle as required
            return Order.objects.none()

    
class UserOrderHistoryView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(created_by=user)
    
class SellerOrderHistoryView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Filter orders where the order items have products created by the user
        return Order.objects.filter(
            items__product__created_by=user
        ).distinct()