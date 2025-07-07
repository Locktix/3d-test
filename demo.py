#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Démonstration des fonctionnalités du RPG Aventure 3D
"""

import sys
import time
from quest_system import QuestSystem, Quest
from inventory_system import Inventory, Shop, Item, ItemFactory
from ai_system import AISystem, AIController, GoblinAI, TrollAI, MerchantAI
from config import config

def demo_quest_system():
    """Démonstration du système de quêtes"""
    print("🎯 DÉMONSTRATION DU SYSTÈME DE QUÊTES")
    print("=" * 50)
    
    quest_system = QuestSystem()
    
    # Afficher les quêtes disponibles
    print("📜 Quêtes disponibles:")
    for quest in quest_system.available_quests:
        print(f"  - {quest.title} (Niveau {quest.required_level})")
        print(f"    {quest.description}")
        print(f"    Récompenses: {quest.rewards}")
        print()
    
    # Accepter une quête
    print("✅ Acceptation de la quête 'Les Gobelins du Bois'")
    quest_system.accept_quest("quest_001")
    
    # Mettre à jour le progrès
    print("⚔️ Combat contre un gobelin...")
    quest_system.update_quest_progress("quest_001", 1)
    
    print("⚔️ Combat contre un deuxième gobelin...")
    quest_system.update_quest_progress("quest_001", 1)
    
    print("⚔️ Combat contre un troisième gobelin...")
    quest_system.update_quest_progress("quest_001", 1)
    
    # Vérifier la completion
    if quest_system.check_quest_completion("quest_001"):
        result = quest_system.complete_quest("quest_001")
        print(f"🎉 {result['message']}")
        print(f"   Récompenses: {result['rewards']}")
    
    print()

def demo_inventory_system():
    """Démonstration du système d'inventaire"""
    print("🎒 DÉMONSTRATION DU SYSTÈME D'INVENTAIRE")
    print("=" * 50)
    
    # Créer un inventaire
    inventory = Inventory(max_weight=50.0)
    
    # Créer des objets avec la fabrique
    print("🔨 Création d'objets avec la fabrique:")
    
    sword = ItemFactory.create_weapon("sword", "iron", 1)
    print(f"  - {sword.name}: {sword.description}")
    print(f"    Dégâts: {sword.stats['damage']}, Valeur: {sword.value}")
    
    potion = ItemFactory.create_potion("health", 2)
    print(f"  - {potion.name}: {potion.description}")
    print(f"    Soin: {potion.stats['heal']}, Valeur: {potion.value}")
    
    material = ItemFactory.create_material("iron", 5)
    print(f"  - {material.name}: {material.description}")
    print(f"    Quantité: {material.stats['quantity']}, Valeur: {material.value}")
    
    # Ajouter à l'inventaire
    print("\n📦 Ajout à l'inventaire:")
    inventory.add_item(sword)
    inventory.add_item(potion)
    inventory.add_item(material)
    
    print(f"  Poids actuel: {inventory.current_weight}/{inventory.max_weight}")
    print(f"  Valeur totale: {inventory.get_total_value()} or")
    
    # Système de boutique
    print("\n🏪 Système de boutique:")
    shop = Shop()
    
    # Acheter un objet
    player_gold = 200
    buy_result = shop.buy_item(inventory, player_gold, "sword_iron")
    if buy_result["success"]:
        print(f"  ✅ {buy_result['message']}")
        player_gold -= buy_result["cost"]
        print(f"  Or restant: {player_gold}")
    
    # Vendre un objet
    sell_result = shop.sell_item(inventory, "sword_iron_1")
    if sell_result["success"]:
        print(f"  💰 {sell_result['message']}")
        player_gold += sell_result["price"]
        print(f"  Or total: {player_gold}")
    
    print()

