from BusinessLayer.accountService import AccountService
from BusinessLayer.transactionSerive import TransactionSerive
from Database.bank import accounts,customers

accountService=AccountService()
transactionService = TransactionSerive()
accountService.addAccount('ankita','1234567890')

accountService.addAccount('gaurav','9456661610')

print(len(accounts),len(customers))

transactionService.addMoney('ank1234567890',700)
transactionService.withdrawl('ank1234567890',100)
transactionService.checkBalance('ank1234567890')
transactionService.transferMoney('ank1234567890','gau456661610',1000)
transactionService.checkBalance('ank1234567890')
transactionService.checkBalance('gau9456661610')

#changes




