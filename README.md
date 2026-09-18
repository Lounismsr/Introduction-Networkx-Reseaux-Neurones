# Introduction à NetworkX et les réseaux de neurones

Mini-projet de fin de cycle — Licence en Mathématiques Appliquées
Université Abderrahmane Mira de Béjaïa, Faculté des Sciences Exactes,
Département de Recherche Opérationnelle
Année universitaire 2023–2024

**Présenté par :** Mesrour Lounis, Mokhtari Anis Badredine, Ourtilane Mohand
**Sous la direction de :** Mlle Aoudia

## 📄 Contenu

Ce projet explore deux domaines des mathématiques appliquées et de
l'informatique :

1. **La théorie des graphes** — définitions, types de graphes (orienté,
   complet, biparti, pondéré...), propriétés (ordre, degré, cycles),
   représentations matricielles, algorithmes classiques (DFS/BFS, plus
   courts chemins).
2. **NetworkX** — création, manipulation et visualisation de graphes
   avec cette bibliothèque Python.
3. **Les réseaux de neurones** — modélisation du neurone biologique et
   artificiel, fonctions d'activation (sigmoïde, ReLU), architectures
   (feedforward, RNN), apprentissage profond.
4. **Application pratique** — création d'un réseau de neurones avec
   Keras (régression sur des données bruitées) puis visualisation de
   son architecture avec NetworkX et Matplotlib.

## 📁 Structure du dépôt

```
.
├── rapport.pdf                        # Rapport complet du mini-projet
├── presentation.pptx                  # Support de soutenance
├── creation_reseau_neurones.py        # Création et entraînement du modèle Keras
├── visualisation_networkx.py          # Visualisation du réseau avec NetworkX
├── requirements.txt                   # Dépendances Python
└── README.md
```

## 🚀 Utilisation

```bash
pip install -r requirements.txt

python creation_reseau_neurones.py   # entraîne le modèle et affiche les résultats
python visualisation_networkx.py     # affiche la structure du réseau
```

## 🧠 Architecture du réseau

- Couche d'entrée : 1 neurone linéaire
- Couche cachée 1 : 10 neurones ReLU
- Couche cachée 2 : 10 neurones ReLU
- Couche de sortie : 1 neurone linéaire

Le réseau est entraîné à approximer la fonction `y = 0.1*x*cos(x)` à
partir de données bruitées, avec l'optimiseur Adam et une perte MSE.

## 📚 Références

Voir la bibliographie complète dans le rapport (`rapport.pdf`).

## 📝 Note

Ce projet a été réalisé dans le cadre de la Licence (2023-2024) et est
partagé ici à titre de portfolio académique.
