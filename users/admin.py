from django.contrib import admin
from django.contrib.auth.admin import UserCreationForm,UserChangeForm

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['email','username', 'gender','is_staff',]
	fieldsets = (

		(none,{'fields':('email','password','gender',)}),
		('Permissions',{'fields':('is_staff','is_active')}),
		)

	add_fieldsets = (

		(None,{
			'classes':('wide',),
			'fields':('email','password1','password2','is_staff','is_active')
			})

		)
admin.site.register(CustomUser,CustomUserAdmin)
		

# Register your models here.
