# This is a simple project of a restraunt menu. It is a simple project to calculate the total bill.
menu={
    "Veg Biryani": 150,
    "Chicken Biryani": 200,
    "Veg Noodles": 100,
    "sandwich": 50,
    "Pasta": 120,
    "Pizza": 250,
    "burger": 80,
}
print("Welcome to the 4SquareCode Restraunt")
print("Here is the menu:")
for item in menu:
    print(item, ":", menu[item])
order=input("Enter the items you want to order seperated by commas: ").split(",")
bill=0
for item in order:
    bill+=menu[item]
print("Your total bill is: ", bill)
# do you want anything else?
print("Do you want anything else?")
if input("Enter 'yes' or 'no': ")=="yes":
    print("Here is the menu:")
    for item in menu:
        print(item, ":", menu[item])
    order=input("Enter the items you want to order seperated by commas: ").split(",")
    for item in order:
        bill+=menu[item]
    print("Your total bill is: ", bill)
print("Here is the menu:")
for item in menu:
    print(item, ":", menu[item])
order=input("Enter the items you want to order seperated by commas: ").split(",")
print("Thank you for visiting us. Have a nice day!")