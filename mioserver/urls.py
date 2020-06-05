from django.urls import path
from . import views
urlpatterns = [
    path('api/product/', views.ProductListCreate.as_view()),
    path('api/image/', views.ImageListCreate.as_view()),
    path('api/product/<str:product_type>/',
         views.ProductListFiltered.as_view()),
]
