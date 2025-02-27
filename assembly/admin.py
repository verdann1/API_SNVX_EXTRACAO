from django.contrib import admin
from assembly.models import Assembly


@admin.register(Assembly)
class AssemblyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
