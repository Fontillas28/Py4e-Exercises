#Write a program which repeatedly reads integers until the user enters “done”. 
#Once “done” is entered, print out the total, count, and average of the integers.
#If the user enters anything other than a integers, detect their mistake using try and except and print an error message and skip to the next integers.

#Markers
total = 0
count = 0

#Loop
while True:
    inp_num = input('Enter Integer: ')
    if inp_num == 'done':
        break
    try:
        inp_num = int(inp_num)
        total = inp_num + total
        count = count + 1
        average = total/count
    except:
        print('Invalid Input')
        continue


#Print final statement
print('Total:', total, 'Count:', count, 'Average:', average)