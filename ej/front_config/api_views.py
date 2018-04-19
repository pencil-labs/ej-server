from .models import SocialMedia, ColorPallet
from .serializers import SocialMediaSerializer, ColorPalletSerializer
from rest_framework.viewsets import ModelViewSet

class SocialMediaViewSet(ModelViewSet):
    serializer_class = SocialMediaSerializer
    queryset = SocialMedia.objects.all()

class ColorPalletViewSet(ModelViewSet):
    serializer_class = ColorPalletSerializer
    queryset = ColorPallet.objects.all()
