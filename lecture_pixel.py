from PIL import Image
import os

def lire_pixel(x, y):
    # Cherche une image .png dans le dossier courant
    image_name = None
    for file_name in os.listdir():
        if file_name.lower().endswith(".png"):
            image_name = file_name
            break

    if image_name is None:
        raise FileNotFoundError("Aucune image .png trouvée dans le dossier.")

    # Ouvrir l'image
    img = Image.open(image_name)

    # S'assurer qu'elle est en RGB (3 canaux)
    img = img.convert("RGB")

    # Récupérer la valeur du pixel (R, G, B)
    pixel = img.getpixel((x, y))

    # Afficher la valeur
    print(f"Pixel à la position ({x}, {y}) : {pixel}")

    return pixel


# Exemple d’utilisation : lire le pixel en (50, 100)
lire_pixel(50, 100)
