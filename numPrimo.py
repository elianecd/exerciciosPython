flag = False
num = int(input("Digite um número: \n"))

while flag == False:
    if num <= 2:
        num = int(input("Número inválido. Digite novamente: \n"))
    else:
        flag = True
        break

maior_primo = 0

for i in range(num - 1, 1, -1):
    is_primo = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_primo = False
            break
    if is_primo:
        maior_primo = i
        break

if maior_primo:
    print(f"O maior número primo menor que {num} é {maior_primo}.")
else:
    print(f"Não há números primos menores que {num}.")
