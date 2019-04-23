print(" Sua aventura esta prestes a começar, porem qual dificuldade você quer enfrentar?")
print("facil")
print("medio")
print("dificil")
res = input(" ")
rota = 0

while ( rota == 0 ):
    if res == "facil":
        print("Voce escolheu facil")
        rota = 1
    elif res == "medio":
        print("Voce escolheu medio")
        rota = 2
    elif res == "dificil":
        print("Voce escolheu dificil")
        rota = 3    
    else:
        print("hmm... Poderia escolher denovo?")
        res = input(" ")

print(rota)
