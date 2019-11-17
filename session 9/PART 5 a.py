d = ["ST", "BĐ", "BTL", "CG", "ĐĐ", "HBT"]
p = [150300, 247100, 333300, 266800, 420900, 318000]

maximum = 0
for y in p:
    if maximum < y:
        maximum = y
    else:
        pass
   
for i,x in enumerate(p):
    if x == maximum:
        print("districk " + d[i] + " highest population")
    else:
        pass

minimum = p[0]
for a in p:
    if minimum > a:
        minimum = a
    else:
        pass
    
for b,c in enumerate(p):
    if c == minimum:
        print("distrik " + d[b] + "smallest population")
    else:
        pass
