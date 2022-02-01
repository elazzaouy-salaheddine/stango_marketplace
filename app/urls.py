from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("users/", include('user.urls')),
    path("products/", include('product.urls')),
    path("api/comments/", include('comment.urls')),
    path("api/categores/", include('category.urls')),

    path('', include('home.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
