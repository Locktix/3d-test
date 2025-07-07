#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Système d'inventaire et de commerce pour le RPG
"""

import json
from typing import List, Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class Item:
    """Classe représentant un objet"""
    id: str
    name: str
    description: str
    item_type: str  # weapon, armor, potion, material, quest
    value: int
    weight: float
    rarity: str  # common, uncommon, rare, epic, legendary
    stats: Dict[str, int] | None = None
    
    def __post_init__(self):
        if self.stats is None:
            self.stats = {}

class Inventory:
    """Système d'inventaire"""
    
    def __init__(self, max_weight: float = 100.0):
        self.items = []
        self.max_weight = max_weight
        self.current_weight = 0.0
        
    def add_item(self, item: Item) -> bool:
        """Ajouter un objet à l'inventaire"""
        if self.current_weight + item.weight <= self.max_weight:
            self.items.append(item)
            self.current_weight += item.weight
            return True
        return False
        
    def remove_item(self, item_id: str) -> Optional[Item]:
        """Retirer un objet de l'inventaire"""
        for i, item in enumerate(self.items):
            if item.id == item_id:
                removed_item = self.items.pop(i)
                self.current_weight -= removed_item.weight
                return removed_item
        return None
        
    def get_item(self, item_id: str) -> Optional[Item]:
        """Obtenir un objet par son ID"""
        for item in self.items:
            if item.id == item_id:
                return item
        return None
        
    def get_items_by_type(self, item_type: str) -> List[Item]:
        """Obtenir tous les objets d'un certain type"""
        return [item for item in self.items if item.item_type == item_type]
        
    def has_item(self, item_id: str) -> bool:
        """Vérifier si l'inventaire contient un objet"""
        return any(item.id == item_id for item in self.items)
        
    def get_total_value(self) -> int:
        """Calculer la valeur totale de l'inventaire"""
        return sum(item.value for item in self.items)
        
    def save_inventory(self, filename: str = "inventory_save.json"):
        """Sauvegarder l'inventaire"""
        save_data = {
            "max_weight": self.max_weight,
            "current_weight": self.current_weight,
            "items": [
                {
                    "id": item.id,
                    "name": item.name,
                    "description": item.description,
                    "item_type": item.item_type,
                    "value": item.value,
                    "weight": item.weight,
                    "rarity": item.rarity,
                    "stats": item.stats
                }
                for item in self.items
            ]
        }
        
        with open(filename, 'w') as f:
            json.dump(save_data, f)
            
    def load_inventory(self, filename: str = "inventory_save.json"):
        """Charger l'inventaire"""
        try:
            with open(filename, 'r') as f:
                save_data = json.load(f)
                
            self.max_weight = save_data["max_weight"]
            self.current_weight = save_data["current_weight"]
            self.items = []
            
            for item_data in save_data["items"]:
                item = Item(
                    id=item_data["id"],
                    name=item_data["name"],
                    description=item_data["description"],
                    item_type=item_data["item_type"],
                    value=item_data["value"],
                    weight=item_data["weight"],
                    rarity=item_data["rarity"],
                    stats=item_data["stats"]
                )
                self.items.append(item)
                
        except FileNotFoundError:
            pass  # Pas de sauvegarde existante

