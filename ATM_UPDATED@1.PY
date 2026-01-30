class MyAtm:
    def __init__(self):
        #rather than just writting pin will write self.
        self.name = ''
        self.account_number = ''
        self.pin = ''
        self.pin_attempts = 0
        self.is_locked = False
        self.balance = 5000
        self.menu()
        print("me to execute ho gaya obj jo  create kardia tumne")
    #create the menu what features we have or what we can do
    def menu(self):
        user_input = input("""
        hii how  can i help you?
       1. press 1 to create account
       2. press 2 to create pin
       3. press 3 to change pin
       4. press 4 to check balance
       5. press 5 to withdraw
       6. press 6 to deposit
        """)

        if user_input == '1':
            self.create_account()
        elif user_input == '2':
            self.create_pin()
        elif user_input == '3':
            self.change_pin()
        elif user_input == '4':
            self.check_balance()
        elif user_input == '5':
            self.withdraw()
        elif user_input == '6':
            self.deposit()
        else:
            print("Thank you! Have a nice day ")
            #exit()
  
    # ---------------- CREATE ACCOUNT ----------------
    def create_account(self):
        if self.account_number != '':
            print("Account already exists.")
            self.menu()
            return

        self.name = input("Enter account holder name: ")

        import random
        self.account_number = str(random.randint(10000000, 99999999))

        print("\nAccount created successfully!")
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)

        self.menu()

    # ------------------verify pin------------------------
    def verify_pin(self):

        if self.is_locked:
            print("Account is locked due to multiple wrong PIN attempts.")
            return False

        if self.pin == '':
            print("No PIN found. Please create a PIN first.")
            return False

        user_pin = input("Enter your PIN: ")

        if user_pin == self.pin:
            self.pin_attempts = 0   
            return True
        else:
            elf.pin_attempts += 1
            print(f"Incorrect PIN. Attempts left: {3 - self.pin_attempts}")

            if self.pin_attempts >= 3:
                self.is_locked = True
                print("Account locked! Please contact bank.")

            return False



     # ---------------- CREATE PIN ----------------
    def create_pin(self):
        if self.account_number == '':
            print("Please create account first.")
            self.menu()
            return

        new_pin = input("Enter new 4-digit PIN: ")
        confirm_pin = input("Re-enter PIN: ")

        if new_pin != confirm_pin:
            print("PIN mismatch.")
            self.create_pin()
            return

        if not new_pin.isdigit() or len(new_pin) != 4:
            print("PIN must be exactly 4 digits.")
            self.create_pin()
            return

        self.pin = new_pin
        print("PIN created successfully.")
        self.menu()

    # ---------------- CHANGE PIN ----------------
    def change_pin(self):
        if self.verify_pin():
            new_pin = input("Enter new 4-digit PIN: ")
            confirm_pin = input("Re-enter PIN: ")

            if new_pin != confirm_pin:
                print("PIN mismatch.")
                self.menu()
                return

            if not new_pin.isdigit() or len(new_pin) != 4:
                print("PIN must be exactly 4 digits.")
                self.menu()
                return

            self.pin = new_pin
            print("PIN changed successfully.")

        self.menu()

    # ---------------- CHECK BALANCE ----------------
    def check_balance(self):
        if self.verify_pin():
            print("Current Balance:", self.balance)
        self.menu()

    # ---------------- WITHDRAW ----------------
    def withdraw(self):
        if self.verify_pin():
            amount = float(input("Enter amount to withdraw: "))

            if amount > self.balance:
                print("Insufficient balance.")
            else:
                self.balance -= amount
                print("Withdrawal successful.")
                print("Remaining Balance:", self.balance)

        self.menu()

    # ---------------- DEPOSIT ----------------
    def deposit(self):
        if self.verify_pin():
            amount = float(input("Enter amount to deposit: "))
            self.balance += amount
            print("Deposit successful.")
            print("Updated Balance:", self.balance)

        self.menu()


# -------- PROGRAM START --------
obj = MyAtm()