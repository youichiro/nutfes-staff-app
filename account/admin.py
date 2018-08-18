from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('student_id', 'name', 'grade', 'department', 'phone_number')


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('student_id', 'password')}),
        ('Personal info', {'fields': ('name', 'grade', 'department', 'phone_number')}),
        ('Permissions', {'fields': ('is_superuser', )}),
        ('Important dates', {'fields': ('last_login', )}),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('student_id', 'name', 'grade', 'phone_number')
    list_filter = ('is_superuser', )
    search_fields = ('student_id', 'name', 'grade', 'department')
    ordering = ('department', )


admin.site.register(User, MyUserAdmin)
