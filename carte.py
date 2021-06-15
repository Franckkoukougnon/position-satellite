# Appel de la bibliothèque Folium
import folium
# Créer une carte centrée sur les coordonnées GPS indiquée
carte = folium.Map(location=[43.920044, 5.051804])
# Sauvegarder cette carte dans un fichier HTML
carte.save('Carte1.html')
