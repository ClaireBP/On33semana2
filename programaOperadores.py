# Solicitar ao usuario para digitar dois números
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número:'))
#Operações Aritmeticas
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
divisaoInteira = num1 // num2
modulo = num1 % num2
potencia = num1 ** num2
# Exibir os resultados
print('\n Resultados das operações aritmeticas:')
print('Soma:', soma)
print('Subtracao:', subtracao)
print('Multiplicacao:', multiplicacao)
print('Divisao:', divisao)
print('DivisaoInteira:', divisaoInteira)
print('Modulo:', modulo)
print('Potencia:', potencia)
# Comparações com operadores
print('\n Resultados das operações de comparação:')
print('Igualdade:', num1 == num2)
print('Diferenca:', num1 != num2)
print('Maior:', num1 > num2)
print('Maior ou igual:', num1 >= num2)
print('Menor:', num1 < num2)
print('Menor ou igual:', num1 <= num2)
# Operadores de atribuição
print('\n Resultados dos Operadores de atribuição:')
num1 += 5
print('num1 += 5:', num1)
num2 /= 2
print('num2 /= 2:', num2)
#Verificar presença na lista de elementos
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if num1 in lista_numeros:
    print(f'o número {num1} está na lista de numeros')
else:
    print(f'o número {num1} não está na lista de números')
# Compare a identidade de objetos
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print('\n Resultados das operações de identidade de objetos:')
print('x is z:', x is z)
print('x is y:', x is y)
print('x is not y:', x is not y)


