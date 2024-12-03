from consts import TAB

def lire_une_entree(sms):
    """Lit une entrée et la retourne"""
    print(f"{sms}:")
    lecture = input(f">{TAB}")
    print()
    return lecture
