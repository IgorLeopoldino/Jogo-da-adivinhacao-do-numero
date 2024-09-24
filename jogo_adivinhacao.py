#biblioteca de randomização importada
from random import randint

#variável do num do computador
num_pc = randint(1,10)

#função para condicionar os números
def num(num_user, num_pc):
    if num_user < num_pc:
      return "Número escolhido é menor que do computador\nTente novamente!"
    
    elif num_user > num_pc:
      return "Número escolhido é maior que do computador\nTente novamente!" 
     
    else:
      return "Você acertou! Parabéns!"

while True:
  num_user = int(input("Chute um número de 1 a 10: ")) #variável input do num que o user digitou
  resultado = num(num_user, num_pc)
  print(resultado) #resultado para o usuário na tela

  if num_user == num_pc:
    break