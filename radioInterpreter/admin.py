from django.contrib import admin
from .models import Theme, Key, RadioKey


# Register your models here.
class ThemeDetailAdmin(admin.ModelAdmin):
    list_display = ['name_theme', 'os']


class KeyDetailAdmin(admin.ModelAdmin):
    list_display = ['name_key']


class RadioKeyDetailAdmin(admin.ModelAdmin):
    model = Theme
    # TODO: Preciso exibir todas as keys em uma outra coluna
    list_display = ['get_name', 'get_name_os']
    fields = ['theme', 'keys']

    def get_name(self, obj):
        return obj.theme.name_theme

    def get_name_os(self, obj):
        return obj.theme.os

    get_name.admin_order_field = 'theme'  # Allows column order sorting
    get_name.short_description = 'Theme Name'  # Renames column head


admin.site.register(Theme, ThemeDetailAdmin)
admin.site.register(Key, KeyDetailAdmin)
admin.site.register(RadioKey, RadioKeyDetailAdmin)
