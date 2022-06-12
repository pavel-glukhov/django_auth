from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

api_router = DefaultRouter()

api_router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(api_router.urls)),
    path('auth/token/', views.CreateToken.as_view(), name='token'),
    path('auth/signup/', views.Signup.as_view(), name='signup'),
]
