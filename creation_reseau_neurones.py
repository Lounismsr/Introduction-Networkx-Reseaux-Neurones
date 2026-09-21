"""
Création et entraînement d'un réseau de neurones simple avec Keras.

Ce script génère un jeu de données bruité, construit un réseau de
neurones feedforward (2 couches cachées de 10 neurones ReLU), l'entraîne
puis affiche la comparaison entre les données réelles et la prédiction.

Issu du projet "Introduction à NetworkX et les réseaux de neurones"
(Licence Mathématiques Appliquées, Université de Béjaïa, 2023-2024).
"""

import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras


def creer_donnees(n_points=1000):
    """Génère un jeu de données bruité: y = 0.1*x*cos(x) + bruit."""
    x_data = np.linspace(-10, 10, num=n_points)
    y_data = 0.1 * x_data * np.cos(x_data) + 0.1 * np.random.normal(size=n_points)
    return x_data, y_data


def creer_modele():
    """Construit le réseau de neurones feedforward.

    Architecture :
    - Couche d'entrée : 1 neurone linéaire
    - Couche cachée 1 : 10 neurones ReLU
    - Couche cachée 2 : 10 neurones ReLU
    - Couche de sortie : 1 neurone linéaire
    """
    model = keras.Sequential()
    model.add(keras.layers.Dense(units=1, activation="linear", input_shape=[1]))
    model.add(keras.layers.Dense(units=10, activation="relu"))
    model.add(keras.layers.Dense(units=10, activation="relu"))
    model.add(keras.layers.Dense(units=1, activation="linear"))
    model.compile(loss="mse", optimizer="adam")
    return model


def main():
    # 1. Génération des données
    x_data, y_data = creer_donnees()
    print("Données créées avec succès")

    plt.figure()
    plt.scatter(x_data, y_data, s=5)
    plt.grid()
    plt.title("Données d'entraînement bruitées")
    plt.savefig("donnees_bruitees.png", dpi=150)
    plt.show()

    # 2. Création et résumé du modèle
    model = creer_modele()
    model.summary()

    # 3. Entraînement
    model.fit(x_data, y_data, epochs=700, verbose=1)

    # 4. Prédiction et affichage du résultat
    y_predicted = model.predict(x_data)

    plt.figure()
    plt.scatter(x_data, y_data, s=5, label="Données réelles")
    plt.plot(x_data, y_predicted, "r", linewidth=4, label="Prédiction du modèle")
    plt.grid()
    plt.legend()
    plt.title("Résultat de l'apprentissage")
    plt.savefig("resultat_apprentissage.png", dpi=150)
    plt.show()

    # Sauvegarde du modèle entraîné (optionnel)
    model.save("modele_reseau_neurones.keras")


if __name__ == "__main__":
    main()
