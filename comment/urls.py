from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CommentList, CommentDetail, ProductReviewsForm

urlpatterns = [
    # code omitted for brevity
    path('', ProductReviewsForm),
    path('<int:pk>/', CommentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
