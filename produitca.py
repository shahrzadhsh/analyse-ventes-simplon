import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')
données['chiffre_affaires'] = données['prix'] * données['qte']
figure_produitca = px.pie(
    données,
    values='chiffre_affaires',
    names='produit',
    title="Chiffre d'affaires par produit"
)
figure_produitca.write_html('chiffre-affaires-par-produit.html')