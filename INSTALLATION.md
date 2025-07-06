# Guide d'Installation - Flyff Universe Clone

## 🚀 Installation Rapide

### Prérequis
- **Node.js** 18.0.0 ou supérieur
- **npm** 8.0.0 ou supérieur
- **Git** (pour cloner le repository)

### Étapes d'Installation

1. **Cloner le repository**
   ```bash
   git clone https://github.com/votre-username/3d-test.git
   cd 3d-test
   ```

2. **Installer les dépendances**
   ```bash
   npm install
   ```

3. **Démarrer le serveur de développement**
   ```bash
   npm run dev
   ```

4. **Ouvrir dans le navigateur**
   - Allez à `http://localhost:3000`
   - Le jeu devrait se charger automatiquement

## 🛠️ Scripts Disponibles

| Commande | Description |
|----------|-------------|
| `npm run dev` | Démarre le serveur de développement |
| `npm run build` | Construit le projet pour la production |
| `npm run preview` | Prévisualise la build de production |
| `npm run deploy` | Déploie sur GitHub Pages |
| `npm run lint` | Vérifie le code avec ESLint |

## 🌐 Déploiement sur GitHub Pages

### Déploiement Automatique
Le projet est configuré pour se déployer automatiquement sur GitHub Pages à chaque push sur la branche `main`.

### Déploiement Manuel
```bash
npm run deploy
```

L'URL sera : `https://locktix.github.io/testcaca/`

## 🔧 Configuration

### Variables d'Environnement
Créez un fichier `.env.local` à la racine du projet :
```env
VITE_GAME_TITLE=Flyff Universe Clone
VITE_API_URL=http://localhost:3001
```

### Personnalisation
- **Couleurs** : Modifiez `tailwind.config.js`
- **Paramètres du jeu** : Ajustez `src/stores/gameStore.ts`
- **Zones** : Personnalisez `src/components/game/Terrain.tsx`
- **Items** : Modifiez `src/data/gameData.ts`

## 🎮 Contrôles

### Mouvement
- **WASD** ou **Flèches** : Déplacer le personnage
- **Espace** : Sauter

### Interface
- **I** : Inventaire
- **C** : Personnage
- **K** : Compétences
- **Entrée** : Chat
- **Échap** : Fermer les fenêtres

### Caméra
- **Clic gauche + glisser** : Rotation
- **Molette** : Zoom

## 🐛 Dépannage

### Problèmes Courants

#### Erreur "Cannot find module"
```bash
# Supprimer node_modules et réinstaller
rm -rf node_modules package-lock.json
npm install
```

#### Erreur de port déjà utilisé
```bash
# Changer le port dans vite.config.ts
server: {
  port: 3001, // ou un autre port libre
  open: true
}
```

#### Erreur de build
```bash
# Nettoyer le cache
npm run build -- --force
```

#### Problème de performance
- Vérifiez que votre navigateur supporte WebGL
- Désactivez les extensions de navigateur
- Utilisez un navigateur moderne (Chrome, Firefox, Safari, Edge)

### Logs de Développement
```bash
# Activer les logs détaillés
DEBUG=* npm run dev
```

## 📱 Compatibilité

### Navigateurs Supportés
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

### Systèmes d'Exploitation
- ✅ Windows 10/11
- ✅ macOS 10.15+
- ✅ Linux (Ubuntu 20.04+)

### Matériel Minimum
- **RAM** : 4 GB
- **GPU** : Support WebGL 2.0
- **Stockage** : 1 GB libre

## 🔒 Sécurité

### Bonnes Pratiques
- Ne committez jamais les fichiers `.env`
- Utilisez HTTPS en production
- Validez les entrées utilisateur
- Mettez à jour régulièrement les dépendances

### Audit de Sécurité
```bash
npm audit
npm audit fix
```

## 📊 Performance

### Optimisations Incluses
- Code splitting automatique
- Lazy loading des composants
- Compression des assets
- Cache des ressources

### Monitoring
```bash
# Analyser la taille du bundle
npm run build -- --analyze
```

## 🤝 Support

### Ressources Utiles
- [Documentation React](https://react.dev/)
- [Documentation Three.js](https://threejs.org/docs/)
- [Documentation Vite](https://vitejs.dev/)

### Communauté
- Issues GitHub
- Discussions GitHub
- Discord (si disponible)

---

**Bon jeu !** 🎮✨ 