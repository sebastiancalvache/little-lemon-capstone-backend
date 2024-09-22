from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'tables', views.BookingViewSet)
urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuitemView.as_view()),
    path('booking/', include(router.urls)),
]