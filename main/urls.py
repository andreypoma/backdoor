from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main),
    path('create/', views.create),
    path('<int:id>/', views.game),
    path('<int:id>/delete', views.destroy),
    path('<int:id>/join', views.joinGame),
    path('<int:id>/leave', views.leaveGame),
]