#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Système de quêtes pour le RPG Aventure 3D
"""

import json
import random
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class Quest:
    """Classe représentant une quête"""
    id: str
    title: str
    description: str
    objectives: List[str]
    rewards: Dict[str, int]
    required_level: int
    is_completed: bool = False
    is_active: bool = False

class QuestSystem:
    """Système de gestion des quêtes"""
    
    def __init__(self):
        self.available_quests = []
        self.active_quests = []
        self.completed_quests = []
        self.quest_progress = {}
        
        self.load_quests()
        
    def load_quests(self):
        """Charger les quêtes depuis le fichier JSON"""
        quests_data = {
            "quests": [
                {
                    "id": "quest_001",
                    "title": "Les Gobelins du Bois",
                    "description": "Éliminez 3 gobelins qui terrorisent le village",
                    "objectives": ["Tuer 3 gobelins"],
                    "rewards": {"exp": 100, "gold": 50, "item": "Épée en fer"},
                    "required_level": 1
                },
                {
                    "id": "quest_002", 
                    "title": "Le Trésor du Donjon",
                    "description": "Explorez le donjon et trouvez le trésor caché",
                    "objectives": ["Entrer dans le donjon", "Trouver le trésor"],
                    "rewards": {"exp": 200, "gold": 100, "item": "Armure en cuir"},
                    "required_level": 3
                },
                {
                    "id": "quest_003",
                    "title": "Le Troll des Montagnes",
                    "description": "Défiez le troll qui vit dans les montagnes",
                    "objectives": ["Trouver le troll", "Vaincre le troll"],
                    "rewards": {"exp": 300, "gold": 150, "item": "Épée magique"},
                    "required_level": 5
                },
                {
                    "id": "quest_004",
                    "title": "Les Potions du Sage",
                    "description": "Récupérez 5 potions pour le sage du village",
                    "objectives": ["Trouver 5 potions"],
                    "rewards": {"exp": 80, "gold": 30, "item": "Potion de force"},
                    "required_level": 2
                },
                {
                    "id": "quest_005",
                    "title": "Le Gardien de la Fontaine",
                    "description": "Protégez la fontaine du village des créatures",
                    "objectives": ["Défendre la fontaine", "Tuer 5 ennemis près de la fontaine"],
                    "rewards": {"exp": 150, "gold": 75, "item": "Bouclier"},
                    "required_level": 4
                }
            ]
        }
        
        for quest_data in quests_data["quests"]:
            quest = Quest(
                id=quest_data["id"],
                title=quest_data["title"],
                description=quest_data["description"],
                objectives=quest_data["objectives"],
                rewards=quest_data["rewards"],
                required_level=quest_data["required_level"]
            )
            self.available_quests.append(quest)
            
    def get_available_quests(self, player_level: int) -> List[Quest]:
        """Obtenir les quêtes disponibles pour le niveau du joueur"""
        return [quest for quest in self.available_quests 
                if quest.required_level <= player_level and not quest.is_completed]
                
    def accept_quest(self, quest_id: str) -> bool:
        """Accepter une quête"""
        for quest in self.available_quests:
            if quest.id == quest_id and not quest.is_active:
                quest.is_active = True
                self.active_quests.append(quest)
                self.quest_progress[quest_id] = 0
                return True
        return False
        
    def update_quest_progress(self, quest_id: str, progress: int = 1):
        """Mettre à jour le progrès d'une quête"""
        if quest_id in self.quest_progress:
            self.quest_progress[quest_id] += progress
            
    def check_quest_completion(self, quest_id: str) -> bool:
        """Vérifier si une quête est terminée"""
        for quest in self.active_quests:
            if quest.id == quest_id:
                # Logique simple : quête terminée après 3 actions
                if self.quest_progress.get(quest_id, 0) >= 3:
                    return True
        return False
        
    def complete_quest(self, quest_id: str) -> Dict[str, Any] | None:
        """Terminer une quête et donner les récompenses"""
        for quest in self.active_quests:
            if quest.id == quest_id:
                quest.is_completed = True
                quest.is_active = False
                self.active_quests.remove(quest)
                self.completed_quests.append(quest)
                
                # Donner les récompenses
                rewards = quest.rewards.copy()
                
                return {
                    "quest": quest,
                    "rewards": rewards,
                    "message": f"Quête '{quest.title}' terminée !"
                }
        return None
        
    def get_quest_status(self, quest_id: str) -> Dict[str, Any] | None:
        """Obtenir le statut d'une quête"""
        for quest in self.active_quests:
            if quest.id == quest_id:
                progress = self.quest_progress.get(quest_id, 0)
                return {
                    "quest": quest,
                    "progress": progress,
                    "max_progress": 3,
                    "percentage": (progress / 3) * 100
                }
        return None
        
    def save_quests(self):
        """Sauvegarder l'état des quêtes"""
        save_data = {
            "active_quests": [quest.id for quest in self.active_quests],
            "completed_quests": [quest.id for quest in self.completed_quests],
            "quest_progress": self.quest_progress
        }
        
        with open('quests_save.json', 'w') as f:
            json.dump(save_data, f)
            
    def load_quests_save(self):
        """Charger l'état des quêtes"""
        try:
            with open('quests_save.json', 'r') as f:
                save_data = json.load(f)
                
            # Restaurer les quêtes actives
            for quest_id in save_data.get("active_quests", []):
                for quest in self.available_quests:
                    if quest.id == quest_id:
                        quest.is_active = True
                        self.active_quests.append(quest)
                        break
                        
            # Restaurer les quêtes terminées
            for quest_id in save_data.get("completed_quests", []):
                for quest in self.available_quests:
                    if quest.id == quest_id:
                        quest.is_completed = True
                        self.completed_quests.append(quest)
                        break
                        
            # Restaurer le progrès
            self.quest_progress = save_data.get("quest_progress", {})
            
        except FileNotFoundError:
            pass  # Pas de sauvegarde existante 