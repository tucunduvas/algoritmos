
def fibo(n):
    if n<=1:
        return 1
    print(fibo(n-1))
    print(fibo(n-2))
    return (fibo(n-1) + fibo(n-2))
print(fibo(7))

