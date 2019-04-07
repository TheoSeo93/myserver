from restaurant.models import MenuSection
from restaurant.models import Item
from rest_framework import serializers


class MenuSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuSection
        fields = ('id', 'name')

    def create(self, validated_data):
        """
        Create and return a new `Section` instance, given the validated data.
        """
        return MenuSection.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Section` instance, given the validated data.
        """

        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name')

    def create(self, validated_data):
        """
        Create and return a new `Section` instance, given the validated data.
        """
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Section` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.menuName)
        instance.save()
        return instance
