class Bank:

    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello",cname,"Your Account Number ",acno,"Is Opened with ",balance,"Rs ")

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Sorry You Need Another ",amount-self.balance,"Rs")
    def checkBalance(self):
        print("Your Current Balance Is ",self.balance)


b1=Bank()
b1.openAccount(101,"Mitul Sindhav",500000)


while True:

    print("*"*40)
    print("1.Deposit")
    print("2.withdraw")
    print("3. check balance")
    print("4. Exit")
    print("*"*40)


    choice=int(input("Enter Your Choice :"))
    print("*"*40)

    if choice==1:
        amount=int(input("Enter Deposit Amount :"))
        b1.deposit(amount)
        print("*"*40)
    elif choice==2:
        amount=int(input("Enter withdrawal Amount:"))
        b1.withdraw(amount)
        print("*"*40)
    elif choice==3:
        b1.checkBalance()
    elif choice==4:
        print("Thank You for Using Our Services.")
        print("*"*40)
        break
    else:
        print("Invalid Choice.Please Try Again")
        print("*"*40)
        
        
        

