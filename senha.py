senha = input(" digite a senha")

while senha != "123456789":
    senha = input("digite o numero: ")
    if senha == "123456789":
        print("senha correta!")
    else:
        print("senha incorreta! tente novamente.")    