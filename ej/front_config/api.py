import ej.front_config.api_views


def register(router):
    router.register(r'social_media', ej.front_config.api_views.SocialMediaViewSet)
    router.register(r'color_pallet', ej.front_config.api_views.ColorPalletViewSet)
