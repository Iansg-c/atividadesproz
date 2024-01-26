#função da calculadora
def calculadora():
 
 num1 = float(input("Digite o primeiro número: "))
 num2 = float(input("Digite o segundo número: "))
 operacao = float(input("Escolha a operação: "))

 if operacao == 1:
   return num1 + num2
  
 if operacao == 2:
    return num1 - num2
  
 if operacao == 3:
    return num1 * num2
  
 if operacao == 4:
    if num2 != 0:
      return num1 / num2
    else:
     return "Não é possível dividir por zero" 

#lista de comandos      
comandos = ["Confira a lista de comandos: ","Soma = 1 ","Subtração = 2","Multiplicação = 3 ","Divisão = 4","Sair da calculadora = 0"]
for i in comandos:
  print(i)

#.
resultado = calculadora()
print(f"O resultado é: {resultado}")

#loop da opção de sair
sair = int(input("Digite qualquer número diferente de 0 para continuar: "))
while sair != 0: 
  resultado = calculadora()
  print(f"O resultado é: {resultado}")
  sair = int(input("Digite qualquer número diferente de 0 para continuar: "))