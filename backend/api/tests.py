from django.test import TestCase

# Create your tests here.
import random
from faker import Faker
from rest_framework import status
from rest_framework.test import (APITestCase)
from api.views import AccountViewSet
from rest_framework.test import APIClient
from .models import Account, Currency, JournalEntryLines, ACCOUNTING_TYPE_CHOICES, JOURNAL_ENTRY_LINES_CHOICES
from .views import AccountViewSet
fake = Faker()


class AccountTestCases(APITestCase):
    """
    Testcases class for all account related APIs
    """

    def setUp(self):
        self.account_model = Account
        self.client = APIClient()
        self.account_type_class = ACCOUNTING_TYPE_CHOICES
        self.account_type = random.choice(
            [choice for choice in self.account_type_class]
        )
        self.number = str(random.randint(1000, 9999))
        self.account_data = {
            "number": self.number,
            "name": "Sehwag ",
            "default_accounting_type": self.account_type
        }
        self.account = Account.objects.create(
            **self.account_data
        )

    def test_listing_of_all_accounts(self):
        """
        Testcase method to list all the accounts.
        """
        response = self.client.get("/api/account/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),
                         self.account_model.objects.count())

    def test_add_account(self):
        """
        Testcase method to add account data by passing data as json and returns account object.
        """
        account_number = self.number
        account_type = self.account_type
        account_data = {
            "number": account_number,
            "name": "Ponting",
            "default_accounting_type": account_type
        }
        response = self.client.post("/api/account/", account_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_account_with_negative_account_number(self):
        """
        Negative Testcase method to add account data by passing wrong account number as json and returns 400 BAD REQUEST response.
        """
        account_number = self.number + str(random.randint(0, 1))
        account_type = self.account_type
        account_data = {
            "number": account_number,
            "name": "Ponting",
            "default_accounting_type": account_type
        }
        response = self.client.post("/api/account/", account_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_account_with_wrong_account_type(self):
        """
        Negative Testcase method to add account data by passing wrong account type as input data as json and returns 400 BAD REQUEST.
        """
        account_number = self.number
        account_data = {
            "number": account_number,
            "name": "Ponting",
            "default_accounting_type": "c"
        }
        response = self.client.post("/api/account/", account_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_account_detail(self):
        """
        Testcase method to retrieve account detail by passing account number as uuid parameter and returns account object.
        """
        response = self.client.get(f"/api/account/{self.account.uid}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_negative_retrieve_account_by_passing_wrong_uid(self):
        """
        Testcase method to retrieve account detail by passing wrong uuid as string and returns 400_BAD_REQUEST.
        """
        response = self.client.get(
            f"/api/account/68ba5f79-b5cd-4fe0-883e-3480957e7586/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_account_details(self):
        """
        Testcase method to update account details by passing account number as uuid parameter and returns account object.
        """
        account_data = {
            "number": self.number,
            "name": "MsDhoni",
            "default_accounting_type": self.account_type
        }
        response = self.client.put(
            f"/api/account/{self.account.uid}/", account_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_negative_update_account_details_by_passing_wrong_account_number(self):
        """
        Testcase method to update account details by passing wring account number as parameter and returns 400 BAD REQUEST response.
        """
        account_data = {
            "number": self.number + str(random.randint(0, 1)),
            "name": "MsDhoni",
            "default_accounting_type": self.account_type
        }
        response = self.client.put(
            f"/api/account/{self.account.uid}/", account_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_update_account_details_by_passing_wrong_account_name(self):
        """
        Testcase method to update account details by passing wring account name as sting parameter and returns 400 BAD REQUEST.
        """
        account_data = {
            "number": self.number,
            "name": "Sachin Tendulkar",
            "default_accounting_type": self.account_type
        }
        response = self.client.put(
            f"/api/account/{self.account.uid}/", account_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_update_account_details_by_passing_wrong_account_type(self):
        """
        Testcase method to update account details by passing wrong account type as string parameter and returns 400 BAD REQUEST.
        """
        account_data = {
            "number": self.number,
            "name": "MsDhoni",
            "default_accounting_type": "c"
        }
        response = self.client.put(
            f"/api/account/{self.account.uid}/", account_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_account(self):
        """
        Testcase method to delete account by passing uuid parameter and returns 204 NO CONTENT response.
        """
        response = self.client.delete(f"/api/account/{self.account.uid}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_negative_delete_account_by_passing_wrong_uid(self):
        """
        Testcase method to delete account by passing wrong uuid parameter and returns 204 NO CONTENT response.
        """
        response = self.client.delete(
            f"/api/account/fb275f7f-df8d-4d51-b533-a9f2510bf4a6/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_partial_update_account_details(self):
        """
        Testcase method to partial update account details by passing uuid parameter and returns account object.
        """
        account_data = {
            "number": "Sachin"
        }
        response = self.client.patch(
            f"/api/account/{self.account.uid}/", account_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_account_details_by_updating_account_number(self):
        """
        Testcase method to partial update account details by passing uuid parameter and returns account object.
        """
        account_data = {
            "number": self.number
        }
        response = self.client.patch(
            f"/api/account/{self.account.uid}/", account_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_account_details_by_updating_account_type(self):
        """
        Testcase method to partial update account details by passing uuid parameter and returns account object.
        """
        account_data = {
            "default_accounting_type": self.account_type
        }
        response = self.client.patch(
            f"/api/account/{self.account.uid}/", account_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_negative_partial_update_account_details_by_negative_account_name(self):
        """
        Testcase method to partial update account details by passing wrong account name and returns 400 BAD REQUEST.
        """
        account_data = {
            "name": "Sachin Tendulkar"
        }
        response = self.client.patch(
            f"/api/account/{self.account.uid}/", account_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_partial_update_account_details_by_negative_account_number(self):
        """
        Testcase method to partial update account details by passing wrong account name and returns 400 BAD REQUEST.
        """
        account_data = {
            "number": self.number + str(random.randint(0, 1))
        }
        response = self.client.patch(
            f"/api/account/{self.account.uid}/", account_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_partial_update_account_details_by_negative_account_type(self):
        """
        Testcase method to partial update account details by passing wrong account name and returns 400 BAD REQUEST.
        """
        account_data = {
            "default_accounting_type": "c"
        }
        response = self.client.patch(
            f"/api/account/{self.account.uid}/", account_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CurrencyTestCases(TestCase):
    """
    Testcase class for Currency model.
    """

    def setUp(self):
        """
        setup method to create all required fields whenever any testcase runs.
        """
        self.client = APIClient()
        self.currency_model = Currency
        self.currency = Currency.objects.create(
            code="INR",
            name="Indian Rupee",
        )

    # List of currency model testcases.
    def test_list_of_currency_objects(self):
        """
        Testcase method to list all currency objects and returns 200 OK response.
        """
        response = self.client.get("/api/currency/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),
                         self.currency_model.objects.count())

    # Positive Create Currency model testcases.

    def test_add_currency_object(self):
        """
        Testcase method to add currency object and returns 201 CREATED response.
        """
        currency_code = "USD"
        currency_name = "US Dollar"
        currency_data = {
            "code": currency_code,
            "name": currency_name
        }
        response = self.client.post("/api/currency/", currency_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Negative Add Currency model testcases.

    def test_negative_add_currency_object_by_wrong_currency_code(self):
        """
        Testcase method to add currency object by passing wrong currency code and returns 400 BAD REQUEST response.
        """
        currency_code = "INDIA"
        currency_name = "US Dollar"
        currency_data = {
            "code": currency_code,
            "name": currency_name
        }
        response = self.client.post("/api/currency/", currency_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_add_currency_object_by_wrong_currency_code(self):
        """
        Testcase method to add currency object by passing currency name with more than 10 chars and returns 400 BAD REQUEST response.
        """
        currency_code = "INDIA"
        currency_name = "Indonesia Currency"
        currency_data = {
            "code": currency_code,
            "name": currency_name
        }
        response = self.client.post("/api/currency/", currency_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Positive Retrieve Currency model testcases.

    def test_retrieve_currency_object(self):
        """
        Testcase method to retrieve currency object and returns 200 OK response.
        """
        response = self.client.get(f"/api/currency/{self.currency.uid}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Negative Retrieve Currency model testcases.

    def test_negative_retrieve_currency_object_by_passing_wrong_uid(self):
        """
        Testcase method to retrieve currency object and returns 400 NOT FOUND response.
        """
        response = self.client.get(
            f"/api/currency/7f405313-e214-483b-9c58-eea8015b0093/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Positive Update Currency model testcases.

    def test_update_currency_object(self):
        """
        Testcase method to update currency object and returns 200 OK response.
        """
        currency_code = "USD"
        currency_name = "US Dollar"
        currency_data = {
            "code": currency_code,
            "name": currency_name
        }
        response = self.client.put(
            f"/api/currency/{self.currency.uid}/", currency_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Negative Update Currency model testcases.

    def test_negative_update_currency_object_by_passing_wrong_code(self):
        """
        Testcase method to update currency object and returns 400 BAD REQUEST response.
        """
        currency_code = "INDIA"
        currency_name = "US Dollar"
        currency_data = {
            "code": currency_code,
            "name": currency_name
        }
        response = self.client.put(
            f"/api/currency/{self.currency.uid}/", currency_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_update_currency_object_by_passing_wrong_name(self):
        """
        Testcase method to update currency object by passing currency name with more than 10 chars and returns 400 BAD REQUEST response.
        """
        currency_code = "INDIA"
        currency_name = "Indonesia Currency"
        currency_data = {
            "code": currency_code,
            "name": currency_name
        }
        response = self.client.put(
            f"/api/currency/{self.currency.uid}/", currency_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_update_currency_object_by_passing_wrong_uuid(self):
        """
        Testcase method to update currency object by passing wrong uuid and returns 400 NOT FOUND response.
        """
        currency_code = "IND"
        currency_name = "INDIA"
        currency_data = {
            "code": currency_code,
            "name": currency_name
        }
        response = self.client.put(
            f"/api/currency/49bc6aa4-4805-4c09-9f39-00b2d09dd3b1/", currency_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Positive Testcases for partial update currency objects.

    def test_partial_update_currency(self):
        """
        Testcase method to partial update currency object and returns 200 OK response.
        """
        currency_name = "US Dollar"
        currency_data = {
            "name": currency_name
        }
        response = self.client.patch(
            f"/api/currency/{self.currency.uid}/", currency_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_currency_by_passing_currency_code(self):
        """
        Testcase method to partial update currency object by passing currency code and returns 200 OK response.
        """
        currency_code = "USD"
        currency_data = {
            "code": currency_code
        }
        response = self.client.patch(
            f"/api/currency/{self.currency.uid}/", currency_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Negative Testcases for partial update currency objects.

    def test_negative_partial_update_currency_by_passing_wrong_currency_code(self):
        """
        Testcase method to partial update currency object by passing currency code with more than 3 chars and returns 400 BAD REQUEST response.
        """
        currency_code = "US Dollar"
        currency_data = {
            "code": currency_code
        }
        response = self.client.patch(
            f"/api/currency/{self.currency.uid}/", currency_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_partial_update_currency_by_passing_wrong_currency_name(self):
        """
        Testcase method to partial update currency object by passing currency name with more than 3 chars and returns 200 OK response.
        """
        currency_name = "Indonesia Currency"
        currency_data = {
            "name": currency_name
        }
        response = self.client.patch(
            f"/api/currency/{self.currency.uid}/", currency_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_partial_update_currency_by_passing_wring_uid(self):
        """
        Testcase method to partial update currency object by passing wrong uuid and returns 400 NOT FOUND response.
        """
        currency_name = "Indonesia Currency"
        currency_data = {
            "name": currency_name
        }
        response = self.client.patch(
            f"/api/currency/49bc6aa4-4805-4c09-9f39-00b2d09dd3b1/", currency_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Positive testcases for delete currency object

    def test_delete_currency(self):
        """
        Testcase method to delete currency object and returns 204 NO CONTENT response.
        """
        response = self.client.delete(f"/api/currency/{self.currency.uid}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Negative testcases for delete currency object

    def test_negative_delete_currency_by_passing_wrong_uid(self):
        """
        Testcase method to delete currency object and returns 404 NOT FOUND response.
        """
        response = self.client.delete(
            f"/api/currency/6f19fb60-59ab-4979-9a43-f17f3dc21429/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class JournalEntryLinesTestCases(TestCase):
    """
    Testcase class for Journal Entry Lines.
    """

    def setUp(self):
        self.client = APIClient()
        self.accounting_date = fake.date_this_year(
            before_today=True, after_today=True).strftime('%Y-%m-%d')
        self.account_type_class = ACCOUNTING_TYPE_CHOICES
        self.account_type = random.choice(
            [choice for choice in self.account_type_class]
        )
        self.number = str(random.randint(1000, 9999))
        self.account_data = {
            "number": self.number,
            "name": "Sehwag ",
            "default_accounting_type": self.account_type
        }
        self.account = Account.objects.create(
            **self.account_data
        )
        self.currency_code = "USD"
        self.currency_name = "US Dollar"
        self.currency_data = {
            "code": self.currency_code,
            "name": self.currency_name
        }
        self.currency = Currency.objects.create(
            **self.currency_data
        )

        self.reclined = fake.boolean()
        self.amount = random.uniform(100, 500)
        self.state = random.choice(
            [choice for choice in self.account_type_class]
        )
        self.description = fake.text()
        self.journal_entry_accounting_type_choices = JOURNAL_ENTRY_LINES_CHOICES
        self.journal_entry_accounting_type = random.choice(
            [choice for choice in self.journal_entry_accounting_type_choices])
        self.journal_entry_data = {
            "accounting_date": self.accounting_date,
            "account": self.account,
            "state": self.state,
            "description": self.description,
            "reconciled": self.reclined,
            "currency": self.currency,
            "amount": self.amount,
            "accounting_type": JOURNAL_ENTRY_LINES_CHOICES.DRAFT
        }
        self.journal_entry = JournalEntryLines.objects.create(
            **self.journal_entry_data)

    # Positive test case for list of journal entries

    def test_list_of_journal_entries(self):
        """
        Testcase method to list all journal entries and returns 200 OK response.
        """
        response = self.client.get("/api/journal-entry-lines/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), JournalEntryLines.objects.count())

#     # Positive test case for retrieve journal entry

    def test_retrieve_journal_entry(self):
        """
        Testcase method to retrieve journal entry object and returns 200 OK response.
        """
        response = self.client.get(
            f"/api/journal-entry-lines/{self.journal_entry.uid}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#     # Negative test case for retrieve journal entry

    def test_negative_retrieve_journal_entry_by_passing_wrong_uid(self):
        """
        Testcase method to retrieve journal entry object by passing wrong uid and returns 404 NOT FOUND response.
        """
        response = self.client.get(
            f"/api/journal-entry-lines/335b2c6c-6402-4de8-8319-3923d7395895/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#     # Positive Test case for adding journal entry

    def test_add_journal_entry(self):
        """
        Testcase method to add journal entry and returns 201 CREATED response.
        """
        journal_entry_data = {
            "accounting_date": self.accounting_date,
            "account": self.account.uid,
            "state": self.state,
            "description": fake.text(),
            "reconciled": fake.boolean(),
            "currency": self.currency.uid,
            "amount": random.uniform(10, 100),
            "accounting_type": self.journal_entry_accounting_type
        }
        response = self.client.post(
            "/api/journal-entry-lines/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     # Negative test case for adding journal entry

    def test_negative_add_journal_entry_by_adding_wrong_account_date(self):
        """
        Testcase method to add journal entry by adding wrong acount date and returns 400 BAD REQUEST response.
        """
        journal_entry_data = {
            "accounting_date": "Test",
            "account": self.account,
            "state": self.state,
            "description": fake.text(),
            "reconciled": fake.boolean(),
            "currency": self.currency,
            "amount": random.uniform(10, 100),
            "accounting_type": self.journal_entry_accounting_type
        }
        response = self.client.post(
            "/api/journal-entry-lines/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_add_journal_entry_by_adding_wrong_account(self):
        """
        Testcase method to add journal entry by adding wrong account and returns 400 BAD REQUEST response.
        """
        journal_entry_data = {
            "accounting_date": self.accounting_date,
            "account": "TYest",
            "state": self.state,
            "description": fake.text(),
            "reconciled": fake.boolean(),
            "currency": self.currency,
            "amount": random.uniform(10, 100),
            "accounting_type": self.journal_entry_accounting_type
        }
        response = self.client.post(
            "/api/journal-entry-lines/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_add_journal_entry_by_adding_wrong_state(self):
        """
        Testcase method to add journal entry by adding wrong state and returns 400 BAD REQUEST response.
        """
        journal_entry_data = {
            "accounting_date": self.accounting_date,
            "account": "TYest",
            "state": "Test",
            "description": fake.text(),
            "reconciled": fake.boolean(),
            "currency": self.currency,
            "amount": random.uniform(10, 100),
            "accounting_type": self.journal_entry_accounting_type
        }
        response = self.client.post(
            "/api/journal-entry-lines/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_add_journal_entry_by_adding_wrong_description(self):
        """
        Testcase method to add journal entry by adding wrong description and returns 400 BAD REQUEST response.
        """
        journal_entry_data = {
            "accounting_date": self.accounting_date,
            "account": self.account,
            "state": self.state,
            "description": " ",
            "reconciled": fake.boolean(),
            "currency": self.currency,
            "amount": random.uniform(10, 100),
            "accounting_type": self.journal_entry_accounting_type
        }
        response = self.client.post(
            "/api/journal-entry-lines/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_add_journal_entry_by_adding_wrong_reconciled(self):
        """
        Testcase method to add journal entry by adding wrong reconciled and returns 400 BAD REQUEST response.
        """
        journal_entry_data = {
            "accounting_date": self.accounting_date,
            "account": self.account,
            "state": self.state,
            "description": fake.text(),
            "reconciled": "TEst",
            "currency": self.currency,
            "amount": random.uniform(10, 100),
            "accounting_type": self.journal_entry_accounting_type
        }
        response = self.client.post(
            "/api/journal-entry-lines/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_add_journal_entry_by_adding_wrong_currency(self):
        """
        Testcase method to add journal entry by adding wrong currency and returns 400 BAD REQUEST response.
        """
        journal_entry_data = {
            "accounting_date": self.accounting_date,
            "account": self.account,
            "state": self.state,
            "description": fake.text(),
            "reconciled": fake.boolean(),
            "currency": ":test",
            "amount": random.uniform(10, 100),
            "accounting_type": self.journal_entry_accounting_type
        }
        response = self.client.post(
            "/api/journal-entry-lines/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_add_journal_entry_by_adding_wrong_amount(self):
        """
        Testcase method to add journal entry by adding wrong amount and returns 400 BAD REQUEST response.
        """
        journal_entry_data = {
            "accounting_date": self.accounting_date,
            "account": self.account,
            "state": self.state,
            "description": fake.text(),
            "reconciled": fake.boolean(),
            "currency": self.currency,
            "amount": "TEst",
            "accounting_type": self.journal_entry_accounting_type
        }
        response = self.client.post(
            "/api/journal-entry-lines/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_add_journal_entry_by_adding_wrong_accounting_type(self):
        """
        Testcase method to add journal entry by adding wrong accounting_type and returns 400 BAD REQUEST response.
        """
        journal_entry_data = {
            "accounting_date": self.accounting_date,
            "account": self.account,
            "state": self.state,
            "description": fake.text(),
            "reconciled": fake.boolean(),
            "currency": self.currency,
            "amount": "TEst",
            "accounting_type": self.journal_entry_accounting_type
        }
        response = self.client.post(
            "/api/journal-entry-lines/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Positive testcases for update journal entry

    def test_update_journal_entry(self):
        """
        Testcase method to update journal entry and returns 200 OK response.
        """
        journal_entry_data = {
            "accounting_date": self.accounting_date,
            "account": self.account.uid,
            "state": self.state,
            "description": fake.text(),
            "reconciled": fake.boolean(),
            "currency": self.currency.uid,
            "amount": 1200.21,
            "accounting_type": "booked"
        }
        response = self.client.put(
            f"/api/journal-entry-lines/{self.journal_entry.uid}/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Negative testcases for update journal entry

    def test_negative_update_journal_entry_by_passing_wrong_uid(self):
        """
        Testcase method to update journal entry by passing wrong uid and returns 404 NOT FOUND response.
        """
        journal_entry_data = {
            "accounting_date": self.accounting_date,
            "account": self.account.uid,
            "state": self.state,
            "description": fake.text(),
            "reconciled": fake.boolean(),
            "currency": self.currency.uid,
            "amount": 1200.21,
            "accounting_type": "booked"
        }
        response = self.client.put(
            f"/api/journal-entry-lines/49bc6aa4-4805-4c09-9f39-00b2d09dd3b1/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_negative_update_journal_entry_by_passing_wrong_account_date(self):
        """
        Testcase method to update journal entry by passing wrong date and returns 403 FORBIDDEN response.
        """
        journal_entry_data = {
            "accounting_date": "TEst",
            "account": self.account.uid,
            "state": self.state,
            "description": fake.text(),
            "reconciled": fake.boolean(),
            "currency": self.currency.uid,
            "amount": 1200.21,
            "accounting_type": "booked"
        }
        response = self.client.put(
            f"/api/journal-entry-lines/{self.journal_entry.uid}/", data=journal_entry_data)
        self.assertEqual(response.status_code, 400)

    def test_negative_update_journal_entry_by_passing_wrong_account_account(self):
        """
        Testcase method to update journal entry by passing wrong account and returns 400 BAD REQUEST response.
        """
        journal_entry_data = {
            "accounting_date": self.accounting_date,
            "account": "TEst",
            "state": self.state,
            "description": fake.text(),
            "reconciled": fake.boolean(),
            "currency": self.currency.uid,
            "amount": 1200.21,
            "accounting_type": "booked"
        }
        response = self.client.put(
            f"/api/journal-entry-lines/{self.journal_entry.uid}/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_update_journal_entry_by_passing_wrong_account_description(self):
        """
        Testcase method to update journal entry by passing wrong description and returns 400 BAD REQUEST response.
        """
        journal_entry_data = {
            "accounting_date": self.accounting_date,
            "account": self.account,
            "state": self.state,
            "description": "",
            "reconciled": fake.boolean(),
            "currency": self.currency.uid,
            "amount": 1200.21,
            "accounting_type": "booked"
        }
        response = self.client.put(
            f"/api/journal-entry-lines/{self.journal_entry.uid}/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_update_journal_entry_by_passing_wrong_account_currency(self):
        """
        Testcase method to update journal entry by passing wrong currency and returns 400 BAD REQUEST response.
        """
        journal_entry_data =  {
            "accounting_date": self.accounting_date,
            "account": self.account,
            "state": self.state,
            "description": self.description,
            "reconciled": self.reclined,
            "currency": self.currency,
            "amount": self.amount,
            "accounting_type": JOURNAL_ENTRY_LINES_CHOICES.DRAFT
        }
        journal_entry = JournalEntryLines.objects.create(**journal_entry_data)
        response = self.client.put(
            f"/api/journal-entry-lines/{journal_entry.uid}/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_update_journal_entry_by_passing_wrong_account_accounting_type(self):
        """
        Testcase method to update journal entry by passing wrong currency and returns 403 FORBIDDEN response.
        """
        journal_entry_data = {
            "accounting_date": self.accounting_date,
            "account": self.account,
            "state": self.state,
            "description": fake.text(),
            "reconciled": fake.boolean(),
            "currency": self.currency,
            "amount": 1200,
            "accounting_type": JOURNAL_ENTRY_LINES_CHOICES.BOOKED
        }
        journal_entry = JournalEntryLines.objects.create(**journal_entry_data)
        response = self.client.put(
            f"/api/journal-entry-lines/{journal_entry.uid}/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Negative Testcase for partial update

    def test_negative_partial_update_journal_by_passing_wrong_uid(self):
        """
        Testcase method to partial update journal entry by passing wrong uid and returns 404 NOT FOUND response.
        """
        journal_entry_data = {
            "accounting_date": self.accounting_date,
        }
        response = self.client.patch(
            f"/api/journal-entry-lines/44d10ae8-a17e-45ee-8189-f482fdbac7ca/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_negative_partial_update_journal_by_passing_wrong_accounting_date(self):
        """
        Testcase method to partial update journal entry by passing wrong uid and returns 400 BAD REQUEST response.
        """
        journal_entry_data = {
            "accounting_date": "TEst",
        }
        response = self.client.patch(
            f"/api/journal-entry-lines/{self.journal_entry.uid}/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_partial_update_journal_by_passing_wrong_account(self):
        """
        Testcase method to partial update journal entry by passing wrong account id and returns 400 BAD REQUEST response.
        """
        journal_entry_data = {
            "account": "TEst",
        }
        response = self.client.patch(
            f"/api/journal-entry-lines/{self.journal_entry.uid}/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_partial_update_journal_by_passing_wrong_state(self):
        """
        Testcase method to partial update journal entry by passing wrong account id and returns 400 BAD REQUEST response.
        """
        journal_entry_data = {
            "state": "TEst",
        }
        response = self.client.patch(
            f"/api/journal-entry-lines/{self.journal_entry.uid}/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_partial_update_journal_by_passing_wrong_description(self):
        """
        Testcase method to partial update journal entry by passing wrong description and returns 400 BAD REQUEST response.
        """
        journal_entry_data = {
            "description": "",
        }
        response = self.client.patch(
            f"/api/journal-entry-lines/{self.journal_entry.uid}/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_partial_update_journal_by_passing_wrong_currency(self):
        """
        Testcase method to partial update journal entry by passing wrong currency and returns 400 BAD REQUEST response.
        """
        journal_entry_data = {
            "currency": "",
        }
        response = self.client.patch(
            f"/api/journal-entry-lines/{self.journal_entry.uid}/", data=journal_entry_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Positive Testcase for delete journal entry
    def test_positive_delete_journal_entry(self):
        """
        Testcase method to delete journal entry and returns 204 NO CONTENT response.
        """
        response = self.client.delete(
            f"/api/journal-entry-lines/{self.journal_entry.uid}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Negative Testcase for delete journal entry

    def test_negative_delete_journal_entry(self):
        """
        Testcase method to delete journal entry by passing wring uid and returns 404 NOT founf response.
        """
        response = self.client.delete(
            f"/api/journal-entry-lines/{self.journal_entry.uid}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
