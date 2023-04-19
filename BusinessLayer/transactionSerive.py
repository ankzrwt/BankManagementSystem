from Database.bank import accounts

class TransactionSerive:

    def addMoney(self,accountNo:str,amount:int)->bool:
        for account in accounts:
            if accountNo==account.getAccountNo():
                # account.balance+=amount
                account.setBalance(account.getBalance()+amount)
                print("amount added successfully")
                return True
        print("invalid account")
        return False
    
    def withdrawl(self,accountNo:str,amount:int)->bool:
        for account in accounts:
            if accountNo==account.getAccountNo():
                if account.getBalance()<amount:
                    print("your balance is low")
                    return False
                #account.balance-=amount
                account.setBalance(account.getBalance()-amount)
                print("withdrawl successful")
                return True
        print("invalid acc")
        return False
    
    def checkBalance(self,accountNo:str):
        for account in accounts:
            if accountNo==account.accountNo:
                print(account.balance)
                return
        print("invalit account")
        return
    
    def transferMoney(self,fromAccountNo,toAccountNo,amount):
        isFromAccountExist = False
        isToAccountExist = False
        for account in accounts:
            if fromAccountNo==account.accountNo:
                isFromAccountExist = True
            if toAccountNo == account.accountNo:
                isToAccountExist = True

        if isFromAccountExist==isToAccountExist==True:

            if self.withdrawl(fromAccountNo,amount):
                self.addMoney(toAccountNo,amount)









    
            
        
