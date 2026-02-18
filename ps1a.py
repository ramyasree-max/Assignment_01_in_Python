#Inputs required
AnnualSalary=int(input("Enter your annual salary : "))
PortionSaved=float(input("Enter monthly saving rate : "))
TotalCost=int(input("Enter total cost of dream house : "))

PostionOfDownPayment=0.25
AnnualReturn=0.04

#Initial values
CurrentSavings=0
MonthlySalary=AnnualSalary/12
DownPayment=TotalCost*PostionOfDownPayment
months=0

#By using while loop
while CurrentSavings<down_payment:
      CurrentSavings+=CurrentSavings*(annual_return/12)
      CurrentSavings+=MonthlySalary*PortionSaved
      months+=1
      
#No.of months required

print(f"Number of months : {months}")
