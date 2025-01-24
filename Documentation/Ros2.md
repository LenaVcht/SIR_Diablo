## **Sommaire**

- [Prérequis](#Prérequis)
- [Simulations](#Simulations)
- [Commandes Terminal](#Commandes-Terminal)
- [Contrôle depuis le clavier](#Contrôle-depuis-le-clavier)
- [Récupération d'informations depuis le robot](#Récupération-d'informations-depuis-le-robot)
- [Bibliographie](#Bibliographie)

## **Prérequis**

L'ensemble d'outils informatiques Ros2 est installé sur le robot Diablo. Il permet de publier des messages dans des topics à partir du terminal ou d'un script Python ou C++. Afin de travailler sur des scripts depuis son ordinateur, il est nécessaire d'installer ros2 foxy sur sa machine. Ensuite, il faut clôner le dépôt git officiel du robot Diablo. Vous trouverez ci-dessous les liens utilisés:

- https://docs.ros.org/en/foxy/index.html
- https://github.com/DDTRobot/diablo_ros2

A noter que ros2 foxy fonctionne sous ubuntu 20.04 et windows. Vous trouverez également des tutoriels ros2 utiles pour la prise en main de cet outil. ROS 2 Foxy est officiellement compatible avec Python 3.8, car cette version est celle incluse par défaut dans Ubuntu 20.04. 
Pour installer cette version de python, il faut lancer les commandes suivantes dans un terminal sous linux:

```bash
sudo apt update
sudo apt install python3.8 python3.8-venv python3.8-dev
```

Vous pouvez aussi l'installer directement depuis le site de python:
- https://www.python.org/downloads/

## **Simulations**

## **Commandes Terminal**

## **Contrôle depuis le clavier**

Vous pouvez ensuite utiliser le package ros2 avec un node publisher python disponible sur ce dépôt pour contrôler le robot à partir de votre clavier. Le publisher publie des requêtes de mouvement sur le topic MotionCtrl de motion_msgs.msg. Afin de visualiser ces messages dans un terminal, vous pouvez utiliser la commande suivante: ros2 topic echo /diablo/MotionCmd. 

### Librairies utilisées

Le script utilise plusieurs librairies python:

- rclpy: Bibliothèque principale de ROS 2,
- rclpy.node, Node: Classe de base pour créer un nœud ROS 2,
- motion_msgs.msg, MotionCtrl: Message utilisé pour envoyer les commandes au robot,
- sys: Module système pour interagir avec le terminal
- termios: Pour gérer le mode "raw" du terminal
- tty: Pour capturer les touches pressées sans appuyer sur Entrée

### Contenu d'un package Ros2

### Fonctionnement du code

La classe "KeyboardNodeControl" est la classe principale pour contrôler le robot depuis le clavier. Plusieurs fonctions et méthodes sont mises en place dans le publisher:

- init dans la classe "KeyboardNodeControl": initialise le noeud, crée un publisher et initialise les paramètres du robot Diablo.
- get_key dans la classe "KeyboardNodeControl": capture une touche pressée sur le clavier sans appuyer sur Entrée. Utilise les librairies sys, tty et termios.
- run_keyboard_control dans la classe "KeyboardNodeControl": exécute le contrôle clavier. Il crée les messages MotionCmd, lit les caractères appuyés et publie les messages sur le topic.
- main: initialise ros2, crée une instance de la classe KeyboardControlNode, exécute le nœud (boucle ROS 2), détruit le nœud proprement et ferme ros2.
  
## **Récupération d'informations depuis le robot**

## **Bibliographie**
Manuel du robot Diablo
https://diablo-sdk-docs.readthedocs.io/en/latest/index.html

Site du constructeur du robot Diablo
https://directdrive.com/

Documentation ros2 foxy
https://docs.ros.org/en/foxy/index.html

Dépôt git du robot Diablo
https://github.com/DDTRobot/diablo_ros2/blob/main/docs/docs_en/README_EN.md

Installation de python
https://www.python.org/downloads/


