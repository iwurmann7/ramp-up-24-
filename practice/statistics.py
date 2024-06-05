def addition(numbers):
    temp = 0    
    for n in numbers:
        temp += n
    return temp   


def statistics(numbers):
    print("Maximum value:", max(numbers))
    print("Minimum value:", min(numbers))
    print("Sum of all numbers:", addition(numbers))
    print("Average of all numbers:", (addition(numbers))//len(numbers))

def list_of_numbers():
    input_string = input("Enter a list of numbers separated by spaces: ")
        # Convert the list of strings to a list of integers
    number_list = [int(num) for num in input_string.split()]
    return number_list
numbers = list_of_numbers()
statistics(numbers)



 
