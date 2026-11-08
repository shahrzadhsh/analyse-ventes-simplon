import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure_produit = px.pie(
    données,
    values='qte',
    names='produit',
    title='Quantité vendue par produit'
)
figure_produit.write_html('quantite-vendue-par-produit.html')