class Cuidador:
    def __init__(self, id: str, nome: str, documento: str):
        self.__id = id
        self.__nome = nome
        self.__documento = documento

class Habitat:
    def __init__(self, id: str, nome: str, tipoAmbiente: str, cuidador: Cuidador):
        self.__id = id
        self.__nome = nome
        self.__tipoAmbiente = tipoAmbiente
        self.__cuidador = cuidador

class Animal:
    def __init__(self, id: str, nome: str, especie: str, idade: int, habitat: Habitat):
        self.__id = id
        self.__nome = nome
        self.__especie = especie
        self.__idade = idade
        self.__habitat = habitat

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_especie(self):
        return self.__especie

    def get_idade(self):
        return self.__idade