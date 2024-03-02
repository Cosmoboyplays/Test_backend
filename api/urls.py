from django.urls import path

from api.views import ProductsList, LessonsList

app_name = 'api'

urlpatterns = [
    path('products/', ProductsList.as_view(), name='products-list'),
    path('lessons/', LessonsList.as_view(), name='lessons-list'),
]
