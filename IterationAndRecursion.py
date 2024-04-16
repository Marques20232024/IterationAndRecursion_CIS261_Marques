def factorial_iterative(num):
    fact = 1
    for number in range(2, num+1):
        fact = number * fact
    return fact

def faactorial_recursive(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursive(num - 1)
    
def main():
    print("Factorial results using iterative function")
    print("0!", functorial_inerative(0))
    print("5!", functorial_inerative(5))
    print("10", functorial_inerative(10))
    print("25!", functorial_inerative(25))
    print("50!", functorial_inerative(50))
    print("100!", functorial_inerative(100))
    print("Funtorial results using recursive function")
    print("0!", functorial_recursive(0))
    print("5!", functorial_recursive(5))
    print("10", functorial_recursive(10))
    print("25!", functorial_recursive(25))
    print("50!", functorial_recursive(50))
    print("100!", functorial_recursive(100))
    
if __name__ == "__main__":
    main()
    
