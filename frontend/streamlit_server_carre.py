# import libs
import streamlit as st

# bibliotheque d'appel d'api
import requests

# autre facon d'afficher du texte
st.text("bienvenue 2")

# variables du carre
nbre = st.number_input('Nombre')

# btn de prediction
btn = st.button("calculer")

#action de click
if btn:
    # faire appel à l'api distante
    headers = {'Content-Type': 'application/json'}
    my_json = {"nbre": float(nbre)}
    
    # appel de l'api
    reponse = requests.post('http://167.172.49.80:3003/api/carre', json=my_json, headers=headers)
    
    if (reponse.status_code == 200):
        resultat = reponse.json()
        # affichage du resultat
        st.write(f'Le carré du nombre {float(nbre)} est {resultat["carre"]}')
    else:
        st.write(f'Erreur. code {reponse.status_code}')
    
    