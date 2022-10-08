from django.contrib import admin
from api import models

# Register your models here.

@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id','name','summary','created_at']


@admin.register(models.Advocates)
class AdvocateAdmin(admin.ModelAdmin):
    list_display = ['id','name','short_bio','advocate_years_exp','company']

@admin.register(models.SocialLink)
class SocialLink(admin.ModelAdmin):
    list_display = ['id','advocate_id','platform_name','link']