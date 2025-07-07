#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script d'installation automatique pour le RPG Aventure 3D
"""

import subprocess
import sys
import os
from pathlib import Path

def check_python_version():
    """Vérifier la version de Python"""
    if sys.version_info < (3, 8):
        print("❌ Erreur: Python 3.8 ou supérieur est requis")
        print(f"Version actuelle: {sys.version}")
        return False
    print(f"✅ Python {sys.version.split()[0]} détecté")
    return True

def install_dependencies():
    """Installer les dépendances"""
    print("📦 Installation des dépendances...")
    
    try:
        # Installer les dépendances depuis requirements.txt
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dépendances installées avec succès")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de l'installation: {e}")
        return False

def create_directories():
    """Créer les répertoires nécessaires"""
    print("📁 Création des répertoires...")
    
    directories = ["saves", "logs", "assets"]
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Répertoire {directory} créé")

def test_installation():
    """Tester l'installation"""
    print("🧪 Test de l'installation...")
    
    try:
        # Tester l'import d'Ursina
        import ursina
        print("✅ Ursina importé avec succès")
        
        # Tester l'import de pygame
        import pygame
        print("✅ Pygame importé avec succès")
        
        # Tester l'import de numpy
        import numpy
        print("✅ NumPy importé avec succès")
        
        return True
    except ImportError as e:
        print(f"❌ Erreur d'import: {e}")
        return False

def create_launcher_script():
    """Créer un script de lancement"""
    print("🚀 Création du script de lancement...")
    
    if sys.platform == "win32":
        # Script batch pour Windows
        launcher_content = """@echo off
echo Lancement du RPG Aventure 3D...
python main.py
pause
"""
        with open("lancer_jeu.bat", "w", encoding="utf-8") as f:
            f.write(launcher_content)
        print("✅ Script de lancement Windows créé: lancer_jeu.bat")
        
    else:
        # Script shell pour Linux/Mac
        launcher_content = """#!/bin/bash
echo "Lancement du RPG Aventure 3D..."
python3 main.py
"""
        with open("lancer_jeu.sh", "w") as f:
            f.write(launcher_content)
        os.chmod("lancer_jeu.sh", 0o755)
        print("✅ Script de lancement Unix créé: lancer_jeu.sh")

def main():
    """Fonction principale d'installation"""
    print("🎮 Installation du RPG Aventure 3D")
    print("=" * 40)
    
    # Vérifier Python
    if not check_python_version():
        sys.exit(1)
    
    # Installer les dépendances
    if not install_dependencies():
        print("❌ Échec de l'installation des dépendances")
        sys.exit(1)
    
    # Créer les répertoires
    create_directories()
    
    # Tester l'installation
    if not test_installation():
        print("❌ Échec du test d'installation")
        sys.exit(1)
    
    # Créer le script de lancement
    create_launcher_script()
    
    print("\n" + "=" * 40)
    print("🎉 Installation terminée avec succès!")
    print("\nPour lancer le jeu:")
    
    if sys.platform == "win32":
        print("  - Double-cliquez sur 'lancer_jeu.bat'")
        print("  - Ou tapez: python main.py")
    else:
        print("  - Double-cliquez sur 'lancer_jeu.sh'")
        print("  - Ou tapez: python3 main.py")
    
    print("\n🎮 Bon jeu!")

if __name__ == "__main__":
    main() 