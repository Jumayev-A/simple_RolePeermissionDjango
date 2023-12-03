from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Group urls
    path('',views.group, name='group'),
    path('group_add/', views.group_add, name='group_add'),
    path('group_update/<uuid:id>/', views.group_update, name='group_update'),

    # Users urls
    path('users/', views.users, name='users'),
    path('users_add/', views.users_add, name='users_add'),
    
]