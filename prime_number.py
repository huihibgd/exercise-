def is_prime(number):
    if number > 2:
      for i in range(2,number-1):
       if number%i==0:
         return False
       else:
         return True
    elif number == 2:
     return True
    else:
     return False
    
result=is_prime(1)  
if result:
    print("True") 
else:
    print("False")  
