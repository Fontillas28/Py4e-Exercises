# Gather inputs
hrs = input('Enter Hours Worked: ')

#Try & Except Clauses
try:
    hrs = float(hrs)
except:
    print('Error, please enter numeric value')
    quit()

#Gather inputs
rate = input('Enter Hourly Pay: ')

#Try & Except Clauses
try:
    rate = float(rate)
except:
    print('Error, please enter numeric value')
    quit()

# Calculates Gross Income With 1.5x Pay for More Than 40 Hours
if hrs > 40:
    pay = (40 * rate) + ((hrs - 40) * (rate * 1.5))
else:
    pay = hrs * rate

# Display Income
print('Pay:', pay)