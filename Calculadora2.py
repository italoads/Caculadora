# testando def

ValorInicial = 0
NovoValor = 0
Funcao = 0
SimNao = 0
Resultado = 0


ValorInicial = float(input("1º Valor: "))
print("escolha uma opção     [1] Somar [2] Subtrair [3] Dividir [4] Multiplicar [5] Porcentagem [6] Raiz Quadrada:")
Funcao = int(input("Função: "))                     
NovoValor = float(input("2º Valor: "))

def calcular (ValorInicial, NovoValor):
    Resultado = 0
    if Funcao == 1:
        Resultado = float(ValorInicial + NovoValor)
        print("A soma dos valores é" +" "+ str( Resultado))
    
    elif Funcao == 2:
        Resultado = float(ValorInicial - NovoValor)
        print("A subtração dos valores é" +" "+ str( Resultado))
    
    elif Funcao == 3 and NovoValor == 0:
        print("Impossível fazer divisão por 0")
    
    elif Funcao == 3:
        Resultado = float(ValorInicial / NovoValor)
        print("A divisão dos valores é" +" "+ str( Resultado))
    elif Funcao == 4:
        Resultado = float(ValorInicial * NovoValor)
        print("A multiplicação dos valores é" +" "+ str( Resultado))
    elif Funcao == 5:
        Resultado = float(ValorInicial / (NovoValor*NovoValor)
    else:
        print("Erro")
        return ValorInicial
    return Resultado

calcular(ValorInicial, NovoValor)

SimNao = input("Continuar? [s] ou [n]: ")
while SimNao.lower() == "s":
    print("escolha uma opção     [1] Somar [2] Subtrair [3] Dividir [4] Multiplicar:      ")
    Funcao = int(input("Função: "))                     
    NovoValor = float(input("2º Valor: "))
    calcular(ValorInicial, NovoValor)
    SimNao = input("Continuar?: ")

print("Obrigado por testar minha calculadora :)")