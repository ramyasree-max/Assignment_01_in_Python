#Inputs as per we required
annual_salary=int(input("Enter your annual salary : "))
portion_saved=float(input("Enter monthly saving rate : "))
total_cost=int(input("Enter total cost of dream house : "))

#Constants given in assignment
postion_of_down_payment=0.25
annual_return=0.04

#Initial values
current_savings=0
monthly_salary=annual_salary/12
down_payment=total_cost*postion_of_down_payment
months=0

#Loops
while current_savings<down_payment:
      current_savings+=current_savings*(annual_return/12)
      current_savings+=monthly_salary*portion_saved
      months+=1
      
#Output to show the no.of months
print(f"Number of months : {months}")