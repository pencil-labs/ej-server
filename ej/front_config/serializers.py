
from rest_framework import serializers
from .models import SocialMedia


class SocialMediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ('id','url','name', 'link', 'priority', 'material_icon', 'fa_icon')
