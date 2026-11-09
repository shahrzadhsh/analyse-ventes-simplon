-- ==========================================
/* 

PROJET SIMPLON : ANALYSE DES VENTES

Analyse des ventes d'une PME
Objectif :
Calculer le chiffre d'affaires total sur la période étudiée.
*/
-- ==========================================
-- 2.Vérifiez que votre import a fonctionné en exécutant la requête SQL suivante :
SELECT * FROM ventes; 

--3. Créez les requêtes SQL pour répondre aux questions clés sur les ventes de l'entreprise :

------- a. Calcul du chiffre d'affaires total
SELECT  SUM ( prix * qte) as Chiffre_Affaire_total
FROM ventes;

------- b. Le vente par produit
SELECT  produit,
		SUM ( prix * qte)  AS vente_par_produit
FROm ventes
Group By  produit;

------- c. Le vente par region
SELECT region,
		SUM(prix * qte) AS vente_par_région
FROM ventes
GROUP BY region;
