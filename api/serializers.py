from rest_framework import serializers
from hub.models import Products, Lessons


class ProductsSerializer(serializers.ModelSerializer):
    num_lessons = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = ['id', 'author', 'name', 'created_timestamp', 'price', 'min_users', 'max_users', 'description', 'num_lessons']

    def get_num_lessons(self, obj):
        return obj.lessons_set.count()

    def to_representation(self, instance):
        self.fields['lessons_set'] = LessonsSerializer(instance.lessons_set.select_related('product'), many=True)
        return super().to_representation(instance)

    """В строке  self.fields['lessons'] = LessonsSerializer(instance.lessons.select_related('product'), many=True)  
    происходит оптимизация запросов к базе данных. Здесь, при сериализации объекта  Products , метод  select_related(
    'product')  используется для выборки связанных объектов  Lessons  вместе с объектом  Products  в одном запросе к 
    базе данных. Это позволяет избежать проблемы N + 1, где для каждого объекта  Products  выполняется дополнительный 
    запрос к базе данных для получения связанных объектов  Lessons .

    Таким образом, использование  select_related  в методе  to_representation  помогает уменьшить количество запросов к 
    базе данных путем объединения необходимых данных в один запрос, что повышает производительность и эффективность 
    работы вашего приложения."""


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ['id', 'product', 'title', 'video_link']
