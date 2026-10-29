text = input("Enter a string: ")

reverse = text[::-1]

print("Original String:", text)
print("Reverse String:", reverse)

if text == reverse:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")

print("Program executed successfully")