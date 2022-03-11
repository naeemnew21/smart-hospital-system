"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls', namespace = 'user')),
    path('patient/', include('xpatient.urls', namespace = 'patient')),
    path('hr/', include('xstaff_hr.urls', namespace = 'hr')),
    path('secretary/', include('xstaff_secretary.urls', namespace = 'secretary')),
    path('dr/', include('xstaff_doctor.urls', namespace = 'doctor')),
    
    
    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name="patient/settings.html"),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name="patient/changed_done.html"),
         name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), 
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="user/password_reset_confirm.html"), 
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), 
         name='password_reset_complete'),      

    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



handler404 = 'user.views.handle_404'  #page_not_found
handler500 = 'user.views.handle_500'  #internal_server_error
handler403 = 'user.views.handle_403'  #permission_denied