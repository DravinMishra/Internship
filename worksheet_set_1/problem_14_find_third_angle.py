#Write a Python program to get the third side of right-angled triangle from two given side

# angle_1 = 90
# angle_2 = int(input("Enter a angle : "))
# if angle_2 <= 0 :
#     print("enter angle between 0 to 90")
# elif angle_2 >= 90 :
#     print("Enter a angle less than 90")
# else :
#     angle_3 = 180 - (angle_1+angle_2)
#     print(angle_3)

angle_1 = 90
def angle(angle_2):
    if angle_2 <= 0:
        return "Enter an angle between 0 to 90"
    elif angle_2 >= 90:
        return "Enter an angle less than 90"
    else:
        angle_3 = 180 - (angle_1 + angle_2)
        return angle_3
n = int(input("Enter an angle: "))
result = angle(n)
print(result)