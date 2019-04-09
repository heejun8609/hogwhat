from django.contrib import admin
from .models import ThisMonthDisease, AtTimesLikeThis

@admin.register(ThisMonthDisease)
class ThisMonthDiseaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'symptoms', 'treatments']
    search_fields = ['name']


@admin.register(AtTimesLikeThis)
class AtTimesLikeThisAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'reference']
    search_fields = ['question']
    list_filter = ['reference']