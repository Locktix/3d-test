#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration du RPG Aventure 3D
"""

import json
from pathlib import Path

class GameConfig:
    """Configuration du jeu"""
    
    def __init__(self):
        self.config_file = "game_config.json"
        self.default_config = {
            # Configuration graphique
            "graphics": {
                "resolution": [1280, 720],
                "fullscreen": False,
                "vsync": True,
                "fps_limit": 60,
                "render_distance": 100,
                "shadows": True,
                "antialiasing": True
            },
            
            # Configuration audio
            "audio": {
                "master_volume": 1.0,
                "music_volume": 0.7,
                "sfx_volume": 0.8,
                "voice_volume": 0.9,
                "enable_audio": True
            },
            
            # Configuration des contrôles
            "controls": {
                "mouse_sensitivity": 1.0,
                "invert_mouse_y": False,
                "keyboard_layout": "qwerty",  # qwerty ou azerty
                "gamepad_enabled": False
            },
            
            # Configuration du gameplay
            "gameplay": {
                "difficulty": "normal",  # easy, normal, hard, nightmare
                "auto_save": True,
                "auto_save_interval": 300,  # secondes
                "show_hints": True,
                "show_minimap": True,
                "show_health_bars": True,
                "show_damage_numbers": True
            },
            
            # Configuration de l'IA
            "ai": {
                "enemy_aggression": 1.0,
                "enemy_detection_range": 1.0,
                "enemy_speed": 1.0,
                "npc_interaction_range": 3.0,
                "enemy_respawn_time": 60  # secondes
            },
            
            # Configuration de l'interface
            "ui": {
                "ui_scale": 1.0,
                "show_fps": True,
                "show_coordinates": False,
                "show_debug_info": False,
                "language": "french"
            },
            
            # Configuration des sauvegardes
            "save": {
                "max_save_slots": 10,
                "auto_backup": True,
                "backup_interval": 24,  # heures
                "save_directory": "saves/"
            }
        }
        
        self.config = self.load_config()
        
    def load_config(self):
        """Charger la configuration"""
        try:
            if Path(self.config_file).exists():
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    # Fusionner avec la configuration par défaut
                    return self.merge_configs(self.default_config, config)
            else:
                # Créer le fichier de configuration par défaut
                self.save_config(self.default_config)
                return self.default_config
        except Exception as e:
            print(f"Erreur lors du chargement de la configuration: {e}")
            return self.default_config
            
    def save_config(self, config=None):
        """Sauvegarder la configuration"""
        if config is None:
            config = self.config
            
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde de la configuration: {e}")
            
    def merge_configs(self, default, user):
        """Fusionner les configurations par défaut et utilisateur"""
        merged = default.copy()
        
        for key, value in user.items():
            if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
                merged[key] = self.merge_configs(merged[key], value)
            else:
                merged[key] = value
                
        return merged
        
    def get(self, key_path, default=None):
        """Obtenir une valeur de configuration"""
        keys = key_path.split('.')
        value = self.config
        
        try:
            for key in keys:
                value = value[key]
            return value
        except (KeyError, TypeError):
            return default
            
    def set(self, key_path, value):
        """Définir une valeur de configuration"""
        keys = key_path.split('.')
        config = self.config
        
        # Naviguer vers le bon niveau
        for key in keys[:-1]:
            if key not in config:
                config[key] = {}
            config = config[key]
            
        # Définir la valeur
        config[keys[-1]] = value
        
        # Sauvegarder
        self.save_config()
        
    def reset_to_defaults(self):
        """Réinitialiser à la configuration par défaut"""
        self.config = self.default_config.copy()
        self.save_config()
        
    def get_graphics_settings(self):
        """Obtenir les paramètres graphiques"""
        return self.get('graphics', {})
        
    def get_audio_settings(self):
        """Obtenir les paramètres audio"""
        return self.get('audio', {})
        
    def get_control_settings(self):
        """Obtenir les paramètres de contrôle"""
        return self.get('controls', {})
        
    def get_gameplay_settings(self):
        """Obtenir les paramètres de gameplay"""
        return self.get('gameplay', {})
        
    def get_ai_settings(self):
        """Obtenir les paramètres d'IA"""
        return self.get('ai', {})
        
    def get_ui_settings(self):
        """Obtenir les paramètres d'interface"""
        return self.get('ui', {})
        
    def get_save_settings(self):
        """Obtenir les paramètres de sauvegarde"""
        return self.get('save', {})

# Instance globale de configuration
config = GameConfig()

# Fonctions utilitaires
def get_resolution():
    """Obtenir la résolution actuelle"""
    return config.get('graphics.resolution', [1280, 720])

def is_fullscreen():
    """Vérifier si le mode plein écran est activé"""
    return config.get('graphics.fullscreen', False)

def get_master_volume():
    """Obtenir le volume principal"""
    return config.get('audio.master_volume', 1.0)

def get_difficulty():
    """Obtenir le niveau de difficulté"""
    return config.get('gameplay.difficulty', 'normal')

def get_language():
    """Obtenir la langue"""
    return config.get('ui.language', 'french')

def get_mouse_sensitivity():
    """Obtenir la sensibilité de la souris"""
    return config.get('controls.mouse_sensitivity', 1.0)

def is_auto_save_enabled():
    """Vérifier si la sauvegarde automatique est activée"""
    return config.get('gameplay.auto_save', True)

def get_auto_save_interval():
    """Obtenir l'intervalle de sauvegarde automatique"""
    return config.get('gameplay.auto_save_interval', 300)

def get_enemy_aggression():
    """Obtenir l'agressivité des ennemis"""
    return config.get('ai.enemy_aggression', 1.0)

def get_enemy_detection_range():
    """Obtenir la portée de détection des ennemis"""
    return config.get('ai.enemy_detection_range', 1.0)

def get_ui_scale():
    """Obtenir l'échelle de l'interface"""
    return config.get('ui.ui_scale', 1.0)

def show_fps():
    """Vérifier si l'affichage FPS est activé"""
    return config.get('ui.show_fps', True)

def show_debug_info():
    """Vérifier si l'affichage des infos de debug est activé"""
    return config.get('ui.show_debug_info', False) 