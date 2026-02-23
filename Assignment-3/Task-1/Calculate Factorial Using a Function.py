num=int(input("Enter the number to calculate factorial: "))
def fact_rec(num):
    if num ==1  or num ==0:
        return 1
   
    else:
        factorial=num * fact_rec(num-1)
        return factorial
print(fact_rec(num))