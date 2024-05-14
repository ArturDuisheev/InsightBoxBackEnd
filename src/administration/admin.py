from django.contrib import admin

from administration.models import PaymentModel as pay_mod


class AdministrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_amount', 'status')
    readonly_fields = ('created_at',)

admin.site.register(pay_mod.Payment, AdministrationAdmin)

class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'id')

admin.site.register(pay_mod.Package, PackageAdmin)
