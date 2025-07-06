# Flyff Universe Clone - MMORPG 3D

Un clone de MMORPG 3D inspiré de Flyff Universe, développé avec React, Three.js et TypeScript. Jouable directement dans votre navigateur !

## 🎮 Fonctionnalités

- **Monde 3D immersif** avec Three.js et React Three Fiber
- **Système de classes** : Guerrier, Mage, Archer, Assassin
- **Zones variées** : Flaris, Saint Morning, Darkon
- **Interface utilisateur moderne** avec Tailwind CSS et Framer Motion
- **Système d'inventaire** et d'équipement
- **Barres de statut** (vie, mana, expérience)
- **Chat en temps réel** (simulé)
- **Animations fluides** et effets visuels
- **Responsive design** compatible mobile

## 🚀 Installation et Démarrage

### Prérequis
- Node.js 18+ 
- npm ou yarn

### Installation
```bash
# Cloner le repository
git clone https://github.com/votre-username/3d-test.git
cd 3d-test

# Installer les dépendances
npm install

# Démarrer le serveur de développement
npm run dev
```

Le jeu sera accessible à l'adresse : `http://localhost:3000`

### Build pour Production
```bash
# Construire le projet
npm run build

# Prévisualiser la build
npm run preview
```

## 🎯 Contrôles

- **WASD** ou **Flèches** : Déplacer le personnage
- **Espace** : Sauter
- **Clic gauche** : Rotation de la caméra
- **Molette** : Zoom avant/arrière

### Raccourcis Interface
- **C** : Ouvrir/Fermer le personnage
- **I** : Ouvrir/Fermer l'inventaire
- **K** : Ouvrir/Fermer les compétences
- **Entrée** : Ouvrir/Fermer le chat

## 🏗️ Architecture

```
src/
├── components/
│   ├── game/          # Composants 3D du jeu
│   │   ├── Player.tsx # Modèle 3D du joueur
│   │   └── Terrain.tsx # Terrain et environnement
│   ├── ui/            # Interface utilisateur
│   │   └── GameUI.tsx # Interface principale
│   ├── LoginScreen.tsx
│   ├── LoadingScreen.tsx
│   └── GameWorld.tsx
├── stores/
│   └── gameStore.ts   # État global avec Zustand
├── App.tsx
└── main.tsx
```

## 🛠️ Technologies Utilisées

- **React 18** - Framework UI
- **TypeScript** - Typage statique
- **Three.js** - Moteur 3D
- **React Three Fiber** - Intégration React/Three.js
- **React Three Drei** - Utilitaires Three.js
- **Zustand** - Gestion d'état
- **Tailwind CSS** - Styling
- **Framer Motion** - Animations
- **Vite** - Build tool
- **React Router** - Navigation

## 🎨 Classes Disponibles

### ⚔️ Guerrier
- **Spécialité** : Combat rapproché, défense
- **Arme** : Épée à deux mains
- **Rôle** : Tank, DPS

### 🔮 Mage
- **Spécialité** : Magie élémentaire, sorts
- **Arme** : Baguette magique
- **Rôle** : DPS, Support

### 🏹 Archer
- **Spécialité** : Combat à distance, précision
- **Arme** : Arc
- **Rôle** : DPS, Kiting

### 🗡️ Assassin
- **Spécialité** : Furtivité, dégâts critiques
- **Arme** : Dagues
- **Rôle** : DPS, Burst

## 🌍 Zones du Monde

### 🏘️ Flaris (Niveaux 1-20)
- Zone de départ paisible
- Village de Flarine
- Eau et verdure
- Parfaite pour les débutants

### 🏰 Saint Morning (Niveaux 21-42)
- Plus grande ville de Madrigal
- Désert fantastique
- Arène PvP
- Pumpkin Town

### ⚫ Darkon (Niveaux 51-120)
- Zone industrielle sombre
- Machines hostiles
- Donjons dangereux
- Boss puissants

## 🚀 Déploiement sur GitHub Pages

Le projet est configuré pour être déployé automatiquement sur GitHub Pages :

```bash
# Déployer sur GitHub Pages
npm run deploy
```

L'URL sera : `https://votre-username.github.io/3d-test/`

## 🔧 Configuration

### Variables d'Environnement
Créez un fichier `.env.local` :
```env
VITE_GAME_TITLE=Flyff Universe Clone
VITE_API_URL=http://localhost:3001
```

### Personnalisation
- Modifiez `tailwind.config.js` pour changer les couleurs
- Ajustez `src/stores/gameStore.ts` pour les paramètres du jeu
- Personnalisez les zones dans `src/components/game/Terrain.tsx`

## 🤝 Contribution

Les contributions sont les bienvenues ! Voici comment contribuer :

1. Fork le projet
2. Créez une branche feature (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📝 TODO

- [ ] Système de combat en temps réel
- [ ] Multi-joueurs avec WebSocket
- [ ] Système de quêtes
- [ ] Boutiques et commerce
- [ ] Système de guildes
- [ ] Donjons et raids
- [ ] Système de craft
- [ ] Animations de personnages
- [ ] Effets sonores et musique
- [ ] Sauvegarde des données

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🙏 Remerciements

- Inspiré par [Flyff Universe](https://universe.flyff.com/)
- Icônes par [Lucide React](https://lucide.dev/)
- Polices par Google Fonts

## 📞 Support

Pour toute question ou problème :
- Ouvrez une issue sur GitHub
- Contactez-nous via Discord
- Consultez la documentation

---

**Amusez-vous bien dans le monde de Madrigal !** 🎮✨ 