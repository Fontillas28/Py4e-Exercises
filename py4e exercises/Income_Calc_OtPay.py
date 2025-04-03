# Gather inputs
hrs = input('Enter Hours Worked: ')
rate = input('Enter Hourly Pay: ')

# Calculates Gross Income With 1.5x Pay for More Than 40 Hours
if float(hrs) > 40:
    pay = (40 * float(rate)) + (((float(hrs) - 40)) * (float(rate) * 1.5))
else:
    pay = float(hrs) * float(rate)

# Display Income
print('Pay:', pay)