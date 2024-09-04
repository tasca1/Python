# identificar se os valores digitados pelo usuário são válidos para compor um CPF. O usuário poderá informar apenas números ou no seguinte formato 123.456.789-98. A função retorna 1 se o valor informado pode formar um cpf ou 0, caso contrário.

#funcao que verifica tamanho do cpf e caractere

def validar_cpf(cpf):
  num_cpf = ""
  for caractere in cpf:
      if caractere.isdigit():
          num_cpf += caractere
  
  if len(num_cpf) != 11:
      return 0 

  if num_cpf == num_cpf[0] * 11:
      return 0

  #calculadora do primeiro e segundo digito
  
  def calcular(cpf, pesos):
      soma = 0
      for i in range(len(pesos)):
          soma += int(cpf[i]) * pesos[i]
      resto = soma % 11
      if resto < 2:
          return 0
      else:
          return 11 - resto


  #pesos  
  
  pesos1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
  digito1 = calcular(num_cpf[:9], pesos1)


  pesos2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
  digito2 = calcular(num_cpf[:10], pesos2)

 
  #verificacao digitos
  numeros_fornecidos = num_cpf[-2:]
  cpf_calculados = f"{digito1}{digito2}"

  
  if numeros_fornecidos == cpf_calculados:
      return 1
  else:
      return 0
#final
v_cpf = input("Informe o seu CPF: ")
if validar_cpf(v_cpf):
  print("CPF válido")
else:
  print("CPF inválido")




  


