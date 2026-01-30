#pascal class- while writting the name of a class
# it should always start from a capital letter like every word start with captial letter like
#class consist of data and functionality
    #atm pin,balance
    #constructor is a function inside class
    #it seems like def__init__(self):
    #whenever we will create any variable inside the class it will be written inside the constructor
    #constructor is a special function because it has a super power because to execute to the code written inside it we didn't need to call it explicitly it execute automatically by creating a object
class MyAtm:
    def __init__(self):
        #rather than just writting pin will write self.
        self.pin = ''
        self.balance = 0
        self.menu()
        print("me to execute ho gaya obj jo  create kardia tumne")
    #create the menu what features we have or what we can do
    def menu(self):
        user_input = input("""
        hii how  can i help you?
        1.press one to create pin
        2.press 2 to change pin
        3.press 3 to check balance
        4.press 4 to withdraw
        5.press 5 to deposite
        6.anything else to exit
        press : 
        """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        elif user_input == '5':
            self.deposite()
        else:
            print("Thank you! Have a nice day 😊")
            #exit()


    def create_pin(self):
        new_pin = input("enter your  new pin: ")
        confirm_pin = input("re_enter your pin for confirmation: ")
        if new_pin == confirm_pin:
            self.pin = new_pin
            print("pin created successfully")
        else:
            print("pin mis-matched")
            self.create_pin()
        self.menu()

    def change_pin(self):
        if self.pin == '':
            print("you have not created a pin yet.")
            return

        old_pin = input("enter your old pin: ")

        if old_pin != self.pin:
            print("incorrect pin ! try again")

        new_pin = input("Enter your new PIN: ")
        confirm_pin = input("Re-enter your new PIN: ")

        if new_pin != confirm_pin:
            print("PIN mismatch. Try again.")
            return
        elif not new_pin.isdigit() or len(new_pin) != 4:
            print("PIN must be 4 digits.")
            return
        else:
            self.pin = new_pin
            print("PIN changed successfully ")
        self.menu()

    def check_balance(self):
        user_pin = input("enter your pin.")
        if self.pin == user_pin:
            print("your account balance is :", self.balance)
        else:
            print("incorrect pin")
        self.menu()

    def withdraw(self):
        user_pin = input("enter your pin.")
        if self.pin == user_pin:
            amount = float(input("enter the amount you want: "))
            if amount > self.balance:
                print("you have insufficient balance in your account")
            else:
                balance = self.balance - amount
                self.balance = balance
                print("withdraw is successful")
                print("your current balance is: ",self.balance)
        else:
            print("incorrect pin")
        self.menu()
    
    def deposite(self):
        user_pin = input("enter your pin: ")
        if self.pin == user_pin:
            amount = float(input("enter the amount you want to deposite: "))
            self.balance += amount
            print("money deposited successfully")
            print("your current balance is: ",self.balance)
        else:
            print("incorrect pin")
        self.menu()
obj = MyAtm()
    #by writting print(type(obj)) i can see the class from where it belongs to <class '__main__.MyAtm'>
    #obj. then it will show two option .pin and .balance 
