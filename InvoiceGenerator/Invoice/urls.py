from django.urls import  path
from .views import  ItemView

urlpatterns = [
    path('products/', ItemView.as_view()),
    path('Get-products/', ItemView.as_view()),
    path('products/<int:id>', ItemView.as_view()),
]
