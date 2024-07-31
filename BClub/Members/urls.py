from django.urls import path
from . import views

app_name = 'Members'

urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('member_conf/', views.member_config, name="config"),
    
]