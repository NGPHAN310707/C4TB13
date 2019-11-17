a = [49, 100, 33, 89, 41]
b = sorted(a,reverse=True)

print("Highest score:")
for i, x in enumerate(b):
    print(i+1,x,sep=".")

for y in range(len(b)):
    if y < len(b)-1:
        pass
    else:
        c = int(input("Enter your new high-score: "))
        for i, x in enumerate(b):
            print(i+1,x,sep=".")
        print(y+2,c,sep=".")
