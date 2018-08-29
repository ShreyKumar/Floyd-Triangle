rows = input("Enter the number of rows for your Floyd Triangle: ")

count = 1

for i in range(1, rows+1):
    for j in range(i):
        print count,
        count += 1
    print("")
