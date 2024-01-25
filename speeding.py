def speeding_ticket():
    while True:
     speed=float(input("Enter your speed:  "))
     is_birthday=bool(input("Is toaday your birthday? (True or False):  "))

     if is_birthday is True:
        speed=speed - 5

     if speed <= 60:
        print("No ticket")
     elif speed > 80:
        print("Big ticket")
     elif speed>60 and speed<=80:
        print("Small ticket")
     else:
        print("invalid input")
        break
speeding_ticket()


