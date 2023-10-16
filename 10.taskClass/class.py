#1.Create the bankAccount Details
class CreateAccount:
    def __init__(self,bank,accountNumber,name,balance,pin):
        self.bank=bank
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance
        self.pin=pin
        self.createMenu()
    def createMenu(self):
        user_input=input("enter the what would you do:")
        if user_input=="1":
            self.createPin()
        elif user_input=="2":
            self.checkBalance()
        elif user_input=="3":
            self.deposit()
        elif user_input=="4":
            self.withdrawl()
    def createPin(self):
        Newpin=self.pin
        print("Pin Generated Successfully")
    def checkBalance(self):
        user_pin=int(input("enter the pin:"))
        if user_pin==self.pin:
            print("Dear {} your balance is: {}.-{}".format(self.name,self.balance,self.bank))
        else:
            print("Incorrect pin")
    def deposit(self):
        user_pin=int(input("enter the pin:"))
        if user_pin==self.pin:
            amount=int(input("deposit the amount:"))
            self.balance+=amount
            print("Transaction Successfully Credited in your account Rs.{} your balance is:{} -{}".format(amount,self.balance,self.bank))
        else:
            print("In Correct Pin")
        
    def withdrawl(self):
        user_pin=int(input("enter the pin:"))
        if user_pin==self.pin:
            amount=int(input("transferred the amount:"))
            if amount<=self.balance:
                self.balance-=amount
                print(" your transaction Successfully Debited in your Account Rs.{} your balance is:{} -{}".format(amount,self.balance,self.bank))
            else:
                print("In Suffiecient Funds")
        else:
            print("In Correct Pin")
        



CreateAccount("SBI","62256723222","Suresh",int(input("your currernt amount is:")),int(input("create pin:")))


#MathFunctions

class Math:
    def __init__(self,one,two,three,four):
        self.one=one
        self.two=two
        self.three=three
        self.four=four
    def Addition(self):
        total=0
        value=(self.one,self.two,self.three,self.four)
        for i in value:
            total+=i
        print(total)
    def Subtraction(self):
        total=0
        value=(self.one,self.two,self.three,self.four)
        for i in value:
            total-=i
        print(total)
    def Multiply(self):
        total=1
        value=(self.one,self.two,self.three,self.four)
        for i in value:
            total*=i
        print(total)
    def Division(self):

        total=100
        value=(self.one,self.two,self.three,self.four)
        for i in value:
            total/=i
        print(total)
   

obj1=Math(int(input("enter the num:")),int(input("enter the num:")),int(input("enter the num:")),int(input("enter the num:")))
obj1.Addition()
obj1.Subtraction()
obj1.Multiply()
obj1.Division()

#3.reverse the letters

word_1=input("enter the word1:")
print(word_1[::-1])

word_2=input("enter the word2:").split()
print(*word_2[::-1])

word_3=input("enter the word3:").split()
join_space=" ".join(word_3[::-1])
print(join_space[::-1])


