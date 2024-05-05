n = int(input("Enter a limit that you want to print till it"))
num = int(input("Which number multiplication you want"))

for i in range(1, n):
    result = i * num
    print(str(i)+" x "+str(num)+" = "+str(result))
