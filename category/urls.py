from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CategoryList, CategoryDetail, BarndList

urlpatterns = [
    # code omitted for brevity
    path('', CategoryList.as_view()),
    path('<int:pk>/', CategoryDetail.as_view()),
    path('brands/', BarndList.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
