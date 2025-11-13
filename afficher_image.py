import streamlit as st
from PIL import Image #On importe la classe Image de la bibliothèque PIL (Pillow)

img = Image.open("dembele.png")#On ouvre le fichier image dembele.png
                                                    #/On le met dans une variable appelée img



st.image(img, caption="Dembélé", use_column_width=True)#Montre l’image dans la page Streamlit, avec un texte en dessous
                                                       #caption="Dembélé"  un petit texte sous l’image
                                                       #use_column_width=True  l’image s’adapte à la largeur de la page

