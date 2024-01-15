from django.urls import path
from tgcode.views import ListTgcodeView

urlpatterns = [
    path('', ListTgcodeView.as_view())
]