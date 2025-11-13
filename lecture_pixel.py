from PIL import Image

def lire_pixel(image_path, x, y):
    # Ouvrir l'image
    img = Image.open(image_path)

    # Convertir en mode RGB pour être sûr d'avoir 3 canaux
    img = img.convert("RGB")

    # Récupérer la valeur du pixel (R, G, B)
    pixel = img.getpixel((x, y))

    print(f"Pixel à la position ({x}, {y}) : {pixel}")
    return pixel

# Exemple d'utilisation
lire_pixel("dembele.png", 50, 100)
