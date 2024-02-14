from rest_framework import serializers

class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)


class ProductSrializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    desc = serializers.CharField(max_length=1000)