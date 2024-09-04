EXERCICIO 1) FIbonacci

OPCAO 1:
qnt_termos = int(input("Quantos termos da sequencia voce deseja saber: "))

if qnt_termos <= 0:
  print("Voce so pode escolher termos positivos")
else:

  lista = [0, 1]

  for i in range(2, qnt_termos):
    novo_termo = lista[-1] + lista[-2]
    lista.append(novo_termo)

  if qnt_termos == 1:
    lista = [0]
  print(f"Os primeiros {qnt_termos} termos da sequencia sao: {lista}")

OPCAO 2:
num1 = int(input("Qual o primeiro número da sequencia de fibonacci que você deseja: "))

num2 = int(input("Qual o segundo número da sequencia de fibonacci que você deseja: "))

num_termo = (int(input("Némeros de termos na sequencia de fibonacci: ")))

if num1 and num2 <= 0:
  print("Digite apenas numeros positivos.")

if num1 < num2:
  for i in range(num1, num_termo):
    print (num1, )
    num1, num2 = num2, num1 + num2

EXERCICIO 2)

Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Insira o preço do produto 1, R$:"))
produto2 = float(input("Insira o preço do produto 2, R$:"))
produto3 = float(input("Insira o preço do produto 2, R$:"))

if produto1 < produto2 and produto1 < produto3:
  produto_mais_barato = "Produto 1"
elif produto2 < produto1 and produto2 < produto3:
  produto_mais_barato = "Produto 2"
else:
  produto_mais_barato = "Produto 3"

# Mostrar o resultado
print("Você deve comprar o", produto_mais_barato, "pois ele é o mais barato")

EXERCICIO 3)

O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50

print("\n Bem vindo a tabela de preços da Lojas Quase Dois! ")

x = int(input("Até quantos produtos você deseja saber na tebela: "))

din = 1.99
for i in range(1, x + 1):
   print(i ,"- R$", din,)
   din += 1.99

EXERCICIO 4)

Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

print("\nBem vindo ao Posto de Gasolina SC!! ")

escolha = int(input("\n 1- Alcool \n 2- Gasolina \n\n Faça a sua escolha  de acordo com as opções:"))

if escolha == 1:
  litro_alc = 1.9
  num_alc = (int(input("\n Quantos litros de álcool você abasteceu: ")))
  alc_total = (litro_alc * num_alc)


  if num_alc <= 20:  
    desconto = (litro_alc * 0.97)
    val_alc = (num_alc * desconto)
    print(f'\n\nEm nossa promoção você não precisa pagar {alc_total :.2f}R$. \n Com nosso desconto de 3% você precisa pagar {val_alc :.2f}R$ de A-álcool.')

  else:
    desconto = (litro_alc * 0.95)
    val_alc = (num_alc * desconto)
    print(f'\n\n Em nossa promoção você não precisa pagar {alc_total :.2f}R$. \n Com nosso desconto de 5% você precisará pagar {val_alc :.2f}R$ de A-álcool.')


if escolha == 2:
  litro_gas = 2.5
  num_gas = (int(input("\n Quantos litros de gasolina você abasteceu: ")))
  gas_total = (litro_gas * num_gas)


  if num_gas <= 20:  
    desconto = (litro_gas * 0.96)
    val_gas = (num_gas * desconto)
    print(f'\n\n Em nossa promoção você não precisa pagar {gas_total :.2f}R$. \n Com nosso desconto de 4% Você precisará pagar {val_gas :.2f}R$ de G-gasolina.')

  else:
    desconto = (litro_gas * 0.94)
    val_gas = (num_gas * desconto)
    print(f'\n\n Em nossa promoção você não precisa pagar {gas_total :.2f}R$. \n Com nosso desconto de 6% Você precisará pagar {val_gas :.2f}R$ de G-gasolina.')

else:
  print("Coloque um número compatível com o sistema.")

EXERCICIO 5) Estoque de mercado com dois sistemas de cliente e funcionário totalmente interligados.

produtos = ["arroz", "feijao", "cafe", "macarrao", "farinha", "ovos", "carnes", "cebola", "batata", "oleo"]
qnt_estoque = [20, 10, 40, 25, 100, 35, 20, 15, 30, 60]

