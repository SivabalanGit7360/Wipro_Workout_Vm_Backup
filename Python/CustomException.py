
class BelowMinimumBalance(Exception):
    def __init__(self):
        self.msg = "Withdrawing below minimum balance"
    def __str__(self):
        return self.msg
    
class BankAccount:
    def __init__(self,number,curbal,minbal):
        self.number = number
        self.curbal = curbal
        self.minbal = minbal
        
    def withdraw(self,amount):
        curbal = self.curbal
        self.curbal -= amount
        if self.curbal < self.minbal:
            self.curbal = curbal
            raise BelowMinimumBalance
        return self.curbal
 
try:   
    ba = BankAccount(41356,1000,500)
    ba.withdraw(2000)
except BelowMinimumBalance as e:
    print(e)