def numeros(a,b,c):
  if a > b and a > c:
    return a

  elif b > a and b > c:
    return b

  elif c > a and c > b:
    return c

  else:
    print("Números iguais não são válidos")

num1 = int(input("Diga um número: "))
num2 = int(input("Diga um número: "))
num3 = int(input("Diga um número: "))

programa = numeros(num1,num2,num3)

print("\n",programa)

for i in range(1,30):
  print("jec maior de sc")

x = int(input("Diga outro valor: "))
y = int(input("Outro: "))
z = int(input("Ultimo: "))

ultimo = numeros(x,y,z)
print(ultimo)

-----------------------------------------------------------

print("\n Olá iremos calculcar o perimetro do triangulo que você pedir!!")

def perimetro(a,b,c):
  return a + b + c


lado1 = int(input("Diga um número: "))
lado2 = int(input("Diga um número: "))
lado3 = int(input("Diga um número: "))

perimetro_total = perimetro(lado1,lado2,lado3)
print(perimetro_total)

-------------------------------------------------------

def media(nota):
  if nota <= 10 and nota >=9: 
    nota = "A"
    return nota
 
  elif nota < 9 and nota >=8:
    nota = "B"
    return nota

  elif nota < 8 and nota >= 7:
    nota = "C"
    return nota

  elif nota < 7 and nota >= 6:
    nota = "D"
    return nota

  elif nota < 6:
    nota = "F"
    return nota

n1 = float(input("\nQual nota você tirou: "))

notafinal = media(n1)
print(notafinal)

---------------------------------------------------------

def escola (total, faltas, nota):
  totalfaltas = total * 0.25

  if faltas <= totalfaltas and nota>= 6:
    return 1

  else:
    return 0 

faltas1 = int(input("Total de aulas faltadas"))
total1 = int(input("Total de aulas "))
nota1 = int(input("Nota final "))

resultado = escola(total1,faltas1, nota1)
if resultado == 1:
  print("Aprovado")

elif resultado == 0:
  print("Reprovado")

--------------------------------------------------------

def cle(idade):
  if idade < 16:
    return "Não eleitor"

  elif idade >= 16 or idade <= 18 or idade > 65:
    return "Eleitor obrigatório"

  elif 18 < idade and idade <= 65:
    return "Eleitor facultativo"

idadeeleitor = int(input("Qual a sua idade? "))

resposta = cle(idadeeleitor)
print(resposta)

--------------------------------------------------------

def programa(num):
  if num % 2 == 0:
    return 1
  else:
    return -1

numero = int(input("Escolha um número: "))

resposta = programa(numero)
print(resposta)

--------------------------------------------------------

def fatorial(base):
  if base < 0:
    return "Não existe"

  elif base == 0:
    return 1

  for i in range (base - 1,1,-1):
    base = base * i
    
  return base

total = int(input("Diga um número para calcularmos o fatorial"))

resposta = fatorial(total)
print(resposta)

cpf = "145382206"
soma = 0
pesos = [10, 9, 8, 7, 6, 5, 4, 3, 2]
soma = int(cpf[0]) * pesos[0]
print(soma)
for i in range(len(pesos)):
    soma = soma + (cpf[i]) * pesos
resto = soma % 11
print(soma)
    




  
  

  