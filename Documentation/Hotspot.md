# Transformer un Raspberry Pi en Point d'Accès WiFi

## Introduction


## Matériel Nécessaire
### Liste des composants :
- **Raspberry Pi 3** *(tout modèle fonctionne, mais celui-ci est plus stable)* : [Lien Amazon](https://www.amazon.com/Raspberry-Pi-MS-004-00000024-Model-Board/dp/B01LPLPBS8)
- **Clé WiFi** *(optionnel, mais améliore le signal)* : [Lien Amazon](https://www.amazon.com/Adapter-1200Mbps-TECHKEY-Wireless-Network-300Mbps/dp/B07J65G9DD)
- **Clavier, souris, écran, alimentation** (ex : powerbank)

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

## Étape 3 : Configuration d'une IP Statique pour `wlan0`
Éditez le fichier de configuration :
```bash
sudo nano /etc/dhcpcd.conf
```
Ajoutez ces lignes à la fin :
```ini
interface wlan0
static ip_address=192.168.0.10/24
denyinterfaces eth0
denyinterfaces wlan0
```
Sauvegardez avec `CTRL+X`, `Y`, puis `ENTRÉE`.

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
dhcp-range=192.168.0.11,192.168.0.30,255.255.255.0,24h
```

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
Remplacez `MON_RESEAU` et `MON_MOT_DE_PASSE` par vos propres identifiants.

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
bridge_ports eth0 wlan0
```

## Étape 9 : Redémarrage
Redémarrez le Raspberry Pi :
```bash
sudo reboot
```

## Étape 10 : Connexion au Point d'Accès
Depuis un autre appareil, recherchez le réseau nommé `MON_RESEAU` et connectez-vous avec `MON_MOT_DE_PASSE`.

## Conclusion 🎉
Votre Raspberry Pi fonctionne maintenant comme un **point d'accès WiFi** ! Vous pouvez l'utiliser pour partager une connexion internet ou créer un réseau local. 🚀

---

📌 *Pour toute question ou amélioration, n'hésitez pas à contribuer sur GitHub !* 💡






lien vers le tutorial https://www.instructables.com/Raspberry-Pi-Wifi-Hotspot/ 
