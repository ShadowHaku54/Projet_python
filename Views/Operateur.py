from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

# Style personnalisé pour l'entrée
custom_style = Style.from_dict({
    "prompt": "bold #00ff00",  # Couleur verte pour l'invite
})

def lire_une_entree(sms):
    """Lit une entrée utilisateur et la retourne"""
    return prompt(f"{sms} :\n> ", style=custom_style)

from prompt_toolkit.validation import Validator, ValidationError

class NombreValidator(Validator):
    """Valideur pour vérifier si la saisie est un nombre entier"""
    def validate(self, document):
        try:
            int(document.text)  # Conversion pour valider
        except ValueError:
            raise ValidationError(
                message="❌ Entrer un nombre valide.",
                cursor_position=len(document.text)  # Position du curseur
            )

def saisir_un_nombre(sms):
    """Saisit un nombre valide"""
    validator = NombreValidator()

    nombre_saisie = prompt(
        f"{sms} :\n> ",
        style=custom_style,
        validator=validator,
        validate_while_typing=False  # Valider seulement après Entrée
    )

    return int(nombre_saisie)  # Convertir la chaîne en entier avant de la retourner

class ChaineValidator(Validator):
    """Valideur pour vérifier la longueur minimale de la chaîne"""
    def __init__(self, min_length):
        self.min_length = min_length

    def validate(self, document):
        if len(document.text) < self.min_length:
            raise ValidationError(
                message=f"❌ La chaîne doit contenir au moins {self.min_length} caractères.",
                cursor_position=len(document.text)
            )

def saisir_une_chaine(sms, min_char):
    """Saisit une chaîne valide avec une longueur minimale"""
    validator = ChaineValidator(min_char)

    chaine_saisie = prompt(
        f"{sms} :\n> ",
        style=custom_style,
        validator=validator,
        validate_while_typing=False
    )

    return chaine_saisie

def error_message(message):
    print(f"\033[1;31m{message}\033[0m")

def main():
    print("Bienvenue dans le programme de saisie.")
    print("-------------------------------------")

    # Saisir un nombre
    nombre = saisir_un_nombre("Entrez un nombre valide")
    print(f"Nombre validé : {nombre}")

    # Saisir une chaîne
    MIN_CHAR = 3
    chaine = saisir_une_chaine("Entrez une chaîne (au moins 3 caractères)", MIN_CHAR)
    print(f"Chaîne validée : {chaine}")


if __name__ == "__main__":
    main()