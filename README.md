# Python Snake game

## Français
Ce projet reflète l'évolution du développement d'un jeu snake multi-joueurs.

- Développement de la logique en console
- Ajout des graphisme 2D avec la bibliothèque Pygame
- Ajout du réseau (utilisation de sockets)

#### Prérequis
- Installation de Python
- Installation de NumPy
- Installation de Pygame pour les jeux autres que celui en console

### Jeu en console
- Pour lancer le jeu en console : aller dans le dossier "executables" et lancer "run_console.bat".

### Jeu solo
- Pour lancer le jeu : aller dans le dossier "executables/graphic" et lancer le fichier "main.py".


### Jeu multi-joueurs
- Attention, vous devez préciser l'adresse ip du serveur. Pour celà, rendez-vous dans le fichier "executables/graphic_with_network/ConstantVariables.py". Vous y trouverez : 
    - NETWORK_IP = "127.0.0.1" - remplacer 127.0.0.1 par l'adresse ip de votre serveur
- Pour lancer le serveur : aller dans le dossier "executables/graphic_with_network", exécuter le fichier "main_server.py".
- Pour lancer un client : aller dans le dossier "executables/graphic_with_network", exécuter le fichier "main_client.py".

#### Remarques
- Les autres dossiers ont été utilisés pour simplifier le développement