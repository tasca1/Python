1) Faça um programa que peça dois números e imprima o maior deles.

num1 = int(input("Me diga um numero: "))
num2 = int(input("Me diga outro numero: "))

if num1 > num2 : 
  print(num1)
else:
  print(num2)

2) Faça um programa que leia três números e imprima o maior deles.

num1 = int(input("Me diga um numero: "))
num2 = int(input("Me diga outro numero: "))
num3 = int(input("Me diga outro numero: "))

if num1 > num2 and num1 > num3 :
  print(num1)

if num2 > num1 and num2 > num3 :
  print(num2)

if num3 > num1 and num3 > num2 :
  print(num3)

else:
  print("Coloque números distintos")

3) Faça um programa que receba como entrada três valores e os imprima em ordem crescente.

num1 = int(input("Me diga um numero: "))
num2 = int(input("Me diga outro numero: "))
num3 = int(input("Me diga outro numero: "))

valores = [num1, num2, num3]

valores.sort()
print("A sequencia é", valores) 

4) As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12 unidades. Escreva um programa que leia o número de maçãs compradas, calcule e imprima o custo total da compra.

qtd_maca = int(input("Quantas maçãs você deseja comprar?  "))

if qtd_maca < 12 :
  preco = qtd_maca * 1.3
  print("Você irá pagar", preco , " reais pelas suas", qtd_maca , " maçãs")

else:
  preco = qtd_maca
  print("Você irá pagar", preco , " reais pelas suas", qtd_maca , " maçãs")

5) Faça um programa para aprovar empréstimos bancários. O código deve pedir três informações: valor do empréstimo, número de parcelas e salário do solicitante. Aprovar empréstimo caso o valor das parcelas represente no máximo 30% do salário do solicitante.

valor_e = float(input("Diga o valor do empréstimo que você deseja: "))
num_parcela = int(input("Qual o número de parcelas? "))
valor_s = float(input("Qual o seu salário? "))

valor_p = (valor_e / num_parcela)

porcentagem_s = (valor_s * 0.3)

if valor_p > porcentagem_s :
  print("Empréstimo invalidado, você não consegue pagar ")

if valor_p <= porcentagem_s : 
  print("Empréstimo aprovado!")

6) A empresa paga ao corretor uma comissão calculada de acordo com o valor de suas vendas. Se o valor da venda de um corretor for maior que R$ 50.000,00 a comissão será de 12% do valor vendido. Se o valor da venda do corretor estiver entre R$ 30.000,00 e R$ 50.000,00 (incluindo extremos) a comissão será de 9,5%. Em qualquer outro caso, a comissão será de 7%. Escreva um programa onde será informado nome do corretor e o valor da venda, após isto o programa irá calcular o valor da comissão.

print("Bem vindo ao site da Arouca imóveis!")
nome = input("Primeramente, qual o seu nome? ")

valorvenda = float(input("E qual foi o valor da venda? "))

if valorvenda <= 29999.99:
  comissao = (valorvenda * 0.07)
  print ("O cálculo da sua comissão Senhor(a)", nome , "com a venda do imóvel de", valorvenda, "R$, será de",  comissao ,"R$." )

if valorvenda >= 30000 and valorvenda <= 50000 :
  comissao = (valorvenda * 0.095)
  print ("O cálculo da sua comissão Senhor(a)", nome , "com a venda do imóvel de", valorvenda, "R$, será de",  comissao ,"R$." )

if valorvenda > 50000 :
    comissao = (valorvenda * 0.12)
    print ("O cálculo da sua comissão Senhor(a)", nome , "com a venda do imóvel de", valorvenda, "R$, será de",  comissao ,"R$." )

7) Faça um programa onde serão informados as quatro notas do aluno. O programa irá então apresentar a média, se foi aprovado (nota ≥ 7) ou se ficou em exame. Caso o aluno ficou em exame, o programa irá então perguntar qual foi a nota do exame e então irá calcular a nova média (média anteior com a nota do exame) e informar se ele foi aprovado (nova média ≥ 5) ou se foi reprovado.

n1 = float(input("Digite sua nota: "))
n2 = float(input("Digite sua nota: "))
n3 = float(input("Digite sua nota: "))
n4 = float(input("Digite sua nota: "))

nota = (n1 + n2 + n3 + n4) / 4 

if nota >= 7 :
 print("Párabens, aprovado!")

if nota < 7 :
    print("\n Puxa vida, você pegou EXAME")
    notaexame = float(input("Qual sua nota no exame? "))
    exame = (nota + notaexame) / 2

if exame >= 5 : 
  print("Párabens, aprovado!")

if exame < 5 : 
  print("Reprovado.")


