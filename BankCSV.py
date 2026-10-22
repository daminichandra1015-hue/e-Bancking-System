import csv
import os
FILENAME="accounts.csv"
#Create csv file if it doesnot exits
if not os.path.exists(FILENAME):
    with open(FILENAME,"w",newline="") as file:
        writer=csv.writer(file)
        write.writerow(["AccountNo","Name","Balance"])
#Create Account
def create_account():
    acc_no=int(input("Enter Account Number : "))
    name=input("Enter Coustomer Name :")
    balance=float(input("Enter the Balance : "))
    with open("FILENAME","a",newline="") as file:
        writer=csv.writer(file)
        writer.writerow([acc_no,name,balance])
    print("Account Created Successfully!")
#Display All Accounts
def display_accounts():
    with open(FILENAME,"r")as file:
        reader=csv.reader(file)
        next(reader)
        print("\nAccount no\tName\tBalance")
        print("--------------------------------------")
        for row in reader:
            print(row[0],"\t",row[1],"\t",row[2])
#Deposit Money
def deposit():
     acc_no=int(input("Enter Account Number : "))
     amount=float(input("Enter Deposit Amount : "))

     rows=[]
     with open(FILENAME,"r")as file:
         reader=csv.reader(file)
         rows=list(reader)
     found=False
     for i in range(1,len(rows)):
         if rows[i][0]==acc_no:
             rows[i][2]==str(float(rows[i][2])+amount)
             found=True
             break
     if found:
         with open("FILENAME","w",newline="")as file:
             writer=csv.writer(file)
             writer.writerows(rows)
             print("Amount Deposited Successfully!")
     else:
         print("Accounr Not Found!")
#Withdraw Money
def withdraw():
     acc_no=int(input("Enter Account Number : "))
     amount=float(input("Enter Withdraw Amount : "))

     row=[]
     with open(FILENAME,"r") as file:
         reader=csv.reader(file)
         rows=list(reader)
     found=False
     for i in range(1,len(rows)):
         if rows[i][0]==acc_no:
             balance=float(rows[i][2])
             if balance>=amount:
                 rows[i][2]=str(balance-amount)
                 print("Withdrawal Successfully!")
             else:
                 print("Insufficient Balance!")
             found=True
             break
         if found:
             with open("FILENAME","w",newline="")as file:
              writer=csv.writer(file)
             writer.writerows(rows)
     else:
         print("Accounr Not Found!")
#Check Balance
def check_balance():
    acc_no=int(input("Enter Account Number : "))
    with open(FILENAME,"r") as file:
         reader=csv.reader(file)
         rows=list(reader)
    found=False
    for rows in reader:
        if rows[0]==acc_no:
            print("\nAccount Number : ",rows[0])
            print("\nCustomer Name : ",rows[1])
            print("\nBalance : ",rows[2])
            found=True
            break
        if not found:
            print("Account Not Found!")
#main Menu
while True:
    print("\n======E-Banking Management System=====")
    print("1.Create Account")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Check Balance")
    print("5.Display All Accounts")
    print("6.Exit")
    choice=input("Enter your choice :")
    if choice=='1':
        create_account()
    if choice=='2':
        deposit()
    if choice=='3':
        withdraw()
    if choice=='4':
        check_balance()
    if choice=='5':
        display_accounts()
    if choice=='6':
        print("Thank You for Using E-Banking System!!!")
        break
else:
     print("Invalid Choice!")