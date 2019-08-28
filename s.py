deposit_sum =    int(input("deposit sum:"))
interest_rate =  float(input("interest rate in %:"))
tax_rate =       float(input("tax in %:"))
months =         int(input("nuber of months:"))

interest = deposit_sum * (interest_rate/100) * (months/12)
taxes = interest * (tax_rate/100)
interest_after_tax = interest - taxes
total_account = deposit_sum + interest_after_tax

print("Deposit: " + str(deposit_sum))
print("Interest rate: " + str(interest_rate) + "%")
print("Period of deposit: " + str(interest_rate) + " months")
print("Interest: " + str(interest_after_tax))
print("Total account after " + str(months) + " months: " + str(total_account))
