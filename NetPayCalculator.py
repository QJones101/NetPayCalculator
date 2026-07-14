# Put how much you make an hour and per minute
pay_hourly = 17.31
pay_minutes = 0.29

# Self explanitory just say how many hours and minutes you worked for Week 1
workhours = int(input("Enter Hours Worked Week 1: "))


workminutes = int(input("Enter Minutes Worked Week 1: "))


# Here is where the calculation combining your input with your pay
week1_total_hour_pay = workhours * pay_hourly
week1_total_minute_pay = workminutes * pay_minutes
week1_total_pay = week1_total_hour_pay + week1_total_minute_pay

print(f"{workhours}:{workminutes}")

# This is the same thing as above just this will take into account of Week 2 of your hours and minutes
workhours = int(input("Enter Hours Worked Week 2: "))


workminutes = int(input("Enter Minutes Worked Week 2: "))


week2_total_hour_pay = workhours * pay_hourly
week2_total_minute_pay = workminutes * pay_minutes
week2_total_pay = week2_total_hour_pay + week2_total_minute_pay

print(f"{workhours}:{workminutes}")

print(f"-" * 40)
print(f"Total Pay is: ${round(week1_total_pay + week2_total_pay, 2)}")


# This is a function to calculate your gross pay into your take home pay by using the gross amount of money you got from the previous script
def netpaycalculator(gross_pay):

    #This factors in employee taxes however fed_with(federal withholding) taxes differ by how much you make a year
    pre_tax = 6.19
    post_tax = 2.20
    tax_rate = (0.062,0.0145,0.10)
    oasdi,medicare,fed_with = tax_rate
    taxable_wages = gross_pay - pre_tax

    oasdi_dollar = taxable_wages * oasdi
    medicare_dollar = taxable_wages * medicare
    fed_withold_dollar = taxable_wages * fed_with

    annualized_income = taxable_wages * 26

#This is where you change your annual income so federal withholding changes
    if annualized_income > 16100:
        fed_withold_dollar = ((annualized_income - 16100) * 0.10) / 26
    else:
        fed_withold_dollar = 0.0


    employee_taxes = oasdi_dollar + medicare_dollar + fed_withold_dollar


    net_pay = taxable_wages - employee_taxes - post_tax


    return round(net_pay, 2)

#The rest is self explanitory

print(f"-" * 40)
user_input = input("What is your gross salary going to be: $")
user_input_float = float(user_input)

print(f"-" * 40)
print(f"your take home check will be ${netpaycalculator(user_input_float)}")
print(f"-" * 40)