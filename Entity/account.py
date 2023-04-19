class Account:
    
    def __init__(self,customerId):
        self.customerId=customerId
        self.accountNo=None
        self.balance=None

    def getCustomer(self):
        return self.customerId
    
    def setCustomer(self,customerId):
        self.customerId=customerId

    def getAccountNo(self):
        return self.accountNo
    
    def setAccountNo(self,accountNo):
        self.accountNo=accountNo

    def getBalance(self):
        return self.balance
    
    def setBalance(self,balance):
        self.balance=balance
        


