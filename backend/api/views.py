from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Account, Currency, JournalEntryLines, JOURNAL_ENTRY_LINES_CHOICES
from .serializers import (
    AccountSerializer,
    CurrencySerializer,
    JournalEntryLinesCUDSerializer,
    JournalEntryLinesListSerializer,
)


def hello_world(request):
    return JsonResponse({"message": "Hello World"})


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class JournalEntryLinesViewSet(viewsets.ModelViewSet):
    queryset = JournalEntryLines.objects.all()
    serializer_class = JournalEntryLinesCUDSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = JournalEntryLinesListSerializer
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        # Check if the entry is booked
        if instance.accounting_type == JOURNAL_ENTRY_LINES_CHOICES.BOOKED:
            return Response(
                {"error": "Booked entries cannot be updated."},
                status=status.HTTP_403_FORBIDDEN,
            )

        return super().update(request, args, *kwargs)