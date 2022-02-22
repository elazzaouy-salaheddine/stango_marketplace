from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CategoryList, CategoryDetail, BarndList, index, category_details
urlpatterns = [
    # code omitted for brevity
    path('api/', CategoryList.as_view()),
    path('api/<int:pk>/', CategoryDetail.as_view()),
    path('api/brands/', BarndList.as_view()),
    path('', index, name='categories'),
    path('<slug:slug>/', category_details, name='category_details'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
