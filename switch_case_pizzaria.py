# exibe os codigos disponiveis
print("codigo de produto ")
print("1 banana")
print("2 romeu e julieta")
print("3 chocolate")
print("4 chocolate branco")
print("0 sair")
  
# solicite o codigo do  produto ao usuario
codigo = int(input("digite o codigo do produto: "))

# usa math-case para mostrar o preço com base no codigo 
match codigo:
    case 1:
        print("produto: banana - preço R$ 35,99")
    case 2:
        print("produto: romeu e julieta - R$ 29,99")
    case 3: 
        print("produto: chocolate - R$ 28,99")
    case 4:
        print("produto: chocolate branco - 32,99")
    case 0:
        print(" saindo progama ...")
        exit() #encerra o progama se o godigo for 0 
    case _: 
        print("codigo invalido. por favor, tente novamente")
