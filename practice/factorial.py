def with_loop(n):
    temp = 1
    for i in range(1, n + 1):
        temp *= i
    return temp
def with_recursion(n):
    return 1 if n == 0 else n * with_recursion(n - 1)
n = int(input("Enter a number: "))
print (with_loop(n))
print (with_recursion(n))
