from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from tgcode.models import TgCode
from tgcode.serializers import TgCodeSerializer

class ListTgcodeView(ListCreateAPIView):
    serializer_class=TgCodeSerializer
    def get_queryset(self):
        search = self.request.query_params.get('tgcode')
        if search : 
            return TgCode.objects.filter(tgcode=search)
        return TgCode.objects.all()
