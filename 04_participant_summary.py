full_name = input("Please enter your full name:")
staff_number = input("Please enter your staff number:")
level = int(input("Please enter your post level:"))

if full_name=="":
    print("Full Name field cannot be left empty!")
elif staff_number.isdigit()==False:
    print("Staff Number must be a numeric value!")
else:
    full_name = full_name.strip().title()
    parts = full_name.split()
    name = parts[0]
    surname = parts[1]
    print("")
    print("******Staff Member Details:******")
   
    print(f"Name: ",f"{name}")
    print(f"Surname: ", f"{surname}")
    print(f"Staff Number: ",f"{staff_number}")
    print(f"Post Level: ",f"{level}")