from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['email','username', 'gender',]
	fieldsets = (

		(None,{'fields':('email','password','username','gender',)}),
		('Permissions',{'fields':('is_staff','is_active')}),
		)

	add_fieldsets = (

		(None,{
			'classes':('wide',),
			'fields':('email','username','password1','password2','is_staff','is_active')
			}),

		)
admin.site.register(CustomUser,CustomUserAdmin)
		

# Register your models here.
