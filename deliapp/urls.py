from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('backtodash', views.backtodashboard, name='index'),
    path('login', views.user_login, name='login'),
    path('signup', views.user_signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
    path('accounts/login/', views.user_login, name='login'),
    path('accounts/login/login', views.user_login, name='login'),
    path('accounts/login/signup/', views.user_signup, name='signup'),
    path('accounts/login/signup/login', views.user_logout, name='login'),
    path('accounts/login/signup/signup', views.user_logout, name='signup'),
    path('trackorder', views.trackorder, name='track'),
    path('createdelivery', views.createdelivery, name='createdelivery'),
    path('mapinte', views.mapinte, name='mapinte'),
path('delivery/<int:delivery_id>/', views.view_delivery, name='delivery_detail'),
    path('createdelivery/', views.create_delivery, name='create_delivery'),
        path('updatedelivery/<int:delivery_id>/', views.updatedelivery, name='update_delivery'),
        path('blockchainauth', views.blockchainauth, name='blockchainauth'),
        path('carbon_emission', views.carbon_emission, name='carbon_emission'),
        path('trackorder/', views.fetch_deliveries, name='track_order'),
        path('delivery/trackorder', views.fetch_deliveries, name='delivery_trackorder'),
        path('delivery/carbon_emission', views.carbon_emission, name='carbon_emission'),
        

]

