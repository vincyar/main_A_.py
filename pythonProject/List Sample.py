name = []
n = int(input("Enter a limit"))
print("Enter values")
for i in range(n):
    Torque = input()
    name.append(Torque)
print()
for j in name:
    print(j)
obj = {"place": "Malappuram",
       "name": "Sree Shabareesh"}
print(obj.get("name"))
