h = input("type your numbers, seperate them with 'space': ")
k = h.split(" ")

for i in range(len(k)):
    k[i] = int(k[i])

for x in k:
    if x % 2 == 0:
        print(x,sep=" ")
    else:
        pass
