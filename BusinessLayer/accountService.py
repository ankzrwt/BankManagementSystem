from Entity.account import Account
from Entity.customer import Customer
from Database.bank import accounts,customers

class AccountService:

    def validInput(self,name,phone)->bool:
        if len(name)<3:
            print("invalid name")
            return False
        if len(phone)!=10:
            print("invalid phone")
            return False
        return True

    def createCustomerId(self,name,phone)->str:
        return name[:3]+phone


    def addAccount(self,name,phone):
        global accounts
        global customers
        if self.validInput(name,phone):
            customerToAdd=Customer(name,phone)
            customerToAdd.setCustomerId(self.createCustomerId(name,phone))
            customerAccount=Account(customerToAdd.getCustomerId())
            customerAccount.setAccountNo(customerToAdd.getCustomerId())
            customerAccount.setBalance(0)
            accounts.append(customerAccount)
            customers.append(customerToAdd)


            
        






    