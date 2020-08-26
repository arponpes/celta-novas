from django.contrib import admin
from core.models import Business, CommunityManager

class BusinessAdmin(admin.ModelAdmin):
    list_display = (
        'business_name',
        'business_email',
        'business_address'
    )


class CommunityManagerAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'phone_number'
    )

admin.site.register(Business, BusinessAdmin)
admin.site.register(CommunityManager, CommunityManagerAdmin)