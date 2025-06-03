class AtmMchine:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
        
    def menu(self):
        user_input = input("""
              ATM MACHINE Menu to select an option.
              1. Create Account
              2. Change Pin
              3. Check Balance
              4. Withdraw Money
              5. Deposit Money
              6. Exit
              """)
        
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.check_balance()
        elif user_input == "4":
            self.withdraw_money()
        elif user_input == "5":
            self.deposit_money()
        else:
            exit()
            
    def create_pin(self):
        user_input = input('Enter your pin: ')
        self.pin = user_input
        user_blance = int(input('Enter your blance: '))
        self.balance = user_blance
        print('Pin created successfully')
        self.menu()
        
    def change_pin(self):
        user_input = input('Enter your old pin: ')
        if user_input == self.pin:
            new_pin = input('Enter your new pin: ')
            self.pin = new_pin
            print('Pin changed successfully')
        else:
            print('Invalid pin')
        self.menu()
            
    def check_balance(self):
        user_input = input('Enter your pin: ')
        if user_input == self.pin:
            print('Your balance is: ', self.balance)
        else:
            print('Invalid pin')
        self.menu()
        
    def withdraw_money(self):
        user_input = input('Enter your pin: ')
        if user_input == self.pin:
            amount = int(input('Enter the amount you want to withdraw: '))
            if amount <= self.balance:
                self.balance -= amount
                print(f'Withdrawal successful. Your new balance is: {self.balance}')
            else:
                print('Insufficient balance')
        else:
            print('Invalid pin')
        self.menu()
    
    def deposit_money(self):
        user_input = input('Enter your pin: ')
        if user_input == self.pin:
            amount = int(input('Enter the amount you want to deposit: '))
            self.balance += amount
            print(f'Deposit successful. Your new balance is: {self.balance}')
        else:
            print('Invalid pin')
        self.menu()