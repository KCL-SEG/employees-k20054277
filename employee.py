"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contractType, contractLength, contractPay, bonusType, bonusCount, bonusPay):
        self.name = name
        self.contractType = contractType
        self.contractLength = contractLength
        self.contractPay = contractPay
        self.bonusType = bonusType
        self.bonusCount = bonusCount
        self.bonusPay = bonusPay

    def get_pay(self):
        totalPay = (self.contractLength * self.contractPay) + (self.bonusCount *self.bonusPay)
        return totalPay
  
    def __str__(self):
        tempExplenamtion = self.name
        if self.contractType == "monthly":
            tempExplenamtion = tempExplenamtion + " works on a monthly salary of " + str(self.contractPay) 
        else:
            tempExplenamtion = tempExplenamtion + " works on a contract of " + str(self.contractLength) +" at " + str(self.contractPay) + "/hr"
            
        if  self.bonusType == "contract":
            tempExplenamtion = tempExplenamtion + " and receives a commission for " + str(self.bonusCount) +" contract(s) at " + str(self.bonusPay) + "/contract"
        elif self.bonusType == "fixed":
            tempExplenamtion = tempExplenamtion + " and receives a bonus commission of " + str(self.bonusPay)

            
        tempExplenamtion = tempExplenamtion + ". their total pay is " + str(self.get_pay()) +"."
        return tempExplenamtion


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "monthly", 1, 4000, "none", 0, 0 )

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "hourly", 100, 25, "none", 0, 0 )

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "monthly", 1, 3000, "contract", 4, 200 )

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "hourly", 150, 25, "contract", 3, 220 )

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "monthly", 1, 2000, "fixed", 1, 1500 )

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "hourly", 120, 30, "fixed", 1, 600 )
