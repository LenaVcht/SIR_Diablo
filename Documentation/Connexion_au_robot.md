# **Connexion au robot**

<p align="center">
  <img src="images/Comment ajouter le jeu Google Chrome Dinosaur à votre Android.jpg" width="500">
</p>

## **Sommaire**

- [Connexion HDMI](#Connexion-HDMI)
- [Connexion SSH](#Connexion-SSH)
- [Connexion VNC](#Connexion-VNC)
- [Connexion mmWaves](#Connexion-mmWaves)
- [Annexes](#Annexes)
- [Bibliographie](#Bibliographie)

## **Connexion HDMI**

La méthode la plus simple pour se connecter au robot est d'utiliser un écran, un câble HDMI to mini HDMI, une souris et un clavier. Ensuite il faut juste connecter tous les périphériques au Raspberry Pi et on a accès au système d'exploitaton du robot comme sur un ordinateur classique. Cette méthode est utile pour pouvoir mettre en place les autres types de connexion sans fil.

## **Connexion SSH**

La connexion SSH permet d'ouvrir un terminal du robot depuis un autre ordinateur.

Tout d'abord, il faut **vérifier que SSH est bien activé** sur le Raspberry et l'ordinateur.

Sur **windows**, SSH est généralement activé par défault. Pour vérifier :
```powershell
ssh
```

Sur **linux** (ce qui est le cas du Raspberry), il faut executer la commande :
```bash
sudo systemctl status ssh
```
Si il n'y a pas d'erreur, c'est que SSH est activé, sinon il faut **activer SSH**. Pour cela il existe plusieurs méthodes :

**Méthode 1 :**

Sur le Raspberry Pi, on  ouvre un terminal et exécute :
```bash
sudo raspi-config
```
Puis:
1. Aller dans Interface Options → SSH.
2. Sélectionner Yes pour activer SSH.
3. Quitter et redémarrer le Raspberry Pi :
```bash
sudo reboot
```

**Méthode 2 :**

Si raspi-config n'est pas disponible, il faut activer SSH manuellement :
```bash
sudo systemctl enable ssh
sudo systemctl start ssh
```
Puis on vérifie que ssh est bien activé :
```bash
sudo systemctl status ssh
```

Une fois activé, on peut se **connecter en SSH** avec un ordinateur, il suffit d'ouvrir un terminal est exécuter :
```bash
ssh diablo@<IP_DU_RASPBERRY>
```

Mais avant cela, il faut que l'ordinateur et le Raspberry soient connecté au même réseau, soit par ethernet, soit via wifi.

### **Ethernet**

En ethernet, c'est très simple, il suffit de connecte le robot et l'ordinateur avec un câble ethernet.

### **Wifi (eduroam)**

En wifi c'est plus compliqué, car le robot est sous linux. Il faut :
1. Télécharger l'installeur eduroam python sur ce lien : https://cat.eduroam.org/
2. Executer le fichier python et rentrer l'identifiant (première lettre du prénom + nom + @insa-lyon.fr) et le mdp de connexion.
3. Rajouter : les paramètres nécesssaire de la connexion (Authentification ...)
4. Connecte le robot à eduroam.

Une fois le robot et l'ordinateur connectés, que cela soit en wifi ou ethernet, il faut récupérer l'adresse ip. Pour cela on execute :
```bash
ifconfig
```

Voici ce que l'on obtient :
<p align="center">
  <img src="images/ifconfig.png" width="500">
</p>

Il faut prendre l'adresse ip de l'interface wlan0 pour le wifi ou eth0 pour ethernet.

Enfin, pour démarrer la connexion SSH, on execute la commande :
```bash/powershell
ssh diablo@<IP_DU_RASPBERRY>
```
> Le mot de passe est : diablo123

A rajouter : aperçu final du terminal

## **Connexion VNC**

Il est également possible de faire un déport d'affichage complet grâce à une connexion VNC. Ainsi, on a accès au bureau complet du Raspberry comme si on y était connecté en HDMI. Pour établir cette connexion, nous avons utilisé TigerVNC. Mais le problème était que c'était beaucoup trop lent. Charger une page internet prenait plusieurs minutes, donc nous avons abandonné cette solution.

## **Connexion mmWaves**

Cette partie est juste une agrégation de nos recherches menées sur la connexion en mmWave et comment il serait possible de la mettre en oeuvre. Jamais nous n'avons pu experimenter cette connexion avec du vrai hardware, il est donc possible que la solution présentée ne soit pas fonctionnelle, d'ailleurs certains de nos problèmes sont restés sans réponses. Cette documentation s'appuie sur les manuels officiels et ouvre la voie vers de futurs experimentations potentielles.

### **Modem EM9190**

<p align="left">
  Pour établir une connexion en mmWaves, nous utilisons un modem 5G EM9190 de la marque Sierra Wireless (le manuel de l'EM9190 se trouve dans le dossier "manuels"). 
  Ce module prend en charge plusieurs types de transmission, mais nous nous concentrerons uniquement sur la partie relative à la transmission mmWave.

Le tableau ci-dessous répertorie les bandes de fréquences prises en charge par le module Sierra Wireless. Pour une transmission mmWave, les bandes prises en charges sont n257, n258, n260 et n261. On a également les   capacités DL(reception)/UL(émission).

<p align="center">
  <img src="images/CarammWaves.PNG" width="700">
</p>

Voici les caractéristiques de chaque bande à notre disposition :

n257 : Fréquence : 26,5 GHz – 29,5 GHz.

n258 : Fréquence : 24,25 GHz – 27,5 GHz.

n260 : Fréquence : 37 GHz – 40 GHz.

n261 : Fréquence : 27,5 GHz – 28,35 GHz.

Ces bandes sont particulièrement adaptées aux déploiements en milieu urbain dense et aux scénarios exigeant des débits élevés, tels que les environnements industriels ou les stades. Cependant, notre projet se concentre spécifiquement sur l'utilisation de la bande des 26 GHz, correspondant à la bande **n258**.

<p align="center">
  <img src="images/EM9190connector.PNG" width="500">
</p>
  
Le modem dispose de plusieurs types de connecteurs, chacun ayant une utilité spécifique :
  
- **1 connecteur M.2** : interface utilisée pour connecter le périphérique à un hôte, comme un ordinateur (voir Annexe 1).
- **4 connecteurs RF MHF4** : dédiés à la transmission via LTE/Sub-6/GNSS, désignés comme suit : MAIN, MIMO1, AUX/GNSS L1, MIMO2/GNSS L5.
- **8 connecteurs IF** : destinés à la transmission via mmWaves, identifiés par les ports suivants : IFH1, IFV1, IFH2, IFV2, IFH3, IFV3, IFH4, IFV4.

### **Module d'antenne QTM525**

Le modem permet de connecter jusqu'à 4 modules d'antennes mmWaves, chaque module étant relié par 2 câbles : l’un à une entrée IFH (Horizontale) et l’autre à une entrée IFV (Verticale). Les modules d'antennes compatibles avec le modem EM9190 sont les modèles QTM525 et QTM527, la principale différence résidant dans leur puissance d'émission. L'utilisation de 4 antennes n'est pas obligatoire, notamment avec le module QTM525, mais il est impératif de respecter l’assignation correcte des ports mmWave dans chaque configuration (voir Annexe 1).

Dans le cadre d'une expérimentation simplifiée, nous proposons de commencer avec un seul module QTM525. Par conséquent, cette section se concentrera uniquement sur l’utilisation du module QTM525 (le manuel du QTM525 est lui aussi disponible dans le dossier "manuels").

<p align="center">
  <img src="images/QTM525.jpg" width="300"> <img src="images/QTM525schema.PNG" width="500">
</p>

Il existe deux variantes, QTM525-2 et QTM525-5, mais ça n'a peut d'incidence car les deux peuvent oppérer sur la bande n258 (pour plus de caractéristiques sur le module d'antenne voir Annexe 2).

On peut observer ci-dessus la face avant du module d'antenne QTM525, comprenant le connecteur et ses 10 broches. Pour notre projet, seules 5 broches sont nécessaires :
- Les deux premières broches, IF1 et IF2, seront connectées aux connecteurs IF du modem à l'aide de câbles coaxials MHF7S.
- Deux autres broches, VPH et VDD, seront utilisées pour l'alimentation.
- Enfin, la broche PON servira à activer un composant du module d'antenne.

<p align="center">
  <img src="images/QTM525Pin.PNG" width="520"> <img src="images/Pin2.PNG" width="400">
</p>

La connexion des broches est assurée par le module IPEX MPN 20865-010E-01, monté sur le QTM525. Ce module est composé de deux parties, la première est intégrée au QTM525, tandis que la seconde est un élément distinct permettant de fixer les fils sur les broches en s’emboîtant sur la première partie (les manuels du module sont disponibles dans le dossier "manuels").

<p align="center">
  <img src="images/Modulebroche.PNG" width="300">
</p>

### **Mise en place**

Voici la mise en place d'un système de transmission en mmWaves avec le module EM9190.

<p align="center">
  <img src="images/Mise en place.PNG" width="600">
</p>

- Les connecteurs coaxials MHF7S sont reliés au connecteur IF du modem EM9190.
- Le premier connecteur d'alimentation VDC power est raccordé à une tension de 3,7 volts.
- Le deuxième connecteur d'alimentation QTM_IO_1.9V est connecté au modem EM9190, au niveau du port M.2.
- Chaque connecteur QTMx_PON est également relié au modem EM9190, au niveau du port M.2.

### **Difficultés rencontrées**

Maintenant que nous savons comment tout mettre en place, il faut trouver le hardware compatible, c'est justement cela qui nous a posé des difficultés.

#### **Connexion à l'hôte**

Le premier problème concerne la connexion à l'hôte. Elle se réalise via un connecteur M.2, ce connecteur est couramment utilisé dans les ordinateurs modernes pour connecter des composants tels que des disques SSD, des cartes réseau sans fil et d'autres périphériques d'extension. La carte réseau EM9190 utilise un connecteur **M.2 3042-S3 Type B** spécéfique aux modules **WWAN** et supporte les interfaces **PCIe et USB3**.

Ainsi, pour intégrer l'EM9190 avec un ordinateur ou une carte Raspberry, il est nécessaire d'avoir un port **M.2 Type B**, compatible avec les interfaces **PCIe ou USB** et compatible également avec une utilisation réseau **WWAN**.

Lors de nos recherches pour trouver une carte d'extension compatible avec le Raspberry Pi 4B, **nous n'avons pas trouvé de modèles compatibles**.

Malgré tout, nous avons quelques pistes :

La première piste est le manuel **dev kit de Sierra Wireless** (disponible dans le dossier "manuels). Mais le manuel ne fait pas mention des modules d'antennes spécifiques à l'utilisation des mmWaves. Il reste alors encore la question de savoir comment alimenter l'antenne en 3.7V et comment connecter les broches QTM_PON et QTM_IO_1.9V au connecteur M.2.

Il existe aussi des adaptateurs **M.2 Type B vers USB3**, spécifique pour la transmition 3G/4G/5G, mais il reste encore la même question de l'alimentation et de la connection des broches. Voici le lien vers l'adaptateur : https://www.newegg.com/p/3C6-01NE-000M2

#### **Connecteurs MHF7S**

Le deuxième problème concerne les connecteurs MHF7S nécessaire à la connexion du module d'antenne. Le manuel préconise d'utiliser des câbles MHF7S I-PEX, mais le constructeur ne fait que des câbles coaxials supportant maximum 15GHz, ce qui est insufisant pour l'utilisation de la bande 26GHz.

## **Annexes**

### **Annexe 1**

<p align="center">
  <img src="images/Annexe1.PNG" width="500">
</p>

### **Annexe 2**

<p align="center">
  <img src="images/OverviewQTM525.PNG" width="500">
</p>

<p align="center">
  <img src="images/CaraQTM25.PNG" width="500">
</p>

<p align="center">
  <img src="images/Cara2QTM525.PNG" width="500">
</p>

## **Bibliographie**

### **Connexion mmWaves**

SIte du manuel de l'EM9190 : \
https://manuals.plus/sierra-wireless/airprime-em9190-5g-module-manual \

Site de sierra-wireless : \
https://source.sierrawireless.com/devices/em-series/em9190/#sthash.LF0QUKzM.eMAEwvXY.dpbs

