# Entrada de dados e cálculo do IMC.
print('Cálculo de IMC')
nome = input('Digite_seu_nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = input('Digite sua idade: ')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
IMC = peso/(altura*altura)
if IMC<18.5:
    print('Abaixo do peso')
elif IMC<24.9:
    print('Peso normal')
elif IMC<29.9:
    print('Sobrepeso')
elif IMC<34.9:
    print('Obesidade Grau I')
elif IMC<39.9:
    print('Obesidade Grau II')
else:
    print('Obesidade Grau III ou Morbida')