def demo_ai_system():
    """Démonstration du système d'IA"""
    print("🤖 DÉMONSTRATION DU SYSTÈME D'IA")
    print("=" * 50)
    
    # Créer des entités factices pour la démo
    class MockEntity:
        def __init__(self, pos):
            self.position = pos
            
        def __sub__(self, other):
            # Permettre la soustraction de positions
            if isinstance(other, list):
                return [self.position[0] - other[0], self.position[1] - other[1], self.position[2] - other[2]]
            return self.position
    
    # Créer des entités
    goblin_entity = MockEntity([10, 0, 10])
    troll_entity = MockEntity([20, 0, 20])
    merchant_entity = MockEntity([0, 0, 5])
    
    # Créer les contrôleurs d'IA
    ai_system = AISystem()
    
    goblin_ai = ai_system.add_ai_controller(goblin_entity, "goblin")
    troll_ai = ai_system.add_ai_controller(troll_entity, "troll")
    merchant_ai = ai_system.add_ai_controller(merchant_entity, "merchant")
    
    print("👹 Gobelin:")
    print(f"  Santé: {goblin_ai.health}/{goblin_ai.max_health}")
    print(f"  Dégâts: {goblin_ai.damage}")
    print(f"  Vitesse: {goblin_ai.speed}")
    print(f"  Portée de détection: {goblin_ai.detection_range}")
    
    print("\n🧌 Troll:")
    print(f"  Santé: {troll_ai.health}/{troll_ai.max_health}")
    print(f"  Dégâts: {troll_ai.damage}")
    print(f"  Vitesse: {troll_ai.speed}")
    print(f"  Portée de détection: {troll_ai.detection_range}")
    
    print("\n👨‍💼 Marchand:")
    print(f"  Santé: {merchant_ai.health}/{merchant_ai.max_health}")
    print(f"  Vitesse: {merchant_ai.speed} (statique)")
    print(f"  Portée d'interaction: {merchant_ai.detection_range}")
    
    # Simuler des comportements
    print("\n🎮 Simulation des comportements:")
    player_pos = [0, 0, 0]
    
    print("  Joueur loin des ennemis:")
    goblin_ai.update(player_pos, 0)
    print(f"    Gobelin: {goblin_ai.state.value}")
    
    print("  Joueur proche du gobelin:")
    goblin_ai.entity.position = [2, 0, 2]  # Proche du joueur
    goblin_ai.update(player_pos, 0)
    print(f"    Gobelin: {goblin_ai.state.value}")
    
    print("  Gobelin attaqué:")
    goblin_ai.take_damage(15)
    print(f"    Gobelin santé: {goblin_ai.health}")
    print(f"    État: {goblin_ai.state.value}")
    
    print()

def demo_config_system():
    """Démonstration du système de configuration"""
    print("⚙️ DÉMONSTRATION DU SYSTÈME DE CONFIGURATION")
    print("=" * 50)
    
    # Afficher la configuration actuelle
    print("📋 Configuration actuelle:")
    print(f"  Résolution: {config.get('graphics.resolution')}")
    print(f"  Mode plein écran: {config.get('graphics.fullscreen')}")
    print(f"  Volume principal: {config.get('audio.master_volume')}")
    print(f"  Difficulté: {config.get('gameplay.difficulty')}")
    print(f"  Langue: {config.get('ui.language')}")
    print(f"  Sensibilité souris: {config.get('controls.mouse_sensitivity')}")
    
    # Modifier une configuration
    print("\n🔧 Modification de la configuration:")
    config.set('gameplay.difficulty', 'hard')
    config.set('audio.master_volume', 0.8)
    print("  Difficulté changée à 'hard'")
    print("  Volume principal changé à 0.8")
    
    print(f"  Nouvelle difficulté: {config.get('gameplay.difficulty')}")
    print(f"  Nouveau volume: {config.get('audio.master_volume')}")
    
    # Réinitialiser
    print("\n🔄 Réinitialisation à la configuration par défaut:")
    config.reset_to_defaults()
    print(f"  Difficulté: {config.get('gameplay.difficulty')}")
    print(f"  Volume: {config.get('audio.master_volume')}")
    
    print()

def main():
    """Fonction principale de démonstration"""
    print("🎮 DÉMONSTRATION DU RPG AVENTURE 3D")
    print("=" * 60)
    print("Ce script démontre toutes les fonctionnalités du RPG")
    print("sans lancer le moteur 3D complet.")
    print()
    
    try:
        # Démarrer les démonstrations
        demo_quest_system()
        demo_inventory_system()
        demo_ai_system()
        demo_config_system()
        
        print("🎉 DÉMONSTRATION TERMINÉE!")
        print("=" * 60)
        print("Toutes les fonctionnalités principales ont été testées.")
        print("Pour jouer au vrai jeu, lancez: python main.py")
        
    except Exception as e:
        print(f"❌ Erreur lors de la démonstration: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 