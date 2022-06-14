from django.urls import path, include
from . import views
app_name = 'membership'
urlpatterns = [
       path('memberships/', views.MembershipView.as_view(), name='select'),
]