# testando def
def calcular(v1, v2, operacao):
    if operacao == 1:
        res = v1 + v2
        print(f"A soma é: {res}")
    elif operacao == 2:
        res = v1 - v2
        print(f"A subtração é: {res}")
    elif operacao == 3:
        if v2 == 0:
            print("Erro: Divisão por zero!")
            return v1 
        res = v1 / v2
        print(f"A divisão é: {res}")
    elif operacao == 4:
        res = v1 * v2
        print(f"A multiplicação é: {res}")
    else:
        print("Opção inválida")
        return v1
    return res

# --- Começo ---
valor_acumulado = float(input("Digite o 1º valor: "))
continuar = 's'

while continuar.lower() == 's':
    print("\n[1] Somar [2] Subtrair [3] Dividir [4] Multiplicar")
    opcao = int(input("Escolha a função: "))
    proximo_valor = float(input("Digite o próximo valor: "))

    valor_acumulado = calcular(valor_acumulado, proximo_valor, opcao)
    
    print(f"Valor atual: {valor_acumulado}")
    
    continuar = input("\nDeseja realizar outra operação? [s/n]: ").lower()
    while continuar not in ('s', 'n'):
        continuar = input("Por favor, responda apenas [s] ou [n]: ").lower()

print("Obrigado por testar minha calculadora :)")