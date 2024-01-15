from django.urls import path
from tire.views import ListTireView

urlpatterns = [
    path('', ListTireView.as_view())
]