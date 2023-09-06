from django.urls import path
from apps.products.views import ProductAPIView
# from django.conf import settings
# from django.conf.urls.static import static
#
#
urlpatterns = [
    path('', ProductAPIView.as_view(), name='product-list')
]

#
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)