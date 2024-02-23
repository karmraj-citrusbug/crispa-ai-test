from django.urls import include, path
from .views import hello_world
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, CurrencyViewSet, JournalEntryLinesViewSet

router = DefaultRouter()
router.register("account", AccountViewSet, basename="account")
router.register("currency", CurrencyViewSet, basename="currency")
router.register(
    "journal-entry-lines", JournalEntryLinesViewSet, basename="journal_entry_lines"
)

urlpatterns = [
    path("hello/", hello_world, name="hello-world"),
    path("", include(router.urls)),
]
