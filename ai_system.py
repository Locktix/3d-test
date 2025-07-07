#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Système d'IA pour les ennemis et NPCs du RPG
"""

import math
import random
from typing import List, Tuple, Optional
from enum import Enum
from ursina import Vec3

class AIState(Enum):
    """États possibles de l'IA"""
    IDLE = "idle"
    PATROL = "patrol"
    CHASE = "chase"
    ATTACK = "attack"
    FLEE = "flee"
    DEAD = "dead"

class AIController:
    """Contrôleur d'IA de base"""
    
    def __init__(self, entity, ai_type: str = "basic"):
        self.entity = entity
        self.ai_type = ai_type
        self.state = AIState.IDLE
        self.target = None
        self.patrol_points = []
        self.current_patrol_index = 0
        self.detection_range = 10
        self.attack_range = 2
        self.speed = 2
        self.health = 100
        self.max_health = 100
        self.damage = 10
        self.last_attack_time = 0
        self.attack_cooldown = 1.0  # secondes
        
    def update(self, player_position, delta_time: float):
        """Mettre à jour l'IA"""
        if self.health <= 0:
            self.state = AIState.DEAD
            return
            
        distance_to_player = self.get_distance_to_player(player_position)
        
        # Machine à états
        if self.state == AIState.IDLE:
            self.idle_behavior(distance_to_player)
        elif self.state == AIState.PATROL:
            self.patrol_behavior(distance_to_player)
        elif self.state == AIState.CHASE:
            self.chase_behavior(player_position, distance_to_player)
        elif self.state == AIState.ATTACK:
            self.attack_behavior(player_position, distance_to_player, delta_time)
        elif self.state == AIState.FLEE:
            self.flee_behavior(player_position)
            
    def idle_behavior(self, distance_to_player: float):
        """Comportement en mode veille"""
        if distance_to_player <= self.detection_range:
            self.state = AIState.CHASE
        elif random.random() < 0.01:  # 1% de chance de commencer à patrouiller
            self.state = AIState.PATROL
            
    def patrol_behavior(self, distance_to_player: float):
        """Comportement de patrouille"""
        if distance_to_player <= self.detection_range:
            self.state = AIState.CHASE
            return
            
        if not self.patrol_points:
            # Créer des points de patrouille aléatoires
            self.generate_patrol_points()
            
        # Se déplacer vers le point de patrouille actuel
        target_point = self.patrol_points[self.current_patrol_index]
        direction = (target_point - self.entity.position).normalized()
        self.entity.position += direction * self.speed * 0.016  # 60 FPS
        
        # Vérifier si on a atteint le point de patrouille
        if self.get_distance_to_point(target_point) < 1:
            self.current_patrol_index = (self.current_patrol_index + 1) % len(self.patrol_points)
            
    def chase_behavior(self, player_position, distance_to_player: float):
        """Comportement de poursuite"""
        if distance_to_player <= self.attack_range:
            self.state = AIState.ATTACK
        elif distance_to_player > self.detection_range * 1.5:
            self.state = AIState.PATROL
        else:
            # Se diriger vers le joueur
            direction = (player_position - self.entity.position).normalized()
            self.entity.position += direction * self.speed * 0.016
            
    def attack_behavior(self, player_position, distance_to_player: float, delta_time: float):
        """Comportement d'attaque"""
        if distance_to_player > self.attack_range:
            self.state = AIState.CHASE
            return
            
        # Attaquer si le cooldown est terminé
        if delta_time - self.last_attack_time >= self.attack_cooldown:
            self.perform_attack()
            self.last_attack_time = delta_time
            
    def flee_behavior(self, player_position):
        """Comportement de fuite"""
        # Fuir dans la direction opposée au joueur
        direction = (self.entity.position - player_position).normalized()
        self.entity.position += direction * self.speed * 0.016
        
        # Arrêter de fuir après un certain temps
        if random.random() < 0.01:
            self.state = AIState.IDLE
            
    def perform_attack(self):
        """Effectuer une attaque"""
        # Cette méthode sera surchargée par les classes spécifiques
        pass
        
    def take_damage(self, damage: int):
        """Recevoir des dégâts"""
        self.health -= damage
        if self.health <= 0:
            self.state = AIState.DEAD
        elif self.health < self.max_health * 0.3:  # Fuir si santé faible
            self.state = AIState.FLEE
            
    def generate_patrol_points(self):
        """Générer des points de patrouille"""
        center = self.entity.position
        for i in range(5):
            angle = (i / 5) * 2 * math.pi
            radius = random.uniform(5, 15)
            x = center.x + radius * math.cos(angle)
            z = center.z + radius * math.sin(angle)
            self.patrol_points.append(Vec3(x, center.y, z))
            
    def get_distance_to_player(self, player_position) -> float:
        """Calculer la distance au joueur"""
        return (player_position - self.entity.position).length()
        
    def get_distance_to_point(self, point) -> float:
        """Calculer la distance à un point"""
        return (point - self.entity.position).length()

