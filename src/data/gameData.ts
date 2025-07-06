import { Item } from '../stores/gameStore'

export const ITEMS: Record<string, Item> = {
  'sword-basic': {
    id: 'sword-basic',
    name: 'Épée en fer',
    type: 'weapon',
    rarity: 'common',
    level: 1,
    icon: '⚔️'
  },
  'sword-steel': {
    id: 'sword-steel',
    name: 'Épée en acier',
    type: 'weapon',
    rarity: 'uncommon',
    level: 5,
    icon: '⚔️'
  },
  'armor-leather': {
    id: 'armor-leather',
    name: 'Armure en cuir',
    type: 'armor',
    rarity: 'common',
    level: 1,
    icon: '🛡️'
  },
  'armor-chain': {
    id: 'armor-chain',
    name: 'Cotte de mailles',
    type: 'armor',
    rarity: 'uncommon',
    level: 5,
    icon: '🛡️'
  },
  'helmet-basic': {
    id: 'helmet-basic',
    name: 'Casque en cuir',
    type: 'armor',
    rarity: 'common',
    level: 1,
    icon: '⛑️'
  },
  'potion-health': {
    id: 'potion-health',
    name: 'Potion de vie',
    type: 'consumable',
    rarity: 'common',
    level: 1,
    icon: '🧪'
  },
  'potion-mana': {
    id: 'potion-mana',
    name: 'Potion de mana',
    type: 'consumable',
    rarity: 'common',
    level: 1,
    icon: '🧪'
  },
  'scroll-teleport': {
    id: 'scroll-teleport',
    name: 'Parchemin de téléportation',
    type: 'consumable',
    rarity: 'rare',
    level: 10,
    icon: '📜'
  }
}

export const SKILLS = {
  warrior: [
    {
      id: 'slash',
      name: 'Entaille',
      description: 'Attaque de base du guerrier',
      level: 1,
      cooldown: 0,
      icon: '⚔️'
    },
    {
      id: 'charge',
      name: 'Charge',
      description: 'Charge vers l\'ennemi',
      level: 5,
      cooldown: 10,
      icon: '🏃'
    },
    {
      id: 'shield-bash',
      name: 'Coup de bouclier',
      description: 'Assomme l\'ennemi',
      level: 10,
      cooldown: 15,
      icon: '🛡️'
    }
  ],
  mage: [
    {
      id: 'fireball',
      name: 'Boule de feu',
      description: 'Lance une boule de feu',
      level: 1,
      cooldown: 5,
      icon: '🔥'
    },
    {
      id: 'ice-spike',
      name: 'Pointe de glace',
      description: 'Crée une pointe de glace',
      level: 5,
      cooldown: 8,
      icon: '❄️'
    },
    {
      id: 'lightning',
      name: 'Éclair',
      description: 'Lance un éclair',
      level: 10,
      cooldown: 12,
      icon: '⚡'
    }
  ],
  archer: [
    {
      id: 'arrow-shot',
      name: 'Tir de flèche',
      description: 'Tire une flèche',
      level: 1,
      cooldown: 0,
      icon: '🏹'
    },
    {
      id: 'multi-shot',
      name: 'Tir multiple',
      description: 'Tire plusieurs flèches',
      level: 5,
      cooldown: 10,
      icon: '🎯'
    },
    {
      id: 'poison-arrow',
      name: 'Flèche empoisonnée',
      description: 'Flèche qui empoisonne',
      level: 10,
      cooldown: 15,
      icon: '☠️'
    }
  ],
  assassin: [
    {
      id: 'backstab',
      name: 'Coup dans le dos',
      description: 'Attaque furtive',
      level: 1,
      cooldown: 5,
      icon: '🗡️'
    },
    {
      id: 'stealth',
      name: 'Furtivité',
      description: 'Se rend invisible',
      level: 5,
      cooldown: 20,
      icon: '👤'
    },
    {
      id: 'death-mark',
      name: 'Marque de mort',
      description: 'Marque une cible',
      level: 10,
      cooldown: 30,
      icon: '💀'
    }
  ]
}

export const ZONES = {
  flaris: {
    name: 'Flaris',
    description: 'Zone de départ paisible',
    minLevel: 1,
    maxLevel: 20,
    color: '#90EE90',
    enemies: ['Gobelin', 'Loup', 'Bandit']
  },
  saintmorning: {
    name: 'Saint Morning',
    description: 'Plus grande ville de Madrigal',
    minLevel: 21,
    maxLevel: 42,
    color: '#F4A460',
    enemies: ['Orc', 'Troll', 'Dragon']
  },
  darkon: {
    name: 'Darkon',
    description: 'Zone industrielle sombre',
    minLevel: 51,
    maxLevel: 120,
    color: '#696969',
    enemies: ['Démon', 'Machine', 'Boss']
  }
}

export const CLASSES = {
  warrior: {
    name: 'Guerrier',
    description: 'Combat rapproché et défense',
    icon: '⚔️',
    color: '#8B4513',
    startingItems: ['sword-basic', 'armor-leather', 'helmet-basic']
  },
  mage: {
    name: 'Mage',
    description: 'Magie élémentaire et sorts',
    icon: '🔮',
    color: '#4B0082',
    startingItems: ['potion-mana', 'potion-health']
  },
  archer: {
    name: 'Archer',
    description: 'Combat à distance et précision',
    icon: '🏹',
    color: '#228B22',
    startingItems: ['potion-health']
  },
  assassin: {
    name: 'Assassin',
    description: 'Furtivité et dégâts critiques',
    icon: '🗡️',
    color: '#2F4F4F',
    startingItems: ['potion-health']
  }
} 