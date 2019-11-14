
class User:
    def __init__(self, amount):
        self.amount =  amount
    
    def getamount(self):
        return self.__amount
    
    def setamount(self, amount):
        if amount > 10:
            raise ValueError("Montant trop faible")
        else:
            self.__amount = 100

    temperature = property(getamount,setamount)

try:
    a = User(2)
except  ValueError as err:
    print(err)
    
