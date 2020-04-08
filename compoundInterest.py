# Calculate the compound interest 

def compound_interest(principle, rate, time, frequency):
    result = principle * (pow((1 + rate), 24*time))
    return result
 
 
p = float(input("Enter the principal amount: "))
r = float(input("Enter the interest rate: "))/100
t = float(input("Enter the days: "))
n = float(input("Enter the frequency: "))

 
amount = compound_interest(p, r, t, n)
interest = ((amount - p)/p)*100
print("Compound amount is %.2f" % amount)
print("Applied interest rate is  %.2f " % interest )

