from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username','first_name','last_name','mobile','is_staff')
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('mobile',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('mobile',)}),
)

admin.site.register(CustomUser, CustomUserAdmin)