#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Statistiques et analyse du RPG Aventure 3D
"""

import json
import time
from pathlib import Path
from quest_system import QuestSystem
from inventory_system import Inventory, Shop, ItemFactory
from ai_system import AISystem

class GameStats:
    """Classe pour collecter et analyser les statistiques du jeu"""
    
    def __init__(self):
        self.stats_file = "game_stats.json"
        self.stats = self.load_stats()
        
    def load_stats(self):
        """Charger les statistiques existantes"""
        try:
            if Path(self.stats_file).exists():
                with open(self.stats_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return self.get_default_stats()
        except Exception as e:
            print(f"Erreur lors du chargement des stats: {e}")
            return self.get_default_stats()
            
    def get_default_stats(self):
        """Obtenir les statistiques par défaut"""
        return {
            "game_sessions": 0,
            "total_playtime": 0,
            "quests_completed": 0,
            "enemies_defeated": {
                "goblins": 0,
                "trolls": 0,
                "total": 0
            },
            "items_collected": {
                "weapons": 0,
                "armor": 0,
                "potions": 0,
                "materials": 0,
                "total": 0
            },
            "gold_earned": 0,
            "gold_spent": 0,
            "experience_gained": 0,
            "levels_gained": 0,
            "deaths": 0,
            "saves_created": 0,
            "achievements": []
        }
        
    def save_stats(self):
        """Sauvegarder les statistiques"""
        try:
            with open(self.stats_file, 'w', encoding='utf-8') as f:
                json.dump(self.stats, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde des stats: {e}")
            
    def update_session_count(self):
        """Incrémenter le nombre de sessions"""
        self.stats["game_sessions"] += 1
        self.save_stats()
        
    def add_playtime(self, minutes):
        """Ajouter du temps de jeu"""
        self.stats["total_playtime"] += minutes
        self.save_stats()
        
    def add_quest_completed(self, quest_name):
        """Ajouter une quête terminée"""
        self.stats["quests_completed"] += 1
        self.save_stats()
        
    def add_enemy_defeated(self, enemy_type):
        """Ajouter un ennemi vaincu"""
        if enemy_type in self.stats["enemies_defeated"]:
            self.stats["enemies_defeated"][enemy_type] += 1
        self.stats["enemies_defeated"]["total"] += 1
        self.save_stats()
        
    def add_item_collected(self, item_type):
        """Ajouter un objet collecté"""
        if item_type in self.stats["items_collected"]:
            self.stats["items_collected"][item_type] += 1
        self.stats["items_collected"]["total"] += 1
        self.save_stats()
        
    def add_gold_earned(self, amount):
        """Ajouter de l'or gagné"""
        self.stats["gold_earned"] += amount
        self.save_stats()
        
    def add_gold_spent(self, amount):
        """Ajouter de l'or dépensé"""
        self.stats["gold_spent"] += amount
        self.save_stats()
        
    def add_experience(self, amount):
        """Ajouter de l'expérience"""
        self.stats["experience_gained"] += amount
        self.save_stats()
        
    def add_level(self):
        """Ajouter un niveau gagné"""
        self.stats["levels_gained"] += 1
        self.save_stats()
        
    def add_death(self):
        """Ajouter une mort"""
        self.stats["deaths"] += 1
        self.save_stats()
        
    def add_save(self):
        """Ajouter une sauvegarde"""
        self.stats["saves_created"] += 1
        self.save_stats()
        
    def add_achievement(self, achievement_name):
        """Ajouter un succès"""
        if achievement_name not in self.stats["achievements"]:
            self.stats["achievements"].append(achievement_name)
            self.save_stats()
            
    def get_summary(self):
        """Obtenir un résumé des statistiques"""
        return {
            "sessions": self.stats["game_sessions"],
            "playtime_hours": round(self.stats["total_playtime"] / 60, 2),
            "quests": self.stats["quests_completed"],
            "enemies": self.stats["enemies_defeated"]["total"],
            "items": self.stats["items_collected"]["total"],
            "gold_balance": self.stats["gold_earned"] - self.stats["gold_spent"],
            "experience": self.stats["experience_gained"],
            "levels": self.stats["levels_gained"],
            "deaths": self.stats["deaths"],
            "saves": self.stats["saves_created"],
            "achievements": len(self.stats["achievements"])
        }
        
    def print_detailed_stats(self):
        """Afficher les statistiques détaillées"""
        print("📊 STATISTIQUES DÉTAILLÉES DU JEU")
        print("=" * 50)
        
        summary = self.get_summary()
        
        print(f"🎮 Sessions de jeu: {summary['sessions']}")
        print(f"⏰ Temps de jeu total: {summary['playtime_hours']} heures")
        print(f"📜 Quêtes terminées: {summary['quests']}")
        print(f"⚔️ Ennemis vaincus: {summary['enemies']}")
        print(f"🎒 Objets collectés: {summary['items']}")
        print(f"💰 Or gagné: {self.stats['gold_earned']}")
        print(f"💸 Or dépensé: {self.stats['gold_spent']}")
        print(f"💎 Solde d'or: {summary['gold_balance']}")
        print(f"⭐ Expérience gagnée: {summary['experience']}")
        print(f"📈 Niveaux gagnés: {summary['levels']}")
        print(f"💀 Morts: {summary['deaths']}")
        print(f"💾 Sauvegardes créées: {summary['saves']}")
        print(f"🏆 Succès débloqués: {summary['achievements']}")
        
        print("\n👹 Ennemis vaincus par type:")
        for enemy_type, count in self.stats["enemies_defeated"].items():
            if enemy_type != "total":
                print(f"  - {enemy_type.title()}: {count}")
                
        print("\n🎒 Objets collectés par type:")
        for item_type, count in self.stats["items_collected"].items():
            if item_type != "total":
                print(f"  - {item_type.title()}: {count}")
                
        if self.stats["achievements"]:
            print("\n🏆 Succès débloqués:")
            for achievement in self.stats["achievements"]:
                print(f"  - {achievement}")
                
    def generate_report(self):
        """Générer un rapport complet"""
        print("📋 RAPPORT COMPLET DU RPG AVENTURE 3D")
        print("=" * 60)
        
        # Statistiques générales
        self.print_detailed_stats()
        
        # Analyse des performances
        print("\n📈 ANALYSE DES PERFORMANCES")
        print("-" * 30)
        
        if self.stats["game_sessions"] > 0:
            avg_session_time = self.stats["total_playtime"] / self.stats["game_sessions"]
            print(f"Temps moyen par session: {round(avg_session_time, 2)} minutes")
            
        if self.stats["enemies_defeated"]["total"] > 0:
            death_ratio = self.stats["deaths"] / self.stats["enemies_defeated"]["total"]
            print(f"Ratio morts/ennemis vaincus: {round(death_ratio, 3)}")
            
        if self.stats["quests_completed"] > 0:
            quest_efficiency = self.stats["experience_gained"] / self.stats["quests_completed"]
            print(f"Expérience moyenne par quête: {round(quest_efficiency, 1)}")
            
        # Recommandations
        print("\n💡 RECOMMANDATIONS")
        print("-" * 20)
        
        if self.stats["deaths"] > 5:
            print("⚠️  Vous mourrez souvent. Essayez d'utiliser plus de potions!")
            
        if self.stats["gold_spent"] > self.stats["gold_earned"] * 0.8:
            print("💰 Vous dépensez beaucoup d'or. Économisez pour de meilleurs équipements!")
            
        if self.stats["saves_created"] < 5:
            print("💾 Sauvegardez plus souvent pour éviter de perdre votre progression!")
            
        if len(self.stats["achievements"]) < 3:
            print("🏆 Explorez plus le monde pour débloquer des succès!")
            
        print("\n🎮 Continuez à jouer pour améliorer vos statistiques!")

