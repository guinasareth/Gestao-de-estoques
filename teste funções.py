import sys

input1 = input('Digite o primeiro valor: ')
input2 = input('Digite o segundo valor: ')
operacao_input = input('Digite a operação desejada ( -, +, * ou / )')

# validando inputs de números
try:
  numero1 = float(input1)
  numero2 = float(input2)
except:
  print('Erro ao converter um dos inputs numéricos, por favor, digite apenas números.')
  sys.exit()

# funções para cada uma das operações
def soma(numero1, numero2):
  return numero1 + numero2

def subtracao(numero1, numero2):
  return numero1 - numero2

def multiplicacao(numero1, numero2):
  return numero1 * numero2

def divisao(numero1, numero2):
  return numero1 / numero2

# resultados para cada uma das operações
match operacao_input:
  case '+':
    print(soma(float(input1), float(input2)))
  case '-':
    print(subtracao(float(input1), float(input2)))
  case '*':
    print(multiplicacao(float(input1), float(input2)))
  case '/':
    print(divisao(float(input1), float(input2)))
  case _:
    print(f"Operação inválida '{operacao_input}' ")
    sys.exit()
