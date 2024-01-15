#write a program to find a number is composite number or not 


def checking_for_prime(num):
    if num <= 1:
        return "Invalid input. Please enter a number greater than 1."
    elif num == 2:
        return "2 is Prime Number"
    else:
        for i in range(2, num):
            if num % i == 0:
                return "Composite"
        return "Prime"

number = int(input("Enter a number: "))
print(checking_for_prime(number))



# def calculate_factors(n):
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             factors.append(i)
#     if n > 1:
#         factors.append(n)
#     return factors

# n = int(input("Enter a number: "))

# factors = calculate_factors(n)

# if len(factors) > 1:
#     print("The given number is a composite number.")
# else:
#     print("Given input  is a prime number.")