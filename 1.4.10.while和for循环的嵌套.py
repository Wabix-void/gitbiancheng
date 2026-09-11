i = 1
while i < 10:
    j = 1
    while j <= i:
        print(f"{i}*{j}={i*j}\t",end='')
        j += 1
    i += 1
    print()


p = 1
for p in range(1,10):
    for q in range(1,p+1):
        print(f"{p}*{q}={p*q}\t",end='')
    print()