decisao = 1
while True:
    while decisao == 1:
        print("\n\n---------------------------------------------------------------------------")

        print("\n Bem vindo ao site do estoque do Mercadinho SC")

        print(" \n 1- Funcionário \n 2- Clientes")

        escolha = int(input("\n Digite um dos números acima para acessar a área de interesse: "))


        if escolha == 1:
            print("\n\n---------------------------------------------------------------------------")

            print("\n Você está na área de funcionários.")


            senha = int(input("\n Digite a senha de 4 dígitos:"))
            decisao = 4

            while senha != 1234 and decisao == 4:
                for x in range(3,0,-1):                                                 
                    print("\n\n---------------------------------------------------------------------------")
                    print("\nErrado. \nVocê só tem mais", x , "tentativas até o sistema fechar.")
                    senha = int(input("\n Digite a senha de 4 dígitos:"))

                    if x == 1 and senha != 1234:                  
                        print("\n\n---------------------------------------------------------------------------")
                        print("\n\n Suas tentativas acabaram! \n Você será levado de volta ao menu.")

                        decisao = 1

                    if senha == 1234:
                            break



            if senha == 1234:


                print("\n\n---------------------------------------------------------------------------")

                print("\n Login confirmado com sucesso, bem vindo à área de funcionários!")

                continua = 'nao'
                decisao = 6
                while continua == 'nao' and decisao == 6:

                    print("\n\n---------------------------------------------------------------------------")

                    print("\n 1- Voltar ao Menu Principal \n 2- Adicionar produtos ao estoque \n 3- Ver produtos no estoque ")

                    decisao = int(input("\n Digite um dos números acima para acessar a área de interesse: "))



                    if decisao == 2 :
                        continua = 'sim'
                        while continua == 'sim':
                            print("\n\n---------------------------------------------------------------------------")
                            print("\n Estoque do Mercadinho SC: ")
                            for i in range(len(produtos)):
                                print( i+1,"-" , produtos[i])

                            escolher = int(input("\n Digite um dos números dos itens acima para adicionar estoque ao item : ")) - 1
                            if 0 <= escolher < len(produtos):
                                und = int(input(f"Quantos(as) {produtos[escolher]} você deseja adicionar ao estoque? ")) 
                                qnt_estoque[escolher] =  (und + qnt_estoque[escolher])
                                print(f"\nVocê adicionou {und} unidades de {produtos[escolher]} ao estoque.")
                                continua = input("Você deseja continuar? (sim/nao): ").lower()
                                if continua == 'nao':
                                    decisao = 6

                            else:
                                print("Opção inválida. Tente Novamente.")

                    if decisao == 3:
                        print("\n\n---------------------------------------------------------------------------")
                        print("\n Estoque do Mercadinho SC: ")
                        for i in range(len(produtos)):
                            print( i+1,"-" , produtos[i], "-", qnt_estoque[i])
                        print("\n\n---------------------------------------------------------------------------")
                        print("\n 1- Voltar ao menu anterior ")


                        decisao = int(input("\n Digite um dos números acima para acessar a área de interesse: "))
                        decisao+= 5

        elif escolha == 2:

              continua = 'sim'
              while continua == 'sim':
                  print(
                      "\n\n---------------------------------------------------------------------------"
                  )
                  print("\nLista de produtos:")
                  for i in range(len(produtos)):
                      print(f"{i + 1}. {produtos[i]}")

                  escolher = int(
                      input("\nDigite o número do produto que deseja comprar: ")) - 1

                  if 0 <= escolher < len(produtos):
                      und = int(
                          input(f"Quantos(as) {produtos[escolher]} você deseja comprar? "))

                      print(
                          "\n\n---------------------------------------------------------------------------"
                      )
                      if und <= qnt_estoque[escolher]:
                          qnt_estoque[escolher] -= und
                          print(f"\nVocê comprou {und} unidades de {produtos[escolher]}.")
                      else:
                          print(
                              f"\nDesculpe, não temos {und} unidades de {produtos[escolher]} em estoque. Temos apenas {qnt_estoque[escolher]} unidades."
                          )
                  else:
                      print("Escolha inválida. Tente novamente.")

                  continua = input("\nDeseja realizar outra compra? (sim/nao): ").lower()

        else:
          decisao = 8
          print(
              "\n\n---------------------------------------------------------------------------"
          )
          print(
              "\nEscolha inválida, por favor escolha outra opção entre 1 e 2! "
          )

          decisao = 1

