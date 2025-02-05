# Transformer un Raspberry Pi en Point d'Accès WiFi

## Introduction
Ce guide explique comment configurer un Raspberry Pi en point d'accès WiFi avec connexion Internet. Nous utiliserons `hostapd` pour créer le point d'accès, `dnsmasq` pour gérer le DHCP et un pont réseau (`br0`) entre l'interface Ethernet (`eth0`) et WiFi (`wlan0`).

---

## Étape 1 : Installation et Mise à Jour de Raspbian
Mettez à jour votre Raspberry Pi avec ces commandes :
```bash
sudo apt-get update
sudo apt-get upgrade
```
Redémarrez si nécessaire :
```bash
sudo reboot
```

## Étape 2 : Installation de `hostapd` et `dnsmasq`
Installez les paquets nécessaires :
```bash
sudo apt-get install hostapd
sudo apt-get install dnsmasq
```
Désactivez temporairement ces services :
```bash
sudo systemctl stop hostapd
sudo systemctl stop dnsmasq
```
- `hostapd` transforme le Raspberry Pi en un point d'accès WiFi.
- `dnsmasq` attribue automatiquement des adresses IP aux clients WiFi.
- Nous arrêtons les services temporairement avant de les configurer.

## Étape 3 : Configuration d'une IP Statique pour `wlan0`
Éditez le fichier de configuration :
```bash
sudo nano /etc/dhcpcd.conf
```
Ajoutez ces lignes à la fin :
```ini
interface wlan0
static ip_address=192.168.38.1/24
denyinterfaces eth0
denyinterfaces wlan0
```


## Étape 4 : Configuration du Serveur DHCP (`dnsmasq`)
Renommez l'ancien fichier de configuration :
```bash
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
```
Créez un nouveau fichier :
```bash
sudo nano /etc/dnsmasq.conf
```
Ajoutez :
```ini
interface=wlan0
dhcp-range=192.168.38.11,192.168.38.255,255.255.255.0,24h
```
- Définit la plage d'adresses IP pour les clients WiFi.
- `dnsmasq` gère ces adresses et les distribue dynamiquement.

## Étape 5 : Configuration du Point d'Accès (`hostapd`)
Créez le fichier de configuration :
```bash
sudo nano /etc/hostapd/hostapd.conf
```
Ajoutez :
```ini
interface=wlan0
bridge=br0
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
ssid=MON_RESEAU
wpa_passphrase=MON_MOT_DE_PASSE
```
- Définit les paramètres du point d'accès (nom du réseau, sécurité, canal WiFi).
- Remplacez `MON_RESEAU` et `MON_MOT_DE_PASSE` par vos propres identifiants. Dans ce cas, nous avons mis `demo` et `demo12345`

Associez ce fichier à `hostapd` :
```bash
sudo nano /etc/default/hostapd
```
Trouvez la ligne `#DAEMON_CONF=""`, et remplacez-la par :
```ini
DAEMON_CONF="/etc/hostapd/hostapd.conf"
```

## Étape 6 : Activation du Routage Internet
Éditez le fichier `sysctl.conf` :
```bash
sudo nano /etc/sysctl.conf
```
Trouvez la ligne `#net.ipv4.ip_forward=1` et décommentez-la :
```ini
net.ipv4.ip_forward=1
```
Permet au Raspberry Pi de transférer les paquets entre ses interfaces réseau.

## Étape 7 : Ajout d'une Règle Iptables
Ajoutez une règle NAT :
```bash
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```
Sauvegardez cette règle :
```bash
sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"
```
Chargez-la au démarrage :
```bash
sudo nano /etc/rc.local
```
Ajoutez avant `exit 0` :
```bash
iptables-restore < /etc/iptables.ipv4.nat
```
- `iptables` redirige les paquets entre `wlan0` et `eth0`.
- `MASQUERADE` permet aux clients WiFi d'accéder à Internet via le Raspberry Pi.

## Étape 8 : Création d'un Pont Réseau (`br0`)
Installez le paquet nécessaire :
```bash
sudo apt-get install bridge-utils
```
Créez le pont :
```bash
sudo brctl addbr br0
```
Ajoutez `eth0` au pont :
```bash
sudo brctl addif br0 eth0
```
Éditez les interfaces réseau :
```bash
sudo nano /etc/network/interfaces
```
Ajoutez à la fin :
```ini
auto br0
iface br0 inet manual
address 192.168.38.220
netmask 255.255.255.0
bridge_ports eth0 wlan0
```
- `br0` fusionne `wlan0` et `eth0` pour partager la connexion Ethernet avec les clients WiFi.

## Étape 9 : Redémarrage
Redémarrez le Raspberry Pi :
```bash
sudo reboot
```

## Étape 10 : Connexion au Point d'Accès
Depuis un autre appareil, recherchez le réseau nommé `MON_RESEAU` et connectez-vous avec `MON_MOT_DE_PASSE`. Dans ce cas, `demo` et `demo12345`

## Remarque

Dans notre cas, nous avons attribué l'adresse IP `192.168.38.220` à `br0`.  
Ainsi, pour se connecter au robot via SSH, il suffit de taper la commande :

```bash
ssh diablo@192.168.38.220
```
Cependant, attention : SSH ne fonctionne que lorsque les deux appareils sont sur le même réseau.
Cela signifie que l'autre appareil doit être connecté au hotspot du robot, dans ce cas, au réseau `demo` avec le mot de passe `demo12345`.
