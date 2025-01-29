# **Ros2**

<p align="center">
  <img src="https://i.pinimg.com/736x/f6/b7/c1/f6b7c140e4021f3c18b5ee5f384b9e15.jpg" width="300">
</p>

## **Sommaire**

- [Prérequis](#Prérequis)
- [Simulations](#Simulations)
- [Contrôle du robot](#Contrôle-du-robot)
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

Plusieurs simulations sont disponibles pour le robot Diablo. Directement dans le dépôt git du robot, vous avez accès à une simulation Gazebo

```bash
ros2 launch diablo_simulation gazebo.launch.py
```

et Rviz:

```bash
ros2 launch diablo_simulation ctrl.launch.py
```

La simulation Rviz permet, d'après le manuel, un contrôle à distance du robot Diablo à partir d'une interface graphique.

Enfin, vous pouvez utiliser une simulation webots à partir de ce dépôt git: 

- https://github.com/DDTRobot/diablo-sim-env?fbclid=IwZXh0bgNhZW0CMTEAAR0VCfyuZYg65ZIq-W_xi4qtQ5oT87qn8WLMNCBjYjokxaqp7opFCDM8sLA_aem_3PPM0bA57FoDw7_OOmJBoA

## **Contrôle du robot**

Mais ce qui nous intéresse réellement, c'est bien sûr de pouvoir contrôler le robot directement depuis notre ordinateur. Pour cela, plusieurs possibilités : on peut lui envoyer des lignes de commandes directement depuis le terminal de notre ordinateur, ou encore éxécuter un script qui nous permettra de le contrôler depuis certaines touches de notre clavier.

Mais ces méthodes différentes nécessitent la même préparation pour fonctionner dans notre environnement de travail.

Tout d'abord, une fois que le robot est connecté au même réseau (Wi-Fi) que nous, il nous faut son adresse IP. Dans notre exemple, elle se présente sous cette forme : **10.56.12.225**. 
On peut alors s'y conecter grâce à la commande suivante :

```bash
ssh diablo@10.56.12.225
```
*On nous demande alors un mot de passe qui dans le cas de cette connexion est **diablo123**.*

Une fois connectés, notre terminal devient un terminal du robot. Il est maintenant possible d'accéder à tous les packages et noeuds ros2 installés sur le robot depuis ce même terminal.

Avant de lancer le code python ou n'importe quel autre commande, il faut sourcer son environnement depuis le dossier diablo_ws :

```bash
source install/setup.bash
```

Enfin, il est possible de lancer le noeud qui permet le contrôle du robot :

```bash
ros2 run diablo_ctrl ciablo_ctrl_node
```

Le robot est alors prêt à recevoir des commandes !

### **Commandes Terminal**

Une fois cete préparation effectuée, on peut ouvrir un second terminal (également connecté au robot) afin de lui envoyer des commandes. 

#### Etablir la structure des messages

Tout d'abord, il faut que l'on récupère la forme des messages compris par le robot. En étudiant la structure des paquets du robot, on peut déduire que les messages de commande sont échangés sur le topic **/diablo/MotionCmd**. On peut alors utiliser la commande suivante : 

```bash
ros2 topic type /diablo/MotionCmd
```

Cette commande nous permet d'obtenir le type de messages échangés sur le topic : **motion_msgs/msg/MotionCtrl**. Avec la commande suivante, on pourra obtenir la structure précise de ces messages : 

```bash
ros2 interface show motion_msgs/msg/MotionCtrl
```
Ce qui nous renvoie quelque chose sous cette forme : 

```bash
bool mode_mark

MovementCtrlData value
MovementCtrlMode mode
```

Pour avoir plus de détails sur cette structure (ce qui est compris dans les **MovementCtrlData** et **MovementCtrlMode** par exemple), on peut également écouter directement le topic pour analyser les messages que l'on voit passer. On utilise cette commande :

```bash
ros2 topic echo /diablo/MotionCmd
```

Voici la structure précise des messages que l'on observe : 

```bash
{
  mode_mark: false,
  value: {
    forward: 0.0,
    left: 0.0,
    up: 0.0,
    roll: 0.0,
    pitch: 0.0,
    leg_split: 0.0
  },
  mode: {
    pitch_ctrl_mode: false,
    roll_ctrl_mode: false,
    height_ctrl_mode: false,
    stand_mode: false,
    jump_mode: false,
    split_mode: false
  }
}
```

#### Envoyer nos propres messages

Maintenant que l'on connaît la structure des messages envoyés au robot, il ne reste plus qu'à publier nos propres messages directement sur le topic. Pour cela, on va réutiliser la forme vue précédemment, mais en modifiant les valeurs des variables qui nous intéressent. 

Par exemple, si je veux que le robot tourne vers la gauche, je vais lui tenter de lui envoyer ce message : 


```bash
{
  mode_mark: false,
  value: {
    forward: 0.0,
    left: 1.0,
    up: 0.0,
    roll: 0.0,
    pitch: 0.0,
    leg_split: 0.0
  },
  mode: {
    pitch_ctrl_mode: false,
    roll_ctrl_mode: false,
    height_ctrl_mode: false,
    stand_mode: false,
    jump_mode: false,
    split_mode: false
  }
}
```

Pour envoyer ce message au robot, on utilise la commande suivante qui nous permet d'écrire dans le topic **/diablo/MotionCmd** :

```bash
ros2 topic pub /diablo/MotionCmd motion_msgs/msg/MotionCtrl [contenu du message]
```

Ce qui donne, avec notre message d'exemple :

```bash
ros2 topic pub /diablo/MotionCmd motion_msgs/msg/MotionCtrl "{mode_mark: false, value: {forward: 0.0, left: 1.0, up: 0.0, roll: 0.0, pitch: 0.0, leg_split: 0.0}, mode: {pitch_ctrl_mode: false, roll_ctrl_mode: false, height_ctrl_mode: false, stand_mode: false, jump_mode: false, split_mode: false}}"
```

Voilà maintenant notre robot qui se met à tourner sur lui-même, vers la gauche. Mais, comment l'arrêter ? En effet, même si l'on n'envoie qu'un seul message, l'information reste dans le robot jusqu'à être modifiée. Le robot tourne donc en continu. Pour le stopper, une seule possibilité, lui envoyer directement le message inverse. Dans notre exemple :

```bash
ros2 topic pub /diablo/MotionCmd motion_msgs/msg/MotionCtrl "{mode_mark: false, value: {forward: 0.0, left: 0.0, up: 0.0, roll: 0.0, pitch: 0.0, leg_split: 0.0}, mode: {pitch_ctrl_mode: false, roll_ctrl_mode: false, height_ctrl_mode: false, stand_mode: false, jump_mode: false, split_mode: false}}"
```

Cette méthode fonctionne donc pour envoyer des ordres simples au robot. Mais attention, si on lui donne l'ordre d'avancer, il faut être prêt à envoyer l'ordre de s'arrêter dans la foulée, ce qui peut s'avérer compliqué. Une méthode alternative plus intéressante serait de transformer notre clavier en télécommande en assignant des commande à nos différentes touches. C'est ce que nous allons présenter dans la partie suivante.

### **Contrôle depuis le clavier**

Pour cela, nous pouvons utiliser le package ros2 avec un node publisher python disponible sur ce dépôt : diablo_new_ctrl. Il permet de contrôler le robot à partir de votre clavier. Le publisher publie des requêtes de mouvement sur le topic MotionCtrl pour nous, en lisant les inputs de notre clavier.

#### Contenu du package diablo_new_ctrl

Un package ROS 2 est une unité de base qui contient du code, des fichiers de configuration, des messages, des services, des actions, des scripts, et toute autre ressource nécessaire pour créer une application ROS.Pour créer un package ros2, vous pouvez utiliser les commandes suivantes:

En python:

```bash
ros2 pkg create --build-type ament_python my_package
```

En C++:
```bash
ros2 pkg create --build-type ament_cmake my_package
```

A noter que le package doit être créé dans le dossier src du dossier diablo_ws sur le robot Diablo.

Voici les composants typiques que l'on trouve dans un package ROS 2 :

```bash
my_package/
├── CMakeLists.txt
├── package.xml
├── setup.py                # (Si c'est un package Python)
├── src/
│   └── my_package/
│       ├── __init__.py     # Fichier d'initialisation du package Python
│       └── my_node.py      # Exemple de script ROS 2
├── launch/
│   └── my_launch_file.py   # Fichier de lancement ROS 2
├── config/
│   └── params.yaml         # Fichier de configuration (paramètres)
├── msg/
│   └── MyCustomMessage.msg # Messages personnalisés (facultatif)
├── srv/
│   └── MyService.srv       # Services personnalisés (facultatif)
├── action/
│   └── MyAction.action     # Actions personnalisées (facultatif)
├── urdf/
│   └── robot.urdf          # Description du robot (format URDF ou xacro)
├── world/
│   └── my_world.world      # Fichiers de simulation (ex. Gazebo)
├── rviz/
│   └── my_config.rviz      # Configuration pour RViz
└── README.md               # Documentation du package
```

Le package diablo_new_ctrl contient les composants suivants:

```bash
diablo_new_ctrl/
├── package.xml
├── setup.py                # Nécessaire pour un package Python
├── diablo_new_ctrl/
│   ├── __init__.py     # Fichier d'initialisation du package Python
│   └── diablo_publisher.py      # Script python permettant le contrôle du robot Diablo
├── ressource/
│   ├── diablo_new_ctrl.txt    
├── test/
│   ├── test_copyright.py    
│   └── test_flake8.py
│   └── test_pep257.py      
```

*Remarque : Les fichiers package.xml et setup.py doivent être modifiés avec vos informations (nom, e-mail, etc...).*

#### Commandes à lancer en prérequis

Avant d'utiliser un package ros2, il faut le build en utilisant colcon:

```bash
colcon build --packages-select diablo_new_ctrl
```

Il faut également efectuer les commandes explicitées au début de la partie [Contrôle du robot](#Contrôle-du-robot) pour sourcer l'environnement, et lancer le noeud de contrôle du robot.

Enfin, il faut lancer le publisher avec la commande suivante:

```bash
ros2 run diablo_new_ctrl talker
```

Vous pouvez à présent contrôler le robot depuis votre clavier.

#### Librairies utilisées

Le script utilise plusieurs librairies python:

- rclpy: Bibliothèque principale de ROS 2,
- rclpy.node, Node: Classe de base pour créer un nœud ROS 2,
- motion_msgs.msg, MotionCtrl: Message utilisé pour envoyer les commandes au robot,
- sys: Module système pour interagir avec le terminal
- termios: Pour gérer le mode "raw" du terminal
- tty: Pour capturer les touches pressées sans appuyer sur Entrée

#### Fonctionnement du publisher diablo_publisher

La classe "KeyboardNodeControl" est la classe principale pour contrôler le robot depuis le clavier. Plusieurs fonctions et méthodes sont mises en place dans le publisher:

- init dans la classe "KeyboardNodeControl": initialise le noeud, crée un publisher et initialise les paramètres du robot Diablo.
- get_key dans la classe "KeyboardNodeControl": capture une touche pressée sur le clavier sans appuyer sur Entrée. Utilise les librairies sys, tty et termios.
- run_keyboard_control dans la classe "KeyboardNodeControl": exécute le contrôle clavier. Il crée les messages MotionCmd, lit les caractères appuyés et publie les messages sur le topic.
- main: initialise ros2, crée une instance de la classe KeyboardControlNode, exécute le nœud (boucle ROS 2), détruit le nœud proprement et ferme ros2.

Ainsi, le script capture les touches pressées sur le clavier, les lit, update le message MotionCmd à envoyer avant de le publier sur le topic, ce qui met le robot en mouvement. Le contrôle se fait en temps réel. Les fonctionnalités sont les suivantes:

- Avancer: flèche du haut,
- Reculer: flèche du bas,
- Tourner à droite: flèche de droite,
- Tourner à gauche: flèche de gauche,
- Augmenter la vitesse: +,
- Réduire la vitesse: -,
- m: mode marche,
- j: saut,
- s: mode split,
- Ctrl+C: quitter.

### **Récupération d'informations depuis le robot**

## **Bibliographie**

Manuel du robot Diablo
- https://diablo-sdk-docs.readthedocs.io/en/latest/index.html

Site du constructeur du robot Diablo
- https://directdrive.com/

Documentation ros2 foxy
- https://docs.ros.org/en/foxy/index.html

Dépôt git du robot Diablo
- https://github.com/DDTRobot/diablo_ros2/blob/main/docs/docs_en/README_EN.md

Installation de python
- https://www.python.org/downloads/

Simulation Webots du robot Diablo
- https://github.com/DDTRobot/diablo-sim-env?fbclid=IwZXh0bgNhZW0CMTEAAR0VCfyuZYg65ZIq-W_xi4qtQ5oT87qn8WLMNCBjYjokxaqp7opFCDM8sLA_aem_3PPM0bA57FoDw7_OOmJBoA

