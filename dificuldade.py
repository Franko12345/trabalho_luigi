print("Voce se encontra em um barco como...")
print(" ")
print("Prisioneiro, que só quer fugir.")
print("Ladrao, Que quer roubar o tesouro e fugir.")
print(" ")
print("1 para ser o prisioneiro, 2 para ser o ladrao")
res = input(" ")
rota = 0

while ( rota == 0 ):
    if res == "1":
        print("Prisioneiro.")
        rota = 1
    elif res == "2":
        print("Ladrao")
        rota = 2
    else:
        print("hmm... Poderia escolher denovo?")
        res = input(" ")

print(rota)
