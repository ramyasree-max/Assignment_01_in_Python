# ps1c.py

annual_salary = float(input("Enter the starting salary: "))

total_cost = 1000000
semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
months = 36

low = 0
high = 10000
steps = 0
best_rate = None

# check if possible with 100% savings
current_savings = 0
salary = annual_salary

for m in range(1, months + 1):
    current_savings += current_savings * (r / 12)
    current_savings += (salary / 12)
    if m % 6 == 0:
        salary += salary * semi_annual_raise

if current_savings < down_payment - 100:
    print("It is not possible to pay  down payment with in three years.")
else:
    while True:
        steps += 1
        rate = (low + high) // 2
        portion_saved = rate / 10000

        current_savings = 0
        salary = annual_salary

        for m in range(1, months + 1):
            current_savings += current_savings * (r / 12)
            current_savings += (salary / 12) * portion_saved
            if m % 6 == 0:
                salary += salary * semi_annual_raise

        if abs(current_savings - down_payment) <= 100:
            best_rate = portion_saved
            break
        elif current_savings < down_payment:
            low = rate
        else:
            high = rate

    print("Best savings rate:", round(best_rate, 4))
    print("Steps in bisection search:", steps)