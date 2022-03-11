from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, UserProfile, UserVital

        
class CustomUserAdmin(UserAdmin):
    model = MyUser
    list_display = [ 'national_id', 'phone', 'is_active', 'is_staff']
    list_display_links = ['national_id', 'phone']
    
    search_fields = ('national_id','phone',)
    readonly_fields=('username','date_joined', 'last_login')
     
    fieldsets = (
        (None, 
            {'fields': ('first_name', 'last_name','username', 'email', 'password', 'phone', 'national_id')}
        ),
        ('Permissions',
            {'fields': ('is_active', 'is_staff', 'groups')}
         ),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = ( (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'phone', 'national_id', 'is_staff')}
        ),
                     )
    

   
class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    readonly_fields=('user', 'birth_date', 'sex')
    
class UserVitalAdmin(admin.ModelAdmin):
    model = UserVital
    readonly_fields=('user',)   

    
admin.site.register(MyUser, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserVital, UserVitalAdmin)
