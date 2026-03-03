from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movie')
router.register(r'seats', views.SeatViewSet, basename='seat')
router.register(r'bookings', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('', views.home, name='index'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('history/', views.booking_history, name='booking_history'),
    path('api/', include(router.urls)),
]
