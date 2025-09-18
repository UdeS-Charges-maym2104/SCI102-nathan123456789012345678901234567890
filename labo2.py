from datetime import datetime

def age(annerDeNaissance):
    anne=0
    anne=datetime.now().year
    anne=(anne-annerDeNaissance)
    anne=str(anne)
    return "Votre âge est "+anne+" ans."

