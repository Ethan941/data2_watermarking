def texte_en_binaire(texte):
    binaire = ''.join(format(ord(car), '08b') for car in texte)
    return binaire

print(texte_en_binaire("Hi"))









#ord(car)Transforme un caractère en son code ASCII Exemple :ord('A') = 65
#format(..., '08b')Convertit en binaire sur 8 bits  Exemple :format(65, '08b') → "01000001"
 #''.join(...) Colle tous les bits ensemble pour former une longue chaîne binaire.

