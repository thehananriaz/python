

class User():
    def __init__(self, name, age , gender):
        self.name = name
        self.age = age
        self.gender = gender
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Gender : ", self.gender)



class bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0
    def deposit(self,balance):
        self.balance = self.balance + balance
        print("The new amount is: $",self.balance)
    def withdraw(self,amount):
            self.amount = amount
            if self.amount > self.balance:
                print("Sorry you don't have enough")
            else:
                self.balance = self.balance - self.amount
                print("Amount has been withdrawed Succcesfully. You now have ",self.balance)
    def view_balance(self):
            self.show_details()
            print("YOu account balance is $",self.balance)
new= bank("hanan", 21 , "male")
new.deposit(400)
new.deposit(1000)
new.view_balance()