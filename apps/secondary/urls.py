from django.urls import path

from apps.secondary import views

urlpatterns = [
    path('genplaning', views.genPlaning, name="genplaning"),
    path('ajax/get_floors_and_apartments/', views.get_floors_and_apartments, name='get_floors_and_apartments'),
    path('genplaning_detail/<int:apartment_id>/', views.genplaning_detail, name='genplaning_detail'),
]
