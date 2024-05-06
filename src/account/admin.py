from django.contrib import admin

from account import models as acc_mod
from profiles import models as prof_mod


class ProfileInline(admin.StackedInline):
    model = prof_mod.Profile  
    extra = 2

@admin.register(acc_mod.EsUser) 
class NameAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]
    readonly_fields = ['promocode', ]    