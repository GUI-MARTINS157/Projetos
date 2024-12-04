def main()

modelo ={
    "Toyota":{
        "modelo":"Corolla",
        "ano":"2016",
        "motor":"2.0",
        "potência":"154 CV",
        "Fipe":"R$82.409",
    },
        "Honda":{
        "modelo":"Civic",
        "ano":"2013",
        "motor":"1.8",
        "potência":"140 CV",
        "Fipe":"R$62.456",
    },
        "Ford":{
        "modelo":"Ka",
        "ano":"2019",
        "motor":"1.5",
        "potência":"136 CV",
        "Fipe":"R$49.894",
    },
        "Chevrolet":{
        "modelo":"Onix",
        "ano":"2015",
        "motor":"1.4",
        "potência":"106 CV",
        "Fipe":"R$45.204",
    },
        "Volkswagen":{
        "modelo":"Gol",
        "ano":"1994",
        "motor":"2.0 ",
        "potência":"1O9 CV",
        "Fipe":"R$25.193",
    }
}

print("Bem vindo á a descrição dos modelos mais vendidos do Brasil:")

while True:
    carro = input("informe qual a seguinte marca(EX: Volksvagem-Ford-Chevrolet-Honda-Toyota):")

    if carro in modelo:
        print(f"\nMais vendido da marca{modelo}:")
        print(f"ano:{carro[modelo]['ano']}")
        print(f"motor:{carro[modelo]['motor']}")
        print(f"potência:{carro[modelo]['potência']}")
        print(f"Fipe:{carro[modelo]['Fipe']}")

        else:
            print("\nFalha ao achar o modelo, escreva novamente a marca certa.")

        continuar = input("\nRecomeçar (sim/não): "). lower()

        if continuar == ["sim", "ss", "s"]:
            print("\nRecomeçando..\n")
            retrurn




main()