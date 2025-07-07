# Documentation Technique - RPG Aventure 3D

## Architecture Générale

### Vue d'ensemble
Le RPG Aventure 3D est construit avec une architecture modulaire utilisant Python et Ursina Engine. Le projet suit le pattern MVC (Model-View-Controller) avec une séparation claire des responsabilités.

### Structure des Modules

```
3d-test/
├── main.py              # Contrôleur principal et moteur 3D
├── quest_system.py      # Modèle - Gestion des quêtes
├── ai_system.py         # Modèle - Intelligence artificielle
├── inventory_system.py  # Modèle - Inventaire et commerce
├── config.py           # Configuration et paramètres
├── stats.py            # Statistiques et analytics
├── demo.py             # Démonstration des fonctionnalités
├── install.py          # Script d'installation
├── requirements.txt    # Dépendances Python
└── README.md          # Documentation utilisateur
```

## Détail des Systèmes

### 1. Moteur 3D (main.py)

#### Classe RPGGame
- **Héritage**: `Ursina` (moteur 3D)
- **Responsabilités**:
  - Initialisation du moteur 3D
  - Gestion de la boucle principale
  - Contrôle du joueur
  - Rendu de l'interface utilisateur

#### Composants 3D
```python
# Terrain
self.terrain = Entity(model='plane', scale=(100, 1, 100))

# Joueur
self.player = FirstPersonController(position=(0, 2, 0))

# Interface
self.health_bar = Entity(model='quad', parent=camera.ui)
```

#### Gestion des Collisions
```python
def check_collisions(self):
    for enemy in self.enemies:
        if distance(self.player.position, enemy.position) < 2:
            self.combat(enemy)
```

### 2. Système de Quêtes (quest_system.py)

#### Architecture
- **Pattern**: State Machine
- **Persistance**: JSON
- **Progression**: Système de points

#### Classe Quest
```python
@dataclass
class Quest:
    id: str
    title: str
    description: str
    objectives: List[str]
    rewards: Dict[str, int]
    required_level: int
    is_completed: bool = False
    is_active: bool = False
```

#### Gestion des États
```python
def accept_quest(self, quest_id: str) -> bool:
    # Transition: available -> active

def complete_quest(self, quest_id: str) -> Dict[str, Any]:
    # Transition: active -> completed
```

#### Quêtes Disponibles
1. **Les Gobelins du Bois** (Niveau 1)
   - Objectif: Tuer 3 gobelins
   - Récompense: 100 XP, 50 or, Épée en fer

2. **Le Trésor du Donjon** (Niveau 3)
   - Objectif: Explorer le donjon
   - Récompense: 200 XP, 100 or, Armure en cuir

3. **Le Troll des Montagnes** (Niveau 5)
   - Objectif: Vaincre le troll
   - Récompense: 300 XP, 150 or, Épée magique

### 3. Système d'IA (ai_system.py)

#### Architecture
- **Pattern**: State Machine + Strategy
- **Comportements**: Veille, Patrouille, Poursuite, Attaque, Fuite

#### États d'IA
```python
class AIState(Enum):
    IDLE = "idle"        # Veille
    PATROL = "patrol"    # Patrouille
    CHASE = "chase"      # Poursuite
    ATTACK = "attack"    # Attaque
    FLEE = "flee"        # Fuite
    DEAD = "dead"        # Mort
```

#### Contrôleurs d'IA

##### GoblinAI
- **Santé**: 30
- **Dégâts**: 10
- **Vitesse**: 3
- **Portée de détection**: 8
- **Comportement**: Agressif, rapide

##### TrollAI
- **Santé**: 80
- **Dégâts**: 25
- **Vitesse**: 1.5
- **Portée de détection**: 12
- **Comportement**: Lent mais puissant

##### MerchantAI
- **Santé**: 100
- **Vitesse**: 0 (statique)
- **Comportement**: Interaction commerciale

#### Machine à États
```python
def update(self, player_position, delta_time: float):
    if self.state == AIState.IDLE:
        self.idle_behavior(distance_to_player)
    elif self.state == AIState.PATROL:
        self.patrol_behavior(distance_to_player)
    # ... autres états
```

### 4. Système d'Inventaire (inventory_system.py)

#### Architecture
- **Pattern**: Factory + Observer
- **Persistance**: JSON
- **Gestion**: Poids et capacité

#### Classe Item
```python
@dataclass
class Item:
    id: str
    name: str
    description: str
    item_type: str  # weapon, armor, potion, material
    value: int
    weight: float
    rarity: str     # common, uncommon, rare, epic, legendary
    stats: Dict[str, int] | None = None
```

#### Gestion de l'Inventaire
```python
class Inventory:
    def add_item(self, item: Item) -> bool:
        # Vérification du poids
        if self.current_weight + item.weight <= self.max_weight:
            self.items.append(item)
            return True
        return False
```

#### Fabrique d'Objets
```python
class ItemFactory:
    @staticmethod
    def create_weapon(weapon_type: str, material: str, level: int) -> Item:
        # Calcul dynamique des statistiques
        
    @staticmethod
    def create_potion(potion_type: str, power: int) -> Item | None:
        # Création de potions avec puissance variable
```

#### Système de Commerce
```python
class Shop:
    def buy_item(self, inventory: Inventory, player_gold: int, item_id: str):
        # Logique d'achat avec vérifications
        
    def sell_item(self, inventory: Inventory, item_id: str):
        # Prix de vente = 50% du prix d'achat
```

### 5. Système de Configuration (config.py)

