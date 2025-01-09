from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from user.models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
	fieldsets = (
		(None, {"fields": ("email", "password")}),
		("Personal info", {"fields": ("first_name", "last_name")}),
		(
			"Permissions",
			{"fields": ("is_active", "is_staff", "is_superuser", "user_permissions")},
		),
	)
	add_fieldsets = (
		(
			None,
			{
				"classes": ("wide",),
				"fields": (
					"email",
					"password1",
					"password2",
					"is_staff",
					"is_superuser",
				),
			},
		),
	)
	list_display = ("email", "first_name", "last_name", "is_staff", "is_superuser")
	search_fields = ("email", "first_name", "last_name")
	ordering = ("email",)
