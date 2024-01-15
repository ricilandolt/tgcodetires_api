from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from tire.models import Tire
from tire.serializers import TireSerializer

class ListTireView(ListCreateAPIView):
    queryset = Tire.objects.all()
    serializer_class=TireSerializer