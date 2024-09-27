num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even number...")
else:
    print(f"{num} is odd number...")




def palindrome(string):
    temp = ''
    for i in string:
        temp = i + temp

    if string == temp:
        return "palindrome"
    else:
        return "not palindrome"
    


string = input("Enter a string: ")
print(palindrome(string))



def sqrt(number):
    return number ** 2 ,number **3
    
number = int(input("enter a number"))

print(sqrt(number))



def greet():
    print("Hello good a how are you...")


greet()