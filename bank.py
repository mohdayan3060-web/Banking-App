# write your code here
import hashlib
class BankAccount:
  def __init__(self):
    accountNumber=0
    name=str("")
    balance=0
    mobileNumber=0
    Addhar=0
  def display(self):
    print("welcome to HDFC bank !")
    print("1. creating new bankaccount ")
    print("2.deposite money in your existing account ")
    print("3. withdrwal money ")
    print("check bank fees ")
    choose=input("select option")

    if choose=='1':
      
      self.createNewAccount()
      
    elif choose =='2':
      self.deposit()
    elif choose =='3':
      self.withdrawal()
    elif choose == '4':
      self.bankfees() 
    else:
      print("Sorry!")
      print("please choose valid options") 

  def createNewAccount(self):
    print("thanks for choosing HDFC bank ")
    print("let's proceed  it ----------------")
    self.name=str(input("Enter you full name "))
    self.mobileNumber=int(input("enter your 10 digit mobile number :"))
    self.firstDeposite()
    print("you have submitted ",self.balance)
    self.Addhar=int(input("enter you Addhar number "))
    print("congratulation  you account is successfully created ")
    self.accountNumber = self.create_account_number(self.Addhar, self.mobileNumber)
    self.detailes()
    self.display()


 


  def firstDeposite(self):
    print("Enter the ammount you want to submit ")
    self.balance=int(input("make sure ammount not less then 5000 !"))
    

  def create_account_number(self,Addhar,mobileNumber ):
    # 1. Combine inputs into a single string
    combined_data = f"{Addhar}{mobileNumber}"
    
    # 2. & 3. Create a SHA-256 hash and get the hex string
    hash_object = hashlib.sha256(combined_data.encode('utf-8'))
    hex_hash = hash_object.hexdigest()
    
    # 4. Convert the hex hash to a massive integer
    big_number = int(hex_hash, 16)
    
    # 5. Extract a 10-digit number using modulo 10^10
    # This ensures the result is always between 0 and 9,999,999,999
    account_number = big_number % (10**10)
    
    # Optional: Format with leading zeros to ensure it's always 10 characters
    return f"{account_number:010d}"  


  def deposit(self):
    user_name=str(input("Enter  your name "))
    user_input=int(input("Enter your account number "))
    if user_name==self.name and user_input==self.accountNumber:
      sub=int(input("enter the amount you want to submit  "))
      self.balance=self.balance+sub
      print("successfull !")
    else:
      print("please check you credential again:")

    print("your current balance is :",self.balance)
    print("thank you ")
    self.display()  

    
      
    
    
  def withdrawal(self):
    user_input=int(input("Enter you account number "))
    user_name=str(input("Enter your name "))
    user_phone_no=int(input("enter your moble number "))
    if user_input==self.accountNumber and user_name==self.name and user_phone_no==self.mobileNumber:
      extract=int(input("enter the ammount you want to withdrwal "))
      if extract<=self.balance:
        self.balance=self.balance-extract
    else:
      print("please cheack your credential  ")
    print("you current balnce is :",self.balance)
    print("thank you !")
    self.display()     

    
#   def bankfees(self):
#   we will find out solution after some my eaxm are going on----------------------

    pass
  def detailes (self):
    print("your name is :",self.name)
    print("your mobile number is :",self.mobileNumber)
    print("your Addhar is :",self.Addhar)
    print("your account numebr:",self.accountNumber)
    print("your current balance is :",self.balance)

  
obj=BankAccount()
# obj01.menu()  
obj.display()

