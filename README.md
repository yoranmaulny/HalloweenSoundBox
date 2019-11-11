# HalloweenSoundBox
Petit montage pour déclencher un son aléatoire au passage d'une personne.

Le lancement automatique est effectué par un service SystemD, pour sa mise en place voir la section 'Démarrage du script au lancement du raspberrypi'

Pour des questions de droits les sons ne sont pas fournis, à l'origine ils sont disponible dans un sous-répertoire son

## Matériel utilisé
- Raspberry Pi 3
- Capteur PIR
- 2 LED Orange
- 2 Résistance de 330 Ohm
- Une paire de haut parleur de PC
- Une plaque de prototypage
- Quelques câbles Dupont

## Mise en place du script
Le systyème utilisé est un Raspbian Lite Buster

- Copier le script dans le répertoire utilisateur 'pi'
- Installer les librairies python gpiozero et pygame

## Démarrage du script au lancement du raspberrypi

- Copier le fichier halloween-soundbox.service dans /etc/systemd/system en tant que root
    ```bash
    sudo cp halloween-soundbox.service /etc/systemd/system/halloween-soundbox.service
    ```
- Modifier **WorkingDirectory** pour correspondre au chemin de votre script

- Modifier **User** avec le nom d'utilisateur Raspbian utilisé pour créer le script

- Test de démarrage du service
    ```bash
    sudo systemctl start halloween-soundbox.service
    ```
- Arrêt du service
    ```bash
    sudo systemctl stop halloween-soundbox.service
    ```
- Quand tout est ok, ajout du démarrage automatique au redémarrage du système
    ```bash
    sudo systemctl enable halloween-soundbox.service
    ```

## Sources
- [systemd sur https://www.raspberrypi.org](https://www.raspberrypi.org/documentation/linux/usage/systemd.md)
- [Rasp-AutoStart-Script sur MCHobby](https://wiki.mchobby.be/index.php?title=Rasp-AutoStart-Script)
