# Meu primeiro projeto Python!!!
# <- comentario

print("-------inicio-------")
print("Alo Mundo")

# Quando quiser guardar uma String (nome)

nome = "Mateus Borges"
idade = 21

print("Meu nome é: "+nome)
print(idade)

mesesvividos = int(idade*12)
diasvividos = int(mesesvividos*30)

# Frase antes da variavel para a impressão de int
# Python não converte

#Converter com str()
# Ou {} na variavel dentro das "" e "f" fora das ""
# Ou {} e .format

print(str(mesesvividos)+" meses")
print(f"{diasvividos} dias")
print("Minha idade é {}".format(idade))

print("Meu nome é {} e minha idade é {} anos".format(nome,idade))

