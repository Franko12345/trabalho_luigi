class personagem:
    def __init__(self, nome, vida, agilidade):
        self.nome = nome
        self.vida = vida
    def subirPet(self):
        agilidade = 20
    def decerPet(self):
        agilidade = 10
p1 = (loko, 30, 10)
p1.nome = str(input("Qual vai ser o nome de seu personagem?\n"))

class inventario():
   def __init__(self, inventario):
        self.inventario = inventario
    def equipar (self, slot, equipado):
        if self.inventario[slot] != "":
            while confirm != True or confirm != False:
                confirm = input("Esse espaço ja esta ocupado quer subtitui-lo?\n")
                if confirm == "sim":
                    confirm = True
                elif confirm == "nao":
                    confirm = False
                elif confirm == "não":
                    confirm = False
                else:
                    print("Isso não é uma opção. Digite novemente\n")
