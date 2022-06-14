from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("",views.OrderList,name="Order_list"),
    path("create/", views.OrderCreate,name="Order_create"),
    path("update/<int:pk>/",views.OrderUpdate,name="Order_Update"),
    path("delete/<int:pk>/",views.OrderDelete,name="Order_Delete")
]
