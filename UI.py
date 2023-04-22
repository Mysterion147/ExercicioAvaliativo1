import crud_commands
from classes import Animal, Cuidador, Habitat
from crud_commands import ZoologicoAOD

class ZoologicoCLI:

    crud = ZoologicoAOD()

    def menu(self):
        print("1 para criar animal, 2 para ler, 3 para att, 4 para deletar")

    def createAnimal(self):
        print("Crie antes um cuidador")
        nome_c = input("Qual nome?")
        doc_c = input("Qual documento?")
        id_c = input("Qual id?")
        cuidador = Cuidador(id_c, nome_c, doc_c)

        print("Agora um habitat pro anhimal que é cuidado pelo criador que foi criado")
        nome_h = input("Qual nome?")
        type_h = input("Qual tipo?")
        id_h = input("Qual id?")
        habitat = Habitat(id_h, nome_h, type_h, cuidador)

        print("Finalmente, ensira as infos do animal")
        nome_an = input("Qual nome?")
        especie_an = input("Qual a especie?")
        idade_an = input("Qual a idade?")
        id_an = input("Qual id?")  # vale ressaltar q o banco vai gerar seu próprio id para referenciar a documento
        animal = Animal(id_an, nome_an, especie_an, idade_an, habitat)

        self.crud.create_animal(animal)

    def readAnimal(self):
        id_desejado = input("Entre com o id buscado")

        self.crud.read_animal_by_id(id_desejado)

    def updateAnimal(self):
        novo_nome = input("Insira o novo nome")
        nova_especie = input("Insira a nova especie")
        nova_idade = input("Insira a nova idade")

        self.crud.update_animal(novo_nome,nova_especie,nova_idade)

    def deleteAnimal(self):
        print("VOCE ESTA PRESTES A DELETAR UM ANIMAL, ESSA ACAO NAO PODE SER DESFEITA")
        id_goner = input("Insira o id do animal a ser deletado")

        self.crud.delete_animal(id_goner)
