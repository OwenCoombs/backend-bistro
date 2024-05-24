from rest_framework import viewsets

from .models import *
from .serializers import *

# Create your views here.



class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer



class OrderNameViewSet(viewsets.ModelViewSet):
    queryset = OrderName.objects.all()
    serializer_class = OrderNameSerializer




