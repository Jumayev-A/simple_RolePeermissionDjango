from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    
    path('',views.home, name='home'),
    
]