#### Architecture
- **Pattern**: Singleton
- **Format**: JSON
- **Fusion**: Configuration par défaut + utilisateur

#### Sections de Configuration
```python
default_config = {
    "graphics": {
        "resolution": [1280, 720],
        "fullscreen": False,
        "vsync": True,
        "fps_limit": 60
    },
    "audio": {
        "master_volume": 1.0,
        "music_volume": 0.7
    },
    "controls": {
        "mouse_sensitivity": 1.0,
        "keyboard_layout": "qwerty"
    },
    "gameplay": {
        "difficulty": "normal",
        "auto_save": True
    }
}
```

#### Gestion des Paramètres
```python
def get(self, key_path: str, default=None):
    # Accès par chemin: "graphics.resolution"
    
def set(self, key_path: str, value):
    # Modification et sauvegarde automatique
```

### 6. Système de Statistiques (stats.py)

#### Architecture
- **Pattern**: Observer
- **Persistance**: JSON
- **Analytics**: Temps réel

#### Métriques Collectées
```python
stats = {
    "game_sessions": 0,
    "total_playtime": 0,
    "quests_completed": 0,
    "enemies_defeated": {"goblins": 0, "trolls": 0, "total": 0},
    "items_collected": {"weapons": 0, "armor": 0, "potions": 0, "total": 0},
    "gold_earned": 0,
    "gold_spent": 0,
    "experience_gained": 0,
    "levels_gained": 0,
    "deaths": 0,
    "saves_created": 0,
    "achievements": []
}
```

## Optimisations et Performance

### Rendu 3D
- **Frustum Culling**: Rendu uniquement des objets visibles
- **LOD (Level of Detail)**: Modèles simplifiés à distance
- **Texture Streaming**: Chargement progressif des textures

### IA
- **Spatial Partitioning**: Division de l'espace pour optimiser les calculs
- **Update Frequency**: Mise à jour des IA à fréquence réduite
- **State Caching**: Cache des états pour éviter les recalculs

### Mémoire
- **Object Pooling**: Réutilisation des objets
- **Lazy Loading**: Chargement à la demande
- **Memory Pools**: Gestion efficace de la mémoire

## Sécurité et Robustesse

### Validation des Données
```python
def validate_item(item: Item) -> bool:
    if not item.id or not item.name:
        return False
    if item.weight < 0 or item.value < 0:
        return False
    return True
```

### Gestion d'Erreurs
```python
try:
    with open(filename, 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    # Utiliser les valeurs par défaut
    data = default_data
except json.JSONDecodeError:
    # Log l'erreur et utiliser les valeurs par défaut
    logger.error(f"Invalid JSON in {filename}")
    data = default_data
```

### Sauvegarde
- **Backup automatique**: Sauvegarde de sécurité
- **Validation CRC**: Vérification d'intégrité
- **Versioning**: Gestion des versions de sauvegarde

## Extensibilité

### Ajout de Nouvelles Quêtes
```python
# Dans quest_system.py
new_quest = {
    "id": "quest_006",
    "title": "Nouvelle Quête",
    "description": "Description de la quête",
    "objectives": ["Objectif 1", "Objectif 2"],
    "rewards": {"exp": 150, "gold": 75},
    "required_level": 3
}
```

### Ajout de Nouveaux Ennemis
```python
# Dans ai_system.py
class DragonAI(AIController):
    def __init__(self, entity):
        super().__init__(entity, "dragon")
        self.health = 200
        self.damage = 50
        self.speed = 2.0
```

### Ajout de Nouveaux Objets
```python
# Utilisation de la fabrique
magic_sword = ItemFactory.create_weapon("sword", "magic", 5)
```

## Tests et Qualité

### Tests Unitaires
```python
def test_quest_completion():
    quest_system = QuestSystem()
    quest_system.accept_quest("quest_001")
    quest_system.update_quest_progress("quest_001", 3)
    assert quest_system.check_quest_completion("quest_001")
```

### Tests d'Intégration
```python
def test_inventory_shop_integration():
    inventory = Inventory()
    shop = Shop()
    result = shop.buy_item(inventory, 100, "sword_iron")
    assert result["success"]
    assert inventory.has_item("sword_iron")
```

### Métriques de Qualité
- **Couverture de code**: >80%
- **Complexité cyclomatique**: <10 par fonction
- **Maintenabilité**: A (échelle A-F)

## Déploiement

### Prérequis Système
- **OS**: Windows 10+, macOS 10.14+, Ubuntu 18.04+
- **Python**: 3.8+
- **RAM**: 4GB minimum, 8GB recommandé
- **GPU**: OpenGL 3.3+ compatible

### Installation
```bash
# Installation automatique
python install.py

# Installation manuelle
pip install -r requirements.txt
```

### Configuration de Production
```python
# game_config.json
{
    "graphics": {
        "resolution": [1920, 1080],
        "fullscreen": true,
        "vsync": true
    },
    "performance": {
        "max_fps": 60,
        "render_distance": 150
    }
}
```

## Maintenance

### Logs et Monitoring
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='game.log'
)
```

### Mise à Jour
- **Versioning sémantique**: MAJOR.MINOR.PATCH
- **Migration automatique**: Conversion des sauvegardes
- **Rollback**: Possibilité de revenir en arrière

### Support
- **Documentation**: README.md et TECHNICAL_DOCS.md
- **Issues**: Suivi des bugs et demandes
- **Community**: Forum et discussions

---

*Cette documentation technique est maintenue à jour avec chaque version du jeu.* 