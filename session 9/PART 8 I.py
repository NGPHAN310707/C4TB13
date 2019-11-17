h = [49, 100, 33, 89, 41]
k = sorted(h,reverse=True)

print("Highest score:")
for i, x in enumerate(k):
    print(i+1,x,sep=".")
for y in range(len(k)):

    if y< len(k)-1:
        pass
                
    else:
        j= int(input("pls enter again:"))
        k.append(j)
l = sorted(k,reverse=True)
print("HC")
