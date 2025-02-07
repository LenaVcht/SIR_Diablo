import rclpy  # Import de la bibliothèque ROS 2 pour Python
from rclpy.node import Node  # Import de la classe Node, base pour tout nœud ROS 2
from motion_msgs.msg import MotionCtrl  # Import du message MotionCtrl pour contrôler le robot
import sys  # Module pour interagir avec le système (entrée/sortie standard)
import termios  # Module pour gérer les paramètres du terminal
import tty  # Module pour modifier le mode du terminal
import time #Module pour que le robot s'arrête après une durée définie

class KeyboardControlNode(Node):
    """Noeud ROS 2 pour contrôler le robot Diablo via le clavier."""

    def __init__(self):
        super().__init__('keyboard_control_node')  # Initialisation du nœud avec un nom unique
        self.publisher_ = self.create_publisher(MotionCtrl, '/diablo/MotionCmd', 10)  # Création d'un publisher pour envoyer des commandes au robot

        # Affichage des commandes disponibles
        self.get_logger().info(
            "Contrôle du robot Diablo : Flèches (déplacement), + / - (vitesse), w (crawling), q (standing), n/h/y (pitch), g/h/j (roll), espace (stop), ` puis Ctrl+C (quitter)"
        )

        # Paramètres de vitesse
        self.speed = 1.0  # Vitesse linéaire initiale
        self.turn_speed = 1.0  # Vitesse de rotation initiale
        self.speed_increment = 0.1  # Incrément de vitesse lors des ajustements

        msg = MotionCtrl()  # Création d'un message ROS 2 de type MotionCtrl

        msg.mode.stand_mode = False

        # Démarrage de la boucle d'écoute du clavier
        self.run_keyboard_control()

    def get_key(self):
        """Capture une touche pressée sans nécessiter d'appuyer sur Entrée."""
        fd = sys.stdin.fileno()  # Récupère le descripteur du terminal
        old_settings = termios.tcgetattr(fd)  # Sauvegarde les paramètres actuels du terminal
        try:
            tty.setraw(sys.stdin.fileno())  # Passe le terminal en mode brut (raw mode) pour capturer directement une touche
            key = sys.stdin.read(1)  # Lit un seul caractère entré par l'utilisateur
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # Restaure les paramètres initiaux du terminal
        return key

    def run_keyboard_control(self):
        """Boucle principale pour capturer les entrées clavier et envoyer les commandes au robot."""
        try:
            while rclpy.ok():  # Boucle active tant que ROS 2 fonctionne
                key = self.get_key()  # Récupération de la touche pressée par l'utilisateur
                msg = MotionCtrl()  # Création d'un message ROS 2 de type MotionCtrl
                msg.mode_mark = False  # Initialisation du mode par défaut

                # Détection des touches pressées et affectation des commandes associées
                if key == '\x1b':  # Détection d'une touche spéciale (séquence d'échappement pour les flèches directionnelles)
                    key += sys.stdin.read(2)  # Lecture des deux caractères supplémentaires qui suivent '\x1b' pour identifier la touche exacte
                    if key == '\x1b[A':  # Flèche Haut
                        msg.value.forward = self.speed  # Déplacement vers l'avant
                        self.get_logger().info(f"Avancer - Vitesse: {self.speed}")
                    elif key == '\x1b[B':  # Flèche Bas
                        msg.value.forward = -self.speed  # Déplacement vers l'arrière
                        self.get_logger().info(f"Reculer - Vitesse: {self.speed}")
                    elif key == '\x1b[C':  # Flèche Droite
                        msg.value.left = -self.turn_speed  # Rotation vers la droite
                        self.get_logger().info("Tourner à droite")
                    elif key == '\x1b[D':  # Flèche Gauche
                        msg.value.left = self.turn_speed  # Rotation vers la gauche
                        self.get_logger().info("Tourner à gauche")
                        
                    # Publication du message de commande vers le robot
                    self.publisher_.publish(msg)
                    time.sleep(0.1) #Le robot bouge pendant 0.1 secondes
                    msg.value.forward = 0.0
                    msg.value.left = 0.0
                    self.publisher_.publish(msg)
                    self.get_logger().info("Arrêt automatique après 0.1 secondes")


                elif key == '+':  # Augmentation de la vitesse
                    self.speed += self.speed_increment
                    self.get_logger().info(f"Vitesse augmentée: {self.speed}")

                elif key == '-':  # Réduction de la vitesse (avec un minimum de 0.1)
                    self.speed = max(0.1, self.speed - self.speed_increment)
                    self.get_logger().info(f"Vitesse réduite: {self.speed}")

                elif key == ' ':  # Arrêt complet du robot
                    msg.value.forward = 0.0
                    msg.value.left = 0.0
                    self.get_logger().info("Arrêt complet")
                    
                elif key == 'a': #Activation du mode standing
                    msg.mode_mark = True
                    msg.mode.stand_mode = True
                    msg.mode.height_ctrl_mode = True
                    msg.value.up = 1.0
                    self.get_logger().info(f"Standing mode")
                        
                elif key == 'q': #Activation du mode standing
                    msg.mode_mark = True
                    msg.mode.stand_mode = True
                    msg.mode.height_ctrl_mode = True
                    msg.value.up = 0.5
                    self.get_logger().info(f"Standing mode")
                    
                elif key == 'w':
                    msg.mode_mark = True
                    msg.mode.stand_mode = False
                    msg.value.up = -0.5
                    self.get_logger().info(f"Crawling mode")

                elif key == 'y':  # Activation/Désactivation du mode pitch
                    msg.mode_mark = False
                    msg.mode.pitch_ctrl_mode = False
                    msg.value.pitch = 0.5
                    self.get_logger().info(f"Mode pitch à 0.5")
                    
                elif key == 'h':  # Activation/Désactivation du mode pitch
                    msg.mode_mark = False
                    msg.mode.pitch_ctrl_mode = False
                    msg.value.pitch = 0.0
                    msg.value.roll = 0.0
                    self.get_logger().info(f"Modes pitch et roll à 0")
                    
                elif key == 'n':  # Activation/Désactivation du mode pitch
                    msg.mode_mark = False
                    msg.mode.pitch_ctrl_mode = False
                    msg.value.pitch = -0.5
                    self.get_logger().info(f"Mode pitch à -0.5")
                    
                elif key == 'g':
                    msg.value.roll = -1.0
                    self.get_logger().info(f"Mode roll à -1")
                    
                elif key == 'j':
                    msg.value.roll = 1.0
                    self.get_logger().info(f"Mode roll à 1")
                    
                elif key =='`':
                    break

                # Publication du message de commande vers le robot
                self.publisher_.publish(msg)
        
        except KeyboardInterrupt:
            self.get_logger().info("Arrêt du contrôle clavier.")  # Affichage d'un message en cas d'arrêt avec Ctrl+C
            
            
def main(args=None):
    """Fonction principale pour initialiser et exécuter le nœud."""
    rclpy.init(args=args)  # Initialisation de ROS 2
    keyboard_control_node = KeyboardControlNode()  # Création d'une instance du nœud
    rclpy.spin(keyboard_control_node)  # Mise en attente active du nœud
    keyboard_control_node.destroy_node()  # Destruction explicite du nœud (facultatif)
    rclpy.shutdown()  # Arrêt propre de ROS 2

if __name__ == '__main__':
    main()  # Exécution du script si lancé directement