class GoblinAI(AIController):
    """IA spécifique pour les gobelins"""
    
    def __init__(self, entity):
        super().__init__(entity, "goblin")
        self.detection_range = 8
        self.attack_range = 1.5
        self.speed = 3
        self.health = 30
        self.max_health = 30
        self.damage = 10
        self.attack_cooldown = 0.8
        
    def perform_attack(self):
        """Attaque de gobelin"""
        # Attaque rapide et faible
        pass

class TrollAI(AIController):
    """IA spécifique pour les trolls"""
    
    def __init__(self, entity):
        super().__init__(entity, "troll")
        self.detection_range = 12
        self.attack_range = 2.5
        self.speed = 1.5
        self.health = 80
        self.max_health = 80
        self.damage = 25
        self.attack_cooldown = 1.5
        
    def perform_attack(self):
        """Attaque de troll"""
        # Attaque lente mais puissante
        pass

class MerchantAI(AIController):
    """IA pour le marchand"""
    
    def __init__(self, entity):
        super().__init__(entity, "merchant")
        self.detection_range = 5
        self.speed = 0  # Le marchand ne bouge pas
        self.health = 100
        self.max_health = 100
        
    def update(self, player_position, delta_time: float):
        """Le marchand reste toujours en mode veille"""
        distance_to_player = self.get_distance_to_player(player_position)
        
        if distance_to_player <= self.detection_range:
            # Le marchand peut interagir avec le joueur
            pass

class GuardAI(AIController):
    """IA pour les gardes"""
    
    def __init__(self, entity):
        super().__init__(entity, "guard")
        self.detection_range = 15
        self.attack_range = 2
        self.speed = 2.5
        self.health = 60
        self.max_health = 60
        self.damage = 15
        self.attack_cooldown = 1.0
        
    def update(self, player_position, delta_time: float):
        """Les gardes patrouillent et protègent"""
        super().update(player_position, delta_time)
        
        # Les gardes ne fuient jamais
        if self.state == AIState.FLEE:
            self.state = AIState.CHASE

class SageAI(AIController):
    """IA pour le sage"""
    
    def __init__(self, entity):
        super().__init__(entity, "sage")
        self.detection_range = 8
        self.speed = 0  # Le sage ne bouge pas
        self.health = 50
        self.max_health = 50
        
    def update(self, player_position, delta_time: float):
        """Le sage reste toujours en mode veille"""
        distance_to_player = self.get_distance_to_player(player_position)
        
        if distance_to_player <= self.detection_range:
            # Le sage peut donner des conseils et des quêtes
            pass

class AISystem:
    """Système de gestion de l'IA"""
    
    def __init__(self):
        self.ai_controllers = []
        
    def add_ai_controller(self, entity, ai_type: str):
        """Ajouter un contrôleur d'IA"""
        if ai_type == "goblin":
            controller = GoblinAI(entity)
        elif ai_type == "troll":
            controller = TrollAI(entity)
        elif ai_type == "merchant":
            controller = MerchantAI(entity)
        elif ai_type == "guard":
            controller = GuardAI(entity)
        elif ai_type == "sage":
            controller = SageAI(entity)
        else:
            controller = AIController(entity, ai_type)
            
        self.ai_controllers.append(controller)
        return controller
        
    def update_all(self, player_position, delta_time: float):
        """Mettre à jour tous les contrôleurs d'IA"""
        for controller in self.ai_controllers[:]:  # Copie pour éviter les erreurs de modification
            if controller.state != AIState.DEAD:
                controller.update(player_position, delta_time)
            else:
                # Supprimer les entités mortes
                self.ai_controllers.remove(controller)
                
    def get_nearby_enemies(self, player_position, range: float) -> List[AIController]:
        """Obtenir les ennemis proches du joueur"""
        nearby = []
        for controller in self.ai_controllers:
            if (controller.ai_type in ["goblin", "troll"] and 
                controller.get_distance_to_player(player_position) <= range):
                nearby.append(controller)
        return nearby
        
    def get_nearby_npcs(self, player_position, range: float) -> List[AIController]:
        """Obtenir les NPCs proches du joueur"""
        nearby = []
        for controller in self.ai_controllers:
            if (controller.ai_type in ["merchant", "guard", "sage"] and 
                controller.get_distance_to_player(player_position) <= range):
                nearby.append(controller)
        return nearby 