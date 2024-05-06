selection = input("Enter a number to divide 10 with the number")
choice = selection.isdigit()
if str(choice):
    print("Enter a int value")
try:
      selection = int(selection)
      result = 10 / selection
      print("Result is : " + str(result))
except ZeroDivisionError:
      print("Zero cannot divide 10")
except NameError:
      print("Enter a intiger value")

print("Programme completed")
print(choice)