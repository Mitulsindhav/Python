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
acno=int(input("Enter Account Number :"))
cname=input("Enter Customer Name :")
balance=int(input("Enter Initial Balance :"))

b1.openAccount(acno,cname,balance)

file=open(cname+".txt","w")
file.close()
file=open(cname+".txt","a")
file.write("*"*50)
file.write("\n You Account Is Opened  with "+str(balance)+"Rs.")



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
        file.write("\n Your Account Is Credited with "+str(amount)+"Rs.")
        b1.deposit(amount)
        print("*"*40)
    elif choice==2:
        amount=int(input("Enter withdrawal Amount:"))
        file.write("\n Your Account Is Debited with "+str(amount)+"Rs.")
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
        
        
file.close()


