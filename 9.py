n = int(input("tedad: "))
x = int(input("adad: "))

for i in range(n):
    if x % 2 == 0:
        x = x // 2
    else:
        x = (x * 2)-1
    
print(x)