class Shop:
    """Système de boutique"""
    
    def __init__(self):
        self.available_items = []
        self.load_shop_items()
        
    def load_shop_items(self):
        """Charger les objets disponibles dans la boutique"""
        shop_items = [
            {
                "id": "sword_iron",
                "name": "Épée en Fer",
                "description": "Une épée solide en fer forgé",
                "item_type": "weapon",
                "value": 100,
                "weight": 2.0,
                "rarity": "common",
                "stats": {"damage": 15, "durability": 100}
            },
            {
                "id": "sword_steel",
                "name": "Épée en Acier",
                "description": "Une épée tranchante en acier",
                "item_type": "weapon",
                "value": 250,
                "weight": 2.5,
                "rarity": "uncommon",
                "stats": {"damage": 25, "durability": 150}
            },
            {
                "id": "armor_leather",
                "name": "Armure en Cuir",
                "description": "Une armure légère en cuir",
                "item_type": "armor",
                "value": 80,
                "weight": 3.0,
                "rarity": "common",
                "stats": {"defense": 10, "weight": 3}
            },
            {
                "id": "armor_chain",
                "name": "Cotte de Mailles",
                "description": "Une armure en mailles de fer",
                "item_type": "armor",
                "value": 200,
                "weight": 8.0,
                "rarity": "uncommon",
                "stats": {"defense": 25, "weight": 8}
            },
            {
                "id": "potion_health",
                "name": "Potion de Vie",
                "description": "Restaure 50 points de vie",
                "item_type": "potion",
                "value": 30,
                "weight": 0.5,
                "rarity": "common",
                "stats": {"heal": 50}
            },
            {
                "id": "potion_mana",
                "name": "Potion de Mana",
                "description": "Restaure 50 points de mana",
                "item_type": "potion",
                "value": 25,
                "weight": 0.5,
                "rarity": "common",
                "stats": {"mana": 50}
            },
            {
                "id": "potion_strength",
                "name": "Potion de Force",
                "description": "Augmente temporairement la force",
                "item_type": "potion",
                "value": 50,
                "weight": 0.5,
                "rarity": "uncommon",
                "stats": {"strength": 10, "duration": 300}
            },
            {
                "id": "shield_wooden",
                "name": "Bouclier en Bois",
                "description": "Un bouclier simple en bois",
                "item_type": "shield",
                "value": 40,
                "weight": 2.0,
                "rarity": "common",
                "stats": {"defense": 5, "block": 15}
            },
            {
                "id": "shield_iron",
                "name": "Bouclier en Fer",
                "description": "Un bouclier solide en fer",
                "item_type": "shield",
                "value": 120,
                "weight": 4.0,
                "rarity": "uncommon",
                "stats": {"defense": 15, "block": 25}
            }
        ]
        
        for item_data in shop_items:
            item = Item(
                id=item_data["id"],
                name=item_data["name"],
                description=item_data["description"],
                item_type=item_data["item_type"],
                value=item_data["value"],
                weight=item_data["weight"],
                rarity=item_data["rarity"],
                stats=item_data["stats"]
            )
            self.available_items.append(item)
            
    def buy_item(self, player_inventory: Inventory, player_gold: int, item_id: str) -> Dict[str, Any]:
        """Acheter un objet"""
        item = self.get_item(item_id)
        if not item:
            return {"success": False, "message": "Objet non trouvé"}
            
        if player_gold < item.value:
            return {"success": False, "message": "Pas assez d'or"}
            
        if not player_inventory.add_item(item):
            return {"success": False, "message": "Inventaire plein"}
            
        return {
            "success": True,
            "item": item,
            "cost": item.value,
            "message": f"Acheté: {item.name}"
        }
        
    def sell_item(self, player_inventory: Inventory, item_id: str) -> Dict[str, Any]:
        """Vendre un objet"""
        item = player_inventory.remove_item(item_id)
        if not item:
            return {"success": False, "message": "Objet non trouvé dans l'inventaire"}
            
        # Le prix de vente est la moitié du prix d'achat
        sell_price = item.value // 2
        
        return {
            "success": True,
            "item": item,
            "price": sell_price,
            "message": f"Vendu: {item.name} pour {sell_price} or"
        }
        
    def get_item(self, item_id: str) -> Optional[Item]:
        """Obtenir un objet par son ID"""
        for item in self.available_items:
            if item.id == item_id:
                return item
        return None
        
    def get_items_by_type(self, item_type: str) -> List[Item]:
        """Obtenir tous les objets d'un certain type"""
        return [item for item in self.available_items if item.item_type == item_type]
        
    def get_items_by_rarity(self, rarity: str) -> List[Item]:
        """Obtenir tous les objets d'une certaine rareté"""
        return [item for item in self.available_items if item.rarity == rarity]

class ItemFactory:
    """Fabrique d'objets pour créer des objets dynamiquement"""
    
    @staticmethod
    def create_weapon(weapon_type: str, material: str, level: int = 1) -> Item:
        """Créer une arme"""
        base_damage = {"sword": 10, "axe": 15, "mace": 12, "dagger": 8}
        material_multiplier = {"wood": 0.5, "iron": 1.0, "steel": 1.5, "magic": 2.0}
        
        damage = int(base_damage.get(weapon_type, 10) * material_multiplier.get(material, 1.0) * level)
        value = damage * 5
        
        return Item(
            id=f"{weapon_type}_{material}_{level}",
            name=f"{weapon_type.title()} en {material.title()}",
            description=f"Une {weapon_type} en {material} de niveau {level}",
            item_type="weapon",
            value=value,
            weight=2.0,
            rarity="common",
            stats={"damage": damage, "level": level}
        )
        
    @staticmethod
    def create_potion(potion_type: str, power: int = 1) -> Item | None:
        """Créer une potion"""
        potion_data = {
            "health": {"name": "Potion de Vie", "stat": "heal", "base_value": 20},
            "mana": {"name": "Potion de Mana", "stat": "mana", "base_value": 15},
            "strength": {"name": "Potion de Force", "stat": "strength", "base_value": 5},
            "speed": {"name": "Potion de Vitesse", "stat": "speed", "base_value": 3}
        }
        
        if potion_type not in potion_data:
            return None
            
        data = potion_data[potion_type]
        stat_value = data["base_value"] * power
        
        return Item(
            id=f"potion_{potion_type}_{power}",
            name=data["name"],
            description=f"Restaure {stat_value} points de {potion_type}",
            item_type="potion",
            value=stat_value * 2,
            weight=0.5,
            rarity="common",
            stats={data["stat"]: stat_value}
        )
        
    @staticmethod
    def create_material(material_type: str, quantity: int = 1) -> Item | None:
        """Créer un matériau"""
        material_data = {
            "iron": {"name": "Minerai de Fer", "value": 5},
            "gold": {"name": "Minerai d'Or", "value": 15},
            "wood": {"name": "Bois", "value": 2},
            "leather": {"name": "Cuir", "value": 3},
            "cloth": {"name": "Tissu", "value": 1}
        }
        
        if material_type not in material_data:
            return None
            
        data = material_data[material_type]
        
        return Item(
            id=f"material_{material_type}_{quantity}",
            name=f"{data['name']} x{quantity}",
            description=f"{quantity} unité(s) de {data['name'].lower()}",
            item_type="material",
            value=data["value"] * quantity,
            weight=0.1 * quantity,
            rarity="common",
            stats={"quantity": quantity}
        ) 