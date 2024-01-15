#Write a python program to check whether a given string is palindrome or not
strng = input("Enter a string : ")

#Remove all the whitespaces 
strng_without_whitespaces = strng.replace(" " , "") 

#convert it to the lowercase
lower_strng = strng_without_whitespaces.lower()

#reversed lower strng by using slicing
reversed_lower_strng = lower_strng[::-1]

if lower_strng == reversed_lower_strng :
    print(f"The given input {'strng'} is a palindrome ")
else :
    print(f"The given input {'strng'} is not a palindrome ")