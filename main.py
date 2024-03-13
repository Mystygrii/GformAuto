from selenium import webdriver
from autoGform import AutoGform
import os
import json

YesNoField = {'y':True,'n':False}

def writeFile(prenom, nom):
    identifiers = {

        "nom" : nom,
        "prenom" : prenom
    }

    with open('fichier.json','w') as fichier:
        json.dump(identifiers, fichier)

def run():    

    while True:
        try:
            if not os.path.exists("fichier.json"):
                register = "y"
                print("Veuillez enregistrer votre nom et prénom :")
            else:
                print("\033[H\033[J")
                register = input("Voulez enregistrer à nouveau votre nom et prénom ? (y/n) ")

            if register not in YesNoField:
                raise Exception()
            else:
                break

        except:
            print('Répondez par y ou n')
            print("\033[H\033[J")

    if YesNoField[register]:
        print("\033[H\033[J")
        nom = input("Nom : ")
        print("\033[H\033[J")
        prenom = input("Prenom : ")
        print("\033[H\033[J")
        writeFile(nom,prenom)

    else:
        with open('fichier.json', 'r') as fichier:
            data = json.load(fichier)
            nom = data["nom"]
            prenom = data["prenom"]

    autoComplete = AutoGform(nom, prenom)
    autoComplete.complete()

run()