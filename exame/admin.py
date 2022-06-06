from django.contrib import admin

from .models import Exame

@admin.register(Exame)
class ExameAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Jejum', 'Material', 'Prazo', 'Ativo')
