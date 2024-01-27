def fibonacci_sequence(max_value):
 
 
  if max_value==0:
   fibonacci_sequence=[0]
   print(fibonacci_sequence)
  elif max_value>0:
   fibonacci_sequence=[0,1]
   while fibonacci_sequence[-1]+fibonacci_sequence[-2] <= max_value:
     fibonacci_sequence.append(fibonacci_sequence[-1]+fibonacci_sequence[-2])
   print(fibonacci_sequence) 
  else:
   print("Empty list")
fibonacci_sequence(10)