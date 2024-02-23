from django.contrib import admin
from api.models import Account, Currency, JournalEntryLines


class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "uid",
        "number",
        "name",
        "default_accounting_type",
        "created_at",
        "updated_at",
    )


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("uid", "code", "name", "created_at", "updated_at")


class JournalEntryLinesAdmin(admin.ModelAdmin):
    list_display = (
        "uid",
        "account",
        "accounting_date",
        "state",
        "description",
        "reconciled",
        "currency",
        "amount",
        "accounting_type",
        "created_at",
        "updated_at",
    )


admin.site.register(Account, AccountAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(JournalEntryLines, JournalEntryLinesAdmin)
