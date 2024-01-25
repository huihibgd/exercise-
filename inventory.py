inventory={}
def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item]=quantity
    print(f"Add {quantity} {item}s to the inventory ")    
  
def view_inventory():
   for item, quantity in inventory.items():
      print(f"{item} : {quantity}")

def update_item(item, quantity):
   if item in inventory:
      inventory[item]=quantity
      print(f"{item} is updated to {quantity}")
   else:
      print("item is not found in the inventory")  

def manage_inventory():
    while True:
      print("Inventory Management System")
      print("1.Add Item")
      print("2.View Inventory")
      print("3.Update Item Quantity")
      print("4.Exit")
      choice=input("Enter your choice(1/2/3/4):  ")
      
      if choice == '1':
       item=input("Enter item: ")
       quantity=input("Enter quantity:  ")
       add_item(item, quantity)
      elif choice == '2':
       view_inventory()
      elif choice == '3':
       item=input("Enter item: ")
       quantity=input("Enter quantity:  ")
       update_item(item, quantity)
      elif choice== '4':
       print("Exit inventory management system") 
       break     
      else:
       print("Invalid choice, please choose again") 
 


manage_inventory()
          

          






