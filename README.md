# Python Snake game

## Français
Ce projet contient l'évolution du développement d'un jeu snake multi-joueurs.

- Développement de la logique en console
- Ajout des graphisme 2D avec la librery Pygame
- Ajout du réseau avec les sockets

#### Prérequis
- Installation de Python
- Installation de Pygame pour les jeux autre que celui en console

### Jeu en console
- Pour lancer le jeu en console : aller dans le dossier "executables" et lancer "run_console.bat".

### Jeu solo
- Pour lancer le jeu : allez dans le dossier "executables/graphic", ouvrez une invite de commandes et glisser le fichier "main.py" dedans.


### Jeu multi-joueurs
- Attention, vous devez changer l'ip du server, pour celà rendez-vous dans le fichier "executables/graphic_with_network/ConstantVariables.py". Vous y trouverez : 
    - NETWORK_IP = "127.0.0.1" - remplacer 127.0.0.1 par l'IP de votre serveur
- Pour lancer le server : allez dans le dossier "executables/graphic_with_network", ouvrez une invite de commandes et glisser le fichier "main_server.py" dedans.
- Pour lancer un client : allez dans le dossier "executables/graphic_with_network", ouvrez une invite de commandes et glisser le fichier "main_client.py" dedans.

#### Remarques
- Les autres dossiers ont été utilisé pour simplifier le développent