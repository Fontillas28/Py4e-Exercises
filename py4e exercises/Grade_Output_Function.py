#Gather grade input
score = input('Enter Score:')

#Try & Except
try:
    score = float(score)
except:
    print('Bad Score')
    quit()

#Define function for grade computation
def computegrade(grade):
    if grade >= 0.9 and grade <= 1.0:
        return print('A')
    elif grade >= 0.8 and grade < 0.9:
        return print('B')
    elif grade >= 0.7 and grade < 0.8:
        return print('C')
    elif grade >= 0.6 and grade < 0.7:
        return print('D')
    elif grade < 0.6 and grade >= 0:
        return print('F')
    else:
        return print('Bad Grade')
    
computegrade(score)
