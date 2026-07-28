# Système de Recommandation par Décomposition en Valeurs Singulières (SVD)

> **Mathématiques pour l'IA** — Travaux Pratiques / TP

> **Établissement :** Faculté des Sciences Ben M'Sick, Université Hassan II de Casablanca

> **Auteurs :** Ilyass BOUDADE, Mustafa ABDELMOUMEN, Ibrahim EL MOKADDEM, Othman SEMLALI, Khaoula ZANZOUNI, Youssef DOUIBA

---

## 📌 Présentation du Projet

Ce répertoire contient l'implémentation en Python de la **Décomposition en Valeurs Singulières (SVD)** pour un **Système de Recommandation de Films**.

Dans les systèmes de filtrage collaboratif et de recommandation, les matrices de notes utilisateurs-films sont souvent creuses et contiennent des valeurs manquantes (films non notés). En utilisant la réduction de dimension par SVD (approximation matricielle de rang inférieur), nous pouvons projeter la matrice de notes dans un espace de dimension réduite afin de prédire les notes non observées.

---

## 🎯 Énoncé du Problème

Soit une matrice de notes utilisateur-film $A \in \mathbb{R}^{4 \times 4}$ représentant 4 utilisateurs et 4 films :

| Utilisateur | Film 1 | Film 2 | Film 3 | Film 4 |
| :--- | :---: | :---: | :---: | :---: |
| **User 1** | 5 | 3 | 0 | 1 |
| **User 2** | 4 | 0 | 0 | 1 |
| **User 3** | 1 | 1 | 0 | 5 |
| **User 4** | 1 | 0 | 0 | 4 |

> *Note :* La valeur `0` indique l'absence de note pour un film de la part d'un utilisateur.

### Objectif
Prédire les notes manquantes de l'**Utilisateur 2** pour le **Film 2** ($a_{22}$) et de l'**Utilisateur 3** pour le **Film 2** ($a_{32}$) en utilisant une reconstruction SVD tronquée de rang $k$ (avec $k = 2$).

---

## 🧮 Fondements Mathématiques & Étapes

La Décomposition en Valeurs Singulières complète d'une matrice réelle $A \in \mathbb{R}^{m \times n}$ est donnée par :
$$A = U \Sigma V^T$$

Où :
- $U \in \mathbb{R}^{m \times m}$ est une matrice orthogonale dont les colonnes sont les vecteurs propres de $A A^T$ (vecteurs singuliers à gauche).
- $V \in \mathbb{R}^{n \times n}$ est une matrice orthogonale dont les colonnes sont les vecteurs propres de $A^T A$ (vecteurs singuliers à droite).
- $\Sigma \in \mathbb{R}^{m \times n}$ est une matrice diagonale contenant les valeurs singulières $\sigma_i = \sqrt{\lambda_i}$, ordonnées telles que $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$.

---

### Étapes du Déroulement Mathématique

1. **Calcul de la Transposée et des Produits Matriciels :** 
   - Calcul de $A^T$ 
   - Calcul des matrices symétriques $A^T A$ et $A A^T$ 

2. **Calcul des Vecteurs Singuliers à Droite ($V$) et des Valeurs Singulières ($\Sigma$) :** 
   - Résoudre l'équation caractéristique $\det(A^T A - \lambda I) = 0$ pour déterminer les valeurs propres $\lambda_i$.
   - Calculer les valeurs singulières $\sigma_i = \sqrt{\lambda_i}$.
   - Trouver les vecteurs propres normalisés de $A^T A$ pour construire $V$ (et $V^T$).

3. **Calcul des Vecteurs Singuliers à Gauche ($U$) :** 
   - Résoudre $\det(A A^T - \lambda I) = 0$ ou utiliser la relation $u_i = \frac{1}{\sigma_i} A v_i$.
   - Construire la matrice $U$ à partir des vecteurs propres normalisés.

4. **Réduction de Dimension (SVD Tronquée à $k=2$) :**
   - Conserver les $k=2$ plus grandes valeurs singulières ainsi que leurs colonnes/lignes correspondantes dans $U, \Sigma, V^T$ :
     $$A' = U_k \Sigma_k V_k^T$$

5. **Prédiction des Notes :**
   - La matrice reconstruite $A'$ fournit les estimations de toutes les notes manquantes (entrées à zéro) de $A$.
