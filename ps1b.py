
# Part B - Saving with a Raise
#inputs required
AnnualSalary = float(input("Enter your annual salary: "))
PortionSaved = float(input("Enter the percent of your salary to save : "))
TotalCost = float(input("Enter the cost of your dream home: "))
SemiAnnualRaise = float(input("Enter the semi-annual raise : "))

PortionDownPayment = 0.25
DownPayment = TotalCost * PortionDownPayment

CurrenSavings = 0
r = 0.04
months = 0

while CurrentSavings < DownPayment:
    MonthlySalary = AnnualSalary / 12
    CurrentSavings += CurrentSavings * (r / 12)
    CurrentSavings += MonthlySalary * PortionSaved
    months += 1

    if months % 6 == 0:
        AnnualSalary += AnnualSalary * SemiAnnualRaise
# required output
print("Number of months:", months)

