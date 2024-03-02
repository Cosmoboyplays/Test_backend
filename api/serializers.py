from rest_framework import serializers
from hub.models import Products, Lessons


class ProductsSerializer(serializers.ModelSerializer):
    num_lessons = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = ['id', 'author', 'name', 'created_timestamp', 'price', 'min_users', 'max_users', 'description', 'num_lessons']

    def get_num_lessons(self, obj):
        return obj.lessons_set.count()


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ['id', 'product', 'title', 'video_link']
