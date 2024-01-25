
def media_aluno ():
    num1 = float(input("digite sua primeira nota: "))
    num2 = float(input("digite sua segunda nota: "))
    num3 = float(input("digite sua terceira nota: "))
    media = (num1 + num2 + num3) / 3
    return media


resultado = media_aluno()
print(f"seu resultado é: {resultado}")
