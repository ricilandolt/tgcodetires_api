from django.urls import path
from rim.views import ListRimView

urlpatterns = [
    path('', ListRimView.as_view())
]