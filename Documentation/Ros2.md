L'ensemble d'outils informatiques Ros2 est installé sur le robot Diablo. Il permet de publier des messages dans des topics à partir du terminal ou d'un script Python ou C++. Afin de travailler sur des scripts depuis son ordinateur, il est nécessaire d'installer ros2 foxy sur sa machine. Ensuite, il faut clôner le dépôt git officiel du robot Diablo. Vous trouverez ci-dessous les liens utilisés:

- https://docs.ros.org/en/foxy/index.html
- https://github.com/DDTRobot/diablo_ros2

A noter que ros2 foxy fonctionne sous ubuntu 20.04 et windows. Vous trouverez également des tutoriels ros2 utiles pour la prise en main de cet outil.

Vous pouvez ensuite utiliser le package ros2 avec un publisher disponible sur ce dépôt pour contrôler le robot à partir de votre clavier. Le publisher publie des requêtes de mouvement sur le topic MotionCtrl de motion_msgs.msg.

