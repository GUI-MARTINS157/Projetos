def main():
    n = pegar_numero()
    tamanho(n)

def tamanho(n):
    for _ in range(n):
        print("#"*n)

def pegar_numero():
    while True:
        n = int(input("qual o tamanho do coluna? "))
        if n > 0:
            return n 
main()