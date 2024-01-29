def mostrar():
   nome = str(input("Digite seu nome: "))
  
   try:
     nascimento = int(input("Digite seu ano de nascimento: "))
     if nascimento >= 1922 and nascimento < 2022:
       idade = 2022 - nascimento  
       print(nome + ",", f"sua idade é {idade}")
    
     else: 
      print("Dados inválidos, tente novamente")
      return mostrar()
   
   except Exception as erro:
     print("Dados inválidos, tente novamente")
     print(erro)
     return mostrar()
    
idade = mostrar()