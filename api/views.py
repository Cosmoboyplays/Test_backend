from rest_framework import generics
from hub.models import Products, Lessons
from .serializers import ProductsSerializer, LessonsSerializer

from rest_framework import generics


class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class LessonsList(generics.ListCreateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
