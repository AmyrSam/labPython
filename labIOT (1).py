#!/usr/bin/env python
# coding: utf-8

# In[5]:





# In[ ]:





# In[2]:





# In[46]:


class BankAccount(object):#Exercise1
    def __init__(self,balance=0):
        self.balance = balance
        self.pin = 1234
        
    def checkCode(self,value):
        return self.pin == value

    def deposit(self, pin, deposit_amount=0):
        if self.checkCode(pin):
            self.deposit_amount=deposit_amount
            self.balance += deposit_amount
            return self.balance
        else:
            print("Wrong pin code")

    def withdraw(self, pin, withdraw_amount=0):
        if self.checkCode(pin):
            if withdraw_amount < self.balance:
                self.balance -= withdraw_amount
                return self.balance
            else:
                print("Not enough balance")
        else:
            print("Wrong pin code")
            
    def checkBalance(self, pin):
        if self.checkCode(pin):
            return self.balance
        else:
            print("Wrong pin code")
            
    def changePIN(self, oldvalue, newvalue):
        if self.checkCode(oldvalue):
            self.pin = newvalue
            print ('Pin code has been successfully changed.')
        else:
            print ('Wrong pin code. Try again.')

class MinimumBalanceAccount(BankAccount):
    def __init__(self,balance = 0):
        self.balance = balance
        


c = BankAccount()
c.deposit(1234,100)
c.withdraw(1234,50)
c.checkBalance(1234)
c.changePIN(1234,1235)
c.deposit(1235,30)


# In[2]:


class SavingsAccount:#Exercise3
    def _init_(self, balance = 0): #initialize
        self.balance = balance
        self.pin = 1122
        
    def checkPin(self, value): #check pin code
        return self.pin == value

    def Deposit(self, pin, deposit_amount = 0): #deposit
        if self.checkPin(pin):
            self.deposit_amount = deposit_amount
            self.balance += deposit_amount
            return self.balance
        else:
            print("WRONG PIN CODE.")

    def Withdraw(self, pin, withdraw_amount = 0): #withdrawal
        if self.checkPin(pin):
            if withdraw_amount < self.balance:
                self.balance -= withdraw_amount
                return self.balance
            else:
                print("INSUFFICIENT BALANCE.")
        else:
            print("INVALID PIN CODE.")
            
    def addInterest(self, interest): #addInterest | 10% (point form)
        self.Interest = interest #instant variables
        self.balance = (interest * self.balance) + self.balance
        return self.balance
            
    def checkBalance(self, pin): #check balance
        if self.checkPin(pin):
            return self.balance
        else:
            print("INVALID PIN CODE.")           
                       
Acc = SavingsAccount()


# In[3]:


class FeeSavingsAccount:#Exercise4
    def _init_(self, balance = 0): #initialize
        self.balance = balance
        self.pin = 1122
        
    def checkPin(self, value): #check pin code
        return self.pin == value

    def Deposit(self, pin, deposit_amount = 0): #deposit
        if self.checkPin(pin):
            self.deposit_amount = deposit_amount
            self.balance += deposit_amount
            return self.balance
        else:
            print("WRONG PIN CODE.")
    
    def Withdrawal(self, pin, withdraw_amount = 0, charge = 1): #withdraw w/ charge
        if self.checkPin(pin):
            if withdraw_amount < self.balance:
                self.Charge = charge #instant variable
                self.balance -= withdraw_amount + charge
                return self.balance
            else:
                print("INSUFFICIENT BALANCE.")
        else:
            print("INVALID PIN CODE.")
            
    def checkBalance(self, pin): #check balance
        if self.checkPin(pin):
            return self.balance
        else:
            print("INVALID PIN CODE.")           
                       
Acc = FeeSavingsAccount()


# In[4]:





# In[10]:


class CustomList(object):#Exercise4
        def __init__(self, elements=0):
            self.my_custom_list = [0] * elements

        def __setitem__(self, index, value):
            self.my_custom_list[index] = value

        def __getitem__(self, index):
            return "Hey you are accessing {} element whose value is: {}".format(index, self.my_custom_list[index])

        def __str__(self):
            return str(self.my_custom_list)
        
obj = CustomList(12)
obj[0] = 1
print(obj[0])
print(obj)


# In[ ]:




