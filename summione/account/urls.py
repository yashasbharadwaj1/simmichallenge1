from django.urls import path ,include
from . import views
from django.contrib.auth import views as auth_views

app_name='account'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="account/login.html",
                                               ), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='account/logged_out.html'),name="logout"),

   
    path('profile/', views.profile, name='profile'),
   
]
