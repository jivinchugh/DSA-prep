'''
Today, we will be writing and analyzing two different recursive
cases in both space and time complexity:

1 - Factorial (not to be confused with factorial time)

Where n! = n*(n-1)*(n-2)*…*1, and 0! = 1 by definition.

2 - Power

Where n^m = n * (n ^ m-1), anything to the power of 0 is 1

'''
#1 Factorial Function 
print("FACTORIAL OF 5:")
def Factorial(n):
    if n==1:
        return 1
    else:
        return n * Factorial(n-1)
    
print(Factorial(5))

#2POWER 
print ("POWER!!!!!")
def power(base,exp):
    if exp==0 and base==0:
        return "undefined"
    elif exp==0:
        return 1
    elif exp==1 or base == 1:
        return base
    elif base == 0:
        return 0
    elif exp < 0:
        return power(base, exp + 1)/base
    else:
        return base*power(base,exp-1)
#print(power(4,-2))
if __name__ == '__main__':
    print(power(4,-2))