def analyze_game_systems():
    """Analyser les systèmes du jeu"""
    print("🔍 ANALYSE DES SYSTÈMES DU JEU")
    print("=" * 50)
    
    # Analyser le système de quêtes
    print("\n📜 SYSTÈME DE QUÊTES:")
    quest_system = QuestSystem()
    print(f"  Quêtes disponibles: {len(quest_system.available_quests)}")
    print(f"  Quêtes actives: {len(quest_system.active_quests)}")
    print(f"  Quêtes terminées: {len(quest_system.completed_quests)}")
    
    # Analyser le système d'inventaire
    print("\n🎒 SYSTÈME D'INVENTAIRE:")
    shop = Shop()
    print(f"  Objets en boutique: {len(shop.available_items)}")
    
    weapon_count = len(shop.get_items_by_type("weapon"))
    armor_count = len(shop.get_items_by_type("armor"))
    potion_count = len(shop.get_items_by_type("potion"))
    
    print(f"  Armes disponibles: {weapon_count}")
    print(f"  Armures disponibles: {armor_count}")
    print(f"  Potions disponibles: {potion_count}")
    
    # Analyser le système d'IA
    print("\n🤖 SYSTÈME D'IA:")
    ai_system = AISystem()
    print(f"  Contrôleurs d'IA actifs: {len(ai_system.ai_controllers)}")
    
    # Tester la création d'objets
    print("\n🔨 FABRIQUE D'OBJETS:")
    test_weapon = ItemFactory.create_weapon("sword", "steel", 3)
    test_potion = ItemFactory.create_potion("health", 3)
    test_material = ItemFactory.create_material("gold", 10)
    
    if test_weapon:
        print(f"  Arme créée: {test_weapon.name} (Dégâts: {test_weapon.stats['damage']})")
    if test_potion:
        print(f"  Potion créée: {test_potion.name} (Soin: {test_potion.stats['heal']})")
    if test_material:
        print(f"  Matériau créé: {test_material.name} (Quantité: {test_material.stats['quantity']})")

def main():
    """Fonction principale"""
    print("📊 ANALYSEUR DE STATISTIQUES DU RPG AVENTURE 3D")
    print("=" * 60)
    
    # Créer et afficher les statistiques
    stats = GameStats()
    
    # Ajouter quelques statistiques de démonstration
    stats.update_session_count()
    stats.add_playtime(120)  # 2 heures
    stats.add_quest_completed("Les Gobelins du Bois")
    stats.add_enemy_defeated("goblins")
    stats.add_enemy_defeated("goblins")
    stats.add_enemy_defeated("trolls")
    stats.add_item_collected("weapons")
    stats.add_item_collected("potions")
    stats.add_gold_earned(150)
    stats.add_gold_spent(80)
    stats.add_experience(200)
    stats.add_level()
    stats.add_death()
    stats.add_save()
    stats.add_achievement("Premier Combat")
    stats.add_achievement("Quêteur Débutant")
    
    # Afficher les rapports
    stats.generate_report()
    
    # Analyser les systèmes
    analyze_game_systems()
    
    print("\n" + "=" * 60)
    print("✅ Analyse terminée!")
    print("Les statistiques sont sauvegardées dans 'game_stats.json'")

if __name__ == "__main__":
    main() 