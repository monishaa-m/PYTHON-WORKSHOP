def factorial(n): 
    if n == 0 or n == 1: 
        return 1 
    else: 
        return n * factorial(n-1) 
 
num = int(input("Enter a number: ")) 
 
if num < 0: 
    print("Factorial of negative numbers does not exist.") 
elif num == 0: 
    print("Factorial of 0 is 1.") 
else: 
    print("Factorial of", num, "is", factorial(num)) 
