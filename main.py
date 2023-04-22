from UI import ZoologicoCLI

zoo = ZoologicoCLI()
zoo.menu()
number = int(input("Entre com a operação desejada!"))

if(number == 1):
    zoo.createAnimal()

if(number == 2):
    zoo.readAnimal()

if(number == 3):
    zoo.updateAnimal()

if(number == 4):
    zoo.deleteAnimal()