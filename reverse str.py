# string = "Try It"
import string

# new_string = string[::-1]

# print(new_string)


string=str(input("Enter the str"))
reverse=""
for i in range(len(string)):
    reverse = string[i]+reverse
print(reverse)