from django.urls import path
from .views import PrintListView

urlpatterns = [path("", PrintListView.as_view(), name="index")]
