from consts import TAB, MIN_CHAR
import sys
from Controllers.Functions import check_nombre, check_chaine

def lire_une_entree(sms):
    """Lit une entrée et la retourne"""
    print(f"{sms}:")
    lecture = input(f">{TAB}")
    print()
    return lecture

def saisir_un_ombre(sms):
    """Saisie un nombre valide"""
    nombre_saisie = lire_une_entree(sms)

    while not (check_nombre(nombre_saisie)):
        error_message("❌ Erreur! Entrer un nombre. Retry 🔁")
        nombre_saisie = lire_une_entree(sms)

    return nombre_saisie

def saisir_une_chaine(sms):
    print("------------------------------------------------")
    chaine_saisie = lire_une_entree(sms)
    
    while not check_chaine(chaine_saisie, MIN_CHAR):
        remonter_ligne(4)
        error_message("❌ Erreur! La chaine saisie est trop courte. Retry 🔁")
        chaine_saisie = lire_une_entree(sms)
    
    return chaine_saisie
        

def error_message(message):
    print(f"\033[1;31m{message}\033[0m")

def remonter_ligne(nb_lignes):
    for _ in range(nb_lignes):
        sys.stdout.write(f"\033[A")
        effacer_ligne()

def effacer_ligne():
    sys.stdout.write("\033[K")