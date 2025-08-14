#creating a function
def fib(n):
    if(n==0 or n==1):
        return(n)
    return(fib(n-2) + fib(n-1))          #recursive base case

#printing the fibonacci series till 10
for i in range (10):
    print(fib(i) , end=" ")