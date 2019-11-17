d = ["ST", "BĐ", "BTL", "CG", "ĐĐ", "HBT"]
p = [150300, 247100, 333300, 266800, 420900, 318000]
s = [11.743, 9.224, 43.35, 12.04, 9.96, 10.09]
density=[]

for i in range(len(d)):
    density.append(p[i] / s[i])
print(density)
