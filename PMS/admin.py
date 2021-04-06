from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from PMS.models import Member

# Register your models here.


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'national_id_number',
                  'phone_number', 'district', 'date_of_birth', 'id_number')

    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'national_id_number', 'phone_number',
                  'district', 'date_of_birth', 'id_number')

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('first_name', 'last_name',
                    'national_id_number', 'phone_number', 'district')
    list_filter = ('is_admin', 'district',)
    fieldsets = (
        (None, {'fields': ('national_id_number', 'password')}),
        ('Personal Info', {'fields': (
            'date_of_birth', 'first_name', 'last_name', 'phone_number', 'district')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'national_id_number', 'email', 'date_of_birth', 'password1', 'password2')
        })
    )

    search_fields = ('national_id_number', 'phone_number',
                     'first_name', 'last_name')
    ordering = ('national_id_number')
    filter_horizontal = ()

    admin.site.register(Member)
    # admin.site.register(UserAdmin)
    admin.site.unregister(Group)
