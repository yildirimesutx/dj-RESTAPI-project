from django.urls import path
from .views import makale_list_create_api_view, makale_detail_api_view




urlpatterns = [
    path("makaleler/", makale_list_create_api_view, name="makale-listesi" ),
    path('makaleler/<int:pk>/', makale_detail_api_view, name="makale-detay")
]
 