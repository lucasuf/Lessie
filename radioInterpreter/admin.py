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
    # TODO: Exibir os nomes das keys na hora de cadastrar
    # TODO: Exibir os nomes dos themes na hora de cadastrar
    list_display = ['get_name']
    fields = ['theme', 'keys']

    def get_name(self, obj):
        return obj.theme.name_theme

    get_name.admin_order_field = 'theme'  # Allows column order sorting
    get_name.short_description = 'Theme Name'  # Renames column head


admin.site.register(Theme, ThemeDetailAdmin)
admin.site.register(Key, KeyDetailAdmin)
admin.site.register(RadioKey, RadioKeyDetailAdmin)
