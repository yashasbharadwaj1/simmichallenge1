from django.urls import path
from .import views
app_name='contact'
urlpatterns=[
   path('',views.home,name='home'),
   path('contact/',views.contact)
]