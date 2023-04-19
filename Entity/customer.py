class Customer:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.customerId=None
        
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name=name

    def getPhone(self):
        return self.phone
    
    def setPhone(self,phone):
        self.phone=phone

    def getCustomerId(self)->str:
        return self.customerId
    
    def setCustomerId(self,customerId:str):
        self.customerId=customerId