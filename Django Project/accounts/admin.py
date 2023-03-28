from django.contrib import admin


from accounts.models import Realtor,CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    autocomplete_fields = ('groups',)
    search_fields = ('email', 'first_name', 'last_name')
    list_display_links = ('email',)
    readonly_fields = ['last_login', 'date_joined']
    list_display = ('get_full_name', 'email', 'phone', 'is_staff',
                    'is_superuser', 'is_active', 'get_groups', 'last_login')



@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    autocomplete_fields = ('user',)
    list_display = ('user', 'email', 'phone', 'description',
                    'is_mvp')
    list_display_links = ('user',)
    search_fields = ('user__first_name', 'user__last_name', 'email')


