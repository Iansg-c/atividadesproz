def calculadora():
    
    if operacao == "+":
       resultado = num1 + num2
       return resultado
    
    elif operacao == "-":
       resultado = num1 - num2
       return resultado
       
    elif operacao == "*":
       resultado = num1 * num2
       return resultado
    
    elif operacao == "/":
       if num2 != 0:
        resultado = num1 / num2
        return resultado
       else:  
        return "erro, não é possível dividir por zero"
       
num1 = float(input("digite o primeiro número: "))
num2 = float(input("digite o segundo número: "))
operacao = str(input("escolha a operação (+ , - , / , *): "))


resultado = calculadora()
print(f"o resultado é: {resultado}")

    