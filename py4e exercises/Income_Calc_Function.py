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

#Define function to compute pay with overtime included
def computepay(time, money):
    if time > 40:
        return (40 * money) + ((time - 40) * (money *1.5))
    else:
        return time * money

# Display Income
print('Pay:', computepay(hrs, rate))
