from django.contrib import admin

from ads import models as ad_mod

class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'preority')

admin.site.register(ad_mod.AdModel, AdAdmin)
