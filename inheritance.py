class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number
    def send_money(self,amount, receipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES sent to {receipient} successfully.")
        else:
            print("Insufficient amount to send money.")
class PersonalMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, id_no):
        super().__init__(account_balance,phone_number)
        self.id_no = id_no
    def buy_airtime(self,amount):
        self.account_balance -= amount
        print(f"{amount} KES airtime bought successfully.")
class BusinessMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, business_name):
        super().__init__(account_balance,phone_number)
        self.business_name = business_name
    def receive_payment(self,amount):
        self.account_balance += amount
        print(f"{amount} KES received from a customer.")
personal = PersonalMpesa(2000, 700000000,1331239)
personal.send_money(1000, 729405278)
personal.send_money(3000, 789016738)
personal.buy_airtime(100)

business = BusinessMpesa(1000,768935246, "Total Station")
business.receive_payment(1000)
business.send_money(500, 780912356)