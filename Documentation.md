# **Documentation du projet**

<p align="center">
  <img src="https://imgs.search.brave.com/zpZtoP-RhwrMHvearnpxKDSDop-nwRMeGeWOg9V80RM/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tbGZr/M2N2NXl2bnguaS5v/cHRpbW9sZS5jb20v/Y2I6Ym4tYi4yZmUy/MS93OjEyMDEvaDo2/MjcvcTptYXV0by9m/OmJlc3QvaHR0cHM6/Ly93d3cubmluamFv/bmUuY29tL3dwLWNv/bnRlbnQvdXBsb2Fk/cy8yMDI0LzEyL0hv/dy10by1FbmFibGUt/b3ItRGlzYWJsZS1G/aWxlLUhpc3Rvcnkt/aW4tV2luZG93cy0x/MS5wbmc" width="500">
</p>

## **Sommaire**
- Objectif de la documentation
- Le robot Diablo
- Connexion au robot
- Ross
- Bibliographie

## **Objectif de la documentation**

<p align="left">
  Dans le cadre de notre projet sur le robot Diablo, nous avons dû faire face à un matériel, un environnement et un langage nouveaux. Les objectifs étant encore loin d'être atteints, 
  nous avons jugé essentiel de créer une documentation solide pour permettre à de futurs étudiants de poursuivre ce travail. Nous avons donc mis un point d'honneur à rédiger une 
  documentation complète, claire et accessible. Une autre difficulté majeure réside dans l’exploitation des mmWaves et la compatibilité des modules 5G avec le robot. Ainsi, cette 
  documentation poursuit un double objectif : faciliter la prise en main du robot et ouvrir la voie à une connexion utilisant les mmWaves.
</p>

## **Le robot Diablo**

## **Connexion au robot**

### **Connexion ssh**

### **Connexion VNC**

### **Connexion mmWaves**

Cette partie est juste une agrégation de nos recherches menées sur la connexion en mmWave et comment il serait possible de la mettre en oeuvre. Jamais nous n'avons pu experimenter cette connexion avec du vrai hardware, il est donc possible que la solution présentée ne soit pas fonctionnelle. Cette solution s'appuie sur les manuels officiels que l'on a pu trouver pendant nos recherches et ouvre la voie vers de futurs experimentations.

**Hardware**

<p align="left">
  Pour établir une connexion en mmWaves, nous utilisons un modem 5G EM9190 de la marque Sierra Wireless (le manuel de l'EM9190 se trouve dans le dossier "manuel"). 
  Ce module prend en charge plusieurs types de transmission, mais nous nous concentrerons uniquement sur la partie relative à la transmission mmWave.
  
  Le modem dispose de plusieurs types de connecteurs, chacun ayant une utilité spécifique :
  
  <p align="center">
  <img src="images/EM9190connector.PNG" width="500">
  </p>
  
- **1 connecteur M.2** : interface utilisée pour connecter le périphérique à un hôte, comme un ordinateur (voir Annexe 1).
- **4 connecteurs RF MHF4** : dédiés à la transmission via LTE/Sub-6/GNSS, désignés comme suit : MAIN, MIMO1, AUX/GNSS L1, MIMO2/GNSS L5.
- **8 connecteurs MHF7S** : destinés à la transmission via mmWaves, identifiés par les ports suivants : IFH1, IFV1, IFH2, IFV2, IFH3, IFV3, IFH4, IFV4.
  
Pour ce projet, nous nous concentrerons exclusivement sur les interfaces liées à la transmission mmWaves. 

Le modem permet de connecter jusqu'à 4 modules d'antennes mmWaves, chaque module étant relié par 2 câbles : l’un à une entrée H (Horizontale) et l’autre à une entrée V (Verticale). Les modules d'antennes compatibles avec le modem EM9190 sont les modèles QTM525 et QTM527, la principale différence résidant dans leur puissance d'émission. L'utilisation de 4 antennes n'est pas obligatoire, notamment avec le module QTM525, mais il est impératif de respecter l’assignation correcte des ports mmWave dans chaque configuration (voir Annexe 1).

Dans le cadre d'une expérimentation simplifiée, nous proposons de commencer avec un seul module QTM525. Par conséquent, cette section se concentrera uniquement sur l’utilisation du module QTM525 (le manuel du QTM525 est lui aussi disponible dans le dossier "manuel").

<p align="center">
  <img src="images/QTM525.jpg" width="300">
</p>

A rajouter : Précision sur le shield de connecteur et autres infos importantes sur le QTM525

Ensuite il faut trouver un moyen de connecter l'EM9190 au module d'antenne QTM525. Pour cela, il nous faut des câbles coaxials RF compatibles avec des connecteurs type I-PEX (20956-001E-01 (MHF7S) et le connecter (avec un fer à souder ?) sur le module QTM525. Ce câble doit aussi pouvoir supporter des fréquences allant jusqu'à plus de 26 GHz.

A rajouter : ce que l'on a trouvé, problème c'est que ça va que jusqu'à 15 GHz

**Mise en place théorique**

A rajouter : Schéma d'une misen place théorique pour exploiter le modem 91910
  
</p>

## **Ross**

## **Annexes**

<p align="center">
  <img src="images/Annexe1.PNG" width="500">
</p>

## **Bibliographie**

### **Connexion mmWaves**

Manuel de l'EM9190 : \
https://manuals.plus/sierra-wireless/airprime-em9190-5g-module-manual \
Manuel technique de l'EM9190, pdf : \
https://source.sierrawireless.com/resources/airprime/minicard/airprime_em919x-7690_product_technical_specification/#sthash.pqpB43GY.dpbs

