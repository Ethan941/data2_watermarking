from PIL import Image
import os

def rendre_pixels_pairs():
    # Trouver une image .png dans le dossier
    image_name = None
    for file_name in os.listdir():
        if file_name.lower().endswith(".png"):
            image_name = file_name
            break

    if image_name is None:
        raise FileNotFoundError("Aucune image PNG trouvée dans le dossier.")

    # Ouvrir l'image
    img = Image.open(image_name)
    img = img.convert("RGB")
    pixels = img.load()

    largeur, hauteur = img.size

    # Parcourir tous les pixels
    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = pixels[x, y]

            # Forcer chaque valeur à être paire
            r = r - (r % 2)
            g = g - (g % 2)
            b = b - (b % 2)

            pixels[x, y] = (r, g, b)

    # Sauvegarder l'image modifiée
    img.save("image_pairs.png")
    print("Image convertie : image_pairs.png")

# Test
rendre_pixels_pairs()
