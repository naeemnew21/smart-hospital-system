from django.urls import path
from . import views

app_name = 'user'


urlpatterns = [
    path('', views.index, name = 'index'),
    path('fork/', views.fork, name = 'fork'),
    path('deluser/', views.del_user, name = 'deluser'),
    
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    
    path('signup/', views.Registeration.as_view(), name = 'signup'),
    
    
    path('login_api', views.login_api, name = 'login_api'),
    
]

