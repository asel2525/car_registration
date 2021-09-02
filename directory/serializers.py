from rest_framework import serializers
from directory.models import Brand, Mark

class MarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mark
        fields = ['id', 'name', 'brand', ]

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['id', 'name', ]


