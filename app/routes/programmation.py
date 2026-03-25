from fastapi import APIRouter
from datetime import datetime
from typing import List

router = APIRouter()

personne = {
    'nom': 'jean',
    'age': 14,
    'ville': 'Merignac',
    'profession': 'Ingenieur'
}

dict1 = {
    'a': 1,
    'b': 2
}

dict2 = {
    'b': 3,
    'c': 4
}


class Voiture():
    marque: str
    modele: str
    annee: int
    age: int

    def __init__(self, marque, modele, annee):
        print('creation de la classe Voiture')
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.age = self.calculer_age(annee)
        self.description()

    def description(self):
        #print('Voiture créée : ' + self.marque + ' ' + self.modele + ' ' + str(self.annee))
        print(f"Voiture créée : {self.marque} {self.modele} {self.annee} {self.age}")

    def veillir(self):
        self.age += 1
        print('age de la voiture : ' +  str(self.age))

    def calculer_age(self, annee: int) -> int:
        year = datetime.today().year
        age = year - annee
        return age


class ProgrammationAPI():

    def __init__(self, router: APIRouter):
        self.router = router
        self.register_routes()

    def register_routes(self):
        self.router.get('')(self.formatBuildComplexeObjet)
        self.router.get('/{name}')(self.methWithParams)


    def formatBuildComplexeObjet(self):
        result = self.deuxiemeManipulationListe()
        return { 'result': result}

    def manipulationListe(self) -> List[int]:
        listValue = [3, 7, 2, 9, 4]
        listValue.append(5)
        listValue.remove(listValue[1])
        listValue.sort()

        return listValue
    
    def deuxiemeManipulationListe(self) -> List[int]:
        nombres = [12, 5, 8, 130, 44]
        nombres = [result for result in nombres if result > 10]

        return nombres

    def findMostAgedVoiture(self, voitureArray = List[Voiture]):
        voitureArray = [
            Voiture('Ford', 'Fiesta', 2008),
            Voiture('BMW', 'SuperModele', 2025),
            Voiture('Ferrari', 'SuperFerra', 2017),
            Voiture('Porche', 'Boxter', 2001),
            Voiture('Renault', 'Pipo', 2028)
        ]

        result = self.MostAgedVoiture(voitureArray)

        return { 'key': result }

    def MostAgedVoiture(self, car_array = List[Voiture]):
        age = 0
        voitureMostAged: Voiture

        for voiture in car_array:
            if voiture.age > age:
                age = voiture.age
                voitureMostAged = voiture
        
        return voitureMostAged

    def formatDictStr(self, dictInput : dict):
        for key,value in dictInput.items():
            if type(dictInput[key]) == str:
                print(f'{key}: {value}')

    def fusionnerDict(self, dict1: dict, dict2: dict):
        newDict = {}

        for key, value in dict1.items():
            newDict[key] = value

        for key2, value2 in dict2.items():
            newDict[key2] = value2

    def methWithParams(self, name):
        return { 'result': name }



class TestProgrammation(ProgrammationAPI):

    def __init__(self):
        print('on passe dans lenfant')
        return { 'key': 'Value Enfant'}
    
ProgrammationAPI(router)