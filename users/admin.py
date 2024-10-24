from django.contrib import admin
from .models import CustomUser, UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 1


class CustomUserAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline]


admin.site.register(CustomUser, CustomUserAdmin)
