
import random

user_input= input("enter 3 number examble(1,2,3) : ")

user_input_list =user_input.split(",")
system_choises=random.choice(user_input_list)

print(type(system_choises))

user_input_p2=input("please enter a number : ")

if user_input_p2==system_choises:
    print("you win")
    
else:
    print("you lose ")