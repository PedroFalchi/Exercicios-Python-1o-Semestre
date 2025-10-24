a = 1
b = 1
c = -1


for i in range(20):
    r = a + b + c
    print(r)
    a = b
    b = c
    c = r