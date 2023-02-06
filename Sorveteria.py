print('Bem-Vindo(a) à sorveteria ganso')
print(106*'-')
print('| ''Código''|''      Descrição''        | ''     Tamanho P (500ML)''     | ''Tamanho M (1000ML)''  | ''  Tamanho G (1000ML)'' |')
print('| ''  1''   |'' Sabores Tradicionais''  |         ''R$6,00''             | ''   R$10,00''          | ''      R$18,00''            |')
print('| ''  2''   |'' Sabores Especias''      |         ''R$7,00''             | ''   R$12,00''          | ''      R$21,00''            |')
print('| ''  3''   |'' Sabores Premium''       |         ''R$8,00''             | ''   R$14,00''          | ''      R$24,00''            |')
print(106*'-')

tamanho = ["P", "M", "G"]
codigos = {"1": [6.00, 10.00, 18.00],
          "2": [7.00, 12.00, 21.00],
          "3": [8.00, 14.00, 24.00]}

total = []
# pedindo os dados
while True:
   tmn_copo = input("Qual o tamanho do sorvete desejado? ")
   sbr_copo = input("Qual o código do sorvete desejado? ")
   if tmn_copo in tamanho and sbr_copo in codigos:
       pedido = codigos[sbr_copo][tamanho.index(tmn_copo)]
       total.append(pedido)
       algo_mais = input ("Deseja pedir algo mais?"
                          "\nDigite Sim para sim ou Nao para não. ")
       if algo_mais == "Sim":
           continue
       else:
           break
   else:
       print("TAMANHO ou CÓDIGO inválido(s)")
       continue

print ("Valor total da compra:", "R$",sum(total))