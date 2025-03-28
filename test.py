class Bankaccount:

    def __init__(self, accno, name, address, opendate, mobno, DOB,starting_balance,deposit_history,withdrawl_hisotry):
        self.a = accno
        self.b = name
        self.c = address
        self.d = opendate
        self.e = mobno
        self.f = DOB
        self.g = starting_balance
        self.deposit_history=[]
        self.withdrawl_hisotry=[]

    def showaccount(self):
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.d)
        print(self.e)
        print(self.f)

    def modifyaccount(self):
        print(self.a)

    def deposit(self):
        c=float(input("Enter the deposit amount:"))
        self.g=self.g+c
        print("The amount deposit:",c)
        self.deposit_history.append(c)



    def withdrawl(self):
        c=float(input("Enter the withdrawl amount:"))
        self.g=self.g-c
        print("Amount Withdrawl:",c)
        self.withdrawl_hisotry.append(c)



    def currentbalance(self):
        print("Current Balance is:",self.g)

    def transactionhistory(self):
       print("Deposits:",self.deposit_history)
       print("Withdrawl:",self.withdrawl_hisotry)

    def stop():
        print("Stop")

obj=Bankaccount("12345","Veera","Palani","10.10.2019","9087654321","14.10.2001",1000,"c","c")

while True:
        print("Welcome to Indian Bank")
        print("1,Showaccount")
        print("2.Modifyaccount")
        print("3.deposit")
        print("4.withdrawl")
        print("5.currentbalance")
        print("6.transactionhistory")
        print("7.stop")

        option = input("Please select any option [1-7]:")
        if option == "1":
            obj.showaccount()
        if option == "2":
            obj.modifyaccount()
        if option == "3":
            obj.deposit()
        if option == "4":
            obj.withdrawl()
        if option == "5":
            obj.currentbalance()
        if option == "6":
            obj.transactionhistory()
        if option == "7":
            obj.stop()
