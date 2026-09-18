"""
Visualisation de la structure d'un réseau de neurones avec NetworkX.

Ce script construit un graphe orienté représentant l'architecture d'un
réseau de neurones (couches et connexions) et l'affiche avec Matplotlib.

Issu du mini-projet "Introduction à NetworkX et les réseaux de neurones"
(Licence Mathématiques Appliquées, Université de Béjaïa, 2023-2024).
"""

import networkx as nx
import matplotlib.pyplot as plt


def construire_graphe(layers, num_neurons, layer_shift=50):
    """Construit un graphe orienté représentant les couches du réseau.

    Args:
        layers: liste des noms de couches, ex. ['entree', 'cache1', 'cache2', 'sortie']
        num_neurons: liste du nombre de neurones par couche, ex. [1, 10, 10, 1]
        layer_shift: décalage horizontal entre les couches sur le graphe

    Returns:
        Un graphe networkx.MultiDiGraph avec les nœuds positionnés par couche.
    """
    G = nx.MultiDiGraph()

    # Ajout des nœuds pour chaque couche
    for i, layer in enumerate(layers):
        for j in range(num_neurons[i]):
            node_label = f"{layer} {j}"
            G.add_node(node_label, layer=layer, pos=(layer_shift * i, j))

    # Ajout des connexions entre couches successives
    for i in range(len(layers) - 1):
        current_layer, next_layer = layers[i], layers[i + 1]
        for j in range(num_neurons[i]):
            for k in range(num_neurons[i + 1]):
                current_node = f"{current_layer} {j}"
                next_node = f"{next_layer} {k}"
                G.add_edge(current_node, next_node)

    return G


def main():
    layers = ["entree", "cache1", "cache2", "sortie"]
    num_neurons = [1, 10, 10, 1]  # Nombre de neurones par couche

    G = construire_graphe(layers, num_neurons)

    pos = nx.get_node_attributes(G, "pos")
    plt.figure(figsize=(10, 6))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=1200,
        node_color="white",
        edgecolors="black",
        width=1,
        font_size=6,
    )
    plt.title("Réseau de neurones avec NetworkX")
    plt.savefig("reseau_networkx.png", dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
