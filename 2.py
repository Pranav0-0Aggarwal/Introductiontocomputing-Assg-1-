#taking input from user
gross_income=float(input("Enter your gross Income sir-$"))
Num_Dependants=int(input("Enter total number of Dependants-"))

#rounding of tax to pennies
gross_income=round(gross_income,2)

#Defnining some variable some required constant values
std_deduction=10000
dep_deduction=3000
tax=0

#calculating the taxable income
taxable_income=gross_income-std_deduction-dep_deduction*Num_Dependants

#Checking if the taxable income is greater than 0
if taxable_income>0:
    tax=0.20*taxable_income
else :
    tax=0
#printing the tax
print("Your tax = ",tax,sep="$")