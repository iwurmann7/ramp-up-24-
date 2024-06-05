def oddeven(n):
    n = int(n)
    if n%2==0:
        print("The given number is even")
    elif n%2==1:
        print("The given number is odd")
    else:
        print("Error")
oddeven(input("Enter a number: "))

