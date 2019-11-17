x = ["ST", "BĐ", "BTL", "CG", "ĐĐ", "HBT"]
y = [150300, 247100, 333300, 266800, 420900, 318000]

# maximum
#print("max: " + str(max(p)))
#print("min: " + str(min(p)))

# maximum
maximum = 0
for i in y:
    if maximum < i:
        maximum = i
    else:
        pass
print("max: " + str(maximum))

# minimum
minimum = y[0]
for x in y:
    if minimum > x:
        minimum = x
    else:
        pass
print("min: " + str(minimum))
