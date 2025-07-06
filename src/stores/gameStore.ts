import { create } from 'zustand'

export interface Player {
  id: string
  name: string
  level: number
  experience: number
  maxExperience: number
  health: number
  maxHealth: number
  mana: number
  maxMana: number
  position: { x: number; y: number; z: number }
  rotation: { x: number; y: number; z: number }
  class: 'warrior' | 'mage' | 'archer' | 'assassin'
  inventory: Item[]
  equipment: Equipment
}

export interface Item {
  id: string
  name: string
  type: 'weapon' | 'armor' | 'consumable' | 'material'
  rarity: 'common' | 'uncommon' | 'rare' | 'epic' | 'legendary'
  level: number
  icon: string
}

export interface Equipment {
  weapon?: Item
  armor?: Item
  helmet?: Item
  gloves?: Item
  boots?: Item
}

export interface GameState {
  // État de connexion
  isLoggedIn: boolean
  isLoading: boolean
  
  // Données du joueur
  player: Player | null
  
  // État du jeu
  currentZone: string
  otherPlayers: Player[]
  npcs: any[]
  enemies: any[]
  
  // UI
  showInventory: boolean
  showCharacter: boolean
  showSkills: boolean
  showChat: boolean
  
  // Actions
  login: (username: string, password: string) => void
  logout: () => void
  updatePlayer: (updates: Partial<Player>) => void
  movePlayer: (position: { x: number; y: number; z: number }) => void
  toggleUI: (ui: 'inventory' | 'character' | 'skills' | 'chat') => void
  addItem: (item: Item) => void
  removeItem: (itemId: string) => void
  equipItem: (item: Item, slot: keyof Equipment) => void
}

const initialPlayer: Player = {
  id: '1',
  name: 'Héros',
  level: 1,
  experience: 0,
  maxExperience: 100,
  health: 100,
  maxHealth: 100,
  mana: 50,
  maxMana: 50,
  position: { x: 0, y: 0, z: 0 },
  rotation: { x: 0, y: 0, z: 0 },
  class: 'warrior',
  inventory: [],
  equipment: {}
}

export const useGameStore = create<GameState>((set, get) => ({
  // État initial
  isLoggedIn: false,
  isLoading: false,
  player: null,
  currentZone: 'flaris',
  otherPlayers: [],
  npcs: [],
  enemies: [],
  showInventory: false,
  showCharacter: false,
  showSkills: false,
  showChat: false,

  // Actions
  login: (username: string, _password: string) => {
    set({ isLoading: true })
    
    // Simuler une connexion
    setTimeout(() => {
      set({
        isLoggedIn: true,
        isLoading: false,
        player: { ...initialPlayer, name: username }
      })
    }, 1000)
  },

  logout: () => {
    set({
      isLoggedIn: false,
      player: null,
      otherPlayers: [],
      npcs: [],
      enemies: []
    })
  },

  updatePlayer: (updates) => {
    const { player } = get()
    if (player) {
      set({ player: { ...player, ...updates } })
    }
  },

  movePlayer: (position) => {
    const { player } = get()
    if (player) {
      set({ player: { ...player, position } })
    }
  },

  toggleUI: (ui) => {
    set((state) => {
      const key = `show${ui.charAt(0).toUpperCase() + ui.slice(1)}` as keyof GameState
      return {
        [key]: !state[key]
      } as Partial<GameState>
    })
  },

  addItem: (item) => {
    const { player } = get()
    if (player) {
      set({
        player: {
          ...player,
          inventory: [...player.inventory, item]
        }
      })
    }
  },

  removeItem: (itemId) => {
    const { player } = get()
    if (player) {
      set({
        player: {
          ...player,
          inventory: player.inventory.filter(item => item.id !== itemId)
        }
      })
    }
  },

  equipItem: (item, slot) => {
    const { player } = get()
    if (player) {
      set({
        player: {
          ...player,
          equipment: {
            ...player.equipment,
            [slot]: item
          }
        }
      })
    }
  }
})) 