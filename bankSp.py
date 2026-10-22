def exitBank():
    print("EXIT")
    print("ThankYou for visiting ")
    
def check():
    acc_no=int(input("Enter the account number of the customer : "))
    if acc_no in d:
        print("Current Balance in the given account number is : ",d[acc_no]["Balance"])
    else:
        print("Account not Found")
        
def withdraw():
    acc_no=int(input("Enter the account number of the customer : "))
    with_money=int(input("Enter the amount to be withdraw : "))
    if acc_no in d:
        if d[acc_no]["Balance"]>=with_money:
            d[acc_no]["Balance"]-=with_money
        print("Money is Withdrawed from the given account number")
        print("Current Balance : ",d[acc_no]["Balance"])
    else:
        print("Account not Found")
        
def deposit():
    acc_no=int(input("Enter the account number of the customer : "))
    money=int(input("Enter the Amount of money to be deposited : "))
    if acc_no in d:
        d[acc_no]["Balance"]+=money
        print("Money is Deposited to the given account number")
    else:
        print("Account not Found")
        
def create():
    acc_no=int(input("Enter the account number of the customer : "))
    name=input("Enter the name of the customer : ")
    age=int(input("Enter the age of the customer : "))
    ph_no=int(input("Enter the phone number of the customer : "))
    d[acc_no]={
        "Name":name,
        "Age":age,
        "PhoneNumber":ph_no,
        "Balance":0
        }
    print("Account is Created")
#main
d={}
while True:
    print("--------E-Banking Management System----------")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")
    ch=input("Enter Your Choice : ")
    if ch=='1':
        create()
    elif ch=='2':
        deposit()
    elif ch=='3':
        withdraw()
    elif ch=='4':
        check()
    elif ch=='5':
        exitBank()
    else:
        print("Invalid Choice ")
        break
