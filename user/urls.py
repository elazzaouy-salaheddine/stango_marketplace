from django.urls import path
from django.contrib.auth import views
from django.contrib.auth.views import PasswordResetView
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (PaidOrders, ShippedOrders, OrderUpdate,
                    RegisterUser, UserList, UserDetail, StoreView,
                    invite_profiles_list_view, remove_from_friends, send_invitations,
                    reject_invatation, accept_invatation, mysippersProfileListView, ShipperProfileView,
                    sippersProfileListView, ProfileViews, invites_received_view,
                    SotreDetail, BecomeVendor, AccountSetting, load_sub_categoires,
                    StoreProducts, StoreProductCreate, StoreProductUpdate, StoreProductDelete,
                    StoreOrders, SotreOrdersDetail)
urlpatterns = [
    path('api/', UserList.as_view()),
    path('api/<int:pk>/', UserDetail.as_view()),
    # email verification
    # email verfivation token
    path('profile/', ProfileViews, name='profile'),
    path('myshippers/', mysippersProfileListView.as_view(), name='myshippers'),
    path('my-invites/', invites_received_view, name='my_invites_received_view'),
    path('all-profiles/', sippersProfileListView.as_view(),
         name='profilesListViews'),
    path('to-invite-profiles/', invite_profiles_list_view,
         name='invite-profile-list-view'),
    path('invite-send/', send_invitations, name='send-invitations-view'),
    path('invite-delete/', remove_from_friends, name='delete-invitations-view'),

    path('reject-invatation/', reject_invatation, name='reject-invatation-view'),
    path('accept-invatation/', accept_invatation, name='accept-invatation-view'),
    path('<int:pk>/', ShipperProfileView, name='shipper_profile_detail'),


    path('', StoreView, name='store_list'),
    path('<str:store_name>/', SotreDetail, name='store_detail'),
    path('becomevendor/$/', BecomeVendor, name='become_vendor'),


    path('login/$/', views.LoginView.as_view(template_name='registratio/login.html'), name='login'),
    path('logout/$/', views.LogoutView.as_view(), name='logout'),

    path('password_change/$/', views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/$/', views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    path('password_reset/$/', PasswordResetView.as_view(
        template_name='registratio/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/$/', views.PasswordResetDoneView.as_view(
        template_name='registratio/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/$/', views.PasswordResetConfirmView.as_view(
        template_name='registratio/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/$/', views.PasswordResetCompleteView.as_view(
        template_name='registratio/password_reset_complete.html'), name='password_reset_complete'),

    path('register/$/', RegisterUser, name='register_page'),
    path('account_setting/$/', AccountSetting, name='account_setting'),

    path("products/$/", StoreProducts, name="store_products"),
    path("products/create-product/$/",
         StoreProductCreate, name="store_product_create"),
    path('ajax/load-subcate/', load_sub_categoires,
         name='load_sub_categoires'),  # AJAX
    path("products/<int:pk>/update-product/$/",
         StoreProductUpdate, name="store_product_update"),
    path("products/<int:pk>/delete-product/",
         StoreProductDelete, name="store_product_delete"),

    path("orders/$/", StoreOrders, name="store_orders"),
    path("paid-order/$/", PaidOrders, name="paid_orders"),
    path("shipped-order/$/", ShippedOrders, name="shipped_orders"),
    path('orders/<int:pk>/$/', SotreOrdersDetail, name='store_order_detail'),
    path("orders/<int:pk>/update-order/$/",
         OrderUpdate, name="store_order_update"),



]

urlpatterns = format_suffix_patterns(urlpatterns)
