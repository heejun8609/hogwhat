from django.contrib import admin
from .models import Disease, Symptom, SymptomDisease, SymptomUpload


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ['ad_name', 'ad_category', 'ad_definition', 'ad_treatment']
    search_fields = ['ad_name']
    list_filter = ['ad_category']


@admin.register(Symptom)
class SymptomAdmin(admin.ModelAdmin):
    list_display = ['ds_id', 'ds_name']
    search_fields = ['ds_name']
    list_filter = ['ds_name']


@admin.register(SymptomDisease)
class SymptomDiseaseAdmin(admin.ModelAdmin):
    list_display = ['ds_id', 'ad_name']
    search_fields = ['ad_name']
    list_filter = ['ds_id']


@admin.register(SymptomUpload)
class SymptomUploadAdmin(admin.ModelAdmin):
    list_display = ['user', 'ds_id', 'ip', 'ds_photo', 'ds_description', 'ds_created_at']
    search_fields = ['ds_id']




