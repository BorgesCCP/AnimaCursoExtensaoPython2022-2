# comando input () permite que o usuario digite algo
nome = input ("Digite seu nome: ")

print("Seu nome é "+nome)

idade = int(input("digite sua idade: "))
genero = input("Digite seu genero: ")

print("Seu nome é {} e sua idade é {} anos".format(nome,idade))

nome2 = input("Digite seu nome: ")

idade2 = int(input("Digite seu idade: "))
genero2 = input("Digite seu genero: ")

totalIdade = idade + idade2

print(f"Seus nomes são {nome} e {nome2}, e suas idades somam {totalIdade} anos")

dobro = totalIdade*2

print("O dobro da idade de vocês equivale a {} anos".format(dobro))

if (idade>idade2):
  print("{} é mais velho que {}".format(nome,nome2))

else :
  print("{} é mais velho que {}".format(nome2,nome))


if (genero == "M" or "m") and (idade>=18) :
  print("Deve prestar o serviço militar obrigatório")

else :
  print("não é obrigatorio para ti")