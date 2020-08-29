from django.contrib import admin
from .models import Player

class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'position'
    )

admin.site.register(Player, PlayerAdmin)
