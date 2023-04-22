from pymongo import MongoClient
from bson.objectid import ObjectId
from database import Database
from classes import Animal

class ZoologicoAOD:
    def __init__(self):
        self.db = Database("ExercicioAv1", "Animais")
        self.collection = self.db.collection

    def create_animal(self, animal:Animal) -> str:
        try:
            result = self.collection.insert_one({"Animal": animal.get_nome(),"Especie" : animal.get_especie(), "Idade": animal.get_idade()})
            animal_id = str(result.inserted_id)
            print(f"Animal {animal.get_nome()} created with id: {animal_id}")
            return animal_id
        except Exception as error:
            print(f"An error occurred while creating animal: {error}")
            return None

    def read_animal_by_id(self, animal_id: str) -> dict:
        try:
            animal = self.collection.find_one({"_id": ObjectId(animal_id)})
            if animal:
                print(f"Animal found: {animal}")
                return animal
            else:
                print(f"No animal found with id {animal_id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading animal: {error}")
            return None

    def update_animal(self, animal_name: str, animal_species: str, animal_idade: int) -> int:
        try:
            result = self.collection.update_one({"_id": ObjectId(animal_name)}, {"$set": {"Animal": animal_name,"Especie": animal_species, "Idade": animal_idade}})
            if result.modified_count:
                print(f"Animal {animal_name} updated with name {animal_name}, age {animal_idade}, species {animal_species}")
            else:
                print(f"No animal found with id {animal_name}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating animal: {error}")
            return None

    def delete_animal(self, animal_id: str) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(animal_id)})
            if result.deleted_count:
                print(f"Animal {animal_id} deleted")
            else:
                print(f"No animal found with id {animal_id}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting animal: {error}")
            return None