#biblioteca de randomização importada
from random import randint

#variável do num do computador
num_pc = randint(1,10)

#variável input do num que o user digitou
num_user = int(input("Chute um número de 1 a 10: "))

#função para condicionar os números
def num(num_user, num_pc):
    if num_user < num_pc:
      return "Número escolhido é menor que do computador\nTente novamente!"
    
    elif num_user > num_pc:
      return "Número escolhido é maior que do computador\nTente novamente!" 
     
    else:
      return "Você acertou! Parabéns!"


resultado = num(num_user, num_pc)

#resultado para o usuário na tela
print(resultado)

#esse código não possui um loop no número, caso erre o número, será gerado um novo número aleatório para o user acertar.