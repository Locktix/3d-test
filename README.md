# RPG Aventure 3D - Le Royaume Mystérieux

Un jeu d'aventure RPG en 3D créé avec Python et Ursina Engine.

## 🎮 Description

Plongez dans un monde fantastique en 3D où vous devrez explorer, combattre, accomplir des quêtes et interagir avec les habitants du royaume. Ce RPG offre une expérience immersive avec des graphiques 3D, un système de combat, des quêtes, un inventaire et un système de commerce.

## ✨ Fonctionnalités

### 🗺️ Monde 3D
- **Terrain dynamique** avec herbe, montagnes et arbres
- **Village** avec maisons, fontaine et NPCs
- **Donjon** mystérieux à explorer
- **Éclairage** et effets visuels

### ⚔️ Système de Combat
- **Combat en temps réel** contre gobelins et trolls
- **Système de dégâts** et de santé
- **IA intelligente** pour les ennemis
- **Différents types d'ennemis** avec comportements uniques

### 📜 Système de Quêtes
- **5 quêtes principales** avec objectifs variés
- **Système de progression** et récompenses
- **Quêtes de niveau** adaptées au joueur
- **Sauvegarde automatique** des quêtes

### 🎒 Inventaire et Commerce
- **Système d'inventaire** avec poids limité
- **Boutique** avec armes, armures et potions
- **Objets rares** et légendaires
- **Système de vente** et d'achat

### 🤖 IA Avancée
- **Comportements réalistes** pour les ennemis
- **Patrouilles** et détection du joueur
- **NPCs interactifs** (marchand, garde, sage)
- **États d'IA** : veille, patrouille, poursuite, attaque, fuite

## 🚀 Installation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le projet**
   ```bash
   git clone <url-du-repo>
   cd 3d-test
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Lancer le jeu**
   ```bash
   python main.py
   ```

## 🎯 Contrôles

### Mouvement
- **ZQSD** ou **WASD** : Se déplacer
- **Espace** : Sauter
- **Souris** : Regarder autour

### Actions
- **Clic gauche** : Attaquer
- **E** : Interagir avec les objets/NPCs
- **I** : Ouvrir l'inventaire
- **M** : Ouvrir la carte

### Menu
- **Échap** : Menu principal
- **F5** : Sauvegarder
- **F9** : Charger
- **R** : Recommencer (après game over)

## 🎮 Guide de Jeu

### Début de Partie
1. **Explorez le village** pour rencontrer les NPCs
2. **Parlez au sage** pour obtenir votre première quête
3. **Récupérez des potions** pour survivre aux combats
4. **Combattez les gobelins** pour gagner de l'expérience

### Progression
- **Niveau 1-2** : Quêtes de gobelins et collecte de potions
- **Niveau 3-4** : Exploration du donjon et protection de la fontaine
- **Niveau 5+** : Combat contre le troll des montagnes

### Conseils
- **Sauvegardez régulièrement** avec F5
- **Utilisez les potions** quand votre vie est faible
- **Parlez aux NPCs** pour obtenir des quêtes et conseils
- **Explorez le monde** pour trouver des objets cachés

## 🏗️ Architecture du Code

### Structure des Fichiers
```
3d-test/
├── main.py              # Fichier principal du jeu
├── quest_system.py      # Système de quêtes
├── ai_system.py         # Système d'IA
├── inventory_system.py  # Système d'inventaire et commerce
├── requirements.txt     # Dépendances Python
└── README.md           # Ce fichier
```

### Systèmes Principaux

#### 1. RPGGame (main.py)
- **Gestion du monde 3D** avec Ursina Engine
- **Contrôle du joueur** et caméra
- **Interface utilisateur** et HUD
- **Boucle principale** du jeu

#### 2. QuestSystem (quest_system.py)
- **Gestion des quêtes** avec objectifs et récompenses
- **Progression** et sauvegarde des quêtes
- **Système de niveaux** requis

#### 3. AISystem (ai_system.py)
- **IA pour ennemis** avec comportements réalistes
- **États d'IA** : veille, patrouille, poursuite, attaque, fuite
- **NPCs interactifs** avec comportements spécifiques

#### 4. InventorySystem (inventory_system.py)
- **Gestion d'inventaire** avec poids et capacité
- **Système de boutique** avec achats/ventes
- **Fabrique d'objets** pour création dynamique

## 🎨 Personnalisation

### Ajouter de Nouvelles Quêtes
Modifiez `quest_system.py` et ajoutez de nouvelles quêtes dans la méthode `load_quests()`.

### Créer de Nouveaux Ennemis
Ajoutez de nouvelles classes d'IA dans `ai_system.py` en héritant de `AIController`.

### Ajouter des Objets
Utilisez `ItemFactory` dans `inventory_system.py` ou ajoutez des objets dans la boutique.

## 🐛 Dépannage

### Problèmes Courants

1. **Erreur d'import Ursina**
   ```bash
   pip install ursina==5.2.0
   ```

2. **Performance lente**
   - Réduisez la distance de rendu
   - Désactivez les effets visuels

3. **Contrôles non responsifs**
   - Vérifiez que la fenêtre est active
   - Redémarrez le jeu

### Support
Si vous rencontrez des problèmes, vérifiez :
- Version de Python (3.8+)
- Installation correcte des dépendances
- Permissions d'écriture pour les sauvegardes

## 🎵 Crédits

- **Moteur 3D** : Ursina Engine
- **Langage** : Python 3
- **Développement** : Créé avec l'aide de l'IA

## 📄 Licence

Ce projet est open source et disponible sous licence MIT.

---

**Amusez-vous bien dans le Royaume Mystérieux !** 🗡️🛡️✨ 