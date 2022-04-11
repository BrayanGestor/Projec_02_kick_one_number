#importar biblioteca random 
import random

#seta variável
acertou = False

#laço de repetição com variável 
while acertou == False:
  #seta valor aleatorio
  valor_aleatorio = random.randint(1,10)
  
  #recebe valor chute
  valor_chute = int(input("Digite um número de 1 a 10? "))

  #condicona possíveis resultados
  if valor_aleatorio < valor_chute:
    print("Lamento, você chutou acima do valor correto!")
    
  elif valor_aleatorio > valor_chute:
    print("Lamento, você chutou abaixo do valor correto!")
    
  elif valor_aleatorio == valor_chute:
    print("Parabéns, você acertou!!!")
    acertou = True
    
    print("O valor correto é ",valor_aleatorio)