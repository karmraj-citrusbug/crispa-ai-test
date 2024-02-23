from rest_framework import serializers
from .models import Account, Currency, JournalEntryLines


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"

    
class AccountCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["number", "name", "default_accounting_type"]


class CurrencyCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["code"]


class JournalEntryLinesSerializer(serializers.ModelSerializer):
    account = AccountCustomSerializer()
    currency = CurrencyCustomSerializer()

    class Meta:
        model = JournalEntryLines
        fields = ["uid", "description", "accounting_date", "account", "currency","amount", "state", "accounting_type", "reconciled"]
