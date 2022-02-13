from django.urls import path
from django.contrib.auth import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import  (ProfileView, RegisterUser, UserList, UserDetail, StoreView, 
                     SotreDetail, BecomeVendor, AccountSetting, 
                     StoreProducts,StoreProductCreate,StoreProductUpdate,StoreProductDelete, StoreOrders, SotreOrdersDetail)
urlpatterns = [
    path('api/', UserList.as_view()),
    path('api/<int:pk>/', UserDetail.as_view()),
    # register
    # email verification
    # email verfivation token
    # profile user 
    # update user
    # update profile user
    
    #path('profile/', AccountSetting.as_view(), name='profile'),
    path('', StoreView, name='store_list'),
    path('<int:pk>/', SotreDetail, name='store_detail'),
    path('becomevendor/', BecomeVendor, name='become_vendor'),
    
    
    path('login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('register/', RegisterUser, name='register_page'),
    path('account_setting/', AccountSetting, name='account_setting'),
    
    path("products/", StoreProducts, name="store_products"),
    path("products/create-product/", StoreProductCreate, name="store_product_create"),
    path("products/<int:pk>/update-product/", StoreProductUpdate, name="store_product_update"),
    path("products/<int:pk>/delete-product/", StoreProductDelete, name="store_product_delete"),
    
    path("orders/", StoreOrders, name="store_orders"),
    path('orders/<int:pk>/', SotreOrdersDetail, name='store_order_detail'),

    
]

urlpatterns = format_suffix_patterns(urlpatterns)
