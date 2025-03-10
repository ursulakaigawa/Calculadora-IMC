def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    peso = float(input("Digite o peso em kg: "))
    altura = float(input("Digite a altura em metros: "))
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    print("O IMC é:", imc)
    print("Classificação:", classificacao)

if __name__ == "__main__":
    main()
