#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RPG Aventure 3D - Le Royaume Mystérieux
Un jeu d'aventure en 3D créé avec Ursina Engine
"""

import sys
import json
import random
from pathlib import Path
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class RPGGame(Ursina):
    def __init__(self):
        super().__init__()
        self.setup_game()
        
    def setup_game(self):
        """Configuration initiale du jeu"""
        # Configuration de la fenêtre
        window.title = "RPG Aventure 3D - Le Royaume Mystérieux"
        window.borderless = False
        window.fullscreen = False
        window.exit_button.visible = False
        window.fps_counter.enabled = True
        
        # Configuration de l'éclairage
        Sky()
        DirectionalLight().look_at(Vec3(1, -1, -1))
        
        # Variables du jeu
        self.player_health = 100
        self.player_max_health = 100
        self.player_level = 1
        self.player_exp = 0
        self.player_gold = 50
        self.inventory = []
        self.quests = []
        self.current_quest = None
        
        # Création du monde
        self.create_world()
        self.create_player()
        self.create_ui()
        self.create_npcs()
        self.create_enemies()
        self.create_items()
        
    def create_world(self):
        """Création du monde 3D"""
        # Terrain principal
        self.terrain = Entity(
            model='plane',
            scale=(100, 1, 100),
            color=color.green,
            texture='grass',
            collider='box'
        )
        
        # Montagnes
        for i in range(10):
            mountain = Entity(
                model='cube',
                position=(random.randint(-40, 40), 5, random.randint(-40, 40)),
                scale=(random.randint(3, 8), random.randint(5, 15), random.randint(3, 8)),
                color=color.gray,
                texture='stone',
                collider='box'
            )
        
        # Arbres
        for i in range(30):
            tree_trunk = Entity(
                model='cylinder',
                position=(random.randint(-45, 45), 1, random.randint(-45, 45)),
                scale=(0.5, 2, 0.5),
                color=color.brown,
                collider='cylinder'
            )
            tree_leaves = Entity(
                model='sphere',
                position=(tree_trunk.position + Vec3(0, 2, 0)),
                scale=(2, 2, 2),
                color=color.green,
                parent=tree_trunk
            )
        
        # Village
        self.create_village()
        
        # Donjon
        self.create_dungeon()
        
    def create_village(self):
        """Création du village"""
        # Maisons
        for i in range(5):
            house = Entity(
                model='cube',
                position=(random.randint(-20, 20), 1, random.randint(-20, 20)),
                scale=(3, 2, 3),
                color=color.orange,
                texture='brick',
                collider='box'
            )
            roof = Entity(
                model='cone',
                position=(house.position + Vec3(0, 2, 0)),
                scale=(2, 1, 2),
                color=color.red,
                parent=house
            )
        
        # Fontaine centrale
        self.fountain = Entity(
            model='cylinder',
            position=(0, 0.5, 0),
            scale=(2, 1, 2),
            color=color.blue,
            collider='cylinder'
        )
        
    def create_dungeon(self):
        """Création du donjon"""
        # Entrée du donjon
        self.dungeon_entrance = Entity(
            model='cube',
            position=(30, 1, 30),
            scale=(4, 3, 4),
            color=color.dark_gray,
            texture='stone',
            collider='box'
        )
        
        # Porte du donjon
        self.dungeon_door = Entity(
            model='cube',
            position=(30, 1.5, 32),
            scale=(2, 2, 0.1),
            color=color.brown,
            collider='box'
        )
        
    def create_player(self):
        """Création du joueur"""
        self.player = FirstPersonController(
            position=(0, 2, 0),
            speed=10,
            jump_height=2,
            gravity=1
        )
        
        # Épée du joueur
        self.player_sword = Entity(
            model='cube',
            position=(0.5, -0.3, 0.5),
            scale=(0.1, 0.5, 0.1),
            color=color.gray,
            parent=camera
        )
        
    def create_ui(self):
        """Création de l'interface utilisateur"""
        # Barre de vie
        self.health_bar = Entity(
            model='quad',
            parent=camera.ui,
            position=(-0.8, 0.4, 0),
            scale=(0.3, 0.05, 1),
            color=color.red
        )
        
        self.health_text = Text(
            text=f"Vie: {self.player_health}/{self.player_max_health}",
            position=(-0.8, 0.45, 0),
            scale=1.5,
            color=color.white
        )
        
        # Niveau et expérience
        self.level_text = Text(
            text=f"Niveau: {self.player_level}",
            position=(-0.8, 0.35, 0),
            scale=1.2,
            color=color.white
        )
        
        self.exp_text = Text(
            text=f"Expérience: {self.player_exp}",
            position=(-0.8, 0.3, 0),
            scale=1.2,
            color=color.white
        )
        
        # Or
        self.gold_text = Text(
            text=f"Or: {self.player_gold}",
            position=(-0.8, 0.25, 0),
            scale=1.2,
            color=color.yellow
        )
        
        # Menu principal
        self.menu_button = Button(
            text="Menu",
            position=(0.8, 0.4, 0),
            scale=(0.2, 0.05, 1),
            color=color.blue,
            on_click=self.show_menu
        )
        
    def create_npcs(self):
        """Création des personnages non-joueurs"""
        # Marchand
        self.merchant = Entity(
            model='sphere',
            position=(5, 1, 5),
            scale=(0.5, 1, 0.5),
            color=color.green,
            collider='sphere'
        )
        
        # Garde
        self.guard = Entity(
            model='sphere',
            position=(-5, 1, -5),
            scale=(0.5, 1, 0.5),
            color=color.blue,
            collider='sphere'
        )
        
        # Sage
        self.sage = Entity(
            model='sphere',
            position=(0, 1, 10),
            scale=(0.5, 1, 0.5),
            color=color.violet,
            collider='sphere'
        )
        
    def create_enemies(self):
        """Création des ennemis"""
        self.enemies = []
        
        # Gobelins
        for i in range(5):
            goblin = Entity(
                model='sphere',
                position=(random.randint(-30, 30), 1, random.randint(-30, 30)),
                scale=(0.4, 0.8, 0.4),
                color=color.red,
                collider='sphere'
            )
            goblin.health = 30
            goblin.damage = 10
            goblin.speed = 2
            self.enemies.append(goblin)
        
        # Trolls
        for i in range(2):
            troll = Entity(
                model='sphere',
                position=(random.randint(-40, 40), 1.5, random.randint(-40, 40)),
                scale=(0.6, 1.2, 0.6),
                color=color.dark_gray,
                collider='sphere'
            )
            troll.health = 80
            troll.damage = 25
            troll.speed = 1
            self.enemies.append(troll)
            
    def create_items(self):
        """Création des objets"""
        self.items = []
        
        # Potions de vie
        for i in range(10):
            potion = Entity(
                model='sphere',
                position=(random.randint(-40, 40), 0.5, random.randint(-40, 40)),
                scale=(0.2, 0.2, 0.2),
                color=color.pink,
                collider='sphere'
            )
            potion.type = "potion"
            potion.value = 20
            self.items.append(potion)
        
        # Épées
        for i in range(3):
            sword = Entity(
                model='cube',
                position=(random.randint(-40, 40), 0.5, random.randint(-40, 40)),
                scale=(0.1, 0.5, 0.1),
                color=color.gray,
                collider='box'
            )
            sword.type = "weapon"
            sword.damage = 15
            self.items.append(sword)
            
    def show_menu(self):
        """Afficher le menu principal"""
        # Sauvegarder le jeu
        self.save_game()
        
        # Menu simple
        menu_text = Text(
            text="MENU PRINCIPAL\n\n1. Continuer\n2. Sauvegarder\n3. Charger\n4. Quitter",
            position=(0, 0.2, 0),
            scale=2,
            color=color.white
        )
        
    def save_game(self):
        """Sauvegarder le jeu"""
        save_data = {
            'player_health': self.player_health,
            'player_level': self.player_level,
            'player_exp': self.player_exp,
            'player_gold': self.player_gold,
            'inventory': self.inventory,
            'position': [self.player.position.x, self.player.position.y, self.player.position.z]
        }
        
        with open('save_game.json', 'w') as f:
            json.dump(save_data, f)
            
    def load_game(self):
        """Charger le jeu"""
        try:
            with open('save_game.json', 'r') as f:
                save_data = json.load(f)
                
            self.player_health = save_data['player_health']
            self.player_level = save_data['player_level']
            self.player_exp = save_data['player_exp']
            self.player_gold = save_data['player_gold']
            self.inventory = save_data['inventory']
            
            # Position du joueur
            pos = save_data['position']
            self.player.position = Vec3(pos[0], pos[1], pos[2])
            
            self.update_ui()
            
        except FileNotFoundError:
            print("Aucune sauvegarde trouvée")
            
    def update_ui(self):
        """Mettre à jour l'interface utilisateur"""
        self.health_text.text = f"Vie: {self.player_health}/{self.player_max_health}"
        self.level_text.text = f"Niveau: {self.player_level}"
        self.exp_text.text = f"Expérience: {self.player_exp}"
        self.gold_text.text = f"Or: {self.player_gold}"
        
    def check_collisions(self):
        """Vérifier les collisions"""
        # Collision avec les ennemis
        for enemy in self.enemies:
            if distance(self.player.position, enemy.position) < 2:
                self.combat(enemy)
                
        # Collision avec les objets
        for item in self.items:
            if distance(self.player.position, item.position) < 1:
                self.pickup_item(item)
                
    def combat(self, enemy):
        """Système de combat"""
        # Attaque du joueur
        enemy.health -= 20
        
        # Attaque de l'ennemi
        self.player_health -= enemy.damage
        
        # Vérifier si l'ennemi est mort
        if enemy.health <= 0:
            self.enemies.remove(enemy)
            destroy(enemy)
            self.player_exp += 50
            self.player_gold += random.randint(10, 30)
            
        # Vérifier si le joueur est mort
        if self.player_health <= 0:
            self.game_over()
            
        self.update_ui()
        
    def pickup_item(self, item):
        """Ramasser un objet"""
        if item.type == "potion":
            self.player_health = min(self.player_max_health, self.player_health + item.value)
        elif item.type == "weapon":
            self.inventory.append(item)
            
        self.items.remove(item)
        destroy(item)
        self.update_ui()
        
    def game_over(self):
        """Fin de partie"""
        game_over_text = Text(
            text="GAME OVER\n\nAppuyez sur R pour recommencer",
            position=(0, 0, 0),
            scale=3,
            color=color.red
        )
        
    def update(self):
        """Boucle principale du jeu"""
        self.check_collisions()
        
        # Contrôles
        if held_keys['r']:
            self.restart_game()
            
        if held_keys['f5']:
            self.save_game()
            
        if held_keys['f9']:
            self.load_game()
            
    def restart_game(self):
        """Redémarrer le jeu"""
        self.player_health = self.player_max_health
        self.player_level = 1
        self.player_exp = 0
        self.player_gold = 50
        self.inventory = []
        self.player.position = Vec3(0, 2, 0)
        self.update_ui()

if __name__ == '__main__':
    # Créer et lancer le jeu
    game = RPGGame()
    game.run() 