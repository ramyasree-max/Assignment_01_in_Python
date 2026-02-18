AnnualSalary = float(input("Enter the starting salary: "))

TotalCost = 1000000
SemiAnnualRaise = 0.07
r = 0.04
PortionDownPayment = 0.25
DownPayment = TotalCost * PortionDownPayment
months = 36

low = 0
high = 10000
steps = 0
BestRate = None

# check if possible with 100% savings
CurrentSavings = 0
Salary = AnnualSalary

for m in range(1, months + 1):
    CurrentSavings += CurrentSavings * (r / 12)
    CurrentSavings += (Salary / 12)
    if m % 6 == 0:
        Salary += Salary * SemiAnnualRaise

if CurrentSavings < DownPayment - 100:
    print("It is not possible to pay  down payment with in three years.")
else:
    while True:
        steps += 1
        rate = (low + high) // 2
        PortionSaved = rate / 10000

        CurrentSavings = 0
        Salary = AnnualSalary

        for m in range(1, months + 1):
            CurrentSavings += CurrentSavings * (r / 12)
            CurrentSavings += (Salary / 12) * PortionSaved
            if m % 6 == 0:
                Salary += Salary * SemiAnnualRaise

        if abs(CurrentSavings - DownPayment) <= 100:
            BestRate = PortionSaved
            break
        elif CurrentSavings < DownPayment:
            low = rate
        else:
            high = rate

    print("Best savings rate:", round(best_rate, 4))

    print("Steps in bisection search:", steps)
