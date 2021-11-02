nth = int(input("Enter the number u want"))

n1 , n2 = 0 , 1
count = 0

if nth < 0:
    print("Please enter the positive number")
elif nth == 1:
    print("The fibonace of 1 is ", nth)
else:
    while count < nth:
        print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        count += 1