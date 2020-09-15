# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  None

def factorial_calc(x): 
    total = 1
    for x in range(1, x+1):
        total = total * x
        
    return total

# be sure to return the factorial

if __name__=='__main__':
    x = int(input("Enter a number: "))
    print(factorial_calc(x))
