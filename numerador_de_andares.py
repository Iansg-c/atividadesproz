#NUMERAÇÃO DOS ANDARES COM FOR
print("Numeração dos andares com for: ")

for i in range(1,21):
    if i != 13:
        print(f"{i}º andar")

#NUMERAÇÃO DOS ANDARES COM WHILE
print("Numeração dos andares com while: ")       
andar = 1
  
while (andar < 21):
  if andar != 13:
     print(f"{andar}º andar")
  andar = andar + 1

#NUMERAÇÃO DOS ANDARES UTILIZANDO WHILE EM ORDEM DECRESCENTE
print("Numeração dos andares utilizando while em ordem decrescente: ")       
andar = 1

andar = 20
while andar > 0:
   if andar != 13:
      print(f"{andar}º andar")
   andar = andar - 1

#NUMERAÇÃO DOS ANDARES EM ORDEM DECRESCENTE UTILIZANDO FOR
print("Numeração dos andares utilizando for em ordem decrescente: ")  

for i in range(20,0,-1):
   if i != 13:
      print(f"{i}º andar")

