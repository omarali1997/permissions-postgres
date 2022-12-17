from .models import Snack,Post
from rest_framework import serializers

class SweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        # fields = '__all__'
        fields = ['id','title','purchaser','description']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['id','title','description']