from rest_framework import serializers
from . import models

class ImageSerializer(serializers.Serializer):
    class Meta:
        model = models.Image
        fileds = '__all__'


class CommentSerializer(serializers.Serializer):
    class Meta:
        model = models.Comment
        fileds = '__all__'

class LikeSerializer(serializers.Serializer):
    class Meta:
        model = models.Like
        fileds = '__all__'

