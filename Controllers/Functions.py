def check_nombre(nombre):
    nombre = nombre.split('.', 1)
    return nombre[0].isdigit() and nombre[-1].isdigit()

def check_chaine(chaine, size_m):
    return len(chaine.strip()) >= size_m

