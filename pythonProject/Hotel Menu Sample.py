print("Hi, Sir")
print("We have a lots of dishes include Pizza , Burger , Masala Dosha and Chilli Chicken etc ")
dish = input("What do you want?")
dish[0].upper()
if dish == "Pizza":
    print("You have ordered Pizza, Please wait")
elif dish == "Burger":
    print("You have ordered Burger, Please wait")
elif dish == "Masala Dosha":
    print("You have ordered Masala Dosha, Please wait")
elif dish == "Chilli Chicken":
    print("You have ordered Chilli Chicken, Please wait")
else:
    print("Please choose items that on list")
