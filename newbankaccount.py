class Checkingaccount:

    def __init__(self, bal):
        self.__balance = bal

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return self.__balance
        else:
            return 'Insufficent Funds'

    def get_balance(self):
        interest = 1.02
        return self.__balance * interest
    
    def set_balance(self, bal):
        self.__balance = bal


class Moneymarket:
    def __init__(self, bal):
        self.__balance = bal

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return self.__balance
        else:
            return 'Insufficent Funds'

    def get_balance(self):
        interest = 1.05
        return self.__balance * interest
    
    def set_balance(self, bal):
        self.__balance = bal
    

class Savings:
    def __init__(self, bal):
        self.__balance = bal

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance += amount
        else:
            return "Insufficient Funds"

    def get_balance(self):
        interest = 1.03
        return self.__balance * interest
    


def main():

    
    objChecking = Checkingaccount(1200)
    tony_account = float(input("Tony, How much money is in your account? "))

    objChecking.set_balance(tony_account)
    
    answer = input("What would you like to do. Please enter 'd' to deposit or 'w' to withdraw. Press 'q' to exit. ")
    
    while answer != 'q':
        
        if answer == 'd':

            deposit = float(input('How much would you like to deposit? '))
            print(f"You deposited ${deposit:.2f}")
            new_balance = objChecking.deposit(deposit)
            print(f"Your new balance is ${new_balance:.2f}")
            new_balance_plusinterest = objChecking.get_balance()
            print(f"This checking account yields 2% interest. Your new balance with interest will be ${new_balance_plusinterest:.2f}")
            answer = input("What would you like to do. Please enter 'd' to deposit or 'w' to withdraw. Press 'q' to exit. ")
        
        elif answer == 'w':

            withdraw = float(input('How much would you like to withdraw? '))
            print(f"You withdrew ${withdraw:.2f}")
            new_balance2 = objChecking.withdraw(withdraw)
            if new_balance2 != 'Insufficent Funds':
                print(f"Your new balance is ${new_balance2:.2f}")
                new_balance2_plusinterest = objChecking.get_balance()
                print(f"This checking account yields 2% interest. Your new balance with interest will be ${new_balance2_plusinterest:.2f}")
            else:
                print(new_balance2)
            answer = input("What would you like to do. Please enter 'd' to deposit or 'w' to withdraw. Press 'q' to exit. ")
        
        else:
            print("You must enter 'd', 'w', or 'q'")
            answer = input("What would you like to do. Please enter 'd' to deposit or 'w' to withdraw. Press 'q' to exit. ")
    
    print('Thank you')


if __name__ == '__main__':
    main()