def main():
    print("---calcular expontecial🤑👸---")
    n = float(input("qual o número?"))
    result =formatar (calcula_quadrado(n))
    print(f"o quadrado de {n} é {result}")
    result =(calcula_cubo(n))
    print(f"o cubo de {n} é {result}")


def calcular_quadrado(n):
    return n * n
 
def calcular_quadrado(n):
    return n ** 3

def calcular_quadrado(n):
    n = f"{n:_.2f}"
    return n * n.replace(".", ",").replace("_", ".")


main()        