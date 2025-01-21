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

<p align="left">1
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

<p align="left">
  Pour établir une connexion en mmWaves nous disposons d'un modem 5G EM9190 de la marque Sierra Wireless.
  
  <p align="center">
  <img src="https://imgs.search.brave.com/Md5F8oEZjSophWG4jSvM_w3Zs433iq5DtVdAdncX4xg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zLmFs/aWNkbi5jb20vQHNj/MDQva2YvSGJmMWQ4/MjE3MDQyZDQ3NDZi/NTc2NWRhMjM5NTdh/MjYwNC5qcGdfNzIw/eDcyMHE1MC5qcGc" width="300">
  </p>

   Interface du modem :
   - 1 connecteur M.2 : interface utilisée pour connecter le périphérique à un hôte (Annexe 1)
   - 4 connecteur 5G (MAIN, MIMO1, AUX/GNSS L1, MIMO2/GNSS L5)
  En plus de ce modem, on peut connecter jusqu'à 8 câbles MHF7S similaire au 20955-001R-13 de la marque I-PEX  (2 câbles par module d'antenne) à connecter aux 8 connecteurs coaxials MHF7S sur le côté du modem. On peut donc utiliser jusqu'à 4 modules d'antenne 5G de type QTM525 ou QTM527.
</p>

## **Ross**

## **Bibliographie**

### **Connexion mmWaves**

Manuel de l'EM9190 : \
https://manuals.plus/sierra-wireless/airprime-em9190-5g-module-manual \
Manuel technique de l'EM9190, pdf : \
https://source.sierrawireless.com/resources/airprime/minicard/airprime_em919x-7690_product_technical_specification/#sthash.pqpB43GY.dpbs

