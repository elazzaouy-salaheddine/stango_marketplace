from django import urls
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings 
from django.conf.urls.static import static
from .views import CartTemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("users/", include('user.urls')),
    path("products/", include('product.urls')),
    path("comments/", include('comment.urls')),
    path("api/categores/", include('category.urls')),
    path("order/", include('order.urls'), name="order"),
    path("categories/", include('category.urls'), name="categorie"),

    path('', include('home.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('carttemplate/', CartTemplate, name='cart_template'),

    
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "app.views.page_not_found_view"
