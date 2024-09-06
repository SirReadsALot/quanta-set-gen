n =int(input("Enter PQ num: "))
l = []
ml = []
sp = [0.5, -0.5]
Q = []
spF = 0

for i in range(0, n):
    l.append(i)
    
for j in range(-l[-1], l[0]): 
    ml.append(j)
k = sorted(l, reverse=True)
ml = ml + k
ml = sorted(ml)

print("AQ numbers:", l, "\n")
print("MQ numbers:", ml, "\n")

for u in range(len(l)):
    if u%2 == 0:
        Q.append([n, l[0], ml[0], sp[0]])
        l.pop(0)
        ml.pop(0)
    else:
        Q.append([n, l[0], ml[0], sp[1]])
        l.pop(0)
        ml.pop(0)

print("Number sets:", Q)

