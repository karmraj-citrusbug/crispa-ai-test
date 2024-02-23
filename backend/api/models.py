import uuid
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ACCOUNTING_TYPE_CHOICES(models.TextChoices):
    DEBIT = "debit", "Debit"
    CREDIT = "credit", "Credit"


class JOURNAL_ENTRY_LINES_CHOICES(models.TextChoices):
    DRAFT = "draft", "Draft"
    BOOKED = "booked", "Booked"


class Account(BaseModel):
    number = models.CharField(max_length=4)
    name = models.CharField(max_length=10)
    default_accounting_type = models.CharField(
        max_length=10,
        choices=ACCOUNTING_TYPE_CHOICES.choices,
        default=ACCOUNTING_TYPE_CHOICES.DEBIT,
    )


class Currency(BaseModel):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=10)


class JournalEntryLines(BaseModel):

    accounting_date = models.DateField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    state = models.CharField(
        max_length=10,
        choices=ACCOUNTING_TYPE_CHOICES.choices,
        default=ACCOUNTING_TYPE_CHOICES.DEBIT,
    )
    description = models.TextField()
    reconciled = models.BooleanField(default=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    accounting_type = models.CharField(
        max_length=10,
        choices=JOURNAL_ENTRY_LINES_CHOICES.choices,
        default=JOURNAL_ENTRY_LINES_CHOICES.DRAFT,
    )
