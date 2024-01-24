def case_counter():
    text=input("Enter text:  ")
    uppercase_letters=0; lowercase_letters=0
    for character in text:
      if character.isupper():
        uppercase_letters += 1
      elif character.islower():
        lowercase_letters += 1
      else:   
        uppercase_letters + 0, lowercase_letters + 0  
    print(f"uppercase letters: {uppercase_letters}, lowercase letters: {lowercase_letters}.")
    
case_counter()