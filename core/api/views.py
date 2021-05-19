from rest_framework.generics import ListAPIView
from core.models import Item
from .serializers import ItemSerializer

class ItemListView(ListAPIView):
    permission_classes = ()
    serializer_class = ItemSerializer 
    queryset = Item.objects.all()