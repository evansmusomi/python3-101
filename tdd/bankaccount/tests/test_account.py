import unittest
from ..account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount()

    def test_deposit_amount_is_number(self):
        with self.assertRaises(TypeError):
            self.account.deposit("String")

    def test_deposit_amount_is_acceptable(self):
        self.assertEqual(self.account.deposit(100),
            "Minimum deposit is {}".format(self.account.minimum_deposit))

    def test_deposit_updates_balance(self):
        self.assertEqual(self.account.deposit(500), self.account.balance)
        self.assertEqual(self.account.deposit(1000), self.account.balance)
        self.assertEqual(self.account.deposit(15000), self.account.balance)

    def test_withdraw_amount_is_number(self):
        with self.assertRaises(TypeError):
            self.account.withdraw("500")

    def test_withdraw_amount_is_valid(self):
        available_balance = self.account.balance - self.account.minimum_balance
        self.assertEqual(self.account.withdraw(available_balance + 1000),
            "Insufficient funds")
        self.assertEqual(self.account.withdraw(available_balance + 1),
            "Insufficient funds")
        self.assertEqual(self.account.withdraw(available_balance + 100),
            "Insufficient funds")

    def test_withdraw_updates_balance(self):
        self.account.deposit(1000)
        self.assertEqual(self.account.withdraw(500), 500)
        self.assertEqual(self.account.withdraw(200), 300)
