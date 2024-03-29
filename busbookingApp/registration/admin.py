from django.contrib import admin
<<<<<<< HEAD
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    
    list_display = ['id', 'email','name','is_active','is_admin','phone','otp']

    list_filter =('is_admin',)

    ordering = ['id','email']

    fieldsets = (
         (('User Credential'), {'fields': ('email', 'password')}),
         (('personal Info'), {'fields': ('name',)}),
         (('permissions'), {'fields': ('is_admin',)}),
         )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','name', 'password', 'password2'),
        }),
    )

    filter_horizontal = ()

admin.site.register(User, UserModelAdmin)
=======
# from .models import User
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# # Register your models here.

# class UserModelAdmin(BaseUserAdmin):
    
#     list_display = ['id', 'email','name','is_active','is_admin','phone','otp']

#     list_filter =('is_admin',)

#     ordering = ['id','email']

#     fieldsets = (
#          (('User Credential'), {'fields': ('email', 'password')}),
#          (('personal Info'), {'fields': ('name',)}),
#          (('permissions'), {'fields': ('is_admin',)}),
#          )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email','name', 'password1', 'password2'),
#         }),
#     )

#     filter_horizontal = ()

# admin.site.register(User, UserModelAdmin)
>>>>>>> 6e77fe80d5e4e6de116c3b49e9266fea373e1ce4
