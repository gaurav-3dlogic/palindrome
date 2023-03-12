string = input("Enter a string: ")
string_1 = ""

for i in string:
    string_1 = i + string_1  
     
if(string_1 == string):
    print("String is palindrome")
else:
    print("String os not palindrome")