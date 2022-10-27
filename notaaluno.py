nome = input("Digite seu nome: ")
nota = float(input("Digite sua nota"))

if (nota==10):
  print("{} é o bichão mesmo, tirou {}".format(nome,nota))

elif (nota<10) and (nota>6):
  print("{} mediano, nota {}".format(nome,nota))

else:
  print("{} ta fraco, nota {}".format(nome,nota))  