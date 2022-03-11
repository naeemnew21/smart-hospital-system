from django.urls import path
from . import views

app_name = 'hr'


urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('users/', views.UsersView.as_view(), name = 'all_users'),
    path('users/<int:pk>', views.UserUpdateView.as_view(), name = 'update_user'),
    path('jobs/<int:pk>', views.JobUpdateView.as_view(), name = 'update_jop'),
    path('drs/<int:pk>', views.DrUpdateView.as_view(), name = 'update_dr'),
    path('day/<int:pk>', views.AddDelDay.as_view(), name = 'add_del_day'),
    path('sec/<int:pk>', views.SecretaryUpdateView.as_view(), name = 'update_secretary'),
    
]

