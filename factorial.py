def calculate_factorial(number):
    result=1
    if number>0:
        for i in range(1,number+1):
            result=i*result
        print(result)
    elif number==0:
      print(1)    
    else:
        print("Error")
calculate_factorial(-1)