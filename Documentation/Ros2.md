## **Sommaire**

- [Prérequis](#Prérequis)
- [Commandes Terminal](#Commandes-Terminal)
- [Contrôle depuis le clavier](#Contrôle-depuis-le-clavier)
- [Récupération d'informations depuis le robot](#Récupération-d'informations-depuis-le-robot)
- [Bibliographie](#Bibliographie)

## **Prérequis**

L'ensemble d'outils informatiques Ros2 est installé sur le robot Diablo. Il permet de publier des messages dans des topics à partir du terminal ou d'un script Python ou C++. Afin de travailler sur des scripts depuis son ordinateur, il est nécessaire d'installer ros2 foxy sur sa machine. Ensuite, il faut clôner le dépôt git officiel du robot Diablo. Vous trouverez ci-dessous les liens utilisés:

- https://docs.ros.org/en/foxy/index.html
- https://github.com/DDTRobot/diablo_ros2

A noter que ros2 foxy fonctionne sous ubuntu 20.04 et windows. Vous trouverez également des tutoriels ros2 utiles pour la prise en main de cet outil.

## **Commandes Terminal**

## **Contrôle depuis le clavier**

Vous pouvez ensuite utiliser le package ros2 avec un node publisher python disponible sur ce dépôt pour contrôler le robot à partir de votre clavier. Le publisher publie des requêtes de mouvement sur le topic MotionCtrl de motion_msgs.msg. Afin de visualiser ces messages dans un terminal, vous pouvez utiliser la commande suivante: ros2 topic echo /diablo/MotionCmd. 

Le script utilise plusieurs librairies python:

- rclpy: Bibliothèque principale de ROS 2,
- rclpy.node, Node: Classe de base pour créer un nœud ROS 2,
- motion_msgs.msg, MotionCtrl: Message utilisé pour envoyer les commandes au robot,
- sys: Module système pour interagir avec le terminal
- termios: Pour gérer le mode "raw" du terminal
- tty: Pour capturer les touches pressées sans appuyer sur Entrée

## **Récupération d'informations depuis le robot**

## **Bibliographie**

