import numpy as np
import math

# 1. Définition de la matrice initiale des notes A
A = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [1, 0, 0, 4]
], dtype=float)

# 2. Calcul des matrices symétriques
A_T = A.T
A_TA = A_T @ A
AA_T = A @ A_T

# 3. Décomposition propre de A^T * A pour V et Sigma
valeurs_propres_ATA, vecteurs_propres_ATA = np.linalg.eigh(A_TA)

# Tri décroissant des valeurs propres et vecteurs propres
indices_v = np.argsort(valeurs_propres_ATA)[::-1]
valeurs_propres_ATA = valeurs_propres_ATA[indices_v]
V = vecteurs_propres_ATA[:, indices_v]
V_T = V.T

# Calcul des valeurs singulières et construction de la matrice S (Sigma)
valeurs_singulieres = [math.sqrt(max(0, val)) for val in valeurs_propres_ATA]
S = np.diag(valeurs_singulieres)

# 4. Décomposition propre de A * A^T pour U
valeurs_propres_AAT, vecteurs_propres_AAT = np.linalg.eigh(AA_T)
indices_u = np.argsort(valeurs_propres_AAT)[::-1]
U = vecteurs_propres_AAT[:, indices_u]

# 5. Réduction de dimension avec k = 2
k = 2
U_2 = U[:, :k]
S_2 = S[:k, :k]
VT_2 = V_T[:k, :]

# 6. Reconstruction de la matrice approximée A'
A_prime = U_2 @ S_2 @ VT_2

print("Matrice de notes approximée A':")
print(np.round(A_prime, 2))
