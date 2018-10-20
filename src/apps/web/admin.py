from django.contrib import admin
from maincore.models import App, Model, Field, Setting


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    pass

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    pass

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    pass

