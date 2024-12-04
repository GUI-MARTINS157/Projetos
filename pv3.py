def main():
    modelo = {
        "Toyota": {
            "modelo": "Corolla",
            "ano": "2016",
            "motor": "2.0",
            "potência": "154 CV",
            "Fipe": "R$82.409",
        },
        "Honda": {
            "modelo": "Civic",
            "ano": "2013",
            "motor": "1.8",
            "potência": "140 CV",
            "Fipe": "R$62.456",
        },
        "Ford": {
            "modelo": "Ka",
            "ano": "2019",
            "motor": "1.5",
            "potência": "136 CV",
            "Fipe": "R$49.894",
        },
        "Chevrolet": {
            "modelo": "Onix",
            "ano": "2015",
            "motor": "1.4",
            "potência": "106 CV",
            "Fipe": "R$45.204",
        },
        "Volkswagen": {
            "modelo": "Gol",
            "ano": "1994",
            "motor": "2.0",
            "potência": "109 CV",
            "Fipe": "R$25.193",
        }
    }

    print("Bem-vindo à descrição dos modelos mais vendidos do Brasil:")

    while True:
        carro = input("Informe qual a seguinte marca (EX: Volkswagen, Ford, Chevrolet, Honda, Toyota): ").capitalize()

        if carro in modelo:
            print(f"\nMais vendido da marca {carro}:")
            print(f"Modelo: {modelo[carro]['modelo']}")
            print(f"Ano: {modelo[carro]['ano']}")
            print(f"Motor: {modelo[carro]['motor']}")
            print(f"Potência: {modelo[carro]['potência']}")
            print(f"Fipe: {modelo[carro]['Fipe']}")
        else:
            print("\nFalha ao achar o modelo, escreva novamente a marca certa.")

        continuar = input("\nRecomeçar (sim/não): ").lower()

        if continuar not in ['sim', 's']:
            print("\nSaindo... Até a próxima!")
            break
        else:
            print("\nRecomeçando...\n")

# Chama a função main
main()