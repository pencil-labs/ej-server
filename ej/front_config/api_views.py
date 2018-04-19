from .models import SocialMedia
from .serializers import SocialMediaSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

class SocialMediaViewSet(ModelViewSet):
    serializer_class = SocialMediaSerializer
    queryset = SocialMedia.objects.all()

