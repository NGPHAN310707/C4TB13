a = [49, 100, 33, 89, 41]
b = sorted(a,reverse=True)

for i, x in enumerate(b):
    print("HIGHEST SCORE:")
    print(i+1,x,sep=".")
