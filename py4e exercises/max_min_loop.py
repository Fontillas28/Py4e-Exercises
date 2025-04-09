#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
#Once 'done' is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below.
#
#Invalid input
#Maximum is 10
#Minimum is 2


#markers
max_num = None
min_num = None


#loop
while True:
    num = input('Enter a Number: ')
    if num == 'done':
        break
    try:
        num = int(num)
        if max_num is None or num > max_num:
            max_num = num
        if min_num is None or num < min_num:
            min_num = num
    except:
        print('Invalid input')
        continue


#final output
print('Maximum is', max_num)
print('Minimum is', min_num)