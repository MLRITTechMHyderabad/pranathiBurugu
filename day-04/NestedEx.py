class InsufficientFundsError(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        """
        Withdraws money from the account.
        
        :param amount: Amount to withdraw
        :return: Remaining balance or error message
        """    
        try:
            if(amount<0):
                raise ValueError("amount should not be negative")
            elif(self.balance<amount):
                raise InsufficientFundsError("insufficient funds")
            else :
                self.balance-=amount
        except ValueError as e:
            return e
        except InsufficientFundsError as e:
            return e
        except Exception as e:
            return e

# Example Usage:
account = BankAccount(100)
print(account.withdraw(150))  # Should raise InsufficientFundsError
print(account.withdraw(-10))  # Should raise ValueError
