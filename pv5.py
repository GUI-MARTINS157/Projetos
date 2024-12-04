while True:
    p = int(input("Qual o tamanho da linha? "))
    if p > 0:
        break
    else:
        print("Por favor, insira um número maior que 0.")

print("?" * p)