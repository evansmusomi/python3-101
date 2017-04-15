class BankAccount:
    """ A bank account blue print with basic methods and attributes. """

    def __init__(self):
        """ Initialises the bank account """
        self.balance = 0
        self.minimum_balance = 200
        self.minimum_deposit = 200

    def deposit(self, amount):
        """ Deposits specified amount of money into bank account.

        Args:
            amount: how much money to Deposit

        Returns:
            status: transaction status with new balance
        """

        if not isinstance(amount, (int, float)):
            raise TypeError("Expected a number")
        if amount < self.minimum_deposit:
            return "Minimum deposit is {}".format(self.minimum_deposit)
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """ Withdraws specified amount of money from bank account.

        Args:
            amount: how much money to Withdraw

        Returns:
            status: transaction status
        """

        if not isinstance(amount, (int, float)):
            raise TypeError("Expected a number")

        if amount > (self.balance - self.minimum_balance):
            return "Insufficient funds"

        self.balance -= amount
        return self.balance
