from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('finches/<int:finch_id>/assoc_land/<int:land_id>/', views.assoc_land, name='assoc_land'),
    path('finches/<int:finch_id>/unassoc_land/<int:land_id>/', views.unassoc_land, name='unassoc_land'),
    path('lands/', views.LandList.as_view(), name='lands_index'),
    path('lands/<int:pk>/', views.LandDetail.as_view(), name='lands_detail'),
    path('lands/create/', views.LandCreate.as_view(), name='lands_create'),
    path('lands/<int:pk>/update', views.LandUpdate.as_view(), name='lands_update'),
    path('lands/<int:pk>/delete/', views.LandDelete.as_view(), name='lands_delete'),
]
