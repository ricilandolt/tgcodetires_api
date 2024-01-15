from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rim.models import Rim
from rim.serializers import RimSerializer

class ListRimView(ListCreateAPIView):
    queryset = Rim.objects.all()
    serializer_class=RimSerializer