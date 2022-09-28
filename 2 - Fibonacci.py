n = int(input("Que número deseja consultar da sequência? "))

a = 0
b = 1
fibonacci = 0

for i in range(n):
    fibonacci = a + b
    a = b
    b = fibonacci
    
if n != fibonacci:
    print(f"O número {n} não pertence a sequência")
else:
    print(f"O número {n} pertence a sequência")
