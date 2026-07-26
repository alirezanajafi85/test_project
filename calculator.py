def user_input():
    user_inpt=input("pleas enter number for calculator : ")
    listing(user_inpt)
    
    
def listing(an_string):
    user_list=an_string.split(" ")
    proccess(user_list)
    
    print(user_list)

def proccess(a_list):
    if a_list[1] == "+":
        
        a_list[0] = int(a_list[0])
        a_list[2] = int(a_list[2])
        
        javab=a_list[0] + a_list[2]
        
    elif a_list[1] == "-":
        
        a_list[0] = int(a_list[0])
        a_list[2] = int(a_list[2])
        
        javab=a_list[0] - a_list[2]
        
        
    elif a_list[1] == "*":
        
        a_list[0] = int(a_list[0])
        a_list[2] = int(a_list[2])
        
        javab=a_list[0] * a_list[2]
            
        
    print(javab)   
        
        
        
        
        
        
        
        
        
        
user_input()