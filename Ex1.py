import math

Repeticao = 1

while Repeticao > 0 :

    peso = int(input("Digite seu peso: "))
    altura = float(input("Digite sua Altura: "))

    print(f"Digite seu peso (kg): {peso}")
    print(f"Digite sua altura (m): {altura}")
    Repeticao = Repeticao - 1

    imc = round(peso / (altura**2),1)
    if (altura <= 0 or peso <= 0) :
        print("Seu peso ou altura são inválidos")
    else :
        if(imc < 16.0) :
            print(f"Seu IMC é  {imc} - Baixo peso muito grave")
        elif (16.0 <= imc <= 16.9) :
            print(f"Seu IMC é  {imc} - Baixo peso grave")
        elif (17.0 <= imc <= 18.4) :
            print(f"Seu IMC é  {imc} - Baixo peso leve")
        elif (18.5 <= imc <= 24.9 ) :
            print(f"Seu IMC é  {imc} - Peso normal")
        elif (25.0 <= imc <= 29.9 ) :
            print(f"Seu IMC é  {imc} - Sobrepeso")
        elif (30.0 <= imc <= 34.9 ) :
            print(f"Seu IMC é  {imc} - Obesidade Grau I")
        elif (35.0 <= imc <= 39.9 ) :
            print(f"Seu IMC é  {imc} - Obesidade Grau II")
        elif (imc > 40.0 ) :
            print(f"Seu IMC é  {imc} - Obesidade Grau III")

        

        while True :
            Repetir  = input("Deseja calcular o IMC de outra pessoa? (S/N) :")

            if(Repetir == "S") :
                Repeticao = Repeticao + 1
                break
            elif (Repetir == "N") :
                Repeticao = 0
                print("Encerrando Calculadora...")
                break
            else : 
                print("Opção inválida! Digite apenas S para Sim ou N para Não.")
